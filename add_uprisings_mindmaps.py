#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os, re, json

BASE_DIR = r"upsc/modern_history/Peasant-and-Tribal-Uprisings"

MINDMAP_DATA = {
    "military-discontent-uprisings-paika-rebellion": {
        "en": [
            {"label": "Origins & Leaders", "type": "branch", "date": "1817 Odisha", "children": [
                {"label": "Bakshi Jagabandhu: Military chief of the displaced Khurda Raja, led the revolt", "type": "leaf"},
                {"label": "Paikas: Traditional landed militia of Odisha who performed military duties in exchange for rent-free land", "type": "leaf"}]},
            {"label": "Causes & Events", "type": "branch", "date": "Causes", "children": [
                {"label": "British land revenue policies displaced Paikas and disrupted traditional agrarian structure", "type": "leaf"},
                {"label": "Introduction of cowrie currency and artificial rise in salt prices caused massive local distress", "type": "leaf"},
                {"label": "Rebels captured Puri and temporarily drove British forces out of Khurda", "type": "leaf"}]}
        ],
        "hi": [
            {"label": "उत्पत्ति और नेता", "type": "branch", "date": "1817 ओडिशा", "children": [
                {"label": "बख्शी जगबंधु: विस्थापित खुर्दा राजा के सेनापति, जिन्होंने विद्रोह का नेतृत्व किया", "type": "leaf"},
                {"label": "पाइक: ओडिशा के पारंपरिक भू-धारक सैनिक जिन्हें कर-मुक्त भूमि के बदले सैन्य सेवाएं देनी होती थीं", "type": "leaf"}]},
            {"label": "कारण और घटनाएँ", "type": "branch", "date": "कारण", "children": [
                {"label": "ब्रिटिश भू-राजस्व नीतियों ने पाइकों को विस्थापित किया और पारंपरिक कृषि ढांचे को नष्ट किया", "type": "leaf"},
                {"label": "कौड़ी मुद्रा की समाप्ति और नमक की कीमतों में कृत्रिम वृद्धि से भारी स्थानीय संकट पैदा हुआ", "type": "leaf"},
                {"label": "विद्रोहियों ने पुरी पर कब्जा कर लिया और अस्थायी रूप से ब्रिटिश सेना को खुर्दा से खदेड़ दिया", "type": "leaf"}]}
        ]
    },
    "military-discontent-uprisings-ramosi-uprising": {
        "en": [
            {"label": "Ramosi Clan", "type": "branch", "date": "Western Ghats", "children": [
                {"label": "Ramosis: Hill tribe of Western Ghats who served in Maratha army/administration", "type": "leaf"},
                {"label": "Chittur Singh (1822) & Umaji Naik (1825-26): Key leaders of the uprisings", "type": "leaf"}]},
            {"label": "Causes", "type": "branch", "date": "Causes", "children": [
                {"label": "Deposition of Raja Pratapsinh of Satara & Maratha kingdom annexation by British", "type": "leaf"},
                {"label": "Agrarian distress, high land revenue demands, and severe famine in Satara region", "type": "leaf"}]}
        ],
        "hi": [
            {"label": "रामोसी जनजाति", "type": "branch", "date": "पश्चिमी घाट", "children": [
                {"label": "रामोसी: पश्चिमी घाट की पहाड़ी जनजाति जिसने मराठा सेना/प्रशासन में सेवा दी थी", "type": "leaf"},
                {"label": "चित्तूर सिंह (1822) और उमाजी नाइक (1825-26): विद्रोहों के प्रमुख नेता", "type": "leaf"}]},
            {"label": "कारण", "type": "branch", "date": "कारण", "children": [
                {"label": "सतारा के राजा प्रतापसिंह की गद्दी से बेदखली और ब्रिटिश द्वारा मराठा साम्राज्य का विलय", "type": "leaf"},
                {"label": "कृषि संकट, अत्यधिक भू-राजस्व की मांग और सतारा क्षेत्र में पड़ा भीषण अकाल", "type": "leaf"}]}
        ]
    },
    "military-discontent-uprisings-sawantwadi-revolt": {
        "en": [
            {"label": "Context & Spark", "type": "branch", "date": "1844 Ratnagiri", "children": [
                {"label": "Sawantwadi: Border state near Goa/Ratnagiri; led by Phond Sawant and Anna Sahib", "type": "leaf"},
                {"label": "Triggered by British administrative interference and deposition of local Sawantwadi ruler", "type": "leaf"},
                {"label": "Rebels captured local forts, declared independence, and engaged in guerrilla warfare until suppressed in 1845", "type": "leaf"}]}
        ],
        "hi": [
            {"label": "संदर्भ और कारण", "type": "branch", "date": "1844 रत्नागिरी", "children": [
                {"label": "सावंतवाड़ी: गोवा/रत्नागिरी के पास सीमावर्ती राज्य; फोंड सावंत और अन्ना साहब द्वारा नेतृत्व", "type": "leaf"},
                {"label": "ब्रिटिश प्रशासनिक हस्तक्षेप और स्थानीय सावंतवाड़ी शासक की गद्दी से बेदखली के कारण भड़का", "type": "leaf"},
                {"label": "विद्रोहियों ने स्थानीय किलों पर कब्जा किया, स्वतंत्रता की घोषणा की और 1845 में दमन होने तक गुरिल्ला युद्ध लड़ा", "type": "leaf"}]}
        ]
    },
    "peasant-movements-bardoli-movement": {
        "en": [
            {"label": "Satyagraha & Leaders", "type": "branch", "date": "1928 Gujarat", "children": [
                {"label": "Sardar Vallabhbhai Patel: Led the satyagraha (title 'Sardar' given by Bardoli women)", "type": "leaf"},
                {"label": "Women played active role: Mithuben Petit, Kasturba Gandhi organized campaigns", "type": "leaf"}]},
            {"label": "Cause & Inquiry", "type": "branch", "date": "Outcome", "children": [
                {"label": "Bombay Presidency increased land revenue by 30% despite agrarian distress", "type": "leaf"},
                {"label": "Maxwell-Broomfield Commission appointed after successful non-cooperation/revenue boycott", "type": "leaf"},
                {"label": "Commission reduced the revenue hike to 6.03%, marking a complete peasant victory", "type": "leaf"}]}
        ],
        "hi": [
            {"label": "सत्याग्रह और नेता", "type": "branch", "date": "1928 गुजरात", "children": [
                {"label": "सरदार वल्लभभाई पटेल: सत्याग्रह का नेतृत्व किया (बारडोली की महिलाओं द्वारा 'सरदार' उपाधि दी गई)", "type": "leaf"},
                {"label": "महिलाओं ने सक्रिय भूमिका निभाई: मिट्ठूबेन पेटिट, कस्तूरबा गांधी ने अभियानों का आयोजन किया", "type": "leaf"}]},
            {"label": "कारण और परिणाम", "type": "branch", "date": "परिणाम", "children": [
                {"label": "कृषि संकट के बावजूद बॉम्बे प्रेसीडेंसी द्वारा भू-राजस्व में 30% की वृद्धि की गई", "type": "leaf"},
                {"label": "सफल राजस्व बहिष्कार/असहयोग आंदोलन के बाद मैक्सवेल-ब्रूमफील्ड आयोग नियुक्त किया गया", "type": "leaf"},
                {"label": "आयोग ने राजस्व वृद्धि को घटाकर 6.03% कर दिया, जिससे किसानों की पूर्ण विजय हुई", "type": "leaf"}]}
        ]
    },
    "peasant-movements-champaran-satyagraha": {
        "en": [
            {"label": "First Satyagraha", "type": "branch", "date": "1917 Bihar", "children": [
                {"label": "Mahatma Gandhi's first civil disobedience movement in India", "type": "leaf"},
                {"label": "Rajkumar Shukla: Invited Gandhi to Champaran to inspect plight of peasants", "type": "leaf"}]},
            {"label": "Tinkathia System", "type": "branch", "date": "System", "children": [
                {"label": "Peasants legally bound to grow indigo on 3/20th of their land (Tinkathia)", "type": "leaf"},
                {"label": "Exploitation by British planters who demanded high rents and illegal dues", "type": "leaf"}]},
            {"label": "Resolution", "type": "branch", "date": "Outcome", "children": [
                {"label": "Champaran Agrarian Committee formed (Gandhi was member)", "type": "leaf"},
                {"label": "Act abolished Tinkathia system and refunded 25% of illegal extractions to peasants", "type": "leaf"}]}
        ],
        "hi": [
            {"label": "प्रथम सत्याग्रह", "type": "branch", "date": "1917 बिहार", "children": [
                {"label": "भारत में महात्मा गांधी का पहला सविनय अवज्ञा आंदोलन", "type": "leaf"},
                {"label": "राजकुमार शुक्ल: गांधीजी को किसानों की दुर्दशा देखने के लिए चंपारण आमंत्रित किया", "type": "leaf"}]},
            {"label": "तिनकठिया प्रणाली", "type": "branch", "date": "प्रणाली", "children": [
                {"label": "किसानों को अपनी भूमि के 3/20वें हिस्से (तिनकठिया) पर नील उगाने के लिए कानूनी रूप से बाध्य किया गया था", "type": "leaf"},
                {"label": "ब्रिटिश बागान मालिकों द्वारा अत्यधिक लगान और अवैध कर वसूल कर शोषण", "type": "leaf"}]},
            {"label": "समाधान", "type": "branch", "date": "परिणाम", "children": [
                {"label": "चंपारण कृषि समिति का गठन हुआ (गांधीजी इसके सदस्य थे)", "type": "leaf"},
                {"label": "अधिनियम द्वारा तिनकठिया प्रणाली समाप्त; अवैध वसूली का 25% हिस्सा किसानों को वापस किया गया", "type": "leaf"}]}
        ]
    },
    "peasant-movements-kheda-peasant-struggle": {
        "en": [
            {"label": "Context & Leaders", "type": "branch", "date": "1918 Gujarat", "children": [
                {"label": "Mahatma Gandhi, Vallabhbhai Patel, and Indulal Yagnik organized the struggle", "type": "leaf"},
                {"label": "Kheda district suffered total crop failure due to severe drought", "type": "leaf"}]},
            {"label": "Conflict", "type": "branch", "date": "Conflict", "children": [
                {"label": "Revenue code allowed tax suspension if yield was under 25%, but British demanded full payment", "type": "leaf"},
                {"label": "Satyagrahis refused to pay tax; government seized cattle and assets in retaliation", "type": "leaf"}]},
            {"label": "Resolution", "type": "branch", "date": "Outcome", "children": [
                {"label": "Secret instructions issued to collect revenue only from those who could afford to pay", "type": "leaf"}]}
        ],
        "hi": [
            {"label": "संदर्भ और नेता", "type": "branch", "date": "1918 गुजरात", "children": [
                {"label": "महात्मा गांधी, वल्लभभाई पटेल और इंदुलाल याज्ञिक ने आंदोलन का आयोजन किया", "type": "leaf"},
                {"label": "भीषण सूखे के कारण खेड़ा जिले में फसल पूरी तरह नष्ट हो गई थी", "type": "leaf"}]},
            {"label": "संघर्ष", "type": "branch", "date": "संघर्ष", "children": [
                {"label": "राजस्व नियमों के अनुसार 25% से कम उपज होने पर कर माफी का प्रावधान था, परंतु अंग्रेजों ने कर अदायगी पर दबाव डाला", "type": "leaf"},
                {"label": "सत्याग्रहियों ने कर देने से इनकार किया; सरकार ने जवाबी कार्रवाई में पशु और संपत्तियां कुर्क कीं", "type": "leaf"}]},
            {"label": "समाधान", "type": "branch", "date": "परिणाम", "children": [
                {"label": "सरकार ने गुप्त आदेश जारी कर केवल समर्थ किसानों से ही राजस्व वसूलने का निर्देश दिया", "type": "leaf"}]}
        ]
    },
    "peasant-movements-reasons-of-resistance-among-peasants": {
        "en": [
            {"label": "Economic Exploitation", "type": "branch", "date": "Causes", "children": [
                {"label": "High land revenue demands under Zamindari, Ryotwari, and Mahalwari systems", "type": "leaf"},
                {"label": "High rental demands, illegal cesses (Abwabs), and forced labor (Begar) by landlords", "type": "leaf"}]},
            {"label": "Indebtedness & Eviction", "type": "branch", "date": "Causes", "children": [
                {"label": "Usurious moneylenders charging high interest rates leading to land alienation", "type": "leaf"},
                {"label": "Frequent evictions of tenants-at-will (unsecured occupancy rights)", "type": "leaf"}]},
            {"label": "Commercialization", "type": "branch", "date": "Causes", "children": [
                {"label": "Forced cultivation of cash crops (indigo, poppy) disrupting food grain production", "type": "leaf"}]}
        ],
        "hi": [
            {"label": "आर्थिक शोषण", "type": "branch", "date": "कारण", "children": [
                {"label": "जमींदारी, रैयतवाड़ी और महालवाड़ी व्यवस्थाओं के तहत अत्यधिक भू-राजस्व की मांग", "type": "leaf"},
                {"label": "जमींदारों द्वारा अत्यधिक लगान, अवैध उपकरों (अबाव) की वसूली और बेगार प्रथा", "type": "leaf"}]},
            {"label": "ऋणग्रस्तता और बेदखली", "type": "branch", "date": "कारण", "children": [
                {"label": "सूदखोर साहूकारों द्वारा उच्च ब्याज दरों के माध्यम से किसानों की भूमि हड़पना (भूमि हस्तांतरण)", "type": "leaf"},
                {"label": "असुरक्षित काश्तकारों (किराएदारों) को मनमाने ढंग से जमीन से बेदखल करना", "type": "leaf"}]},
            {"label": "कृषि का व्यवसायीकरण", "type": "branch", "date": "कारण", "children": [
                {"label": "खाद्यान्न फसलों के स्थान पर नील और अफीम जैसी नकदी फसलों की अनिवार्य खेती से संकट बढ़ा", "type": "leaf"}]}
        ]
    },
    "peasant-movements-tebhaga-movement": {
        "en": [
            {"label": "Tebhaga Demand", "type": "branch", "date": "1946-47 Bengal", "children": [
                {"label": "Led by Bengal Provincial Kisan Sabha (communist organizers Kamparam Singh & Somnath Lahiri)", "type": "leaf"},
                {"label": "Bargadars (sharecroppers) demanded keeping two-thirds ('Tebhaga') of harvest instead of half", "type": "leaf"},
                {"label": "Only one-third share was to be given to Jotedars (landlords)", "type": "leaf"}]},
            {"label": "Slogan & Response", "type": "branch", "date": "Outcome", "children": [
                {"label": "Famous slogan: 'Adhi Noy, Tebhaga Chai' (We want two-thirds, not half)", "type": "leaf"},
                {"label": "Bargadari Bill drafted but delayed; movement lost steam during partition riots", "type": "leaf"}]}
        ],
        "hi": [
            {"label": "तेभागा की मांग", "type": "branch", "date": "1946-47 बंगाल", "children": [
                {"label": "बंगाल प्रांतीय किसान सभा (कम्पाराम सिंह और सोमनाथ लाहिड़ी) के नेतृत्व में संचालित", "type": "leaf"},
                {"label": "बर्गदारों (बटाईदारों) ने फसल का आधा हिस्सा देने के बजाय दो-तिहाई ('तेभागा') अपने पास रखने की मांग की", "type": "leaf"},
                {"label": "जमींदारों (जोतदारों) को केवल एक-तिहाई हिस्सा देने की बात कही गई", "type": "leaf"}]},
            {"label": "नारे और परिणाम", "type": "branch", "date": "परिणाम", "children": [
                {"label": "प्रसिद्ध नारा: 'आधि नॉय, तेभागा चाई' (आधा नहीं, दो-तिहाई चाहिए)", "type": "leaf"},
                {"label": "बर्गदारी विधेयक तैयार किया गया पर लागू होने में देरी हुई; विभाजन के दंगों के कारण आंदोलन धीमा पड़ा", "type": "leaf"}]}
        ]
    },
    "peasant-movements-telangana-movement": {
        "en": [
            {"label": "Context & Feudalism", "type": "branch", "date": "1946-51 Hyderabad", "children": [
                {"label": "Armed peasant rebellion against the Nizam of Hyderabad, Deshmukhs, and Jagirdars", "type": "leaf"},
                {"label": "Aimed at ending extreme feudal oppression, Vetti (forced labor), and illegal land evictions", "type": "leaf"}]},
            {"label": "Armed Struggle", "type": "branch", "date": "Guerrilla", "children": [
                {"label": "Organized by Andhra Mahasabha and Communist Party of India (CPI)", "type": "leaf"},
                {"label": "Peasant guerrilla squads (Sanghams) liberated 3000 villages, redistributed land, abolished Vetti", "type": "leaf"},
                {"label": "Suppressed after Indian military action (Operation Polo, 1948) merged Hyderabad into India", "type": "leaf"}]}
        ],
        "hi": [
            {"label": "संदर्भ और सामंतवाद", "type": "branch", "date": "1946-51 हैदराबाद", "children": [
                {"label": "हैदराबाद के निजाम, देशमुखों और जागीरदारों के खिलाफ सशस्त्र किसान विद्रोह", "type": "leaf"},
                {"label": "चरम सामंती उत्पीड़न, वेत्ति (बंधुआ मजदूरी) और जबरन भूमि बेदखली को समाप्त करना उद्देश्य था", "type": "leaf"}]},
            {"label": "सशस्त्र संघर्ष", "type": "branch", "date": "गुरिल्ला", "children": [
                {"label": "आंध्र महासभा और भारतीय कम्युनिस्ट पार्टी (CPI) द्वारा आयोजित", "type": "leaf"},
                {"label": "किसान गुरिल्ला दस्तों (संघम) ने 3000 गाँवों को मुक्त कराया, भूमि का पुनर्वितरण किया और वेत्ति प्रथा समाप्त की", "type": "leaf"},
                {"label": "1948 में भारतीय सैन्य कार्रवाई (ऑपरेशन पोलो) द्वारा हैदराबाद के भारत में विलय के बाद दमन", "type": "leaf"}]}
        ]
    },
    "reasons-for-limited-success-of-the-uprisings": {
        "en": [
            {"label": "Lacked National Vision", "type": "branch", "date": "Weaknesses", "children": [
                {"label": "Highly localized, isolated, and focused on immediate regional grievances", "type": "leaf"},
                {"label": "Lacked a unified, modern national perspective or alternative socio-economic blueprint", "type": "leaf"}]},
            {"label": "Backward-looking Goal", "type": "branch", "date": "Weaknesses", "children": [
                {"label": "Aimed to restore old feudal relationships, traditional rights, and local autonomy rather than modern democratic structures", "type": "leaf"}]},
            {"label": "Military Deficit", "type": "branch", "date": "Weaknesses", "children": [
                {"label": "Rebels used traditional weapons (bows, arrows, spears) against advanced British firearms & discipline", "type": "leaf"},
                {"label": "Co-optation: British successfully used local loyalist chiefs to divide and suppress rebels", "type": "leaf"}]}
        ],
        "hi": [
            {"label": "राष्ट्रीय दृष्टिकोण की कमी", "type": "branch", "date": "कमजोरियां", "children": [
                {"label": "अत्यधिक स्थानीय, पृथक और केवल तात्कालिक क्षेत्रीय शिकायतों पर केंद्रित थे", "type": "leaf"},
                {"label": "एकजुट, आधुनिक राष्ट्रीय दृष्टिकोण या वैकल्पिक सामाजिक-आर्थिक खाके का अभाव था", "type": "leaf"}]},
            {"label": "प्रतिगामी लक्ष्य", "type": "branch", "date": "कमजोरियां", "children": [
                {"label": "आधुनिक लोकतांत्रिक संरचनाओं के बजाय पुराने सामंती संबंधों, पारंपरिक अधिकारों और स्थानीय स्वायत्तता को बहाल करना लक्ष्य था", "type": "leaf"}]},
            {"label": "सैन्य कमजोरी", "type": "branch", "date": "कमजोरियां", "children": [
                {"label": "विद्रोहियों ने उन्नत ब्रिटिश आग्नेयास्त्रों और अनुशासन के विरुद्ध पारंपरिक हथियारों (धनुष, तीर, भाले) का उपयोग किया", "type": "leaf"},
                {"label": "फूट डालो और राज करो: ब्रिटिश शासकों ने विद्रोहियों को विभाजित करने और दबाने के लिए स्थानीय वफादार प्रमुखों का सफलतापूर्वक उपयोग किया", "type": "leaf"}]}
        ]
    },
    "responsible-factors-for-tribal-revolts": {
        "en": [
            {"label": "Land Alienation", "type": "branch", "date": "Factors", "children": [
                {"label": "Intrusion of non-tribal settlers, moneylenders, and traders (Dikus) who usurped tribal lands", "type": "leaf"},
                {"label": "Introduction of British land revenue system and cash taxation on tribal economies", "type": "leaf"}]},
            {"label": "Forest Acts", "type": "branch", "date": "Factors", "children": [
                {"label": "State reservation of forests restricted traditional rights to gather timber, graze cattle, and practice Podu (shifting cultivation)", "type": "leaf"}]},
            {"label": "Social & Administrative", "type": "branch", "date": "Factors", "children": [
                {"label": "Introduction of British laws and courts undermined traditional tribal panchayats & self-governance", "type": "leaf"},
                {"label": "Christian missionary activities challenged traditional tribal socio-religious customs", "type": "leaf"}]}
        ],
        "hi": [
            {"label": "भूमि का हस्तांतरण", "type": "branch", "date": "कारक", "children": [
                {"label": "गैर-आदिवासी प्रवासियों, साहूकारों और व्यापारियों (दिखुओं) का प्रवेश जिन्होंने आदिवासियों की जमीनें हड़प लीं", "type": "leaf"},
                {"label": "आदिवासी अर्थव्यवस्थाओं पर ब्रिटिश भू-राजस्व प्रणाली और नकद करों का थोपा जाना", "type": "leaf"}]},
            {"label": "वन अधिनियम", "type": "branch", "date": "कारक", "children": [
                {"label": "वनों को सरकारी घोषित करने से लकड़ी संग्रह, मवेशी चराने और पोडू (झूम खेती) करने के पारंपरिक अधिकारों पर प्रतिबंध", "type": "leaf"}]},
            {"label": "सामाजिक और प्रशासनिक", "type": "branch", "date": "कारक", "children": [
                {"label": "ब्रिटिश कानूनों और अदालतों की शुरूआत ने पारंपरिक आदिवासी पंचायतों और स्वशासन को कमजोर किया", "type": "leaf"},
                {"label": "ईसाई मिशनरी गतिविधियों ने पारंपरिक आदिवासी सामाजिक-धार्मिक रीति-रिवाजों को चुनौती दी", "type": "leaf"}]}
        ]
    },
    "revolts-faraizi-revolt": {
        "en": [
            {"label": "Origins & Sect", "type": "branch", "date": "1838-57 Bengal", "children": [
                {"label": "Faraizis: Followers of Islamic reformist sect founded by Haji Shariatullah", "type": "leaf"},
                {"label": "Dudu Miyan (Shariatullah's son): Assumed leadership and converted it into agrarian struggle", "type": "leaf"}]},
            {"label": "Agrarian Conflict", "type": "branch", "date": "Conflict", "children": [
                {"label": "Protested against exploitation of tenant peasants by Hindu zamindars and British indigo planters", "type": "leaf"},
                {"label": "Proclaimed revolutionary doctrine: 'All land belongs to God; no taxes should be paid to rulers'", "type": "leaf"},
                {"label": "Organized armed peasant bands; suppressed by British forces during late 1850s", "type": "leaf"}]}
        ],
        "hi": [
            {"label": "उत्पत्ति और संप्रदाय", "type": "branch", "date": "1838-57 बंगाल", "children": [
                {"label": "फराइजी: हाजी शरियतुल्लाह द्वारा संस्थापित इस्लामी सुधारवादी संप्रदाय के अनुयायी", "type": "leaf"},
                {"label": "दूदू मियां (शरियतुल्लाह के पुत्र): नेतृत्व संभाला और इसे कृषक संघर्ष में बदल दिया", "type": "leaf"}]},
            {"label": "कृषक संघर्ष", "type": "branch", "date": "संघर्ष", "children": [
                {"label": "हिंदू जमींदारों और ब्रिटिश नील बागान मालिकों द्वारा काश्तकार किसानों के शोषण का विरोध किया", "type": "leaf"},
                {"label": "क्रांतिकारी सिद्धांत की घोषणा की: 'सारी भूमि ईश्वर की है; शासकों को कोई कर नहीं दिया जाना चाहिए'", "type": "leaf"},
                {"label": "सशस्त्र किसान दस्तों का गठन किया; 1850 के दशक के अंत में ब्रिटिश सेना द्वारा दमन", "type": "leaf"}]}
        ]
    },
    "revolts-kuka-movement": {
        "en": [
            {"label": "Origins & Leaders", "type": "branch", "date": "1840s-72 Punjab", "children": [
                {"label": "Bhagat Jawahar Mal (Sian Sahib): Founded as religious purification movement in western Punjab", "type": "leaf"},
                {"label": "Baba Ram Singh: Transformed it into a political campaign to restore Sikh rule after annexation", "type": "leaf"}]},
            {"label": "Action Plan", "type": "branch", "date": "Swadeshi", "children": [
                {"label": "Boycotted British goods, government posts, and British postal services", "type": "leaf"},
                {"label": "Actively opposed cow slaughter; led to violent clashes and suppression by British (65 Kukas blown from cannons in 1872)", "type": "leaf"}]}
        ],
        "hi": [
            {"label": "उत्पत्ति और नेता", "type": "branch", "date": "1840s-72 पंजाब", "children": [
                {"label": "भगत जवाहर मल (सियां साहिब): पश्चिमी पंजाब में धार्मिक शुद्धि आंदोलन के रूप में स्थापित", "type": "leaf"},
                {"label": "बाबा राम सिंह: पंजाब विलय के बाद सिख शासन की बहाली हेतु इसे राजनीतिक अभियान में बदला", "type": "leaf"}]},
            {"label": "कार्य योजना", "type": "branch", "date": "स्वदेशी", "children": [
                {"label": "ब्रिटिश वस्तुओं, सरकारी नौकरियों और ब्रिटिश डाक सेवाओं का पूर्ण बहिष्कार किया", "type": "leaf"},
                {"label": "गो-वध का कड़ा विरोध; हिंसक झड़पें हुईं और अंग्रेजों द्वारा बर्बर दमन किया गया (1872 में 65 कूकाओं को तोप से उड़ाया गया)", "type": "leaf"}]}
        ]
    },
    "revolts-moplah-uprisings": {
        "en": [
            {"label": "Origins", "type": "branch", "date": "Malabar, Kerala", "children": [
                {"label": "Moplahs: Muslim tenants and agricultural laborers in Malabar region", "type": "leaf"},
                {"label": "Jenmis: Hindu landlords backed by British land laws and high revenue demands", "type": "leaf"}]},
            {"label": "Uprisings", "type": "branch", "date": "Revolts", "children": [
                {"label": "Dozens of outbreaks occurred between 1836 and 1854 against eviction & rent hikes", "type": "leaf"},
                {"label": "Major Rebellion (1921): Led by Ali Musaliar & Kunhammed Haji; linked with Khilafat movement, later took communal turn", "type": "leaf"}]}
        ],
        "hi": [
            {"label": "उत्पत्ति", "type": "branch", "date": "मालाबार, केरल", "children": [
                {"label": "मोपला: मालाबार क्षेत्र के मुस्लिम काश्तकार और खेतिहर मजदूर", "type": "leaf"},
                {"label": "जेनमी: ब्रिटिश भूमि कानूनों और उच्च राजस्व मांगों द्वारा समर्थित हिंदू जमींदार", "type": "leaf"}]},
            {"label": "विद्रोह", "type": "branch", "date": "विद्रोह", "children": [
                {"label": "बेदखली और लगान वृद्धि के खिलाफ 1836 और 1854 के बीच दर्जनों छोटे विद्रोह हुए", "type": "leaf"},
                {"label": "मुख्य विद्रोह (1921): अली मुसलियार और कुनहम्मद हाजी के नेतृत्व में; खिलाफत आंदोलन से जुड़ा, बाद में सांप्रदायिक मोड़ लिया", "type": "leaf"}]}
        ]
    },
    "revolts-pagal-panthis": {
        "en": [
            {"label": "Sect & Rise", "type": "branch", "date": "1825-35 Bengal", "children": [
                {"label": "Pagal Panthis: Syncretic religious sect founded by Karam Shah in Mymensingh district", "type": "leaf"},
                {"label": "Tipu Shah (Karam Shah's son): Led the tenant peasants against oppressive zamindars", "type": "leaf"}]},
            {"label": "Action", "type": "branch", "date": "Rebellion", "children": [
                {"label": "Refused to pay rent above traditional rates; captured areas and established a peasant court", "type": "leaf"},
                {"label": "Suppressed after major military campaigns by British in 1830s", "type": "leaf"}]}
        ],
        "hi": [
            {"label": "संप्रदाय और उदय", "type": "branch", "date": "1825-35 बंगाल", "children": [
                {"label": "पागलपंथी: मयमनसिंह जिले में करम शाह द्वारा स्थापित एक समन्वयवादी धार्मिक संप्रदाय", "type": "leaf"},
                {"label": "टीपू शाह (करम शाह का पुत्र): अत्याचारी जमींदारों के खिलाफ काश्तकार किसानों का नेतृत्व किया", "type": "leaf"}]},
            {"label": "कार्रवाई", "type": "branch", "date": "विद्रोह", "children": [
                {"label": "पारंपरिक दरों से अधिक लगान देने से इनकार किया; क्षेत्रों पर कब्जा कर किसान अदालत की स्थापना की", "type": "leaf"},
                {"label": "1830 के दशक में अंग्रेजों द्वारा बड़े सैन्य अभियानों के बाद विद्रोह का दमन किया गया", "type": "leaf"}]}
        ]
    },
    "revolts-sanyasi-revolt": {
        "en": [
            {"label": "Origins & Leaders", "type": "branch", "date": "1763-1800 Bengal", "children": [
                {"label": "Sanyasis (Giri sect) & Madari Fakirs: Wandering monks whose pilgrimage routes were taxed/restricted", "type": "leaf"},
                {"label": "Key Leaders: Manju Shah, Debi Chaudhurani, Bhavani Pathak", "type": "leaf"}]},
            {"label": "Action & Impact", "type": "branch", "date": "Famine 1770", "children": [
                {"label": "Severe Bengal Famine of 1770 and harsh British taxation pushed peasants to join the monks", "type": "leaf"},
                {"label": "Rebels raided British factories, seized government treasuries, and defeated East India Company forces", "type": "leaf"},
                {"label": "Warren Hastings suppressed the revolt; inspired Bankim Chandra's novel 'Anandamath' ('Vande Mataram')", "type": "leaf"}]}
        ],
        "hi": [
            {"label": "उत्पत्ति और नेता", "type": "branch", "date": "1763-1800 बंगाल", "children": [
                {"label": "संन्यासी (गिरि संप्रदाय) और मदारी फकीर: घुमंतू साधु जिनकी तीर्थयात्रा पर अंग्रेजों ने कर लगाए", "type": "leaf"},
                {"label": "प्रमुख नेता: मंजनू शाह, देवी चौधुरानी, भवानी पाठक", "type": "leaf"}]},
            {"label": "कार्रवाई और प्रभाव", "type": "branch", "date": "अकाल 1770", "children": [
                {"label": "1770 के भीषण बंगाल अकाल और अंग्रेजों की क्रूर कर वसूली ने किसानों को संन्यासियों से जुड़ने पर मजबूर किया", "type": "leaf"},
                {"label": "विद्रोहियों ने ब्रिटिश फैक्ट्रियों पर छापे मारे, सरकारी खजाने लूटे और ईस्ट इंडिया कंपनी की सेना को हराया", "type": "leaf"},
                {"label": "वॉरन हेस्टिंग्स ने विद्रोह का दमन किया; बंकिम चंद्र के उपन्यास 'आनंदमठ' (गीत 'वंदे मातरम') का आधार बना", "type": "leaf"}]}
        ]
    },
    "revolts-wahabi-movement": {
        "en": [
            {"label": "Origins", "type": "branch", "date": "Patna Center", "children": [
                {"label": "Islamic revivalist movement founded by Syed Ahmed Barelvi (influenced by Abdul Wahab)", "type": "leaf"},
                {"label": "Aimed to convert India from Dar-ul-Harb (land of infidels/British) to Dar-ul-Islam", "type": "leaf"}]},
            {"label": "Campaigns", "type": "branch", "date": "Trials", "children": [
                {"label": "Vilayat Ali and Inayat Ali: Prominent leaders of Patna center", "type": "leaf"},
                {"label": "Organized armed resistance against British on North-West Frontier; suppressed in 1860s trials", "type": "leaf"}]}
        ],
        "hi": [
            {"label": "उत्पत्ति", "type": "branch", "date": "पटना केंद्र", "children": [
                {"label": "सैयद अहमद बरेलवी द्वारा स्थापित इस्लामी पुनरुत्थानवादी आंदोलन (अब्दुल वहाब से प्रभावित)", "type": "leaf"},
                {"label": "भारत को दार-उल-हर्ब (गैर-इस्लामी शासन/ब्रिटिश) से दार-उल-इस्लाम में बदलने का लक्ष्य", "type": "leaf"}]},
            {"label": "अभियान", "type": "branch", "date": "मुकदमे", "children": [
                {"label": "विलायत अली और इनायत अली: पटना केंद्र के प्रमुख मार्गदर्शक नेता", "type": "leaf"},
                {"label": "उत्तर-पश्चिम सीमा प्रांत पर अंग्रेजों के खिलाफ सशस्त्र प्रतिरोध का आयोजन किया; 1860 के दशक में दमन", "type": "leaf"}]}
        ]
    },
    "tribal-movements-bhil-uprising": {
        "en": [
            {"label": "Bhil Tribe", "type": "branch", "date": "Western Ghats", "children": [
                {"label": "Bhils: Agri-tribals of Khandesh region (Maharashtra/Gujarat border)", "type": "leaf"},
                {"label": "Revolted in 1817-19, 1825, 1831, 1846 against British control", "type": "leaf"}]},
            {"label": "Causes", "type": "branch", "date": "Causes", "children": [
                {"label": "British occupation of Bhil forest territories, agrarian distress, and fear of losing traditional rights", "type": "leaf"},
                {"label": "Sewaram (1825): Led the rebellion; Bhils used hilly terrain to wage guerrilla warfare", "type": "leaf"}]}
        ],
        "hi": [
            {"label": "भील जनजाति", "type": "branch", "date": "पश्चिमी घाट", "children": [
                {"label": "भील: खानदेश क्षेत्र (महाराष्ट्र/गुजरात सीमा) के कृषक आदिवासी", "type": "leaf"},
                {"label": "ब्रिटिश नियंत्रण के खिलाफ 1817-19, 1825, 1831 और 1846 में विद्रोह किया", "type": "leaf"}]},
            {"label": "कारण", "type": "branch", "date": "कारण", "children": [
                {"label": "भील वन क्षेत्रों पर ब्रिटिश कब्जा, कृषि संकट और पारंपरिक अधिकार खोने का डर", "type": "leaf"},
                {"label": "सेवाराम (1825): विद्रोह का नेतृत्व किया; भीलों ने पहाड़ी रास्तों का उपयोग कर गुरिल्ला युद्ध किया", "type": "leaf"}]}
        ]
    },
    "tribal-movements-chuar-uprising": {
        "en": [
            {"label": "Chuar Clan", "type": "branch", "date": "Bengal", "children": [
                {"label": "Chuars: Tribal community of Midnapore and Bankura districts (Bengal)", "type": "leaf"},
                {"label": "Rebelled in phases between 1766 and 1809; Durjan Singh (1798) was major leader", "type": "leaf"}]},
            {"label": "Causes", "type": "branch", "date": "Causes", "children": [
                {"label": "Introduction of Permanent Settlement, high land revenue demands, and sale of tribal lands to outsiders", "type": "leaf"},
                {"label": "Displacement of traditional Chuar guards/militia by British police forces", "type": "leaf"}]}
        ],
        "hi": [
            {"label": "चुआर जनजाति", "type": "branch", "date": "बंगाल", "children": [
                {"label": "चुआर: मिदनापुर और बांकुरा जिलों (बंगाल) का आदिवासी समुदाय", "type": "leaf"},
                {"label": "1766 और 1809 के बीच विभिन्न चरणों में विद्रोह; दुर्जन सिंह (1798) प्रमुख नेता थे", "type": "leaf"}]},
            {"label": "कारण", "type": "branch", "date": "कारण", "children": [
                {"label": "स्थायी बंदोबस्त की शुरूआत, अत्यधिक भू-राजस्व की मांग और बाहरी लोगों को आदिवासी भूमि की नीलामी", "type": "leaf"},
                {"label": "ब्रिटिश पुलिस बलों द्वारा पारंपरिक चुआर प्रहरियों/रक्षकों का विस्थापन", "type": "leaf"}]}
        ]
    },
    "tribal-movements-jaintia-and-garo-rebellion": {
        "en": [
            {"label": "Jaintia (1860-63)", "type": "branch", "date": "Meghalaya", "children": [
                {"label": "Led by U Kiang Nangbah; rebelled against introduction of House Tax and Income Tax by British", "type": "leaf"}]},
            {"label": "Garo (1869-72)", "type": "branch", "date": "Meghalaya", "children": [
                {"label": "Led by Pa Togan Sangma; opposed road construction linking Assam/Bengal through Garo hills", "type": "leaf"}]}
        ],
        "hi": [
            {"label": "जयंतिया विद्रोह (1860-63)", "type": "branch", "date": "मेघालय", "children": [
                {"label": "यू कियांग नांगबाह के नेतृत्व में; अंग्रेजों द्वारा गृह कर और आयकर लगाने के खिलाफ विद्रोह", "type": "leaf"}]},
            {"label": "गारो विद्रोह (1869-72)", "type": "branch", "date": "मेघालय", "children": [
                {"label": "पा तोगन संगमा के नेतृत्व में; गारो पहाड़ियों के बीच असम और बंगाल को जोड़ने वाली सड़क निर्माण का विरोध", "type": "leaf"}]}
        ]
    },
    "tribal-movements-khonda-dora-uprisings": {
        "en": [
            {"label": "Vizag Rebellion", "type": "branch", "date": "1900 Andhra", "children": [
                {"label": "Khonda Doras: Tribal clan in Visakhapatnam agency tracts; led by Korra Mallayya", "type": "leaf"},
                {"label": "Opposed land grabbing by plains moneylenders and forest restrictions imposed by officials", "type": "leaf"},
                {"label": "Mallayya claimed to be incarnation of Pandavas; defeated and imprisoned by police", "type": "leaf"}]}
        ],
        "hi": [
            {"label": "विशाखापत्तनम विद्रोह", "type": "branch", "date": "1900 आंध्र", "children": [
                {"label": "खोंडा डोरा: विशाखापत्तनम एजेंसी क्षेत्र की जनजाति; कोरा मल्लैया द्वारा नेतृत्व", "type": "leaf"},
                {"label": "मैदानी क्षेत्रों के साहूकारों द्वारा भूमि कब्जाने और वन विभाग द्वारा लगाए गए प्रतिबंधों का विरोध", "type": "leaf"},
                {"label": "मल्लैया ने पांडवों के अवतार होने का दावा किया; पुलिस द्वारा पराजित और बंदी बनाए गए", "type": "leaf"}]}
        ]
    },
    "tribal-movements-kol-uprising": {
        "en": [
            {"label": "Chhotanagpur", "type": "branch", "date": "1831-32", "children": [
                {"label": "Kols: Tribals of Chhotanagpur (Jharkhand); led by Buddho Bhagat and Madara Mahato", "type": "leaf"},
                {"label": "Caused by transfer of tribal lands to outsider Sikh/Muslim farmers (Dikus) and high taxation", "type": "leaf"},
                {"label": "Kols waged a violent campaign, burning and plundering properties of outsiders; suppressed by army", "type": "leaf"}]}
        ],
        "hi": [
            {"label": "छोटानागपुर", "type": "branch", "date": "1831-32", "children": [
                {"label": "कोल: छोटानागपुर (झारखंड) के आदिवासी; बुद्धो भगत और मदारा महतो द्वारा नेतृत्व", "type": "leaf"},
                {"label": "आदिवासी जमीनों को बाहरी सिख/मुस्लिम किसानों (दिखुओं) को सौंपने और भारी करों के खिलाफ विद्रोह", "type": "leaf"},
                {"label": "कोलों ने हिंसक अभियान चलाया, बाहरी लोगों की संपत्तियों को लूटा और जलाया; सेना द्वारा दमन", "type": "leaf"}]}
        ]
    },
    "tribal-movements-munda-rebellion": {
        "en": [
            {"label": "Birsa Munda", "type": "branch", "date": "1899-1900", "children": [
                {"label": "Birsa Munda (Dharti Aba): Declared himself messenger of God; led the 'Ulgulan' (Great Tumult)", "type": "leaf"},
                {"label": "Sought to establish independent 'Munda Raj' free of British and Dikus", "type": "leaf"}]},
            {"label": "Causes & Outcome", "type": "branch", "date": "Outcome", "children": [
                {"label": "Destruction of traditional 'Khuntkatti' (joint landholding system) by British land laws", "type": "leaf"},
                {"label": "Rebels attacked police stations and churches; Birsa captured & died in Ranchi jail (1900)", "type": "leaf"},
                {"label": "Led to Chhotanagpur Tenancy Act (1908) protecting tribal land from transfer to non-tribals", "type": "leaf"}]}
        ],
        "hi": [
            {"label": "बिरसा मुंडा", "type": "branch", "date": "1899-1900", "children": [
                {"label": "बिरसा मुंडा (धरती आबा): स्वयं को ईश्वर का दूत घोषित किया; 'उलगुलान' (महान हलचल) का नेतृत्व किया", "type": "leaf"},
                {"label": "अंग्रेजों और दिखुओं से मुक्त स्वतंत्र 'मुंडा राज' की स्थापना का लक्ष्य रखा", "type": "leaf"}]},
            {"label": "कारण और परिणाम", "type": "branch", "date": "परिणाम", "children": [
                {"label": "ब्रिटिश भूमि कानूनों द्वारा पारंपरिक 'खूंटकट्टी' (संयुक्त भूमि स्वामित्व व्यवस्था) का विनाश मुख्य कारण", "type": "leaf"},
                {"label": "विद्रोहियों ने पुलिस थानों और चर्चों पर हमले किए; बिरसा बंदी बने और रांची जेल (1900) में मृत्यु", "type": "leaf"},
                {"label": "परिणाम: छोटानागपुर काश्तकारी अधिनियम (1908) पारित, जिससे आदिवासियों की जमीन गैर-आदिवासियों को हस्तांतरित होना प्रतिबंधित", "type": "leaf"}]}
        ]
    },
    "tribal-movements-rampa-rebellion": {
        "en": [
            {"label": "Alluri Sitarama Raju", "type": "branch", "date": "1922-24 Andhra", "children": [
                {"label": "Led by Alluri Sitarama Raju (non-tribal leader who assumed messianic role)", "type": "leaf"},
                {"label": "Raju was influenced by Gandhi's Non-Cooperation Movement, but advocated armed struggle", "type": "leaf"}]},
            {"label": "Forest Grievance", "type": "branch", "date": "Causes", "children": [
                {"label": "1882 Madras Forest Act banned Podu (shifting cultivation) and traditional forest use", "type": "leaf"},
                {"label": "Rebels conducted guerrilla warfare; Raju captured and shot in 1924", "type": "leaf"}]}
        ],
        "hi": [
            {"label": "अल्लूरी सीताराम राजू", "type": "branch", "date": "1922-24 आंध्र", "children": [
                {"label": "अल्लूरी सीताराम राजू (गैर-आदिवासी नेता जिन्होंने मसीहाई भूमिका निभाई) के नेतृत्व में", "type": "leaf"},
                {"label": "राजू गांधीजी के असहयोग आंदोलन से प्रभावित थे, परंतु सशस्त्र संघर्ष के पक्षधर थे", "type": "leaf"}]},
            {"label": "वन अधिकार समस्या", "type": "branch", "date": "कारण", "children": [
                {"label": "1882 के मद्रास वन अधिनियम द्वारा पोडू (झूम खेती) और पारंपरिक वन उपयोग पर प्रतिबंध लगाया गया", "type": "leaf"},
                {"label": "विद्रोहियों ने गुरिल्ला युद्ध लड़ा; 1924 में राजू को पकड़कर गोली मार दी गई", "type": "leaf"}]}
        ]
    },
    "tribal-movements-santhal-rebellion": {
        "en": [
            {"label": "Santhal Pargana", "type": "branch", "date": "1855-56", "children": [
                {"label": "Led by Sidhu and Kanhu (brothers) in Rajmahal hills (Jharkhand/Bihar)", "type": "leaf"},
                {"label": "Opposed economic exploitation by Dikus (moneylenders, traders, British railway contractors)", "type": "leaf"}]},
            {"label": "Impact", "type": "branch", "date": "Outcome", "children": [
                {"label": "Proclaimed end of British rule; suppressed with extreme brutality (15,000+ Santhals killed)", "type": "leaf"},
                {"label": "Santhal Parganas district created to regulate land transfers and protect tribal customs", "type": "leaf"}]}
        ],
        "hi": [
            {"label": "संथाल परगना", "type": "branch", "date": "1855-56", "children": [
                {"label": "राजमहल पहाड़ियों (झारखंड/बिहार) में सिद्धू और कान्हू (भाइयों) के नेतृत्व में संचालित", "type": "leaf"},
                {"label": "दिखुओं (साहूकारों, व्यापारियों, ब्रिटिश रेलवे ठेकेदारों) द्वारा किए जा रहे आर्थिक शोषण का विरोध", "type": "leaf"}]},
            {"label": "प्रभाव और परिणाम", "type": "branch", "date": "परिणाम", "children": [
                {"label": "ब्रिटिश शासन के अंत की घोषणा की; अंग्रेजों द्वारा अत्यंत क्रूरतापूर्वक दमन (15,000 से अधिक संथाल मारे गए)", "type": "leaf"},
                {"label": "परिणामस्वरूप संथाल परगना जिले का गठन किया गया ताकि आदिवासी भूमि हस्तांतरण को रोका जा सके", "type": "leaf"}]}
        ]
    },
    "tribal-movements-singphos-rebellion": {
        "en": [
            {"label": "Assam Frontier", "type": "branch", "date": "1830 & 1843", "children": [
                {"label": "Singphos: Tribal group of Assam; rebelled under Ningru Duola", "type": "leaf"},
                {"label": "Sparked by British annexation of Assam (Treaty of Yandabo, 1826) and intrusion into tribal lands", "type": "leaf"},
                {"label": "British abolition of slavery disrupted Singpho agrarian economy; suppressed in 1843", "type": "leaf"}]}
        ],
        "hi": [
            {"label": "असम सीमांत", "type": "branch", "date": "1830 और 1843", "children": [
                {"label": "सिंगफो: असम का आदिवासी समूह; निंगरू दुओला के नेतृत्व में विद्रोह", "type": "leaf"},
                {"label": "यांडाबू की संधि (1826) के बाद असम के ब्रिटिश विलय और आदिवासी भूमि में घुसपैठ के कारण भड़का", "type": "leaf"},
                {"label": "ब्रिटिश शासन द्वारा दास प्रथा के उन्मूलन से सिंगफो कृषि अर्थव्यवस्था छिन्न-भिन्न हुई; 1843 में दमन", "type": "leaf"}]}
        ]
    },
    "tribal-movements-tana-bhagat-movement": {
        "en": [
            {"label": "Oraon Reform", "type": "branch", "date": "1914-19 Chhotanagpur", "children": [
                {"label": "Oraon Tribe: Led by Jatra Bhagat & Turia Bhagat in Ranchi region", "type": "leaf"},
                {"label": "Began as religious reform movement to abandon animal sacrifices and alcohol", "type": "leaf"},
                {"label": "Transformed into political satyagraha against British taxes; joined Gandhi's Non-Cooperation Movement", "type": "leaf"}]}
        ],
        "hi": [
            {"label": "उरांव सुधार", "type": "branch", "date": "1914-19 छोटानागपुर", "children": [
                {"label": "उरांव जनजाति: रांची क्षेत्र में जतरा भगत और तुरिया भगत के नेतृत्व में संचालित", "type": "leaf"},
                {"label": "पशु बलि और मदिरा सेवन जैसी कुप्रथाओं को छोड़ने के धार्मिक सुधार आंदोलन के रूप में शुरू हुआ", "type": "leaf"},
                {"label": "ब्रिटिश करों के विरोध में राजनीतिक सत्याग्रह में बदला; गांधीजी के असहयोग आंदोलन में शामिल हुए", "type": "leaf"}]}
        ]
    }
}

# Mapping folder variations to canonical keys
MINDMAP_MAPPINGS = {
    "military-discontent-uprisings-paika-rebellion": "military-discontent-uprisings-paika-rebellion",
    "military-discontent-uprisings-ramosi-uprising": "military-discontent-uprisings-ramosi-uprising",
    "military-discontent-uprisings-sawantwadi-revolt": "military-discontent-uprisings-sawantwadi-revolt",
    "peasant-movements-bardoli-movement": "peasant-movements-bardoli-movement",
    "peasant-movements-champaran-satyagraha": "peasant-movements-champaran-satyagraha",
    "peasant-movements-kheda-peasant-struggle": "peasant-movements-kheda-peasant-struggle",
    "peasant-movements-reasons-of-resistance-among-peasants": "peasant-movements-reasons-of-resistance-among-peasants",
    "peasant-movements-tebhaga-movement": "peasant-movements-tebhaga-movement",
    "peasant-movements-telangana-movement": "peasant-movements-telangana-movement",
    "reasons-for-limited-success-of-the-uprisings": "reasons-for-limited-success-of-the-uprisings",
    "responsible-factors-for-tribal-revolts": "responsible-factors-for-tribal-revolts",
    "revolts-faraizi-revolt": "revolts-faraizi-revolt",
    "revolts-kuka-movement": "revolts-kuka-movement",
    "revolts-moplah-uprisings": "revolts-moplah-uprisings",
    "revolts-pagal-panthis": "revolts-pagal-panthis",
    "revolts-sanyasi-revolt": "revolts-sanyasi-revolt",
    "revolts-wahabi-movement": "revolts-wahabi-movement",
    "tribal-movements-bhil-uprising": "tribal-movements-bhil-uprising",
    "tribal-movements-chuar-uprising": "tribal-movements-chuar-uprising",
    "tribal-movements-jaintia-and-garo-rebellion": "tribal-movements-jaintia-and-garo-rebellion",
    "tribal-movements-khonda-dora-uprisings": "tribal-movements-khonda-dora-uprisings",
    "tribal-movements-kol-uprising": "tribal-movements-kol-uprising",
    "tribal-movements-munda-rebellion": "tribal-movements-munda-rebellion",
    "tribal-movements-rampa-rebellion": "tribal-movements-rampa-rebellion",
    "tribal-movements-santhal-rebellion": "tribal-movements-santhal-rebellion",
    "tribal-movements-singphos-rebellion": "tribal-movements-singphos-rebellion",
    "tribal-movements-tana-bhagat-movement": "tribal-movements-tana-bhagat-movement"
}

def get_clean_title(folder_name):
    title = folder_name.replace('-', ' ')
    skip = {'of', 'and', 'the', 'for', 'in', 'with', 'to', 'on', 'by', 'or', 'a', 'an', 'about'}
    return ' '.join(w if w.lower() in skip else w.capitalize() for w in title.split())

def ensure_base_html(path, folder_name):
    if os.path.exists(path):
        return
    os.makedirs(os.path.dirname(path), exist_ok=True)
    clean_title = get_clean_title(folder_name)
    content = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>{clean_title} - UPSC Civil Services Study Guide | SJMaths</title>
</head>
<body>
    <!-- Interactive Mindmap -->
</body>
</html>
"""
    with open(path, 'w', encoding='utf-8') as f:
        f.write(content)

def create_hi_stub(en_html_path, hi_html_path, folder_name):
    if not os.path.exists(en_html_path):
        ensure_base_html(en_html_path, folder_name)
        
    with open(en_html_path, 'r', encoding='utf-8') as f:
        html = f.read()
    html = html.replace('<html lang="en">', '<html lang="hi">', 1)
    
    clean_title = get_clean_title(folder_name)
    if '<title>' in html:
        html = re.sub(r'<title>[^<]+</title>',
                      f'<title>{clean_title} (Hindi) - UPSC Civil Services Study Guide | SJMaths</title>',
                      html, count=1)
    
    os.makedirs(os.path.dirname(hi_html_path), exist_ok=True)
    with open(hi_html_path, 'w', encoding='utf-8') as f:
        f.write(html)

def inject_mindmap(html_path, folder_name, lang):
    with open(html_path, 'r', encoding='utf-8') as f:
        html = f.read()
    html = html.replace('\r\n', '\n')

    # Remove any old mindmap links/scripts
    for old in ['    <link rel="stylesheet" href="/assets/css/mindmap.min.css?v=2">\n',
                '    <link rel="stylesheet" href="/assets/css/mindmap.min.css?v=1">\n']:
        html = html.replace(old, '')
    html = re.sub(r'\s*<!-- Interactive Mindmap -->.*?<!-- Deep-Dive Study Guide \(Dynamically Rendered\) -->', '\n            <!-- Deep-Dive Study Guide (Dynamically Rendered) -->', html, flags=re.DOTALL)
    html = re.sub(r'\s*<!-- Interactive Mindmap -->.*?renderMindmap\(.*?\);\s*</script>', '', html, flags=re.DOTALL)

    clean_title = get_clean_title(folder_name)
    key = folder_name.lower()
    canonical_key = MINDMAP_MAPPINGS.get(key, key)
    
    branches = MINDMAP_DATA.get(canonical_key, {}).get(lang, [])
    if not branches:
        branches = [{"label": clean_title, "type": "branch", "date": "Topic", "children": [{"label": "Information structured here for UPSC", "type": "leaf"}]}]
        
    mindmap_data = {"label": clean_title, "type": "root", "children": branches}

    css_link = '    <link rel="stylesheet" href="/assets/css/mindmap.min.css?v=2">\n'
    if css_link not in html and '<head>' in html:
        html = html.replace('</head>', css_link + '</head>')

    if lang == 'hi':
        instr = 'किसी कार्ड पर क्लिक करें।'
        title_text = f"{clean_title} &mdash; इंटरैक्टिव माइंडमैप"
    else:
        instr = 'Click any card to expand or collapse.'
        title_text = f"{clean_title} &mdash; Interactive Mindmap"

    mindmap_card = f'''            <!-- Interactive Mindmap -->
            <div class="card-premium" id="mindmap-card">
                <h2 class="card-title"><i class="fas fa-diagram-project"></i> {title_text}</h2>
                <p style="color:var(--text-light);font-size:.87rem;margin-bottom:1.25rem;">
                    <i class="fas fa-circle-info" style="color:#8b5cf6;margin-right:5px;"></i>
                    {instr}
                </p>
                <div id="prehistory-mindmap-container"></div>
            </div>
'''
    if re.search(r'<!-- Deep-Dive Study Guide \(Dynamically Rendered\) -->\s*<div class="card-premium" id="deep-dive-section">', html):
        html = re.sub(r'(<!-- Deep-Dive Study Guide \(Dynamically Rendered\) -->\s*<div class="card-premium" id="deep-dive-section">)', mindmap_card + r'\1', html)
    elif '<div class="tab-panel active" id="notes-panel" role="tabpanel"' in html:
        marker = '<div class="tab-panel active" id="notes-panel" role="tabpanel" aria-labelledby="notes-panel">'
        html = html.replace(marker, marker + '\n' + mindmap_card, 1)
    elif '<body>' in html:
        html = html.replace('<body>', '<body>\n' + mindmap_card, 1)

    tree_json = json.dumps(mindmap_data, ensure_ascii=False)
    inline_script = f'''
    <!-- Interactive Mindmap -->
    <script src="/assets/js/mindmap-engine.min.js?v=2"></script>
    <script>
    renderMindmap({tree_json}, undefined, '{lang}');
    </script>
'''
    if '</body>' in html:
        html = html.replace('</body>', inline_script + '\n</body>')
    else:
        html += inline_script

    with open(html_path, 'w', encoding='utf-8') as f:
        f.write(html)

def main():
    total_en = 0
    total_hi = 0
    
    if not os.path.exists(BASE_DIR):
        print(f"Directory {BASE_DIR} does not exist.")
        return

    for root_dir, dirs, files in os.walk(BASE_DIR):
        dirs[:] = [d for d in dirs if d != 'hi']
        folder_name = os.path.basename(root_dir)
        
        if root_dir == BASE_DIR:
            continue

        en_path = os.path.join(root_dir, 'index.html')
        hi_dir = os.path.join(root_dir, 'hi')
        hi_path = os.path.join(hi_dir, 'index.html')

        ensure_base_html(en_path, folder_name)
        inject_mindmap(en_path, folder_name, 'en')
        total_en += 1

        if not os.path.exists(hi_path):
            create_hi_stub(en_path, hi_path, folder_name)

        inject_mindmap(hi_path, folder_name, 'hi')
        total_hi += 1
        
        print(f"Processed: {folder_name}")

    print(f"\nCreated+patched {total_en} English and {total_hi} Hindi pages.")

if __name__ == '__main__':
    main()
