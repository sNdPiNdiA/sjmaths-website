#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os, re, json

BASE_DIR = r"upsc/modern_history/Expansion-of-East-India-Company"

MINDMAP_DATA = {
    "3-anglo-maratha-wars": {
        "en": [
            {"label": "First Anglo-Maratha War (1775-82)", "type": "branch", "date": "1775-1782", "children": [
                {"label": "Triggered by EIC's support for Raghunathrao (Raghoba) in Peshwa succession dispute; Treaty of Surat (1775) drawn", "type": "leaf"},
                {"label": "Convention of Wadgaon (1779): EIC forces defeated; humiliating agreement forced — later repudiated by Bombay Government", "type": "leaf"},
                {"label": "Treaty of Salbai (1782): Status quo restored; EIC gave up Raghoba's cause; 20-year peace; Madhav Rao II recognised as Peshwa", "type": "leaf"}
            ]},
            {"label": "Second Anglo-Maratha War (1803-05)", "type": "branch", "date": "1803-1805", "children": [
                {"label": "Treaty of Bassein (1802): Peshwa Baji Rao II accepted Subsidiary Alliance — invited British troops into Pune; Marathas saw it as betrayal", "type": "leaf"},
                {"label": "Marathas (Scindia + Bhonsle) attacked British; Lord Wellesley launched war; Delhi and Agra captured from Scindia", "type": "leaf"},
                {"label": "Treaties of Deogaon (Bhonsle) and Surji-Anjangaon (Scindia) 1803: Marathas ceded Cuttack, Gujarat territories; Scindia lost Delhi-Agra region", "type": "leaf"}
            ]},
            {"label": "Third Anglo-Maratha War (1817-19)", "type": "branch", "date": "1817-1819", "children": [
                {"label": "Peshwa attacked British Residency at Pune (Nov 1817); Bhonsle and Holkar joined revolt against British expansion", "type": "leaf"},
                {"label": "Lord Hastings' campaigns crushed all Maratha chiefs; Peshwa Baji Rao II surrendered in 1818 — pensioned at Bithur", "type": "leaf"},
                {"label": "Peshwaship abolished; Satara state created for descendants of Chhatrapati Shivaji; Bombay Presidency expanded enormously", "type": "leaf"}
            ]}
        ],
        "hi": [
            {"label": "प्रथम आंग्ल-मराठा युद्ध (1775-82)", "type": "branch", "date": "1775-1782", "children": [
                {"label": "पेशवा उत्तराधिकार विवाद में रघुनाथराव (राघोबा) के लिए EIC के समर्थन से उत्प्रेरित; सूरत की संधि (1775) बनाई", "type": "leaf"},
                {"label": "वडगाँव का अभिसमय (1779): EIC सेनाएं पराजित; अपमानजनक समझौते पर हस्ताक्षर — बाद में बॉम्बे सरकार ने अस्वीकार किया", "type": "leaf"},
                {"label": "सालबाई की संधि (1782): यथास्थिति बहाल; EIC ने राघोबा का साथ छोड़ा; 20 वर्ष की शांति; माधव राव II पेशवा मान्य", "type": "leaf"}
            ]},
            {"label": "द्वितीय आंग्ल-मराठा युद्ध (1803-05)", "type": "branch", "date": "1803-1805", "children": [
                {"label": "बसई की संधि (1802): पेशवा बाजी राव II ने सहायक संधि स्वीकार की — पुणे में ब्रिटिश सैनिकों को आमंत्रित किया; मराठों ने विश्वासघात माना", "type": "leaf"},
                {"label": "मराठों (सिंधिया + भोंसले) ने ब्रिटिश पर हमला किया; लॉर्ड वेलेजली ने युद्ध छेड़ा; सिंधिया से दिल्ली और आगरा जीते", "type": "leaf"},
                {"label": "देवगाँव (भोंसले) और सुर्जी-अंजनगाँव (सिंधिया) की संधियाँ 1803: मराठों ने कटक, गुजरात क्षेत्र सौंपे; सिंधिया ने दिल्ली-आगरा क्षेत्र खोया", "type": "leaf"}
            ]},
            {"label": "तृतीय आंग्ल-मराठा युद्ध (1817-19)", "type": "branch", "date": "1817-1819", "children": [
                {"label": "पेशवा ने पुणे में ब्रिटिश रेजीडेंसी पर हमला किया (नवं. 1817); भोंसले और होल्कर ब्रिटिश विस्तार के खिलाफ विद्रोह में शामिल", "type": "leaf"},
                {"label": "लॉर्ड हेस्टिंग्स के अभियानों ने सभी मराठा सरदारों को कुचला; पेशवा बाजी राव II ने 1818 में आत्मसमर्पण किया — बिठूर में पेंशनभोगी बने", "type": "leaf"},
                {"label": "पेशवाई समाप्त; छत्रपति शिवाजी के वंशजों के लिए सतारा राज्य बनाया; बॉम्बे प्रेसीडेंसी का भारी विस्तार हुआ", "type": "leaf"}
            ]}
        ]
    },
    "4-anglo-mysore-wars": {
        "en": [
            {"label": "First & Second Mysore Wars", "type": "branch", "date": "1767-1784", "children": [
                {"label": "First Anglo-Mysore War (1767-69): Hyder Ali defeated EIC; Treaty of Madras — mutual defence clause humiliated EIC", "type": "leaf"},
                {"label": "Second Anglo-Mysore War (1780-84): Hyder Ali attacked Carnatic when EIC broke defence treaty; Hyder died 1782; Tipu continued war", "type": "leaf"},
                {"label": "Treaty of Mangalore (1784): Status quo; mutual release of prisoners — last treaty where an Indian power dictated equal terms to EIC", "type": "leaf"}
            ]},
            {"label": "Third & Fourth Mysore Wars", "type": "branch", "date": "1790-1799", "children": [
                {"label": "Third Anglo-Mysore War (1790-92): Lord Cornwallis led triple alliance (EIC + Nizam + Marathas) against Tipu; Treaty of Seringapatam — Tipu ceded half his kingdom, paid Rs 3.3 cr indemnity, gave two sons as hostages", "type": "leaf"},
                {"label": "Fourth Anglo-Mysore War (1799): Lord Wellesley launched war; Tipu refused Subsidiary Alliance; Seringapatam stormed May 1799; Tipu Sultan killed defending his capital", "type": "leaf"},
                {"label": "Mysore divided: Wadiyar dynasty restored as subsidiary ally; Coorg and Kanara went to EIC; Nizam and Marathas got small shares", "type": "leaf"}
            ]},
            {"label": "Tipu Sultan's Legacy", "type": "branch", "date": "Historical Assessment", "children": [
                {"label": "Tipu introduced rocket artillery (Mysorean rockets) — most advanced of its time; influenced British military technology", "type": "leaf"},
                {"label": "Promoted silk weaving, sandalwood industry, trade with France and Turkey — proto-nationalist ruler opposing British colonialism", "type": "leaf"},
                {"label": "Tipu's death at Seringapatam (4 May 1799) marked the end of effective Indian resistance in the South", "type": "leaf"}
            ]}
        ],
        "hi": [
            {"label": "प्रथम और द्वितीय मैसूर युद्ध", "type": "branch", "date": "1767-1784", "children": [
                {"label": "प्रथम आंग्ल-मैसूर युद्ध (1767-69): हैदर अली ने EIC को हराया; मद्रास की संधि — पारस्परिक रक्षा खंड ने EIC को अपमानित किया", "type": "leaf"},
                {"label": "द्वितीय आंग्ल-मैसूर युद्ध (1780-84): EIC के रक्षा संधि तोड़ने पर हैदर अली ने कर्नाटक पर हमला किया; 1782 में हैदर की मृत्यु; टीपू ने युद्ध जारी रखा", "type": "leaf"},
                {"label": "मंगलौर की संधि (1784): यथास्थिति; परस्पर कैदियों की रिहाई — अंतिम संधि जिसमें किसी भारतीय शक्ति ने EIC को बराबरी की शर्तें तय कीं", "type": "leaf"}
            ]},
            {"label": "तृतीय और चतुर्थ मैसूर युद्ध", "type": "branch", "date": "1790-1799", "children": [
                {"label": "तृतीय आंग्ल-मैसूर युद्ध (1790-92): लॉर्ड कॉर्नवालिस ने टीपू के खिलाफ त्रिगुट (EIC + निजाम + मराठा) का नेतृत्व किया; श्रीरंगपट्टनम की संधि — टीपू ने आधा राज्य सौंपा, 3.3 करोड़ रु. क्षतिपूर्ति दी, दो पुत्रों को बंधक दिया", "type": "leaf"},
                {"label": "चतुर्थ आंग्ल-मैसूर युद्ध (1799): लॉर्ड वेलेजली ने युद्ध शुरू किया; टीपू ने सहायक संधि अस्वीकार की; मई 1799 में श्रीरंगपट्टनम पर धावा; टीपू सुल्तान राजधानी बचाते हुए शहीद", "type": "leaf"},
                {"label": "मैसूर विभाजित: वाडियार वंश को सहायक सहयोगी के रूप में बहाल; कूर्ग और कानरा EIC को; निजाम और मराठों को छोटे हिस्से", "type": "leaf"}
            ]},
            {"label": "टीपू सुल्तान की विरासत", "type": "branch", "date": "ऐतिहासिक मूल्यांकन", "children": [
                {"label": "टीपू ने रॉकेट तोपखाना (मैसूर रॉकेट) पेश किए — अपने समय का सबसे उन्नत; ब्रिटिश सैन्य तकनीक को प्रभावित किया", "type": "leaf"},
                {"label": "रेशम बुनाई, चंदन उद्योग, फ्रांस और तुर्की के साथ व्यापार को बढ़ावा दिया — ब्रिटिश उपनिवेशवाद का विरोध करने वाले प्रोटो-राष्ट्रवादी शासक", "type": "leaf"},
                {"label": "श्रीरंगपट्टनम में टीपू की मृत्यु (4 मई 1799) ने दक्षिण में प्रभावी भारतीय प्रतिरोध का अंत किया", "type": "leaf"}
            ]}
        ]
    },
    "bengal-battle-of-buxar": {
        "en": [
            {"label": "Background & Causes", "type": "branch", "date": "1764", "children": [
                {"label": "Mir Qasim (installed by EIC) objected to EIC's abuse of duty-free trade privileges (dastaks) for private trade — revenue losses to Bengal", "type": "leaf"},
                {"label": "Mir Qasim abolished all internal duties to level playing field; EIC refused — declared war; Mir Qasim allied with Shuja ud Daula (Awadh) and Shah Alam II (Mughal Emperor)", "type": "leaf"}
            ]},
            {"label": "The Battle (22 Oct 1764)", "type": "branch", "date": "22 October 1764", "children": [
                {"label": "EIC forces under Hector Munro decisively defeated the combined armies of Mir Qasim, Shuja ud Daula, Shah Alam II", "type": "leaf"},
                {"label": "Strategically more significant than Plassey: EIC now defeated three major powers simultaneously — consolidated Bengal dominance", "type": "leaf"},
                {"label": "Mir Qasim fled; Mir Jafar reinstated as Nawab — but now completely powerless puppet under EIC control", "type": "leaf"}
            ]},
            {"label": "Treaty of Allahabad (1765)", "type": "branch", "date": "1765", "children": [
                {"label": "Shah Alam II granted Diwani (revenue rights) of Bengal, Bihar, Orissa to EIC — legitimised British revenue extraction", "type": "leaf"},
                {"label": "Shuja ud Daula paid Rs 50 lakh war indemnity; gave Allahabad and Kara to Shah Alam; accepted EIC garrison", "type": "leaf"},
                {"label": "EIC became the de facto ruler of Bengal; Nawab retained only Nizamat (criminal justice) functions — Dual Government born", "type": "leaf"}
            ]}
        ],
        "hi": [
            {"label": "पृष्ठभूमि और कारण", "type": "branch", "date": "1764", "children": [
                {"label": "मीर कासिम (EIC द्वारा स्थापित) ने निजी व्यापार के लिए EIC के शुल्क-मुक्त व्यापार विशेषाधिकारों (दस्तकों) के दुरुपयोग पर आपत्ति जताई", "type": "leaf"},
                {"label": "मीर कासिम ने समान अवसर के लिए सभी आंतरिक शुल्क समाप्त किए; EIC ने मना किया — युद्ध घोषित; मीर कासिम ने शुजा उद दौला (अवध) और शाह आलम II (मुगल सम्राट) से गठबंधन किया", "type": "leaf"}
            ]},
            {"label": "युद्ध (22 अक्टूबर 1764)", "type": "branch", "date": "22 अक्टूबर 1764", "children": [
                {"label": "हेक्टर मुनरो के नेतृत्व में EIC सेनाओं ने मीर कासिम, शुजा उद दौला, शाह आलम II की संयुक्त सेनाओं को निर्णायक रूप से हराया", "type": "leaf"},
                {"label": "प्लासी से रणनीतिक रूप से अधिक महत्वपूर्ण: EIC ने एक साथ तीन प्रमुख शक्तियों को हराया — बंगाल वर्चस्व मजबूत हुआ", "type": "leaf"},
                {"label": "मीर कासिम भागा; मीर जाफर को नवाब के रूप में बहाल — लेकिन अब EIC नियंत्रण के तहत पूरी तरह शक्तिहीन कठपुतली", "type": "leaf"}
            ]},
            {"label": "इलाहाबाद की संधि (1765)", "type": "branch", "date": "1765", "children": [
                {"label": "शाह आलम II ने बंगाल, बिहार, उड़ीसा की दीवानी (राजस्व अधिकार) EIC को प्रदान की — ब्रिटिश राजस्व निष्कर्षण को वैध बनाया", "type": "leaf"},
                {"label": "शुजा उद दौला ने 50 लाख रु. युद्ध क्षतिपूर्ति दी; शाह आलम को इलाहाबाद और कारा दिया; EIC गैरिसन स्वीकार किया", "type": "leaf"},
                {"label": "EIC वास्तव में बंगाल का शासक बना; नवाब ने केवल निजामत (आपराधिक न्याय) कार्य बनाए रखे — द्वैध शासन का जन्म", "type": "leaf"}
            ]}
        ]
    },
    "bengal-battle-of-plassey": {
        "en": [
            {"label": "Background & Conspiracy", "type": "branch", "date": "1757", "children": [
                {"label": "Siraj ud Daula, new Nawab of Bengal, objected to EIC's unauthorized fortification of Calcutta and support for his enemies", "type": "leaf"},
                {"label": "Siraj captured Calcutta (June 1756); 'Black Hole of Calcutta' incident — 64 imprisoned, allegedly 43 died (disputed by historians)", "type": "leaf"},
                {"label": "Clive conspired with Mir Jafar (Siraj's commander-in-chief), Jagat Seth bankers, Omichand — agreed to make Mir Jafar Nawab in exchange for rewards", "type": "leaf"}
            ]},
            {"label": "Battle (23 June 1757)", "type": "branch", "date": "23 June 1757", "children": [
                {"label": "Battle at Plassey mango grove: Mir Jafar's forces (largest Nawab contingent) remained neutral during battle — decisive betrayal", "type": "leaf"},
                {"label": "Siraj defeated and killed within 24 hours; Robert Clive installed Mir Jafar as Nawab", "type": "leaf"},
                {"label": "EIC received Rs 17.7 million (1.77 crore) personal gifts to Clive + Rs 24 million to the Company — most profitable battle in history", "type": "leaf"}
            ]},
            {"label": "Significance", "type": "branch", "date": "Post-1757", "children": [
                {"label": "Beginning of British political dominance in Bengal — transition from trading company to territorial power", "type": "leaf"},
                {"label": "Bengal's revenues financed further British conquests across India — Plassey funded Buxar, Mysore, Maratha campaigns", "type": "leaf"},
                {"label": "Often called the 'first battle of Indian independence' in nationalist historiography; symbolises colonial subjugation's start", "type": "leaf"}
            ]}
        ],
        "hi": [
            {"label": "पृष्ठभूमि और षड्यंत्र", "type": "branch", "date": "1757", "children": [
                {"label": "बंगाल के नए नवाब सिराज उद दौला ने EIC के कलकत्ता के अनधिकृत किलेबंदी और उनके दुश्मनों को समर्थन पर आपत्ति जताई", "type": "leaf"},
                {"label": "सिराज ने कलकत्ता पर कब्जा किया (जून 1756); 'कलकत्ता का काला बिल' — 64 कैद, कथित रूप से 43 की मृत्यु (इतिहासकारों में विवादित)", "type": "leaf"},
                {"label": "क्लाइव ने मीर जाफर (सिराज के सेनापति), जगत सेठ बैंकरों, ओमीचंद के साथ षड्यंत्र किया — पुरस्कारों के बदले मीर जाफर को नवाब बनाने पर सहमति", "type": "leaf"}
            ]},
            {"label": "युद्ध (23 जून 1757)", "type": "branch", "date": "23 जून 1757", "children": [
                {"label": "प्लासी के आम के बाग में युद्ध: मीर जाफर की सेनाएं (सबसे बड़ा नवाब दल) युद्ध के दौरान तटस्थ रहीं — निर्णायक विश्वासघात", "type": "leaf"},
                {"label": "सिराज 24 घंटे में पराजित और मारा गया; रॉबर्ट क्लाइव ने मीर जाफर को नवाब बनाया", "type": "leaf"},
                {"label": "EIC को 1.77 करोड़ रु. व्यक्तिगत उपहार क्लाइव को + 2.4 करोड़ कंपनी को मिले — इतिहास की सबसे लाभदायक लड़ाई", "type": "leaf"}
            ]},
            {"label": "महत्व", "type": "branch", "date": "1757 के बाद", "children": [
                {"label": "बंगाल में ब्रिटिश राजनीतिक वर्चस्व की शुरुआत — व्यापारिक कंपनी से क्षेत्रीय शक्ति में परिवर्तन", "type": "leaf"},
                {"label": "बंगाल के राजस्व ने भारत भर में आगे की ब्रिटिश विजयों को वित्तपोषित किया — प्लासी ने बक्सर, मैसूर, मराठा अभियानों को वित्तपोषित किया", "type": "leaf"},
                {"label": "राष्ट्रवादी इतिहास-लेखन में अक्सर 'भारतीय स्वतंत्रता की पहली लड़ाई' कहलाती है; औपनिवेशिक दासता की शुरुआत का प्रतीक", "type": "leaf"}
            ]}
        ]
    },
    "bengal-dual-polity-in-bengal": {
        "en": [
            {"label": "Origins of Dual Polity", "type": "branch", "date": "1765-1772", "children": [
                {"label": "After Buxar (1764): EIC held Diwani (revenue/finance) while Nawab retained Nizamat (administration/criminal justice)", "type": "leaf"},
                {"label": "EIC appointed two Deputy Diwans (Indian officials) to manage day-to-day revenue but remained accountable to no one in Bengal", "type": "leaf"},
                {"label": "Nawab relied on EIC subsidy to pay his own administrative costs — making him financially dependent on EIC", "type": "leaf"}
            ]},
            {"label": "Consequences", "type": "branch", "date": "1765-1772", "children": [
                {"label": "Revenue maximised without accountability: EIC extracted maximum land revenue; no investment in agriculture or infrastructure", "type": "leaf"},
                {"label": "Bengal Famine 1770: Estimated 1/3 of population died (~10 million); EIC raised revenue demand even during famine years", "type": "leaf"},
                {"label": "Administrative vacuum: Nawab had authority but no resources; EIC had resources but no administrative responsibility", "type": "leaf"}
            ]},
            {"label": "Warren Hastings' Abolition (1772)", "type": "branch", "date": "1772", "children": [
                {"label": "Hastings took direct charge of revenue administration; abolished dual polity; district-level revenue collection by EIC officials", "type": "leaf"},
                {"label": "Created Collectors in each district — embryonic form of the District Collector system that persists in India today", "type": "leaf"}
            ]}
        ],
        "hi": [
            {"label": "द्वैध शासन की उत्पत्ति", "type": "branch", "date": "1765-1772", "children": [
                {"label": "बक्सर (1764) के बाद: EIC ने दीवानी (राजस्व/वित्त) धारण की जबकि नवाब ने निजामत (प्रशासन/आपराधिक न्याय) बनाए रखा", "type": "leaf"},
                {"label": "EIC ने दैनिक राजस्व प्रबंधन के लिए दो उप-दीवान (भारतीय अधिकारी) नियुक्त किए लेकिन बंगाल में किसी के प्रति उत्तरदायी नहीं थे", "type": "leaf"},
                {"label": "नवाब अपने प्रशासनिक खर्चों के लिए EIC सब्सिडी पर निर्भर था — उसे EIC पर वित्तीय रूप से आश्रित बनाया", "type": "leaf"}
            ]},
            {"label": "परिणाम", "type": "branch", "date": "1765-1772", "children": [
                {"label": "जवाबदेही के बिना राजस्व अधिकतमीकरण: EIC ने अधिकतम भूमि राजस्व निकाला; कृषि या बुनियादी ढांचे में कोई निवेश नहीं", "type": "leaf"},
                {"label": "बंगाल अकाल 1770: अनुमानित 1/3 जनसंख्या मृत (~1 करोड़); EIC ने अकाल वर्षों में भी राजस्व मांग बढ़ाई", "type": "leaf"},
                {"label": "प्रशासनिक शून्य: नवाब के पास अधिकार था लेकिन संसाधन नहीं; EIC के पास संसाधन था लेकिन प्रशासनिक जिम्मेदारी नहीं", "type": "leaf"}
            ]},
            {"label": "वारेन हेस्टिंग्स द्वारा उन्मूलन (1772)", "type": "branch", "date": "1772", "children": [
                {"label": "हेस्टिंग्स ने राजस्व प्रशासन का प्रत्यक्ष प्रभार लिया; द्वैध शासन समाप्त किया; EIC अधिकारियों द्वारा जिला-स्तरीय राजस्व संग्रह", "type": "leaf"},
                {"label": "प्रत्येक जिले में कलेक्टर बनाए — जिला कलेक्टर प्रणाली का भ्रूण रूप जो आज भी भारत में जारी है", "type": "leaf"}
            ]}
        ]
    },
    "bengal-dual-polity-in-bengal-diwani-and-nizamat": {
        "en": [
            {"label": "Diwani Rights (Revenue)", "type": "branch", "date": "Post-1765", "children": [
                {"label": "Diwani granted by Mughal Emperor Shah Alam II via Treaty of Allahabad (1765) — gave EIC legal right to collect revenues of Bengal, Bihar, Orissa", "type": "leaf"},
                {"label": "Annual revenue: approximately Rs 2.5 crore from Bengal alone; extracted through zamindars and direct collection mechanisms", "type": "leaf"},
                {"label": "EIC used Bengal revenue to finance 'investments' (purchasing Indian goods for export) — no silver bullion needed", "type": "leaf"}
            ]},
            {"label": "Nizamat (Administration)", "type": "branch", "date": "Post-1765", "children": [
                {"label": "Nizamat covered criminal justice, police, general administration — retained by Nawab (Najm ud Daula and successors)", "type": "leaf"},
                {"label": "Nawab's Nizamat funded by EIC stipend of Rs 53 lakh/year — insufficient, leading to administrative decay", "type": "leaf"},
                {"label": "Without revenue, Nawab's authority was nominal; EIC's power was real but exercised without accountability", "type": "leaf"}
            ]},
            {"label": "Structural Contradiction", "type": "branch", "date": "1765-1772", "children": [
                {"label": "Revenue power without administration = exploitation without improvement; administrative power without resources = nominal authority", "type": "leaf"},
                {"label": "Led to the catastrophic Bengal Famine of 1770; Warren Hastings recognised its failure and unified both functions under EIC in 1772", "type": "leaf"}
            ]}
        ],
        "hi": [
            {"label": "दीवानी अधिकार (राजस्व)", "type": "branch", "date": "1765 के बाद", "children": [
                {"label": "दीवानी मुगल सम्राट शाह आलम II द्वारा इलाहाबाद की संधि (1765) के माध्यम से प्रदान की — EIC को बंगाल, बिहार, उड़ीसा का राजस्व संग्रहण का कानूनी अधिकार दिया", "type": "leaf"},
                {"label": "वार्षिक राजस्व: केवल बंगाल से लगभग 2.5 करोड़ रु.; जमींदारों और प्रत्यक्ष संग्रहण तंत्र के माध्यम से निकाला गया", "type": "leaf"},
                {"label": "EIC ने बंगाल राजस्व का उपयोग 'निवेश' (निर्यात के लिए भारतीय माल खरीद) को वित्तपोषित करने के लिए किया — चांदी की सिल्लियां आवश्यक नहीं", "type": "leaf"}
            ]},
            {"label": "निजामत (प्रशासन)", "type": "branch", "date": "1765 के बाद", "children": [
                {"label": "निजामत में आपराधिक न्याय, पुलिस, सामान्य प्रशासन शामिल था — नवाब (नज्म उद दौला और उत्तराधिकारी) के पास बना रहा", "type": "leaf"},
                {"label": "नवाब की निजामत EIC वार्षिक 53 लाख रु. वजीफे से वित्तपोषित थी — अपर्याप्त, प्रशासनिक क्षय का कारण", "type": "leaf"},
                {"label": "राजस्व के बिना नवाब का अधिकार नाममात्र था; EIC की शक्ति वास्तविक थी लेकिन जवाबदेही के बिना प्रयोग की गई", "type": "leaf"}
            ]},
            {"label": "संरचनात्मक विरोधाभास", "type": "branch", "date": "1765-1772", "children": [
                {"label": "प्रशासन के बिना राजस्व शक्ति = सुधार के बिना शोषण; संसाधनों के बिना प्रशासनिक शक्ति = नाममात्र अधिकार", "type": "leaf"},
                {"label": "1770 के विनाशकारी बंगाल अकाल का कारण बना; वारेन हेस्टिंग्स ने इसकी विफलता पहचानी और 1772 में दोनों कार्यों को EIC के तहत एकीकृत किया", "type": "leaf"}
            ]}
        ]
    },
    "bengal-treaty-of-allahabad": {
        "en": [
            {"label": "Context & Parties", "type": "branch", "date": "1765", "children": [
                {"label": "Concluded by Robert Clive in August 1765 with two parties: Shah Alam II (Mughal Emperor) and Shuja ud Daula (Nawab of Awadh)", "type": "leaf"},
                {"label": "Follows EIC's decisive victory at Battle of Buxar (1764) — EIC dictated terms to all defeated parties", "type": "leaf"}
            ]},
            {"label": "Key Provisions", "type": "branch", "date": "1765", "children": [
                {"label": "Shah Alam II: Granted Diwani of Bengal, Bihar, Orissa to EIC; received Allahabad and Kara as jagir; EIC paid him Rs 26 lakh/year pension", "type": "leaf"},
                {"label": "Shuja ud Daula: Paid Rs 50 lakh war indemnity; accepted British military garrison in Awadh at own expense — Awadh became virtual buffer state", "type": "leaf"},
                {"label": "EIC now exercised dual role: revenue sovereign (Diwan) under Mughal fiction while maintaining own military supremacy", "type": "leaf"}
            ]},
            {"label": "Historical Significance", "type": "branch", "date": "Post-1765", "children": [
                {"label": "Transformed EIC from a trading company with territorial possessions into a revenue-collecting state under Mughal legal cover", "type": "leaf"},
                {"label": "Created the legal basis for 'Dual Government' that persisted until Warren Hastings' reforms of 1772", "type": "leaf"},
                {"label": "Shah Alam's granting of Diwani was the most important constitutional act in British Indian history — gave EIC legitimacy over Bengal", "type": "leaf"}
            ]}
        ],
        "hi": [
            {"label": "संदर्भ और पक्षकार", "type": "branch", "date": "1765", "children": [
                {"label": "रॉबर्ट क्लाइव द्वारा अगस्त 1765 में दो पक्षकारों के साथ: शाह आलम II (मुगल सम्राट) और शुजा उद दौला (अवध के नवाब)", "type": "leaf"},
                {"label": "बक्सर की लड़ाई (1764) में EIC की निर्णायक जीत के बाद — EIC ने सभी पराजित पक्षकारों पर शर्तें थोपीं", "type": "leaf"}
            ]},
            {"label": "प्रमुख प्रावधान", "type": "branch", "date": "1765", "children": [
                {"label": "शाह आलम II: बंगाल, बिहार, उड़ीसा की दीवानी EIC को प्रदान की; इलाहाबाद और कारा जागीर के रूप में पाए; EIC ने उन्हें 26 लाख रु./वर्ष पेंशन दी", "type": "leaf"},
                {"label": "शुजा उद दौला: 50 लाख रु. युद्ध क्षतिपूर्ति दी; अपने खर्च पर अवध में ब्रिटिश सैन्य गैरिसन स्वीकार किया — अवध वस्तुतः बफर राज्य बना", "type": "leaf"},
                {"label": "EIC ने दोहरी भूमिका निभाई: मुगल कानूनी आवरण के तहत राजस्व संप्रभु (दीवान) जबकि अपनी सैन्य सर्वोच्चता बनाए रखी", "type": "leaf"}
            ]},
            {"label": "ऐतिहासिक महत्व", "type": "branch", "date": "1765 के बाद", "children": [
                {"label": "EIC को क्षेत्रीय संपत्ति वाली व्यापारिक कंपनी से मुगल कानूनी आवरण के तहत राजस्व संग्रहण करने वाले राज्य में परिवर्तित किया", "type": "leaf"},
                {"label": "वारेन हेस्टिंग्स के 1772 के सुधारों तक बनी रहने वाली 'द्वैध सरकार' का कानूनी आधार बनाया", "type": "leaf"},
                {"label": "शाह आलम का दीवानी प्रदान करना ब्रिटिश भारतीय इतिहास में सबसे महत्वपूर्ण संवैधानिक कार्य था — EIC को बंगाल पर वैधता मिली", "type": "leaf"}
            ]}
        ]
    },
    "british-conquest-of-bengal": {
        "en": [
            {"label": "Commercial Beginnings", "type": "branch", "date": "1600-1756", "children": [
                {"label": "EIC obtained its first factory at Surat (1608) under Mughal Emperor Jahangir; Madras factory 1639; Bombay (Portuguese dowry) 1661", "type": "leaf"},
                {"label": "Bengal factory at Hooghly (1651); Calcutta founded by Job Charnock (1690); Fort William built for defence against European rivals", "type": "leaf"},
                {"label": "Farrukhsiyar's Farman (1717): EIC granted duty-free trade rights in Bengal — exploited extensively using dastaks (passes) for private trade", "type": "leaf"}
            ]},
            {"label": "Conquest Sequence", "type": "branch", "date": "1757-1765", "children": [
                {"label": "Battle of Plassey (1757): Siraj ud Daula defeated by Clive with Mir Jafar's betrayal — EIC gained political foothold in Bengal", "type": "leaf"},
                {"label": "Battle of Buxar (1764): EIC defeated combined forces of Mir Qasim, Mughal Emperor, Awadh Nawab — complete military dominance", "type": "leaf"},
                {"label": "Treaty of Allahabad (1765): EIC received Diwani rights — transformation from trader to revenue-state complete", "type": "leaf"}
            ]},
            {"label": "Administrative Consolidation", "type": "branch", "date": "1765-1793", "children": [
                {"label": "Warren Hastings (1772): Abolished Dual Polity; direct revenue collection; reorganised courts and administration", "type": "leaf"},
                {"label": "Cornwallis Code (1793): Rule of law; Permanent Settlement with zamindars; separation of revenue, judicial, commercial functions", "type": "leaf"}
            ]}
        ],
        "hi": [
            {"label": "वाणिज्यिक शुरुआत", "type": "branch", "date": "1600-1756", "children": [
                {"label": "EIC को मुगल सम्राट जहांगीर के तहत सूरत में पहली कोठी (1608) मिली; मद्रास कोठी 1639; बॉम्बे (पुर्तगाली दहेज) 1661", "type": "leaf"},
                {"label": "हुगली में बंगाल कोठी (1651); जॉब चार्नक द्वारा कलकत्ता की स्थापना (1690); यूरोपीय प्रतिद्वंद्वियों से रक्षा के लिए फोर्ट विलियम बनाया", "type": "leaf"},
                {"label": "फर्रुखसियर का फरमान (1717): EIC को बंगाल में शुल्क-मुक्त व्यापार अधिकार दिया — निजी व्यापार के लिए दस्तकों का व्यापक शोषण", "type": "leaf"}
            ]},
            {"label": "विजय क्रम", "type": "branch", "date": "1757-1765", "children": [
                {"label": "प्लासी की लड़ाई (1757): मीर जाफर के विश्वासघात के साथ क्लाइव ने सिराज उद दौला को हराया — EIC ने बंगाल में राजनीतिक पैर जमाया", "type": "leaf"},
                {"label": "बक्सर की लड़ाई (1764): EIC ने मीर कासिम, मुगल सम्राट, अवध नवाब की संयुक्त सेनाओं को हराया — पूर्ण सैन्य वर्चस्व", "type": "leaf"},
                {"label": "इलाहाबाद की संधि (1765): EIC को दीवानी अधिकार मिले — व्यापारी से राजस्व-राज्य में परिवर्तन पूर्ण", "type": "leaf"}
            ]},
            {"label": "प्रशासनिक समेकन", "type": "branch", "date": "1765-1793", "children": [
                {"label": "वारेन हेस्टिंग्स (1772): द्वैध शासन समाप्त; प्रत्यक्ष राजस्व संग्रहण; न्यायालयों और प्रशासन का पुनर्गठन", "type": "leaf"},
                {"label": "कॉर्नवालिस कोड (1793): कानून का शासन; जमींदारों के साथ स्थायी बंदोबस्त; राजस्व, न्यायिक, वाणिज्यिक कार्यों का पृथक्करण", "type": "leaf"}
            ]}
        ]
    },
    "eic-treaties-surat-purandar-salbai-bassein-poona-gwalior-and-mandsor": {
        "en": [
            {"label": "Early Maratha Treaties", "type": "branch", "date": "1775-1782", "children": [
                {"label": "Treaty of Surat (1775): EIC supported Raghunathrao for Peshwaship; first EIC-Maratha alliance; later repudiated by Calcutta Council", "type": "leaf"},
                {"label": "Treaty of Purandar (1776): EIC negotiated with Peshwa; Raghunathrao's cause abandoned; EIC to help suppress rebels — soon violated", "type": "leaf"},
                {"label": "Treaty of Salbai (1782): Ended First Anglo-Maratha War; 20-year peace; Madhav Rao II as Peshwa; EIC kept Salsette island; status quo restored", "type": "leaf"}
            ]},
            {"label": "Second Phase Treaties", "type": "branch", "date": "1802-1803", "children": [
                {"label": "Treaty of Bassein (1802): Peshwa Baji Rao II accepted Subsidiary Alliance; humiliation that triggered Second Anglo-Maratha War", "type": "leaf"},
                {"label": "Treaty of Poona (1817): After Peshwa attacked Residency; EIC imposed harsh terms; Peshwa's territories significantly reduced", "type": "leaf"},
                {"label": "Treaty of Gwalior (1817): Scindia recognised British paramountcy; gave up claim to Bundelkhand; accepted Subsidiary Alliance", "type": "leaf"}
            ]},
            {"label": "Final Settlements", "type": "branch", "date": "1817-1826", "children": [
                {"label": "Treaty of Mandsor (1818): Holkar accepted Subsidiary Alliance after decisive defeat at Mahidpur (Dec 1817)", "type": "leaf"},
                {"label": "These treaties collectively completed British paramountcy over all Maratha chiefs — end of the Maratha Confederacy as a political power", "type": "leaf"}
            ]}
        ],
        "hi": [
            {"label": "प्रारंभिक मराठा संधियाँ", "type": "branch", "date": "1775-1782", "children": [
                {"label": "सूरत की संधि (1775): EIC ने पेशवाई के लिए रघुनाथराव का समर्थन किया; पहला EIC-मराठा गठबंधन; बाद में कलकत्ता परिषद ने अस्वीकार किया", "type": "leaf"},
                {"label": "पुरंदर की संधि (1776): EIC ने पेशवा के साथ वार्ता की; राघोबा का पक्ष छोड़ा; विद्रोहियों को दबाने में मदद — जल्द उल्लंघन हुआ", "type": "leaf"},
                {"label": "सालबाई की संधि (1782): प्रथम आंग्ल-मराठा युद्ध समाप्त; 20 वर्ष की शांति; माधव राव II पेशवा; EIC ने सालसेट द्वीप रखा; यथास्थिति बहाल", "type": "leaf"}
            ]},
            {"label": "दूसरे चरण की संधियाँ", "type": "branch", "date": "1802-1803", "children": [
                {"label": "बसई की संधि (1802): पेशवा बाजी राव II ने सहायक संधि स्वीकार की; अपमान ने द्वितीय आंग्ल-मराठा युद्ध उत्प्रेरित किया", "type": "leaf"},
                {"label": "पुणे की संधि (1817): पेशवा द्वारा रेजीडेंसी पर हमले के बाद; EIC ने कठोर शर्तें थोपीं; पेशवा के क्षेत्र काफी कम हुए", "type": "leaf"},
                {"label": "ग्वालियर की संधि (1817): सिंधिया ने ब्रिटिश परमाधिकार स्वीकार किया; बुंदेलखंड पर दावा छोड़ा; सहायक संधि स्वीकार की", "type": "leaf"}
            ]},
            {"label": "अंतिम समझौते", "type": "branch", "date": "1817-1826", "children": [
                {"label": "मंदसौर की संधि (1818): महीदपुर में निर्णायक हार (दिसं. 1817) के बाद होल्कर ने सहायक संधि स्वीकार की", "type": "leaf"},
                {"label": "इन संधियों ने सामूहिक रूप से सभी मराठा सरदारों पर ब्रिटिश परमाधिकार पूर्ण किया — मराठा संघ का एक राजनीतिक शक्ति के रूप में अंत", "type": "leaf"}
            ]}
        ]
    },
    "marathas-defeat-and-its-reasons": {
        "en": [
            {"label": "Internal Weaknesses", "type": "branch", "date": "Post-1772", "children": [
                {"label": "Death of Madhav Rao I (1772): Lost the Marathas' greatest military-administrative genius; succession disputes weakened the confederacy", "type": "leaf"},
                {"label": "Absence of central authority: Five independent chiefs (Peshwa, Scindia, Holkar, Bhonsle, Gaekwad) often fought each other instead of the British", "type": "leaf"},
                {"label": "Battle of Panipat III (1761): Marathas lost to Ahmad Shah Durrani; lost 200,000 men including Viswas Rao, Bhau — never fully recovered", "type": "leaf"}
            ]},
            {"label": "Military Deficiencies", "type": "branch", "date": "1790s-1818", "children": [
                {"label": "Maratha cavalry tactics became obsolete against British disciplined infantry with artillery; failure to modernise military", "type": "leaf"},
                {"label": "French officers (De Boigne, Perron) modernised Scindia's infantry; but after Napoleonic Wars, French support ended and these officers left", "type": "leaf"},
                {"label": "No unified command during any of the three Anglo-Maratha wars; each chief fought independently — never coordinated strategy", "type": "leaf"}
            ]},
            {"label": "British Advantages", "type": "branch", "date": "1757-1818", "children": [
                {"label": "Bengal revenues financed British wars across India; Marathas had no comparable consolidated resource base", "type": "leaf"},
                {"label": "British diplomacy (Subsidiary Alliance) isolated each Maratha chief and turned them against each other", "type": "leaf"},
                {"label": "Treaty of Bassein (1802): Peshwa's acceptance split Maratha confederacy; Scindia and Bhonsle went to war alone without coordinated Maratha support", "type": "leaf"}
            ]}
        ],
        "hi": [
            {"label": "आंतरिक कमजोरियाँ", "type": "branch", "date": "1772 के बाद", "children": [
                {"label": "माधव राव I की मृत्यु (1772): मराठों के सबसे महान सैन्य-प्रशासनिक प्रतिभाशाली की हानि; उत्तराधिकार विवादों ने संघ को कमजोर किया", "type": "leaf"},
                {"label": "केंद्रीय प्राधिकरण का अभाव: पाँच स्वतंत्र सरदार (पेशवा, सिंधिया, होल्कर, भोंसले, गायकवाड) अक्सर ब्रिटिश के बजाय एक-दूसरे से लड़े", "type": "leaf"},
                {"label": "पानीपत की तृतीय लड़ाई (1761): मराठे अहमद शाह दुर्रानी से हारे; विश्वास राव, भाऊ सहित 2 लाख लोग खोए — कभी पूरी तरह उबर नहीं पाए", "type": "leaf"}
            ]},
            {"label": "सैन्य कमियाँ", "type": "branch", "date": "1790-1818", "children": [
                {"label": "मराठा घुड़सवार रणनीति तोपखाने के साथ ब्रिटिश अनुशासित पैदल सेना के खिलाफ पुरानी पड़ गई; सेना को आधुनिक बनाने में विफलता", "type": "leaf"},
                {"label": "फ्रांसीसी अधिकारियों (डी बॉइन, पेरन) ने सिंधिया की पैदल सेना को आधुनिक बनाया; लेकिन नेपोलियन युद्धों के बाद फ्रांसीसी समर्थन समाप्त हुआ", "type": "leaf"},
                {"label": "तीनों आंग्ल-मराठा युद्धों में कोई एकीकृत कमांड नहीं; प्रत्येक सरदार स्वतंत्र रूप से लड़ा — कभी समन्वित रणनीति नहीं", "type": "leaf"}
            ]},
            {"label": "ब्रिटिश लाभ", "type": "branch", "date": "1757-1818", "children": [
                {"label": "बंगाल के राजस्व ने पूरे भारत में ब्रिटिश युद्धों को वित्तपोषित किया; मराठों के पास कोई तुलनीय समेकित संसाधन आधार नहीं था", "type": "leaf"},
                {"label": "ब्रिटिश कूटनीति (सहायक संधि) ने प्रत्येक मराठा सरदार को अलग-थलग किया और उन्हें एक-दूसरे के खिलाफ कर दिया", "type": "leaf"},
                {"label": "बसई की संधि (1802): पेशवा की स्वीकृति ने मराठा संघ को विभाजित किया; सिंधिया और भोंसले समन्वित मराठा समर्थन के बिना अकेले युद्ध में गए", "type": "leaf"}
            ]}
        ]
    },
    "prominent-maratha-families-ruling-from-different-places": {
        "en": [
            {"label": "The Five Maratha Sardars", "type": "branch", "date": "18th Century", "children": [
                {"label": "Peshwa: Prime Ministers of Maratha Empire; ruled from Pune; Brahmin family; Balaji Vishwanath founded the hereditary line (1714)", "type": "leaf"},
                {"label": "Scindia (Shinde): Ruled from Gwalior (later); Mahadji Scindia (1761-94) dominated Mughal court and recovered Delhi for Marathas", "type": "leaf"},
                {"label": "Holkar: Ruled from Indore; Malhar Rao Holkar founder; Ahilya Bai Holkar (1767-95) renowned as exemplary administrator and temple builder", "type": "leaf"}
            ]},
            {"label": "Bhonsle & Gaekwad", "type": "branch", "date": "18th Century", "children": [
                {"label": "Bhonsle: Ruled from Nagpur; controlled large central Indian territories including Berar; descendants of Shivaji's lineage", "type": "leaf"},
                {"label": "Gaekwad: Ruled from Baroda (Vadodara); controlled Gujarat; earliest to accept British influence; Treaty of Vadodara (1805)", "type": "leaf"}
            ]},
            {"label": "The Maratha Confederacy", "type": "branch", "date": "1720-1818", "children": [
                {"label": "Peaked under Peshwa Bajirao I (1720-40): expanded to Malwa, Bengal, Punjab, Rajputana — nearly pan-Indian dominion", "type": "leaf"},
                {"label": "Confederacy's fatal flaw: no formal central authority; each sardar pursued own interests and fought rival chiefs, enabling British 'divide and rule'", "type": "leaf"},
                {"label": "After 1818: Peshwa abolished; Gaekwad, Scindia, Holkar, Bhonsle survived as princely states under British paramountcy till 1947", "type": "leaf"}
            ]}
        ],
        "hi": [
            {"label": "पाँच मराठा सरदार", "type": "branch", "date": "18वीं सदी", "children": [
                {"label": "पेशवा: मराठा साम्राज्य के प्रधानमंत्री; पुणे से शासन; ब्राह्मण परिवार; बालाजी विश्वनाथ ने वंशानुगत वंश की स्थापना की (1714)", "type": "leaf"},
                {"label": "सिंधिया (शिंदे): ग्वालियर से शासन (बाद में); महादजी सिंधिया (1761-94) ने मुगल दरबार पर वर्चस्व बनाया और मराठों के लिए दिल्ली वापस ली", "type": "leaf"},
                {"label": "होल्कर: इंदौर से शासन; मल्हार राव होल्कर संस्थापक; अहिल्या बाई होल्कर (1767-95) अनुकरणीय प्रशासक और मंदिर निर्माता के रूप में प्रसिद्ध", "type": "leaf"}
            ]},
            {"label": "भोंसले और गायकवाड", "type": "branch", "date": "18वीं सदी", "children": [
                {"label": "भोंसले: नागपुर से शासन; बेरार सहित बड़े मध्य भारतीय क्षेत्रों पर नियंत्रण; शिवाजी के वंश के वंशज", "type": "leaf"},
                {"label": "गायकवाड: बड़ौदा (वडोदरा) से शासन; गुजरात पर नियंत्रण; ब्रिटिश प्रभाव स्वीकार करने वाले पहले; वडोदरा की संधि (1805)", "type": "leaf"}
            ]},
            {"label": "मराठा परिसंघ", "type": "branch", "date": "1720-1818", "children": [
                {"label": "पेशवा बाजीराव I (1720-40) के अधीन चरम पर: मालवा, बंगाल, पंजाब, राजपूताना तक विस्तार — लगभग सर्व-भारतीय प्रभुत्व", "type": "leaf"},
                {"label": "परिसंघ की घातक खामी: कोई औपचारिक केंद्रीय प्राधिकरण नहीं; प्रत्येक सरदार अपने हितों का पीछा करता था और प्रतिद्वंद्वी सरदारों से लड़ता था", "type": "leaf"},
                {"label": "1818 के बाद: पेशवाई समाप्त; गायकवाड, सिंधिया, होल्कर, भोंसले 1947 तक ब्रिटिश परमाधिकार के तहत रियासतों के रूप में बचे", "type": "leaf"}
            ]}
        ]
    },
    "settlements-at-various-places": {
        "en": [
            {"label": "Early EIC Settlements", "type": "branch", "date": "1600s-1700s", "children": [
                {"label": "Surat (1608): First EIC factory; Mughal permission obtained by Thomas Best's naval victory over Portuguese; became main western India hub", "type": "leaf"},
                {"label": "Madras/Fort St George (1639): Francis Day obtained lease from local Nayak ruler; became Presidency town for South India", "type": "leaf"},
                {"label": "Bombay (1661): Received from Portugal as dowry of Catherine of Braganza; transferred to EIC by Charles II in 1668 for £10/year", "type": "leaf"}
            ]},
            {"label": "Bengal Settlements", "type": "branch", "date": "1651-1700", "children": [
                {"label": "Hooghly Factory (1651): First EIC factory in Bengal; established under Mughal permission after physician Gabriel Boughton secured trading rights", "type": "leaf"},
                {"label": "Calcutta (1690): Job Charnock established settlement; Fort William built 1700; became capital of British India under Warren Hastings", "type": "leaf"},
                {"label": "Farrukhsiyar's Farman (1717): Granted EIC duty-free trade in Bengal against 3,000 rupees annual payment — most exploited charter of EIC in India", "type": "leaf"}
            ]},
            {"label": "Interior Settlements", "type": "branch", "date": "18th-19th Century", "children": [
                {"label": "Seringapatam (1799), Poona (1802 Residency): British residents established as military control points after Subsidiary Alliances", "type": "leaf"},
                {"label": "Delhi (1803): EIC took control after defeating Scindia; Mughal Emperor retained as pensioner; British Resident at Mughal court", "type": "leaf"},
                {"label": "Lahore (1849): After Punjab annexation; Lawrence Brothers administered Punjab Board — model of direct administration", "type": "leaf"}
            ]}
        ],
        "hi": [
            {"label": "प्रारंभिक EIC बस्तियाँ", "type": "branch", "date": "1600-1700 का दशक", "children": [
                {"label": "सूरत (1608): पहली EIC कोठी; थॉमस बेस्ट की नौसैनिक जीत के बाद मुगल अनुमति; पश्चिम भारत का मुख्य केंद्र बना", "type": "leaf"},
                {"label": "मद्रास/फोर्ट सेंट जॉर्ज (1639): फ्रांसिस डे ने स्थानीय नायक शासक से पट्टा प्राप्त किया; दक्षिण भारत के लिए प्रेसीडेंसी शहर बना", "type": "leaf"},
                {"label": "बॉम्बे (1661): कैथरीन ऑफ ब्रगांजा के दहेज के रूप में पुर्तगाल से प्राप्त; चार्ल्स II ने 1668 में £10/वर्ष पर EIC को हस्तांतरित किया", "type": "leaf"}
            ]},
            {"label": "बंगाल की बस्तियाँ", "type": "branch", "date": "1651-1700", "children": [
                {"label": "हुगली कोठी (1651): बंगाल में पहली EIC कोठी; चिकित्सक गेब्रियल बॉटन द्वारा व्यापार अधिकार सुरक्षित करने के बाद मुगल अनुमति से स्थापित", "type": "leaf"},
                {"label": "कलकत्ता (1690): जॉब चार्नक ने बस्ती स्थापित की; 1700 में फोर्ट विलियम बनाया; वारेन हेस्टिंग्स के तहत ब्रिटिश भारत की राजधानी बना", "type": "leaf"},
                {"label": "फर्रुखसियर का फरमान (1717): 3,000 रु. वार्षिक भुगतान पर बंगाल में EIC को शुल्क-मुक्त व्यापार दिया — भारत में EIC का सर्वाधिक शोषित अधिकार-पत्र", "type": "leaf"}
            ]},
            {"label": "आंतरिक बस्तियाँ", "type": "branch", "date": "18वीं-19वीं सदी", "children": [
                {"label": "श्रीरंगपट्टनम (1799), पुणे (1802 रेजीडेंसी): सहायक संधियों के बाद सैन्य नियंत्रण केंद्र के रूप में ब्रिटिश रेजिडेंट स्थापित", "type": "leaf"},
                {"label": "दिल्ली (1803): सिंधिया को हराने के बाद EIC का नियंत्रण; मुगल सम्राट पेंशनभोगी के रूप में बनाए रखे; मुगल दरबार में ब्रिटिश रेजिडेंट", "type": "leaf"},
                {"label": "लाहौर (1849): पंजाब विलय के बाद; लॉरेंस ब्रदर्स ने पंजाब बोर्ड का प्रशासन किया — प्रत्यक्ष प्रशासन का आदर्श", "type": "leaf"}
            ]}
        ]
    },
    "the-subsidiary-alliance-system-and-its-impact": {
        "en": [
            {"label": "System Mechanics", "type": "branch", "date": "Wellesley 1798+", "children": [
                {"label": "Introduced by Lord Wellesley (1798): Indian ruler accepts British troops on his soil; pays for their maintenance", "type": "leaf"},
                {"label": "If ruler can't pay, cedes territory to EIC; ruler surrenders foreign policy control — can't form alliances without British approval", "type": "leaf"},
                {"label": "British Resident placed at court with access to intelligence; ruler must dismiss all non-British European officers", "type": "leaf"}
            ]},
            {"label": "States that Accepted", "type": "branch", "date": "1798-1818", "children": [
                {"label": "Hyderabad (1798): First Indian state; Nizam ceded districts worth Rs 24 lakh to pay for subsidiary force", "type": "leaf"},
                {"label": "Mysore (1799): After Tipu's defeat; Wadiyar dynasty restored under subsidiary alliance; most of southern India controlled", "type": "leaf"},
                {"label": "Awadh (1801), Peshwa/Marathas (1802 Bassein), Scindia (1803), Holkar (1818), Rajputana states (1818-23)", "type": "leaf"}
            ]},
            {"label": "Impact", "type": "branch", "date": "Post-1818", "children": [
                {"label": "Positive for EIC: Eliminated need for expensive frontier wars; ruler pays for his own subjugation; internal security guaranteed", "type": "leaf"},
                {"label": "Negative for Indian states: Financial ruin through subsidiary payments; military dependence; economic exploitation; administrative decay", "type": "leaf"},
                {"label": "Created buffer states (Awadh, Hyderabad, Mysore) that survived until independence — basis of 'Princely India' under British paramountcy", "type": "leaf"}
            ]}
        ],
        "hi": [
            {"label": "प्रणाली की कार्यप्रणाली", "type": "branch", "date": "वेलेजली 1798+", "children": [
                {"label": "लॉर्ड वेलेजली द्वारा प्रवर्तित (1798): भारतीय शासक अपनी भूमि पर ब्रिटिश सैनिकों को स्वीकार करता है; उनके रखरखाव का भुगतान करता है", "type": "leaf"},
                {"label": "यदि शासक भुगतान नहीं कर सकता, EIC को क्षेत्र सौंपता है; शासक विदेश नीति नियंत्रण छोड़ता है — ब्रिटिश अनुमोदन के बिना गठबंधन नहीं", "type": "leaf"},
                {"label": "ब्रिटिश रेजिडेंट खुफिया जानकारी तक पहुंच के साथ दरबार में रखा जाता है; शासक को सभी गैर-ब्रिटिश यूरोपीय अधिकारी बर्खास्त करने होंगे", "type": "leaf"}
            ]},
            {"label": "स्वीकार करने वाले राज्य", "type": "branch", "date": "1798-1818", "children": [
                {"label": "हैदराबाद (1798): पहला भारतीय राज्य; निजाम ने सहायक सेना के भुगतान के लिए 24 लाख रु. मूल्य के जिले सौंपे", "type": "leaf"},
                {"label": "मैसूर (1799): टीपू की हार के बाद; वाडियार वंश सहायक संधि के तहत बहाल; अधिकांश दक्षिण भारत नियंत्रित", "type": "leaf"},
                {"label": "अवध (1801), पेशवा/मराठा (1802 बसई), सिंधिया (1803), होल्कर (1818), राजपूताना राज्य (1818-23)", "type": "leaf"}
            ]},
            {"label": "प्रभाव", "type": "branch", "date": "1818 के बाद", "children": [
                {"label": "EIC के लिए सकारात्मक: महंगे सीमांत युद्धों की आवश्यकता समाप्त; शासक अपनी ही अधीनता का भुगतान करता है; आंतरिक सुरक्षा गारंटीकृत", "type": "leaf"},
                {"label": "भारतीय राज्यों के लिए नकारात्मक: सहायक भुगतानों से वित्तीय बर्बादी; सैन्य निर्भरता; आर्थिक शोषण; प्रशासनिक क्षय", "type": "leaf"},
                {"label": "बफर राज्य (अवध, हैदराबाद, मैसूर) बनाए जो स्वतंत्रता तक बचे — ब्रिटिश परमाधिकार के तहत 'रियासती भारत' का आधार", "type": "leaf"}
            ]}
        ]
    }
}

MINDMAP_MAPPINGS = {
    "3-anglo-maratha-wars": "3-anglo-maratha-wars",
    "4-anglo-mysore-wars": "4-anglo-mysore-wars",
    "bengal-battle-of-buxar": "bengal-battle-of-buxar",
    "bengal-battle-of-plassey": "bengal-battle-of-plassey",
    "bengal-dual-polity-in-bengal": "bengal-dual-polity-in-bengal",
    "bengal-dual-polity-in-bengal-diwani-and-nizamat": "bengal-dual-polity-in-bengal-diwani-and-nizamat",
    "bengal-treaty-of-allahabad": "bengal-treaty-of-allahabad",
    "british-conquest-of-bengal": "british-conquest-of-bengal",
    "eic-treaties-surat-purandar-salbai-bassein-poona-gwalior-and-mandsor": "eic-treaties-surat-purandar-salbai-bassein-poona-gwalior-and-mandsor",
    "marathas-defeat-and-its-reasons": "marathas-defeat-and-its-reasons",
    "prominent-maratha-families-ruling-from-different-places": "prominent-maratha-families-ruling-from-different-places",
    "settlements-at-various-places": "settlements-at-various-places",
    "the-subsidiary-alliance-system-and-its-impact": "the-subsidiary-alliance-system-and-its-impact"
}

def get_clean_title(folder_name):
    title = folder_name.replace('-', ' ')
    skip = {'of', 'and', 'the', 'for', 'in', 'with', 'to', 'on', 'by', 'or', 'a', 'an', 'at', 'its', 'from'}
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
    <title>{clean_title} - UPSC Study Guide | SJMaths</title>
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
                      f'<title>{clean_title} (Hindi) - UPSC Study Guide | SJMaths</title>',
                      html, count=1)
    os.makedirs(os.path.dirname(hi_html_path), exist_ok=True)
    with open(hi_html_path, 'w', encoding='utf-8') as f:
        f.write(html)

def inject_mindmap(html_path, folder_name, lang):
    with open(html_path, 'r', encoding='utf-8') as f:
        html = f.read()
    html = html.replace('\r\n', '\n')

    for old in ['    <link rel="stylesheet" href="/assets/css/mindmap.min.css?v=2">\n',
                '    <link rel="stylesheet" href="/assets/css/mindmap.min.css?v=1">\n']:
        html = html.replace(old, '')
    html = re.sub(r'\s*<!-- Interactive Mindmap -->.*?<!-- Deep-Dive Study Guide \(Dynamically Rendered\) -->', '\n            <!-- Deep-Dive Study Guide (Dynamically Rendered) -->', html, flags=re.DOTALL)
    html = re.sub(r'\s*<!-- Interactive Mindmap -->.*?renderMindmap\(.*?\);\s*</script>', '', html, flags=re.DOTALL)

    clean_title = get_clean_title(folder_name)
    key = folder_name.lower()
    canonical_key = MINDMAP_MAPPINGS.get(key, "bengal-battle-of-plassey")

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
