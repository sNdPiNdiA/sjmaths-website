# -*- coding: utf-8 -*-

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

sec5_raw = [
    # 5 MCQ (0 to 4)
    {
        "type": "MCQ",
        "q_en": "What was the standard tenure of office for a Portuguese Viceroy or Governor of the Estado da Índia in Goa?",
        "q_hi": "गोवा में एस्टाडो दा इंडिया के पुर्तगाली वायसराय या गवर्नर का मानक कार्यकाल क्या था?",
        "opts_en": ["Three years", "Five years", "Seven years", "Ten years"],
        "opts_hi": ["तीन वर्ष", "पांच वर्ष", "सात वर्ष", "दस वर्ष"],
        "ans": 0,
        "sol_en": "Viceroys and Governors of Goa were appointed for a short three-year term, which encouraged them to focus on rapid personal enrichment rather than long-term administrative or defensive policies.",
        "sol_hi": "गोवा के वायसराय और गवर्नरों को तीन साल के छोटे कार्यकाल के लिए नियुक्त किया जाता था, जिसने उन्हें दीर्घकालिक प्रशासनिक या सुरक्षा नीतियों के बजाय तेजी से व्यक्तिगत संवर्धन पर ध्यान केंद्रित करने के लिए प्रोत्साहित किया।"
    },
    {
        "type": "MCQ",
        "q_en": "In 1632, which Mughal Emperor ordered the siege and expulsion of the Portuguese from their trading post at Hugli in Bengal?",
        "q_hi": "1632 में, किस मुगल सम्राट ने बंगाल में हुगली के व्यापारिक केंद्र से पुर्तगालियों की घेराबंदी और निष्कासन का आदेश दिया था?",
        "opts_en": ["Shah Jahan", "Jahangir", "Akbar", "Aurangzeb"],
        "opts_hi": ["शाहजहां", "जहांगीर", "अकबर", "औरंगजेब"],
        "ans": 0,
        "sol_en": "Mughal Emperor Shah Jahan ordered the governor Qasim Khan to lay siege to Hugli in 1632 due to Portuguese piracy, slave trading of local subjects, and refusal to pay imperial custom duties.",
        "sol_hi": "मुगल सम्राट शाहजहां ने पुर्तगाली डकैती, स्थानीय लोगों के दास व्यापार और शाही सीमा शुल्क का भुगतान करने से इनकार करने के कारण 1632 में गवर्नर कासिम खान को हुगली की घेराबंदी करने का आदेश दिया था।"
    },
    {
        "type": "MCQ",
        "q_en": "Which Maratha military commander led the successful siege and capture of the heavily fortified Portuguese city of Bassein in 1739?",
        "q_hi": "किस मराठा सैन्य कमांडर ने 1739 में पुर्तगाली किलेबंद शहर वसई (बसीन) की सफल घेराबंदी और कब्जा करने का नेतृत्व किया था?",
        "opts_en": ["Chimaji Appa", "Peshwa Baji Rao I", "Kanhoji Angre", "Peshwa Balaji Baji Rao"],
        "opts_hi": ["चिमाजी अप्पा", "पेशवा बाजीराव प्रथम", "कान्होजी आंग्रे", "पेशवा बालाजी बाजीराव"],
        "ans": 0,
        "sol_en": "Chimaji Appa, the brother of Peshwa Baji Rao I, led the Maratha army in a grueling siege that resulted in the capture of Bassein (Vasai) in May 1739.",
        "sol_hi": "पेशवा बाजीराव प्रथम के भाई चिमाजी अप्पा ने मराठा सेना का नेतृत्व एक भीषण घेराबंदी में किया, जिसके परिणामस्वरूप मई 1739 में वसई (बसीन) पर कब्जा कर लिया गया।"
    },
    {
        "type": "MCQ",
        "q_en": "What was the term used to describe the unauthorized private trade conducted by Portuguese crown officials for personal gain?",
        "q_hi": "व्यक्तिगत लाभ के लिए पुर्तगाली शाही अधिकारियों द्वारा किए जाने वाले अनधिकृत निजी व्यापार का वर्णन करने के लिए किस शब्द का उपयोग किया जाता था?",
        "opts_en": ["Trato particular", "Cartaz system", "Feitoria monopoly", "Regimento"],
        "opts_hi": ["त्रातो पर्टिकुलर (Trato particular)", "कार्तज प्रणाली (Cartaz system)", "फेइटोरिया एकाधिकार (Feitoria monopoly)", "रेजिमेंटो (Regimento)"],
        "ans": 0,
        "sol_en": "Trato particular was the private trade conducted by viceroys, fort captains, and officers, which diverted revenues from the royal treasury and led to systemic smuggling.",
        "sol_hi": "त्रातो पर्टिकुलर वायसरायों, किले के कप्तानों और अधिकारियों द्वारा किया जाने वाला निजी व्यापार था, जिसने शाही खजाने से राजस्व को हटा दिया और प्रणालीगत तस्करी को जन्म दिया।"
    },
    {
        "type": "MCQ",
        "q_en": "To raise immediate revenues for the Crown, Portuguese authorities in the 17th century began the practice of 'venda de cargos', which meant:",
        "q_hi": "शाही खजाने के लिए तत्काल राजस्व जुटाने के लिए, 17वीं शताब्दी में पुर्तगाली अधिकारियों ने 'वेंडा दे कार्गोस' (venda de cargos) की प्रथा शुरू की, जिसका अर्थ था:",
        "opts_en": ["Selling official administrative and military offices to the highest bidder", "Selling captured ships to local Indian merchants", "Leasing agricultural lands to Jesuit missions", "Selling custom duty exemptions to European rivals"],
        "opts_hi": ["उच्चतम बोली लगाने वाले को आधिकारिक प्रशासनिक और सैन्य पद बेचना", "पकड़े गए जहाजों को स्थानीय भारतीय व्यापारियों को बेचना", "कृषि भूमि जेसुइट मिशनों को पट्टे पर देना", "यूरोपीय प्रतिद्वंद्वियों को सीमा शुल्क छूट बेचना"],
        "ans": 0,
        "sol_en": "Venda de cargos was the practice of selling government and military posts to raise cash, which severely degraded administrative quality and military leadership.",
        "sol_hi": "वेंडा दे कार्गोस नकद जुटाने के लिए सरकारी और सैन्य पदों को बेचने की प्रथा थी, जिसने प्रशासनिक गुणवत्ता और सैन्य नेतृत्व को गंभीर रूप से कमजोर कर दिया।"
    },

    # 5 Multiple Correct MCQ (5 to 9)
    {
        "type": "Multiple Correct MCQ",
        "q_en": "Which of the following accusations were made by the Mughals against the Portuguese at Hugli, leading to the 1632 siege? (Select all that apply)",
        "q_hi": "हुगली में पुर्तगालियों के खिलाफ मुगलों द्वारा निम्नलिखित में से कौन से आरोप लगाए गए थे, जिसके कारण 1632 में घेराबंदी हुई? (सभी लागू विकल्प चुनें)",
        "opts_en": ["Engaging in piracy in the Bay of Bengal", "Kidnapping local inhabitants and selling them into slavery", "Fortifying the settlement without imperial permission", "Providing military support to the Marathas in the Deccan"],
        "opts_hi": ["बंगाल की खाड़ी में समुद्री डकैती में शामिल होना", "स्थानीय निवासियों का अपहरण करना और उन्हें गुलामी में बेचना", "शाही अनुमति के बिना बस्ती की किलेबंदी करना", "दक्कन में मराठों को सैन्य सहायता प्रदान करना"],
        "ans": [0, 1, 2],
        "sol_en": "The Portuguese at Hugli were accused of piracy, active slave trading (including capturing Mughal women), and unauthorized fort construction. The Marathas were not active in Bengal or Deccan politics at this early date (1632).",
        "sol_hi": "हुगली में पुर्तगालियों पर समुद्री डकैती, सक्रिय दास व्यापार (मुगल महिलाओं को पकड़ने सहित) और अनधिकृत किले के निर्माण का आरोप लगाया गया था। इस शुरुआती तारीख (1632) में मराठे बंगाल या दक्कन की राजनीति में सक्रिय नहीं थे।"
    },
    {
        "type": "Multiple Correct MCQ",
        "q_en": "Which factors contributed directly to the financial bankruptcy of the Portuguese Estado da Índia? (Select all that apply)",
        "q_hi": "पुर्तगाली एस्टाडो दा इंडिया के वित्तीय दिवालियापन में किन कारकों ने सीधे योगदान दिया? (सभी लागू विकल्प चुनें)",
        "opts_en": ["Loss of customs revenues due to the growth of private trade (trato particular)", "High military expenses incurred in defending isolated fortresses against Dutch fleets", "Loss of lucrative customs houses like Ormuz (1622) and Malacca (1641)", "Complete exhaustion of gold mines in Portugal"],
        "opts_hi": ["निजी व्यापार (त्रातो पर्टिकुलर) के बढ़ने के कारण सीमा शुल्क राजस्व का नुकसान", "डच बेड़ों के खिलाफ पृथक किलों की रक्षा में होने वाला भारी सैन्य खर्च", "होर्मुज (1622) और मलक्का (1641) जैसे आकर्षक सीमा शुल्क कार्यालयों का नुकसान", "पुर्तगाल में सोने की खदानों का पूरी तरह से समाप्त हो जाना"],
        "ans": [0, 1, 2],
        "sol_en": "Systemic corruption, massive defense costs against Dutch attacks, and the loss of major hubs (Ormuz, Malacca) bankrupt the Estado. Portugal had no significant domestic gold mines; gold was imported from Brazil later.",
        "sol_hi": "प्रणालीगत भ्रष्टाचार, डच हमलों के खिलाफ भारी सुरक्षा लागत और प्रमुख केंद्रों (होर्मुज, मलक्का) के नुकसान ने एस्टाडो को दिवालिया कर दिया। पुर्तगाल में कोई महत्वपूर्ण घरेलू सोने की खदानें नहीं थीं; बाद में ब्राजील से सोना आयात किया गया था।"
    },
    {
        "type": "Multiple Correct MCQ",
        "q_en": "Which of the following territories did the Portuguese lose to the Marathas during the campaigns between 1737 and 1739? (Select all that apply)",
        "q_hi": "1737 और 1739 के अभियानों के दौरान पुर्तगालियों ने मराठों के हाथों निम्नलिखित में से कौन से क्षेत्र खो दिए थे? (सभी लागू विकल्प चुनें)",
        "opts_en": ["Bassein (Vasai)", "Thana (Thane)", "Salsette Island", "Daman"],
        "opts_hi": ["वसई (बसीन)", "थाना (ठाणे)", "साल्सेट द्वीप", "दमन"],
        "ans": [0, 1, 2],
        "sol_en": "The Maratha campaign under Chimaji Appa captured Bassein, Thana, and Salsette Island, dismantling the Província do Norte. Daman was besieged but remained under Portuguese control.",
        "sol_hi": "चिमाजी अप्पा के नेतृत्व में मराठा अभियान ने वसई, ठाणे और साल्सेट द्वीप पर कब्जा कर लिया, जिससे उत्तरी प्रांत का पतन हो गया। दमन की घेराबंदी की गई थी लेकिन वह पुर्तगाली नियंत्रण में ही रहा।"
    },
    {
        "type": "Multiple Correct MCQ",
        "q_en": "How did the practice of selling administrative and military offices (venda de cargos) weaken Portuguese power? (Select all that apply)",
        "q_hi": "प्रशासनिक और सैन्य पदों को बेचने की प्रथा (वेंडा दे कार्गोस) ने पुर्तगाली सत्ता को कैसे कमजोर किया? (सभी लागू विकल्प चुनें)",
        "opts_en": ["Posts were given to wealthy buyers instead of competent military officers", "Buyers used their short tenure to extract maximum bribes and recover their costs", "The army and navy fell under the leadership of corrupt, untrained aristocrats", "It led to a military rebellion that established a republican government in Goa"],
        "opts_hi": ["सक्षम सैन्य अधिकारियों के बजाय अमीर खरीदारों को पद दिए गए", "खरीदारों ने अपने छोटे कार्यकाल का उपयोग अधिकतम रिश्वत वसूलने और अपनी लागत वसूलने के लिए किया", "सेना और नौसेना भ्रष्ट, अप्रशिक्षित अभिजात वर्ग के नेतृत्व में आ गई", "इससे एक सैन्य विद्रोह हुआ जिसने गोवा में एक गणतांत्रिक सरकार की स्थापना की"],
        "ans": [0, 1, 2],
        "sol_en": "Selling offices resulted in incompetent leadership, rapid extraction of bribes to offset purchase costs, and general military decay. No republican rebellion occurred in Goa during this period.",
        "sol_hi": "पदों को बेचने के परिणामस्वरूप अक्षम नेतृत्व, खरीद लागत की भरपाई के लिए रिश्वत की त्वरित वसूली और सामान्य सैन्य पतन हुआ। इस अवधि के दौरान गोवा में कोई गणतांत्रिक विद्रोह नहीं हुआ था।"
    },
    {
        "type": "Multiple Correct MCQ",
        "q_en": "Which regional powers in India actively pushed back against Portuguese expansion or recaptured territories from them in the 17th and 18th centuries? (Select all that apply)",
        "q_hi": "17वीं और 18वीं शताब्दी में भारत की किन क्षेत्रीय शक्तियों ने पुर्तगाली विस्तार का सक्रिय रूप से विरोध किया या उनसे क्षेत्रों को वापस छीन लिया? (सभी लागू विकल्प चुनें)",
        "opts_en": ["The Mughal Empire", "The Maratha Empire", "The Nayakas of Keladi", "The Rajput Kingdoms of Marwar"],
        "opts_hi": ["मुगल साम्राज्य", "मराठा साम्राज्य", "केलादि के नायक", "मारवाड़ के राजपूत साम्राज्य"],
        "ans": [0, 1, 2],
        "sol_en": "The Mughals expelled them from Hugli, the Marathas captured Bassein and the Northern Province, and the Keladi Nayakas seized Portuguese coastal fortresses in Canara (such as Mangalore and Honavar). The Rajputs did not interact militarily with the Portuguese.",
        "sol_hi": "मुगलों ने उन्हें हुगली से खदेड़ दिया, मराठों ने वसई और उत्तरी प्रांत पर कब्जा कर लिया, और केलादि नायकों ने कनारा में पुर्तगाली तटीय किलों (जैसे मैंगलोर और होनावर) पर कब्जा कर लिया। राजपूतों ने पुर्तगालियों के साथ कोई सैन्य संघर्ष नहीं किया था।"
    },

    # 8 True/False (10 to 17)
    {
        "type": "True/False",
        "q_en": "The Mughal Emperor who ordered the capture of Hugli in 1632 was Shah Jahan.",
        "q_hi": "सत्य या असत्य: 1632 में हुगली पर कब्जा करने का आदेश देने वाले मुगल सम्राट शाहजहां थे।",
        "ans": True,
        "sol_en": "Shah Jahan, who was highly displeased with Portuguese arrogance, piracy, and religious conversions, ordered the siege of Hugli.",
        "sol_hi": "शाहजहां, जो पुर्तगाली अहंकार, डकैती और धार्मिक जबरन धर्मांतरण से अत्यधिक नाराज थे, ने हुगली की घेराबंदी का आदेश दिया था।"
    },
    {
        "type": "True/False",
        "q_en": "The Maratha general Chimaji Appa, who captured Bassein, was the ruling Peshwa himself during the siege.",
        "q_hi": "सत्य या असत्य: वसई पर कब्जा करने वाले मराठा जनरल चिमाजी अप्पा घेराबंदी के दौरान खुद शासक पेशवा थे।",
        "ans": False,
        "sol_en": "Chimaji Appa was the brother and military commander of Peshwa Baji Rao I, who was the ruling Peshwa.",
        "sol_hi": "चिमाजी अप्पा पेशवा बाजीराव प्रथम के भाई और सैन्य कमांडर थे, जो उस समय शासक पेशवा थे।"
    },
    {
        "type": "True/False",
        "q_en": "The short three-year term of office for Portuguese Governors in Goa was designed to ensure they did not establish independent local kingdoms.",
        "q_hi": "सत्य या असत्य: गोवा में पुर्तगाली गवर्नरों का छोटा तीन साल का कार्यकाल यह सुनिश्चित करने के लिए डिज़ाइन किया गया था कि वे स्वतंत्र स्थानीय साम्राज्य स्थापित न कर सकें।",
        "ans": True,
        "sol_en": "The Lisbon Crown feared governors would build personal power bases, so it limited their terms to three years, though this also encouraged short-term corruption.",
        "sol_hi": "लिस्बन क्राउन को डर था कि गवर्नर व्यक्तिगत शक्ति आधार बना लेंगे, इसलिए उसने उनका कार्यकाल तीन साल तक सीमित कर दिया, हालांकि इससे अल्पकालिक भ्रष्टाचार को भी बढ़ावा मिला।"
    },
    {
        "type": "True/False",
        "q_en": "The term 'trato particular' refers to the official spice trade conducted exclusively on behalf of the King of Portugal.",
        "q_hi": "सत्य या असत्य: 'त्रातो पर्टिकुलर' शब्द का तात्पर्य विशेष रूप से पुर्तगाल के राजा की ओर से किए जाने वाले आधिकारिक मसाला व्यापार से है।",
        "ans": False,
        "sol_en": "Trato particular was unauthorized private trade conducted by crown officials for their personal gain, violating the royal monopoly.",
        "sol_hi": "त्रातो पर्टिकुलर शाही अधिकारियों द्वारा अपने व्यक्तिगत लाभ के लिए किया जाने वाला अनधिकृत निजी व्यापार था, जो शाही एकाधिकार का उल्लंघन करता था।"
    },
    {
        "type": "True/False",
        "q_en": "The loss of Bassein in 1739 stripped the Portuguese of their fertile Northern Province, which was their major source of timber and food grains.",
        "q_hi": "सत्य या असत्य: 1739 में वसई के नुकसान ने पुर्तगालियों से उनके उपजाऊ उत्तरी प्रांत को छीन लिया, जो उनकी लकड़ी और खाद्यान्न का प्रमुख स्रोत था।",
        "ans": True,
        "sol_en": "The Northern Province (Província do Norte) was the agricultural breadbasket of the Portuguese territory, and its loss crippled Goa's resources.",
        "sol_hi": "उत्तरी प्रांत (प्रॉविन्सिया डो नॉर्ट) पुर्तगाली क्षेत्र का कृषि भंडार था, और इसके नुकसान ने गोवा के संसाधनों को पंगु बना दिया।"
    },
    {
        "type": "True/False",
        "q_en": "Under the system of 'venda de cargos', judicial offices in Goa were sold to the highest bidder but military posts were kept strictly merit-based.",
        "q_hi": "सत्य या असत्य: 'वेंडा दे कार्गोस' प्रणाली के तहत, गोवा में न्यायिक पद उच्चतम बोलीदाता को बेचे जाते थे लेकिन सैन्य पदों को कड़ाई से योग्यता-आधारित रखा जाता था।",
        "ans": False,
        "sol_en": "Both administrative, judicial, and crucial military captaincy posts were sold to raise funds, leading to military incompetence.",
        "sol_hi": "धन जुटाने के लिए प्रशासनिक, न्यायिक और महत्वपूर्ण सैन्य कप्तानी दोनों पदों को बेचा गया, जिससे सैन्य अक्षमता पैदा हुई।"
    },
    {
        "type": "True/False",
        "q_en": "The Maratha navy under Sekhoji Angre played an active role in preventing sea-borne reinforcements from reaching the besieged Portuguese at Bassein in 1739.",
        "q_hi": "सत्य या असत्य: सेखोजी आंग्रे के नेतृत्व में मराठा नौसेना ने 1739 में वसई में घिरे पुर्तगालियों तक समुद्र के रास्ते कुमक पहुंचने से रोकने में सक्रिय भूमिका निभाई थी।",
        "ans": True,
        "sol_en": "The Maratha naval force blockaded the sea access to Bassein, making it impossible for Goa to send sufficient reinforcements to the besieged garrison.",
        "sol_hi": "मराठा नौसैनिक बल ने वसई के समुद्री मार्ग की नाकेबंदी कर दी, जिससे गोवा के लिए घिरे हुए गैरीसन को पर्याप्त कुमक भेजना असंभव हो गया।"
    },
    {
        "type": "True/False",
        "q_en": "Following the fall of Hugli in 1632, the Mughals immediately launched a naval invasion to capture Goa from the Portuguese.",
        "q_hi": "सत्य या असत्य: 1632 में हुगली के पतन के बाद, मुगलों ने पुर्तगालियों से गोवा को छीनने के लिए तुरंत नौसैनिक आक्रमण शुरू कर दिया था।",
        "ans": False,
        "sol_en": "The Mughals had no strong navy and did not attack Goa; their actions against the Portuguese were localized to Bengal and northern ports.",
        "sol_hi": "मुगलों के पास कोई मजबूत नौसेना नहीं थी और उन्होंने गोवा पर हमला नहीं किया; पुर्तगालियों के खिलाफ उनकी कार्रवाई बंगाल और उत्तरी बंदरगाहों तक ही सीमित थी।"
    },

    # 8 Fill in the Blank (18 to 25)
    {
        "type": "Fill in the Blank",
        "q_en": "The Mughal governor of Bengal who executed Shah Jahan's order to capture Hugli was __________ Khan.",
        "q_hi": "बंगाल के मुगल गवर्नर जिन्होंने हुगली पर कब्जा करने के शाहजहां के आदेश को क्रियान्वित किया, उनका नाम __________ खान था।",
        "ans": "Qasim",
        "sol_en": "Qasim Khan Juyuni, the governor of Bengal, launched a coordinated land and water siege of Hugli in 1632.",
        "sol_hi": "बंगाल के गवर्नर कासिम खान जुयूनी ने 1632 में हुगली की भूमि और जल मार्ग से एक समन्वित घेराबंदी शुरू की थी।"
    },
    {
        "type": "Fill in the Blank",
        "q_en": "The fortified city of Bassein and its surrounding regions were known to the Portuguese as the Northern __________. ",
        "q_hi": "वसई (बसीन) का किला और उसके आसपास के क्षेत्र पुर्तगालियों के लिए उत्तरी __________ के रूप में जाने जाते थे।",
        "ans": "Province",
        "sol_en": "The Província do Norte (Northern Province) included Bassein, Daman, Diu, Chaul, and Salsette Island.",
        "sol_hi": "प्रॉविन्सिया डो नॉर्ट (उत्तरी प्रांत) में वसई, दमन, दीव, चोल और साल्सेट द्वीप शामिल थे।"
    },
    {
        "type": "Fill in the Blank",
        "q_en": "The unauthorized private trade by Portuguese officials was known in Portuguese as trato __________.",
        "q_hi": "पुर्तगाली अधिकारियों द्वारा किया जाने वाला अनधिकृत निजी व्यापार पुर्तगाली में त्रातो __________ के रूप में जाना जाता था।",
        "ans": "particular",
        "sol_en": "Trato particular undermined the royal commercial monopolies and depleted the customs revenue of the Crown.",
        "sol_hi": "त्रातो पर्टिकुलर ने शाही व्यापारिक एकाधिकार को कमजोर कर दिया और क्राउन के सीमा शुल्क राजस्व को समाप्त कर दिया।"
    },
    {
        "type": "Fill in the Blank",
        "q_en": "The Maratha commander who captured Bassein in 1739 was Chimaji __________, the brother of Peshwa Baji Rao I.",
        "q_hi": "1739 में वसई पर कब्जा करने वाले मराठा कमांडर चिमाजी __________ थे, जो पेशवा बाजीराव प्रथम के भाई थे।",
        "ans": "Appa",
        "sol_en": "Chimaji Appa planned and executed the Maratha military campaigns against the Portuguese on the Konkan coast.",
        "sol_hi": "चिमाजी अप्पा ने कोंकण तट पर पुर्तगालियों के खिलाफ मराठा सैन्य अभियानों की योजना बनाई और उन्हें अंजाम दिया था।"
    },
    {
        "type": "Fill in the Blank",
        "q_en": "The siege and capture of Hugli by Mughal forces took place in the year __________ CE.",
        "q_hi": "मुगल सेना द्वारा हुगली की घेराबंदी और उस पर कब्जा __________ ईस्वी में हुआ था।",
        "ans": "1632",
        "sol_en": "The siege of Hugli took place in 1632, leading to the destruction of the Portuguese factory and capture of hundreds of prisoners.",
        "sol_hi": "हुगली की घेराबंदी 1632 में हुई थी, जिससे पुर्तगाली कारखाने का विनाश हुआ और सैकड़ों कैदियों को पकड़ लिया गया।"
    },
    {
        "type": "Fill in the Blank",
        "q_en": "The Portuguese practice of selling administrative and military positions to raise quick revenue was called venda de __________.",
        "q_hi": "त्वरित राजस्व जुटाने के लिए प्रशासनिक और सैन्य पदों को बेचने की पुर्तगाली प्रथा को वेंडा दे __________ कहा जाता था।",
        "ans": "cargos",
        "sol_en": "Venda de cargos (sale of offices) allowed wealthy buyers to purchase captaincies of fortresses, degrading military command.",
        "sol_hi": "वेंडा दे कार्गोस (पदों की बिक्री) ने अमीर खरीदारों को किलों की कप्तानी खरीदने की अनुमति दी, जिससे सैन्य कमान का स्तर गिर गया।"
    },
    {
        "type": "Fill in the Blank",
        "q_en": "The standard tenure of a Portuguese Viceroy in Goa was limited to __________ years.",
        "q_hi": "गोवा में पुर्तगाली वायसराय का मानक कार्यकाल __________ वर्ष तक सीमित था।",
        "ans": "three",
        "sol_en": "Viceroy terms were restricted to three years to prevent them from becoming too powerful locally, but this led to rapid self-enrichment.",
        "sol_hi": "वायसराय के कार्यकाल को तीन साल तक सीमित कर दिया गया था ताकि वे स्थानीय स्तर पर बहुत शक्तिशाली न हो सकें, लेकिन इससे त्वरित व्यक्तिगत संवर्धन को बढ़ावा मिला।"
    },
    {
        "type": "Fill in the Blank",
        "q_en": "The Maratha conquest of Bassein was finalized in the year __________ CE.",
        "q_hi": "वसई पर मराठों की विजय को __________ ईस्वी में अंतिम रूप दिया गया था।",
        "ans": "1739",
        "sol_en": "The siege ended with the surrender of the Portuguese garrison in May 1739, after which the Marathas annexed Bassein.",
        "sol_hi": "घेराबंदी मई 1739 में पुर्तगाली गैरीसन के आत्मसमर्पण के साथ समाप्त हुई, जिसके बाद मराठों ने वसई का विलय कर लिया।"
    },

    # 3 Match the Following (26 to 28)
    {
        "type": "Match the Following",
        "q_en": "Match the Portuguese administrative and trade terms with their correct definitions:",
        "q_hi": "पुर्तगाली प्रशासनिक और व्यापारिक शब्दों का उनके सही परिभाषाओं से मिलान करें:",
        "items_en": [{"left": "Trato particular"}, {"left": "Venda de cargos"}, {"left": "Vedor da Fazenda"}],
        "items_hi": [{"left": "त्रातो पर्टिकुलर"}, {"left": "वेंडा दे कार्गोस"}, {"left": "वेडोर दा फजेंडा"}],
        "options_en": [{"val": "0", "text": "Unauthorized private trade by crown officials"}, {"val": "1", "text": "The sale of administrative and military offices"}, {"val": "2", "text": "The chief financial officer of the Estado da Índia"}],
        "options_hi": [{"val": "0", "text": "शाही अधिकारियों द्वारा अनधिकृत निजी व्यापार"}, {"val": "1", "text": "प्रशासनिक और सैन्य पदों की बिक्री"}, {"val": "2", "text": "एस्टाडो दा इंडिया के मुख्य वित्तीय अधिकारी"}],
        "sol_en": "Correct match: Trato particular - private trade; Venda de cargos - sale of offices; Vedor da Fazenda - chief financial officer.",
        "sol_hi": "सही मिलान: त्रातो पर्टिकुलर - निजी व्यापार; वेंडा दे कार्गोस - पदों की बिक्री; वेडोर दा फजेंडा - मुख्य वित्तीय अधिकारी।"
    },
    {
        "type": "Match the Following",
        "q_en": "Match the key territorial losses of the Portuguese with the regional powers that captured them:",
        "q_hi": "पुर्तगालियों के प्रमुख क्षेत्रीय नुकसान का उन पर कब्जा करने वाली क्षेत्रीय शक्तियों से मिलान करें:",
        "items_en": [{"left": "Hugli (1632)"}, {"left": "Bassein (1739)"}, {"left": "Mangalore (1710s)"}],
        "items_hi": [{"left": "हुगली (1632)"}, {"left": "वसई (1739)"}, {"left": "मैंगलोर (1710 का दशक)"}],
        "options_en": [{"val": "0", "text": "Mughal Empire"}, {"val": "1", "text": "Maratha Empire"}, {"val": "2", "text": "Keladi Nayaka Kingdom"}],
        "options_hi": [{"val": "0", "text": "मुगल साम्राज्य"}, {"val": "1", "text": "मराठा साम्राज्य"}, {"val": "2", "text": "केलादि नायक साम्राज्य"}],
        "sol_en": "Correct match: Hugli - Mughals; Bassein - Marathas; Mangalore - Keladi Nayakas.",
        "sol_hi": "सही मिलान: हुगली - मुगल; वसई - मराठा; मैंगलोर - केलादि नायक।"
    },
    {
        "type": "Match the Following",
        "q_en": "Match the historic actors involved in regional resistance with their historical roles:",
        "q_hi": "क्षेत्रीय प्रतिरोध में शामिल ऐतिहासिक अभिनेताओं का उनकी ऐतिहासिक भूमिकाओं से मिलान करें:",
        "items_en": [{"left": "Qasim Khan"}, {"left": "Chimaji Appa"}, {"left": "Soma Shekhar Nayaka"}],
        "items_hi": [{"left": "कासिम खान"}, {"left": "चिमाजी अप्पा"}, {"left": "सोम शेखर नायक"}],
        "options_en": [{"val": "0", "text": "Mughal Governor who expelled the Portuguese from Hugli"}, {"val": "1", "text": "Maratha General who led the capture of Bassein"}, {"val": "2", "text": "Keladi ruler who captured Portuguese forts in Canara"}],
        "options_hi": [{"val": "0", "text": "मुगल गवर्नर जिसने पुर्तगालियों को हुगली से खदेड़ा"}, {"val": "1", "text": "मराठा जनरल जिसने वसई पर कब्जे का नेतृत्व किया"}, {"val": "2", "text": "केलादि शासक जिसने कनारा में पुर्तगाली किलों पर कब्जा किया"}],
        "sol_en": "Correct match: Qasim Khan - Mughal Governor of Bengal; Chimaji Appa - Maratha General; Soma Shekhar Nayaka - Keladi ruler of Canara.",
        "sol_hi": "सही मिलान: कासिम खान - बंगाल के मुगल गवर्नर; चिमाजी अप्पा - मराठा जनरल; सोम शेखर नायक - कनारा के केलादि शासक।"
    },

    # 8 One-Liner (29 to 36)
    {
        "type": "One-Liner",
        "q_en": "Why did the short three-year tenure of Portuguese Viceroys encourage systemic corruption in Goa?",
        "q_hi": "पुर्तगाली वायसरायों का छोटा तीन साल का कार्यकाल गोवा में प्रणालीगत भ्रष्टाचार को क्यों बढ़ावा देता था?",
        "sol_en": "It forced viceroys to prioritize rapid personal enrichment through bribes and private trade before their term expired.",
        "sol_hi": "इसने वायसरायों को अपना कार्यकाल समाप्त होने से पहले रिश्वत और निजी व्यापार के माध्यम से तेजी से व्यक्तिगत संवर्धन को प्राथमिकता देने के लिए मजबूर किया।"
    },
    {
        "type": "One-Liner",
        "q_en": "Who was the Mughal Emperor who ordered the capture of Hugli from the Portuguese?",
        "q_hi": "पुर्तगालियों से हुगली छीनने का आदेश देने वाले मुगल सम्राट कौन थे?",
        "sol_en": "Emperor Shah Jahan.",
        "sol_hi": "सम्राट शाहजहां।"
    },
    {
        "type": "One-Liner",
        "q_en": "Which Maratha general led the capture of Bassein in 1739?",
        "q_hi": "1739 में वसई पर कब्जा करने वाले मराठा जनरल कौन थे?",
        "sol_en": "Chimaji Appa, the brother of Peshwa Baji Rao I.",
        "sol_hi": "चिमाजी अप्पा, जो पेशवा बाजीराव प्रथम के भाई थे।"
    },
    {
        "type": "One-Liner",
        "q_en": "What did the Portuguese term 'venda de cargos' represent in the 17th century?",
        "q_hi": "17वीं शताब्दी में पुर्तगाली शब्द 'वेंडा दे कार्गोस' किसे दर्शाता था?",
        "sol_en": "The practice of selling administrative and military offices to the highest bidder to raise cash for the Crown.",
        "sol_hi": "शाही खजाने के लिए धन जुटाने के लिए प्रशासनिक और सैन्य पदों को उच्चतम बोलीदाता को बेचने की प्रथा।"
    },
    {
        "type": "One-Liner",
        "q_en": "What was the economic significance of the 'Northern Province' to Portuguese Goa?",
        "q_hi": "पुर्तगाली गोवा के लिए 'उत्तरी प्रांत' का आर्थिक महत्व क्या था?",
        "sol_en": "It was Goa's agricultural breadbasket, providing essential food grains, timber for shipbuilding, and customs revenues.",
        "sol_hi": "यह गोवा का कृषि भंडार था, जो आवश्यक खाद्यान्न, जहाज निर्माण के लिए लकड़ी और सीमा शुल्क राजस्व प्रदान करता था।"
    },
    {
        "type": "One-Liner",
        "q_en": "Name the Portuguese practice of private, unlicensed trade that bypassed royal customs houses.",
        "q_hi": "पुर्तगाली अधिकारियों की उस निजी, बिना लाइसेंस वाले व्यापार की प्रथा का नाम बताइए जो शाही सीमा शुल्क कार्यालयों की उपेक्षा करती थी।",
        "sol_en": "Trato particular.",
        "sol_hi": "त्रातो पर्टिकुलर (Trato particular)।"
    },
    {
        "type": "One-Liner",
        "q_en": "Which treaty in 1739 concluded the war between the Marathas and the Portuguese over the Northern Province?",
        "q_hi": "1739 में किस संधि ने उत्तरी प्रांत को लेकर मराठों और पुर्तगालियों के बीच युद्ध को समाप्त किया था?",
        "sol_en": "The Treaty of Pune (or Treaty of Bassein) of 1739.",
        "sol_hi": "1739 की पुणे की संधि (या वसई की संधि)।"
    },
    {
        "type": "One-Liner",
        "q_en": "What religious issue in Bengal contributed to Shah Jahan's decision to expel the Portuguese from Hugli?",
        "q_hi": "बंगाल में किस धार्मिक मुद्दे ने पुर्तगालियों को हुगली से खदेड़ने के शाहजहां के फैसले में योगदान दिया था?",
        "sol_en": "The forced conversion of local Mughal subjects, including orphan children and Mughal women, to Christianity.",
        "sol_hi": "अनाथ बच्चों और मुगल महिलाओं सहित स्थानीय मुगल प्रजा का ईसाई धर्म में जबरन धर्मांतरण।"
    },

    # 8 Assertion-Reason (37 to 44)
    {
        "type": "Assertion-Reason",
        "q_en": "Assertion (A): Portuguese officials in Goa routinely engaged in contraband trade.\nReason (R): The Portuguese Crown paid low salaries, and the three-year viceroy term encouraged rapid self-enrichment.",
        "q_hi": "अभिकथन (A): गोवा में पुर्तगाली अधिकारी नियमित रूप से तस्करी के व्यापार में शामिल रहते थे।\nकारण (R): पुर्तगाली क्राउन बहुत कम वेतन देता था, और तीन साल का वायसराय कार्यकाल त्वरित व्यक्तिगत संवर्धन को बढ़ावा देता था।",
        "opts_en": EN_AR_OPTS,
        "opts_hi": HI_AR_OPTS,
        "ans": 0,
        "sol_en": "Low salaries combined with short, insecure tenures forced and encouraged officials to rely on 'trato particular' and smuggling to build personal wealth, making R a correct explanation of A.",
        "sol_hi": "कम वेतन के साथ-साथ छोटे और असुरक्षित कार्यकाल ने अधिकारियों को व्यक्तिगत संपत्ति बनाने के लिए 'त्रातो पर्टिकुलर' और तस्करी पर भरोसा करने के लिए मजबूर और प्रोत्साहित किया, जिससे R, A की सही व्याख्या करता है।"
    },
    {
        "type": "Assertion-Reason",
        "q_en": "Assertion (A): The loss of Bassein in 1739 was a fatal economic blow to the Portuguese Estado da Índia.\nReason (R): The Northern Province provided Goa with its primary supply of rice, construction timber, and customs revenues.",
        "q_hi": "अभिकथन (A): 1739 में वसई का जाना पुर्तगाली एस्टाडो दा इंडिया के लिए एक घातक आर्थिक झटका था।\nकारण (R): उत्तरी प्रांत ने गोवा को चावल की प्राथमिक आपूर्ति, निर्माण की लकड़ी और सीमा शुल्क राजस्व प्रदान किया था।",
        "opts_en": EN_AR_OPTS,
        "opts_hi": HI_AR_OPTS,
        "ans": 0,
        "sol_en": "The Northern Province was the economic core of Portuguese India; losing it destroyed their food supply and crippled their local economy, making R the correct explanation.",
        "sol_hi": "उत्तरी प्रांत पुर्तगाली भारत का आर्थिक केंद्र था; इसे खोने से उनकी खाद्य आपूर्ति नष्ट हो गई और उनकी स्थानीय अर्थव्यवस्था पंगु हो गई, जिससे R सही व्याख्या है।"
    },
    {
        "type": "Assertion-Reason",
        "q_en": "Assertion (A): Shah Jahan ordered the siege of Hugli in 1632 primarily to assist the British East India Company in Bengal.\nReason (R): The British EIC promised to pay double the customs duties compared to the Portuguese.",
        "q_hi": "अभिकथन (A): शाहजहां ने 1632 में हुगली की घेराबंदी मुख्य रूप से बंगाल में ब्रिटिश ईस्ट इंडिया कंपनी की सहायता के लिए की थी।\nकारण (R): ब्रिटिश ईआईसी ने पुर्तगालियों की तुलना में दोगुना सीमा शुल्क देने का वादा किया था।",
        "opts_en": EN_AR_OPTS,
        "opts_hi": HI_AR_OPTS,
        "ans": 3,
        "sol_en": "Both A and R are false. Shah Jahan expelled the Portuguese due to their own misconduct, piracy, and slave trading, and it was not done to benefit the English, who were not yet a dominant force in Bengal in 1632.",
        "sol_hi": "A और R दोनों गलत हैं। शाहजहां ने पुर्तगालियों को उनके दुराचार, डकैती और दास व्यापार के कारण निकाला था, और यह अंग्रेजों को लाभ पहुंचाने के लिए नहीं किया गया था, जो 1632 में बंगाल में अभी तक एक प्रमुख शक्ति नहीं थे।"
    },
    {
        "type": "Assertion-Reason",
        "q_en": "Assertion (A): The practice of selling administrative offices (venda de cargos) compromised the defense of Portuguese India.\nReason (R): It allowed wealthy, untrained individuals to buy fortress captaincies, sidelining experienced military officers.",
        "q_hi": "अभिकथन (A): प्रशासनिक पदों को बेचने की प्रथा (वेंडा दे कार्गोस) ने पुर्तगाली भारत की रक्षा से समझौता किया।\nकारण (R): इसने अमीर, अप्रशिक्षित व्यक्तियों को किलों की कप्तानी खरीदने की अनुमति दी, जिससे अनुभवी सैन्य अधिकारियों को दरकिनार कर दिया गया।",
        "opts_en": EN_AR_OPTS,
        "opts_hi": HI_AR_OPTS,
        "ans": 0,
        "sol_en": "Venda de cargos prioritized money over military merit, placing crucial defensive strongholds under the control of incompetent captains, directly weakening defense.",
        "sol_hi": "वेंडा दे कार्गोस ने सैन्य योग्यता से अधिक धन को प्राथमिकता दी, जिससे महत्वपूर्ण रक्षात्मक गढ़ अक्षम कप्तानों के नियंत्रण में आ गए, जिसने सीधे तौर पर रक्षा को कमजोर किया।"
    },
    {
        "type": "Assertion-Reason",
        "q_en": "Assertion (A): The Marathas succeeded in capturing Bassein in 1739 despite the strength of its stone fortifications.\nReason (R): Chimaji Appa used advanced mining techniques to breach the walls and blockaded the fort by sea to prevent reinforcement.",
        "q_hi": "अभिकथन (A): 1739 में मराठों ने वसई के पत्थरों के किलों की ताकत के बावजूद उस पर कब्जा करने में सफलता प्राप्त की।\nकारण (R): चिमाजी अप्पा ने दीवारों को तोड़ने के लिए उन्नत सुरंग (माइनिंग) तकनीकों का उपयोग किया और कुमक को रोकने के लिए समुद्र के रास्ते किले की नाकेबंदी की।",
        "opts_en": EN_AR_OPTS,
        "opts_hi": HI_AR_OPTS,
        "ans": 0,
        "sol_en": "The Marathas dug multiple mines beneath the bastions of Bassein to blow them up and coordinated with their naval assets to stop reinforcements, making R the correct explanation.",
        "sol_hi": "मराठों ने वसई के बुर्जों के नीचे कई सुरंगें खोदीं ताकि उन्हें उड़ाया जा सके और कुमक को रोकने के लिए अपने नौसैनिक संपत्तियों के साथ समन्वय किया, जिससे R सही व्याख्या है।"
    },
    {
        "type": "Assertion-Reason",
        "q_en": "Assertion (A): The Portuguese Crown was unable to effectively eliminate the corruption of its officials in Goa.\nReason (R): The Cape Route to India was long and hazardous, taking six to eight months and delaying communications and royal oversight.",
        "q_hi": "अभिकथन (A): पुर्तगाली क्राउन गोवा में अपने अधिकारियों के भ्रष्टाचार को प्रभावी ढंग से समाप्त करने में असमर्थ था।\nकारण (R): भारत के लिए केप मार्ग लंबा और खतरनाक था, जिसमें छह से आठ महीने लगते थे और संचार तथा शाही निगरानी में देरी होती थी।",
        "opts_en": EN_AR_OPTS,
        "opts_hi": HI_AR_OPTS,
        "ans": 0,
        "sol_en": "The massive geographic distance made real-time monitoring impossible, allowing corrupt officials to operate with impunity for years before Lisbon could react.",
        "sol_hi": "विशाल भौगोलिक दूरी ने वास्तविक समय की निगरानी को असंभव बना दिया, जिससे भ्रष्ट अधिकारियों को लिस्बन की प्रतिक्रिया से पहले वर्षों तक बिना किसी डर के काम करने की अनुमति मिली।"
    },
    {
        "type": "Assertion-Reason",
        "q_en": "Assertion (A): The Mughals launched a massive amphibious campaign to conquer Goa after recapturing Hugli in 1632.\nReason (R): The Mughal military lacked a deep-sea combat navy capable of challenging Portuguese ships in open water.",
        "q_hi": "अभिकथन (A): मुगलों ने 1632 में हुगली पर पुनः कब्जा करने के बाद गोवा को जीतने के लिए एक बड़ा उभयचर (amphibious) अभियान शुरू किया था।\nकारण (R): मुगल सेना के पास गहरे समुद्र में लड़ने वाली नौसेना की कमी थी जो खुले पानी में पुर्तगाली जहाजों को चुनौती दे सके।",
        "opts_en": EN_AR_OPTS,
        "opts_hi": HI_AR_OPTS,
        "ans": 3,
        "sol_en": "Assertion A is false because the Mughals never attempted to invade Goa. Reason R is true; the Mughals were essentially a land power and lacked a deep-sea navy, which is why they did not pursue the Portuguese beyond their coastal ports.",
        "sol_hi": "अभिकथन A गलत है क्योंकि मुगलों ने कभी गोवा पर आक्रमण करने का प्रयास नहीं किया। कारण R सही है; मुगल मुख्य रूप से एक थल सेना शक्ति थे और उनके पास गहरे समुद्र की नौसेना नहीं थी, यही कारण है कि उन्होंने तटीय बंदरगाहों से आगे पुर्तगालियों का पीछा नहीं किया।"
    },
    {
        "type": "Assertion-Reason",
        "q_en": "Assertion (A): The Portuguese administration of India remained financially solvent throughout the 18th century.\nReason (R): The Peshwa agreed to pay annual tributes to the Portuguese Crown in exchange for retaining Goa.",
        "q_hi": "अभिकथन (A): 18वीं शताब्दी के दौरान पुर्तगाली भारत का प्रशासन वित्तीय रूप से सक्षम बना रहा।\nकारण (R): पेशवा ने गोवा को बनाए रखने के बदले पुर्तगाली क्राउन को वार्षिक कर देने पर सहमति व्यक्त की थी।",
        "opts_en": EN_AR_OPTS,
        "opts_hi": HI_AR_OPTS,
        "ans": 3,
        "sol_en": "Both A and R are false. The Portuguese administration was bankrupt, and the Peshwa did not pay tribute; instead, the Portuguese lost their Northern Province and were forced to pay concessions to avoid a Maratha invasion of Goa.",
        "sol_hi": "A और R दोनों गलत हैं। पुर्तगाली प्रशासन दिवालिया था, और पेशवा ने कोई कर नहीं दिया; इसके विपरीत, पुर्तगालियों ने अपना उत्तरी प्रांत खो दिया और गोवा पर मराठा आक्रमण से बचने के लिए रियायतें देने को मजबूर हुए।"
    },

    # 5 Statement-Based (45 to 49)
    {
        "type": "Statement-Based",
        "q_en": "Consider the following statements regarding the Mughal capture of Hugli in 1632:\n1. The siege was ordered by Emperor Shah Jahan and executed by Qasim Khan.\n2. The Portuguese garrison was completely reinforced by the British Navy.\nWhich of the statements given above is/are correct?",
        "q_hi": "1632 में मुगलों द्वारा हुगली पर कब्जे के संबंध में निम्नलिखित कथनों पर विचार करें:\n1. घेराबंदी का आदेश सम्राट शाहजहां ने दिया था और इसे कासिम खान ने अंजाम दिया था।\n2. पुर्तगाली गैरीसन को ब्रिटिश नौसेना द्वारा पूरी तरह से सहायता प्रदान की गई थी।\nउपरोक्त कथनों में से कौन सा/से सही है/हैं?",
        "opts_en": ["1 only", "2 only", "Both 1 and 2", "Neither 1 nor 2"],
        "opts_hi": ["केवल 1", "केवल 2", "1 और 2 दोनों", "न तो 1 न ही 2"],
        "ans": 0,
        "sol_en": "Statement 1 is correct. Statement 2 is incorrect because the British did not support the Portuguese; in fact, the British benefited from the removal of their Portuguese trade rivals.",
        "sol_hi": "कथन 1 सही है। कथन 2 गलत है क्योंकि अंग्रेजों ने पुर्तगालियों का समर्थन नहीं किया था; वास्तव में, अंग्रेजों को अपने पुर्तगाली व्यापारिक प्रतिद्वंद्वियों के हटने से लाभ हुआ था।"
    },
    {
        "type": "Statement-Based",
        "q_en": "Consider the following statements regarding the Maratha conquest of Bassein (1739):\n1. The campaign was led by Chimaji Appa as part of Peshwa Baji Rao I's expansionist policy.\n2. The treaty signed after the surrender required the Portuguese to completely evacuate Goa.\nWhich of the statements given above is/are correct?",
        "q_hi": "वसई पर मराठा विजय (1739) के संबंध में निम्नलिखित कथनों पर विचार करें:\n1. इस अभियान का नेतृत्व पेशवा बाजीराव प्रथम की विस्तारवादी नीति के तहत चिमाजी अप्पा ने किया था।\n2. आत्मसमर्पण के बाद हस्ताक्षरित संधि में पुर्तगालियों को गोवा को पूरी तरह से खाली करने की आवश्यकता थी।\nउपरोक्त कथनों में से कौन सा/से सही है/हैं?",
        "opts_en": ["1 only", "2 only", "Both 1 and 2", "Neither 1 nor 2"],
        "opts_hi": ["केवल 1", "केवल 2", "1 और 2 दोनों", "न तो 1 न ही 2"],
        "ans": 0,
        "sol_en": "Statement 1 is correct. Statement 2 is incorrect because the Portuguese were allowed to keep Goa, Daman, and Diu, though they had to surrender the entire Northern Province (including Bassein).",
        "sol_hi": "कथन 1 सही है। कथन 2 गलत है क्योंकि पुर्तगालियों को गोवा, दमन और दीव रखने की अनुमति दी गई थी, हालांकि उन्हें पूरे उत्तरी प्रांत (वसई सहित) को सौंपना पड़ा था।"
    },
    {
        "type": "Statement-Based",
        "q_en": "Consider the following statements regarding the sale of offices (venda de cargos) in Portuguese India:\n1. It was introduced as a temporary measure and abolished within ten years by royal decree.\n2. It allowed private buyers to treat military fortress captaincies as personal profit-making estates.\nWhich of the statements given above is/are correct?",
        "q_hi": "पुर्तगाली भारत में पदों की बिक्री (वेंडा दे कार्गोस) के संबंध में निम्नलिखित कथनों पर विचार करें:\n1. इसे एक अस्थायी उपाय के रूप में पेश किया गया था और शाही आदेश द्वारा दस साल के भीतर समाप्त कर दिया गया था।\n2. इसने निजी खरीदारों को सैन्य किले की कप्तानी को व्यक्तिगत लाभ कमाने वाली जागीर के रूप में मानने की अनुमति दी।\nउपरोक्त कथनों में से कौन सा/से सही है/हैं?",
        "opts_en": ["1 only", "2 only", "Both 1 and 2", "Neither 1 nor 2"],
        "opts_hi": ["केवल 1", "केवल 2", "1 और 2 दोनों", "न तो 1 न ही 2"],
        "ans": 1,
        "sol_en": "Statement 1 is incorrect because the sale of offices persisted throughout the 17th and 18th centuries due to chronic treasury deficits. Statement 2 is correct; buyers ran fortresses for personal trade profit to recoup their investment.",
        "sol_hi": "कथन 1 गलत है क्योंकि खजाने के पुराने घाटे के कारण 17वीं और 18वीं शताब्दी में पदों की बिक्री जारी रही। कथन 2 सही है; खरीदारों ने अपने निवेश की भरपाई के लिए व्यक्तिगत व्यापार लाभ के लिए किलों का संचालन किया।"
    },
    {
        "type": "Statement-Based",
        "q_en": "Consider the following statements regarding 'trato particular' in the Estado da Índia:\n1. It was officially encouraged by the Crown from the beginning to reduce administrative salaries.\n2. It involved officials engaging in private trade, often utilizing crown ships and resources.\nWhich of the statements given above is/are correct?",
        "q_hi": "एस्टाडो दा इंडिया में 'त्रातो पर्टिकुलर' के संबंध में निम्नलिखित कथनों पर विचार करें:\n1. प्रशासनिक वेतन को कम करने के लिए शुरू से ही क्राउन द्वारा इसे आधिकारिक रूप से प्रोत्साहित किया गया था।\n2. इसमें अधिकारी निजी व्यापार में शामिल होते थे, अक्सर शाही जहाजों और संसाधनों का उपयोग करते थे।\nउपरोक्त कथनों में से कौन सा/से सही है/हैं?",
        "opts_en": ["1 only", "2 only", "Both 1 and 2", "Neither 1 nor 2"],
        "opts_hi": ["केवल 1", "केवल 2", "1 और 2 दोनों", "न तो 1 न ही 2"],
        "ans": 1,
        "sol_en": "Statement 1 is incorrect because the Crown initially banned private trade to protect its royal monopolies, only tolerating it later due to inability to pay salaries. Statement 2 is correct.",
        "sol_hi": "कथन 1 गलत है क्योंकि क्राउन ने शुरुआत में अपने शाही एकाधिकार की रक्षा के लिए निजी व्यापार पर प्रतिबंध लगा दिया था, बाद में वेतन देने में असमर्थता के कारण इसे सहन किया गया। कथन 2 सही है।"
    },
    {
        "type": "Statement-Based",
        "q_en": "Consider the following statements regarding the role of the Keladi Nayakas in resisting the Portuguese:\n1. The Keladi Nayakas successfully captured the Portuguese fortresses of Mangalore and Honavar.\n2. The Keladi rulers formed a permanent military alliance with the Dutch VOC to expel the Portuguese from Goa.\nWhich of the statements given above is/are correct?",
        "q_hi": "पुर्तगालियों का विरोध करने में केलादि नायकों की भूमिका के संबंध में निम्नलिखित कथनों पर विचार करें:\n1. केलादि नायकों ने मैंगलोर और होनावर के पुर्तगाली किलों पर सफलतापूर्वक कब्जा कर लिया था।\n2. केलादि शासकों ने पुर्तगालियों को गोवा से बाहर निकालने के लिए डच वीओसी के साथ एक स्थायी सैन्य गठबंधन बनाया था।\nउपरोक्त कथनों में से कौन सा/से सही है/हैं?",
        "opts_en": ["1 only", "2 only", "Both 1 and 2", "Neither 1 nor 2"],
        "opts_hi": ["केवल 1", "केवल 2", "1 और 2 दोनों", "न तो 1 न ही 2"],
        "ans": 0,
        "sol_en": "Statement 1 is correct; the Keladi Nayakas pushed the Portuguese out of several Canara forts. Statement 2 is incorrect because while they traded with the Dutch, they did not form a permanent alliance to invade Goa.",
        "sol_hi": "कथन 1 सही है; केलादि नायकों ने पुर्तगालियों को कई कनारा किलों से बाहर खदेड़ दिया। कथन 2 गलत है क्योंकि जबकि उन्होंने डचों के साथ व्यापार किया, उन्होंने गोवा पर आक्रमण करने के लिए कोई स्थायी गठबंधन नहीं बनाया था।"
    },

    # 12 Open (Why, How, Case Study, Teach the Concept) (50 to 61)
    {
        "type": "Why",
        "q_en": "Why did the short three-year tenure of Portuguese Viceroys in India lead to administrative corruption and decay?",
        "q_hi": "भारत में पुर्तगाली वायसरायों का छोटा तीन साल का कार्यकाल प्रशासनिक भ्रष्टाचार और पतन का कारण क्यों बना?",
        "sol_en": "The short tenure of three years gave viceroys and governors little security or long-term interest in the colony's infrastructure or defense. Since they knew their time was limited, they focused almost exclusively on accumulating personal wealth as quickly as possible. This led to widespread acceptance of bribes, neglect of fortress repairs, and the diversion of state resources into private commercial ventures, leaving the Estado da Índia financially weak and militarily vulnerable.",
        "sol_hi": "तीन साल के छोटे कार्यकाल ने वायसरायों और गवर्नरों को कॉलोनी के बुनियादी ढांचे या रक्षा में बहुत कम सुरक्षा या दीर्घकालिक रुचि दी। चूंकि वे जानते थे कि उनका समय सीमित था, इसलिए उन्होंने लगभग विशेष रूप से जितनी जल्दी हो सके व्यक्तिगत संपत्ति जमा करने पर ध्यान केंद्रित किया। इससे बड़े पैमाने पर रिश्वतखोरी, किलों की मरम्मत की उपेक्षा और निजी वाणिज्यिक उपक्रमों में राज्य के संसाधनों का विचलन हुआ, जिससे एस्टाडो दा इंडिया वित्तीय रूप से कमजोर और सैन्य रूप से असुरक्षित हो गया।"
    },
    {
        "type": "Why",
        "q_en": "Why did Shah Jahan decide to use military force to expel the Portuguese from Bengal in 1632?",
        "q_hi": "शाहजहां ने 1632 में बंगाल से पुर्तगालियों को खदेड़ने के लिए सैन्य बल का उपयोग करने का निर्णय क्यों लिया?",
        "sol_en": "The Portuguese at Hugli had grown arrogant and actively flouted Mughal authority. They engaged in piracy in the Bay of Bengal, blockaded local trade, and captured Mughal subjects to sell into slavery. Furthermore, they conducted forced religious conversions of local residents, including women belonging to the Mughal imperial household. When they fortified Hugli without imperial permission and refused to pay customs duties, Shah Jahan ordered Qasim Khan to crush their settlement.",
        "sol_hi": "हुगली में पुर्तगाली अहंकारी हो गए थे और उन्होंने मुगल सत्ता की सक्रिय रूप से उपेक्षा की थी। वे बंगाल की खाड़ी में समुद्री डकैती में शामिल थे, स्थानीय व्यापार की नाकेबंदी करते थे और मुगल प्रजा को पकड़कर गुलामी में बेचते थे। इसके अलावा, उन्होंने स्थानीय निवासियों का ईसाई धर्म में जबरन धर्मांतरण कराया, जिनमें मुगल शाही घराने की महिलाएं भी शामिल थीं। जब उन्होंने शाही अनुमति के बिना हुगली की किलेबंदी की और सीमा शुल्क देने से इनकार कर दिया, तो शाहजहां ने कासिम खान को उनकी बस्ती को नष्ट करने का आदेश दिया।"
    },
    {
        "type": "Why",
        "q_en": "Why were the Marathas under Chimaji Appa determined to capture the Portuguese Northern Province (Bassein/Vasai)?",
        "q_hi": "चिमाजी अप्पा के नेतृत्व में मराठे पुर्तगाली उत्तरी प्रांत (वसई/बसीन) पर कब्जा करने के लिए क्यों दृढ़ थे?",
        "sol_en": "The Northern Province was highly fertile and strategically located near the Maratha heartland. The Portuguese presence there blocked Maratha access to the sea and trade routes. Furthermore, the Portuguese had a history of religious intolerance, destroying Hindu temples and persecuting local residents in Salsette and Bassein. Peshwa Baji Rao I and Chimaji Appa launched the campaign to eliminate this foreign threat, claim agricultural revenues, and protect the local Hindu population.",
        "sol_hi": "उत्तरी प्रांत अत्यधिक उपजाऊ था और रणनीतिक रूप से मराठा साम्राज्य के करीब स्थित था। वहां पुर्तगाली उपस्थिति ने समुद्र और व्यापार मार्गों तक मराठा पहुंच को अवरुद्ध कर दिया था। इसके अलावा, पुर्तगालियों का धार्मिक असहिष्णुता का इतिहास रहा था, जिसमें उन्होंने साल्सेट और वसई में हिंदू मंदिरों को नष्ट किया और स्थानीय निवासियों को प्रताड़ित किया। पेशवा बाजीराव प्रथम और चिमाजी अप्पा ने इस विदेशी खतरे को खत्म करने, कृषि राजस्व का दावा करने और स्थानीय हिंदू आबादी की रक्षा के लिए अभियान शुरू किया।"
    },
    {
        "type": "How",
        "q_en": "How did the practice of 'venda de cargos' (sale of offices) undermine the military defense of the Estado da Índia?",
        "q_hi": "पदों की बिक्री (venda de cargos) की प्रथा ने एस्टाडो दा इंडिया की सैन्य रक्षा को कैसे कमजोर किया?",
        "sol_en": "To pay off debts, the Portuguese Crown sold military captaincies and administrative posts to the highest bidder rather than appointing officers based on merit or experience. Wealthy buyers viewed these offices as financial investments. Upon taking office, they focused on recouping their purchase costs through illegal trade and bribes, neglecting military training, failing to maintain fortress walls, and under-supplying garrisons with ammunition, leading to rapid military collapses during Dutch and Maratha attacks.",
        "sol_hi": "ऋण चुकाने के लिए, पुर्तगाली क्राउन ने योग्यता या अनुभव के आधार पर अधिकारियों की नियुक्ति करने के बजाय सैन्य कप्तानी और प्रशासनिक पदों को उच्चतम बोलीदाता को बेच दिया। अमीर खरीदार इन पदों को वित्तीय निवेश के रूप में देखते थे। पद संभालने के बाद, उन्होंने अवैध व्यापार और रिश्वत के माध्यम से अपनी खरीद लागत वसूलने पर ध्यान केंद्रित किया, जिससे सैन्य प्रशिक्षण की उपेक्षा हुई, किलों की दीवारों के रखरखाव में विफलता हुई और चौकियों में गोला-बारूद की कमी हो गई, जिसके कारण डच और मराठा हमलों के दौरान तेजी से सैन्य पतन हुआ।"
    },
    {
        "type": "How",
        "q_en": "How did the Marathas execute the siege of Bassein in 1737-1739 to overcome its heavy fortifications?",
        "q_hi": "मराठों ने वसई के भारी किलों पर काबू पाने के लिए 1737-1739 में उसकी घेराबंदी को कैसे अंजाम दिया?",
        "sol_en": "The Marathas under Chimaji Appa realized that Bassein's stone walls could not be breached by simple artillery fire. They utilized advanced mining techniques, digging tunnels under the bastions and placing heavy gunpowder charges to blow up sections of the walls. Simultaneously, they blockaded the fort by sea using Maratha naval forces to prevent Goa from sending reinforcements. After heavy infantry assaults and suffering significant casualties, they forced the isolated Portuguese garrison to surrender.",
        "sol_hi": "चिमाजी अप्पा के नेतृत्व में मराठों ने महसूस किया कि वसई की पत्थरों की दीवारों को साधारण तोपखाने की आग से नहीं तोड़ा जा सकता। उन्होंने उन्नत माइनिंग (सुरंग) तकनीकों का उपयोग किया, बुर्जों के नीचे सुरंगें खोदीं और दीवारों के हिस्सों को उड़ाने के लिए भारी बारूद लगाया। साथ ही, उन्होंने गोवा को सुदृढीकरण भेजने से रोकने के लिए मराठा नौसैनिक बलों का उपयोग करके समुद्र मार्ग से किले की नाकेबंदी की। भारी पैदल सेना के हमलों और महत्वपूर्ण हताहतों के बाद, उन्होंने अलग-थलग पड़े पुर्तगाली गैरीसन को आत्मसमर्पण करने के लिए मजबूर कर दिया।"
    },
    {
        "type": "How",
        "q_en": "How did 'trato particular' divert trade profits away from the Portuguese Crown and into private hands?",
        "q_hi": "'त्रातो पर्टिकुलर' ने व्यापारिक लाभ को पुर्तगाली क्राउन से हटाकर निजी हाथों में कैसे मोड़ दिया?",
        "sol_en": "Under 'trato particular', Portuguese officials used their official positions and royal cargo ships to conduct private, unlicensed trade. Instead of collecting duties and spices for the Crown's monopoly, they loaded their own goods, traded directly with local merchants, and pocketed the profits. They also underreported customs collections at ports like Goa and Ormuz, taking bribes from private traders to allow smuggling. This starved the Lisbon treasury of the revenue needed to maintain the navy.",
        "sol_hi": "'त्रातो पर्टिकुलर' के तहत, पुर्तगाली अधिकारियों ने निजी, बिना लाइसेंस के व्यापार करने के लिए अपने आधिकारिक पदों और शाही मालवाहक जहाजों का उपयोग किया। क्राउन के एकाधिकार के लिए सीमा शुल्क और मसालों को इकट्ठा करने के बजाय, उन्होंने अपना खुद का सामान लादा, स्थानीय व्यापारियों के साथ सीधे व्यापार किया और मुनाफे को जेब में रख लिया। उन्होंने गोवा और होर्मुज जैसे बंदरगाहों पर सीमा शुल्क संग्रह को भी कम दिखाया, जिससे निजी व्यापारियों से रिश्वत लेकर तस्करी की अनुमति दी गई। इसने लिस्बन खजाने को नौसेना के रखरखाव के लिए आवश्यक राजस्व से वंचित कर दिया।"
    },
    {
        "type": "Case Study",
        "q_en": "Case Study: The Mughal siege and capture of Hugli (1632) as an example of regional power pushback.",
        "q_hi": "केस स्टडी: क्षेत्रीय शक्ति के विरोध के उदाहरण के रूप में 1632 में मुगलों द्वारा हुगली की घेराबंदी और कब्जा।",
        "sol_en": "In 1632, the Mughals mobilized a force of over 150,000 men and a large river flotilla to besiege the Portuguese settlement of Hugli. The siege lasted for three months, during which the Mughals cut off all supply lines, blocked the Hugli River with boats, and used mines to blow up the Portuguese fortifications. This case study illustrates that when regional powers consolidated their administrative and military power, the Portuguese, operating far from their naval base in Goa, could not sustain their positions on land against superior Indian armies.",
        "sol_hi": "1632 में, मुगलों ने हुगली की पुर्तगाली बस्ती को घेरने के लिए 1,50,000 से अधिक पुरुषों और एक बड़े नदी बेड़े को जुटाया। यह घेराबंदी तीन महीने तक चली, जिसके दौरान मुगलों ने सभी आपूर्ति लाइनों को काट दिया, नावों के साथ हुगली नदी को अवरुद्ध कर दिया और पुर्तगाली किलेबंदी को उड़ाने के लिए सुरंगों का उपयोग किया। यह केस स्टडी दर्शाती है कि जब क्षेत्रीय शक्तियों ने अपनी प्रशासनिक और सैन्य शक्ति को मजबूत किया, तो गोवा में अपने नौसैनिक अड्डे से बहुत दूर काम करने वाले पुर्तगाली, बेहतर भारतीय सेनाओं के खिलाफ जमीन पर अपनी स्थिति बनाए नहीं रख सके।"
    },
    {
        "type": "Case Study",
        "q_en": "Case Study: The Maratha siege of Bassein (1737-1739) and the collapse of the Portuguese Província do Norte.",
        "q_hi": "केस स्टडी: मराठों द्वारा वसई की घेराबंदी (1737-1739) और पुर्तगाली उत्तरी प्रांत (प्रॉविन्सिया डो नॉर्ट) का पतन।",
        "sol_en": "The campaign of 1737-1739 was a coordinated Maratha assault on the Portuguese Northern Province. Chimaji Appa captured Thana and isolated Bassein. The Portuguese defended Bassein courageously for over two years, but without naval superiority and reinforcement from Lisbon, they were overwhelmed. This case study shows that the loss of Bassein stripped Portuguese India of its most valuable agricultural and revenue-yielding territory, restricting their empire to a small coastal pocket in Goa, Daman, and Diu.",
        "sol_hi": "1737-1739 का अभियान पुर्तगाली उत्तरी प्रांत पर एक समन्वित मराठा हमला था। चिमाजी अप्पा ने ठाणे पर कब्जा कर लिया और वसई को अलग-थलग कर दिया। पुर्तगालियों ने दो साल से अधिक समय तक साहसपूर्वक वसई की रक्षा की, लेकिन नौसैनिक श्रेष्ठता और लिस्बन से कुमक के बिना, वे पराजित हो गए। यह केस स्टडी दर्शाती है कि वसई के नुकसान ने पुर्तगाली भारत को उसके सबसे मूल्यवान कृषि और राजस्व देने वाले क्षेत्र से वंचित कर दिया, जिससे उनका साम्राज्य गोवा, दमन और दीव में एक छोटे से तटीय क्षेत्र तक सीमित रह गया।"
    },
    {
        "type": "Case Study",
        "q_en": "Case Study: The systemic corruption of the Portuguese customs house at Goa and the rise of contraband trade.",
        "q_hi": "केस STUDY: गोवा में पुर्तगाली सीमा शुल्क कार्यालय का प्रणालीगत भ्रष्टाचार और तस्करी व्यापार का उदय।",
        "sol_en": "In the late 17th century, Goa's official customs revenues fell by over 60%, despite continued high volumes of trade. Investigations revealed that customs officials, in league with local Saraswat merchants, allowed ships to unload goods without paying duties in exchange for private payoffs. This case study demonstrates how institutional corruption eroded the financial base of the state, as the wealth generated by trade went entirely to private individuals, leaving the Crown unable to pay for ship repairs or soldier wages.",
        "sol_hi": "17वीं शताब्दी के अंत में, व्यापार की उच्च मात्रा जारी रहने के बावजूद, गोवा का आधिकारिक सीमा शुल्क राजस्व 60% से अधिक गिर गया। जांच से पता चला कि सीमा शुल्क अधिकारियों ने, स्थानीय सारस्वत व्यापारियों के साथ मिलकर, निजी भुगतान के बदले जहाजों को सीमा शुल्क चुकाए बिना सामान उतारने की अनुमति दी थी। यह केस स्टडी दर्शाती है कि कैसे संस्थागत भ्रष्टाचार ने राज्य के वित्तीय आधार को नष्ट कर दिया, क्योंकि व्यापार द्वारा उत्पन्न धन पूरी तरह से निजी व्यक्तियों के पास गया, जिससे क्राउन जहाजों की मरम्मत या सैनिकों के वेतन का भुगतान करने में असमर्थ हो गया।"
    },
    {
        "type": "Teach the Concept",
        "q_en": "Teach the Concept: The difference between state-monopoly trade and unauthorized private trade (trato particular).",
        "q_hi": "अवधारणा समझाएं: राज्य-एकाधिकार व्यापार और अनधिकृत निजी व्यापार (त्रातो पर्टिकुलर) के बीच अंतर।",
        "sol_en": "Explain that state-monopoly trade is controlled directly by the government (the Crown), where all goods must be bought and sold through royal factories, and profits go to the state treasury to fund public services and defense. Unauthorized private trade (trato particular) occurs when government officials use state assets to conduct trade for their personal benefit, bypassing official customs. This deprives the state of revenue, leads to systemic corruption, and compromises the empire's ability to maintain its military forces.",
        "sol_hi": "समझाएं कि राज्य-एकाधिकार व्यापार सीधे सरकार (क्राउन) द्वारा नियंत्रित किया जाता है, जहां सभी सामान शाही कारखानों के माध्यम से खरीदे और बेचे जाने चाहिए, और मुनाफा सार्वजनिक सेवाओं और रक्षा के वित्तपोषण के लिए राज्य के खजाने में जाता है। अनधिकृत निजी व्यापार (त्रातो पर्टिकुलर) तब होता है जब सरकारी अधिकारी अपने व्यक्तिगत लाभ के लिए व्यापार करने के लिए राज्य की संपत्ति का उपयोग करते हैं, जिससे आधिकारिक सीमा शुल्क की अनदेखी होती है। यह राज्य को राजस्व से वंचित करता है, प्रणालीगत भ्रष्टाचार को जन्म देता है और अपनी सैन्य बलों को बनाए रखने की साम्राज्य की क्षमता से समझौता करता है।"
    },
    {
        "type": "Teach the Concept",
        "q_en": "Teach the Concept: The geopolitical role of the 'Northern Province' (Província do Norte) in the Portuguese Empire.",
        "q_hi": "अवधारणा समझाएं: पुर्तगाली साम्राज्य में 'उत्तरी प्रांत' (प्रॉविन्सिया डो नॉर्ट) की भू-राजनीतिक भूमिका।",
        "sol_en": "Explain that the Província do Norte, spanning from Chaul to Daman, was the economic backbone of Portuguese India. Unlike Goa, which was a trade city dependent on imported food, the Northern Province had vast agricultural lands that produced rice and wheat to feed the empire. It was also rich in forests, supplying teakwood for shipbuilding. Understanding this role explains why the Maratha conquest of the Northern Province in 1739 was not just a military defeat, but an economic catastrophe that permanently ended Portuguese imperial ambitions in India.",
        "sol_hi": "समझाएं कि चोल से दमन तक फैला उत्तरी प्रांत (प्रॉविन्सिया डो नॉर्ट) पुर्तगाली भारत की आर्थिक रीढ़ था। गोवा के विपरीत, जो आयातित भोजन पर निर्भर एक व्यापारिक शहर था, उत्तरी प्रांत में विशाल कृषि भूमि थी जिसने साम्राज्य का पेट भरने के लिए चावल और गेहूं का उत्पादन किया। यह जंगलों से भी समृद्ध था, जिसने जहाज निर्माण के लिए सागौन की लकड़ी की आपूर्ति की। इस भूमिका को समझने से यह स्पष्ट होता है कि 1739 में उत्तरी प्रांत पर मराठों की विजय केवल एक सैन्य हार नहीं थी, बल्कि एक आर्थिक तबाही थी जिसने भारत में पुर्तगाली साम्राज्यवादी महत्वाकांक्षाओं को स्थायी रूप से समाप्त कर दिया।"
    },
    {
        "type": "Teach the Concept",
        "q_en": "Teach the Concept: The administrative structure of the Estado da Índia and the division of civil, financial, and military power.",
        "q_hi": "अवधारणा समझाएं: एस्टाडो दा इंडिया की प्रशासनिक संरचना और नागरिक, वित्तीय और सैन्य शक्ति का विभाजन।",
        "sol_en": "Explain that the Portuguese administration was headed by the Viceroy or Governor, who held supreme civil and military authority. However, to prevent abuse of power, the Crown created the 'Vedor da Fazenda' (financial superintendent) to control treasury decisions independently. Fortress captains (Capitães) ruled local forts with significant autonomy. This division of power often resulted in administrative conflicts and delays, as viceroys and financial heads frequently clashed over funds, which weakened military preparedness during crises.",
        "sol_hi": "समझाएं कि पुर्तगाली प्रशासन का नेतृत्व वायसराय या गवर्नर द्वारा किया जाता था, जिसके पास सर्वोच्च नागरिक और सैन्य अधिकार होते थे। हालांकि, सत्ता के दुरुपयोग को रोकने के लिए, क्राउन ने स्वतंत्र रूप से खजाने के निर्णयों को नियंत्रित करने के लिए 'वेडोर दा फजेंडा' (वित्तीय अधीक्षक) का पद बनाया। किले के कप्तानों (Capitães) ने महत्वपूर्ण स्वायत्तता के साथ स्थानीय किलों पर शासन किया। शक्ति का यह विभाजन अक्सर प्रशासनिक संघर्षों और देरी का कारण बनता था, क्योंकि वायसराय और वित्तीय प्रमुख अक्सर धन को लेकर आपस में भिड़ जाते थे, जिससे संकट के समय सैन्य तैयारी कमजोर हो जाती थी।"
    }
]
