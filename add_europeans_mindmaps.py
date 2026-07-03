#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os, re, json

BASE_DIR = r"upsc/modern_history/Arrival-of-Europeans-in-India"

MINDMAP_DATA = {
    "anglo-french-rivalry": {
        "en": [
            {"label": "Origins of Rivalry", "type": "branch", "date": "1740s-1763", "children": [
                {"label": "Both France (Compagnie des Indes) and England (EIC) were competing for trade dominance in South India; conflict mirrored European wars", "type": "leaf"},
                {"label": "War of Austrian Succession (1740-48) triggered First Carnatic War; Seven Years' War (1756-63) triggered Third Carnatic War in India", "type": "leaf"},
                {"label": "French under Dupleix pioneered using Indian troops (sepoys) trained in European warfare — strategy later adopted by EIC", "type": "leaf"}
            ]},
            {"label": "Key Figures", "type": "branch", "date": "French vs British", "children": [
                {"label": "Dupleix (French Governor-General 1742-54): mastermind of French strategy; installed Indian rulers as French clients; recalled to France 1754", "type": "leaf"},
                {"label": "Robert Clive (British): defeated French at Arcot (1751), Plassey (1757); built English dominance on Dupleix's sepoy model", "type": "leaf"},
                {"label": "Lally (French commander 1758-61): captured Fort St David but failed at Madras; defeated at Wandiwash — ended French power in India", "type": "leaf"}
            ]},
            {"label": "Outcome & Significance", "type": "branch", "date": "Post-1763", "children": [
                {"label": "Treaty of Paris (1763): France retained only 5 trading posts (Pondicherry, Chandernagore, Mahe, Karikal, Yanam) — no military or political power", "type": "leaf"},
                {"label": "English victory established unchallenged supremacy; French influence eliminated; way cleared for British paramountcy across India", "type": "leaf"},
                {"label": "Dupleix's recall (1754) was the turning point — French abandoned their vision of an Indian empire while British pursued it", "type": "leaf"}
            ]}
        ],
        "hi": [
            {"label": "प्रतिद्वंद्विता की उत्पत्ति", "type": "branch", "date": "1740-1763", "children": [
                {"label": "फ्रांस (कॉम्पेनी देस इंड्स) और इंग्लैंड (EIC) दोनों दक्षिण भारत में व्यापार वर्चस्व के लिए प्रतिस्पर्धा कर रहे थे; संघर्ष यूरोपीय युद्धों को दर्शाता था", "type": "leaf"},
                {"label": "ऑस्ट्रियन उत्तराधिकार युद्ध (1740-48) ने प्रथम कर्नाटक युद्ध छेड़ा; सप्तवर्षीय युद्ध (1756-63) ने भारत में तृतीय कर्नाटक युद्ध छेड़ा", "type": "leaf"},
                {"label": "डुप्ले के नेतृत्व में फ्रांसीसियों ने यूरोपीय युद्धपद्धति में प्रशिक्षित भारतीय सैनिकों (सिपाहियों) का उपयोग किया — रणनीति बाद में EIC ने अपनाई", "type": "leaf"}
            ]},
            {"label": "प्रमुख व्यक्तित्व", "type": "branch", "date": "फ्रांसीसी बनाम ब्रिटिश", "children": [
                {"label": "डुप्ले (फ्रांसीसी गवर्नर-जनरल 1742-54): फ्रांसीसी रणनीति के सूत्रधार; भारतीय शासकों को फ्रांसीसी ग्राहक के रूप में स्थापित किया; 1754 में वापस बुलाया", "type": "leaf"},
                {"label": "रॉबर्ट क्लाइव (ब्रिटिश): अर्काट (1751), प्लासी (1757) में फ्रांसीसियों को हराया; डुप्ले के सिपाही मॉडल पर अंग्रेजी वर्चस्व बनाया", "type": "leaf"},
                {"label": "लाली (फ्रांसीसी कमांडर 1758-61): फोर्ट सेंट डेविड जीता लेकिन मद्रास में विफल; वांडीवाश में पराजित — भारत में फ्रांसीसी शक्ति का अंत", "type": "leaf"}
            ]},
            {"label": "परिणाम और महत्व", "type": "branch", "date": "1763 के बाद", "children": [
                {"label": "पेरिस की संधि (1763): फ्रांस ने केवल 5 व्यापारिक चौकियां (पांडिचेरी, चंद्रनगर, माहे, करिकल, यनम) बनाए रखीं — कोई सैन्य या राजनीतिक शक्ति नहीं", "type": "leaf"},
                {"label": "अंग्रेजी जीत ने निर्विवाद वर्चस्व स्थापित किया; फ्रांसीसी प्रभाव समाप्त; पूरे भारत में ब्रिटिश परमाधिकार का रास्ता साफ", "type": "leaf"},
                {"label": "डुप्ले की वापसी (1754) निर्णायक मोड़ थी — फ्रांस ने भारतीय साम्राज्य का सपना छोड़ा जबकि ब्रिटेन ने उसे पूरा किया", "type": "leaf"}
            ]}
        ]
    },
    "causes-of-failure-of-portuguese-empire-in-india": {
        "en": [
            {"label": "Military & Naval Decline", "type": "branch", "date": "17th Century", "children": [
                {"label": "Portugal's small population (~1 million) could not sustain large fleets and garrisons across Africa, Brazil, and India simultaneously", "type": "leaf"},
                {"label": "Union with Spain (1580-1640): Portugal's overseas empire neglected; Spanish enemies (Dutch, English) became Portugal's enemies too", "type": "leaf"},
                {"label": "Dutch and English had superior naval technology and commercial organization; Dutch East India Company outcompeted Portuguese by 1620s", "type": "leaf"}
            ]},
            {"label": "Commercial & Administrative Failures", "type": "branch", "date": "16th-17th Century", "children": [
                {"label": "Portuguese trade model based on royal monopoly (Estado da India) was inflexible; profit went to Crown not merchants — no commercial dynamism", "type": "leaf"},
                {"label": "Cartaz system (naval passes): forcing Indian merchants to buy passes for protection alienated local traders; drove them to Dutch and English", "type": "leaf"},
                {"label": "Excessive religious interference: forced conversions and Inquisition in Goa created deep local hostility across India", "type": "leaf"}
            ]},
            {"label": "Political Factors", "type": "branch", "date": "17th Century", "children": [
                {"label": "Loss of Hormuz (1622), Malacca (1641), Ceylon (1658), Cochin (1663) to Dutch; Portuguese Indian Ocean empire dismantled piece by piece", "type": "leaf"},
                {"label": "By 1700, Portuguese retained only Goa, Diu, Daman, and tiny enclaves — from dominant power to minor trader in 150 years", "type": "leaf"}
            ]}
        ],
        "hi": [
            {"label": "सैन्य और नौसैनिक पतन", "type": "branch", "date": "17वीं सदी", "children": [
                {"label": "पुर्तगाल की छोटी आबादी (~10 लाख) अफ्रीका, ब्राज़ील और भारत में एक साथ बड़े बेड़े और गैरिसन बनाए नहीं रख सकती थी", "type": "leaf"},
                {"label": "स्पेन के साथ संघ (1580-1640): पुर्तगाल के विदेशी साम्राज्य की उपेक्षा; स्पेनी दुश्मन (डच, अंग्रेज) पुर्तगाल के भी दुश्मन बने", "type": "leaf"},
                {"label": "डच और अंग्रेजों के पास बेहतर नौसैनिक तकनीक और वाणिज्यिक संगठन थे; 1620 तक डच ईस्ट इंडिया कंपनी ने पुर्तगालियों को पीछे छोड़ा", "type": "leaf"}
            ]},
            {"label": "वाणिज्यिक और प्रशासनिक विफलताएं", "type": "branch", "date": "16वीं-17वीं सदी", "children": [
                {"label": "पुर्तगाली व्यापार मॉडल शाही एकाधिकार (एस्टाडो दा इंडिया) पर आधारित था; लाभ व्यापारियों को नहीं बल्कि क्राउन को — कोई वाणिज्यिक गतिशीलता नहीं", "type": "leaf"},
                {"label": "कारताज़ प्रणाली (नौसैनिक पास): सुरक्षा के लिए भारतीय व्यापारियों को पास खरीदने पर मजबूर करना; उन्हें डच और अंग्रेजों की ओर धकेला", "type": "leaf"},
                {"label": "अत्यधिक धार्मिक हस्तक्षेप: गोवा में जबरन धर्मांतरण और इन्क्विज़िशन ने पूरे भारत में गहरी स्थानीय शत्रुता पैदा की", "type": "leaf"}
            ]},
            {"label": "राजनीतिक कारक", "type": "branch", "date": "17वीं सदी", "children": [
                {"label": "होर्मुज (1622), मलक्का (1641), सीलोन (1658), कोचीन (1663) का डच को नुकसान; पुर्तगाली हिंद महासागर साम्राज्य टुकड़े-टुकड़े समाप्त", "type": "leaf"},
                {"label": "1700 तक पुर्तगालियों ने केवल गोवा, दीव, दमन और छोटी एन्क्लेव बनाए रखीं — 150 वर्षों में प्रमुख शक्ति से मामूली व्यापारी बने", "type": "leaf"}
            ]}
        ]
    },
    "first-carnatic-war": {
        "en": [
            {"label": "Background", "type": "branch", "date": "1746-1748", "children": [
                {"label": "Extension of War of Austrian Succession (1740-48) to India; France supported Maria Theresa's enemies; England supported Austria", "type": "leaf"},
                {"label": "French under Labourdonnais (Governor of Mauritius) sailed to India with fleet; captured Madras in September 1746", "type": "leaf"},
                {"label": "Nawab Anwaruddin of Carnatic demanded Madras be returned; French and English both defied Nawab — first time Europeans ignored Mughal authority openly", "type": "leaf"}
            ]},
            {"label": "Battle of Adyar (1746)", "type": "branch", "date": "November 1746", "children": [
                {"label": "Nawab Anwaruddin sent 10,000-strong army against 230 French soldiers; French musket fire routed Nawab's army at Adyar River — proved Indian armies vulnerable", "type": "leaf"},
                {"label": "French held Madras 1746-48; English held Pondicherry under siege unsuccessfully (Sep 1748) under Admiral Boscawen", "type": "leaf"}
            ]},
            {"label": "Treaty of Aix-la-Chapelle (1748)", "type": "branch", "date": "1748", "children": [
                {"label": "European war ended; Madras returned to English in exchange for Louisburg (Canada); status quo restored in India", "type": "leaf"},
                {"label": "War proved: European-trained sepoys could defeat large Indian armies; Dupleix's ambition for French Indian empire emboldened", "type": "leaf"}
            ]}
        ],
        "hi": [
            {"label": "पृष्ठभूमि", "type": "branch", "date": "1746-1748", "children": [
                {"label": "ऑस्ट्रियन उत्तराधिकार युद्ध (1740-48) का भारत में विस्तार; फ्रांस ने मारिया थेरेसा के दुश्मनों का समर्थन किया; इंग्लैंड ने ऑस्ट्रिया का", "type": "leaf"},
                {"label": "लाबूर्दोनैस (मॉरीशस के गवर्नर) के नेतृत्व में फ्रांसीसी बेड़े के साथ भारत आए; सितंबर 1746 में मद्रास पर कब्जा किया", "type": "leaf"},
                {"label": "कर्नाटक के नवाब अनवरुद्दीन ने मद्रास वापस करने की मांग की; फ्रांसीसी और अंग्रेज दोनों ने नवाब की अनदेखी की — पहली बार यूरोपीयों ने मुगल प्राधिकरण को खुले तौर पर नजरअंदाज किया", "type": "leaf"}
            ]},
            {"label": "अडयार की लड़ाई (1746)", "type": "branch", "date": "नवंबर 1746", "children": [
                {"label": "नवाब अनवरुद्दीन ने 230 फ्रांसीसी सैनिकों के खिलाफ 10,000 की सेना भेजी; अडयार नदी पर फ्रांसीसी मस्केट गोलाबारी ने नवाब की सेना भगाई — साबित हुआ भारतीय सेनाएं कमजोर हैं", "type": "leaf"},
                {"label": "फ्रांसीसियों ने 1746-48 तक मद्रास रखा; एडमिरल बोस्कावेन के नेतृत्व में अंग्रेजों ने पांडिचेरी को असफलतापूर्वक घेरा (सितं. 1748)", "type": "leaf"}
            ]},
            {"label": "ऐक्स-ला-शैपेल की संधि (1748)", "type": "branch", "date": "1748", "children": [
                {"label": "यूरोपीय युद्ध समाप्त; लुईसबर्ग (कनाडा) के बदले मद्रास अंग्रेजों को वापस; भारत में यथास्थिति बहाल", "type": "leaf"},
                {"label": "युद्ध ने साबित किया: यूरोपीय प्रशिक्षित सिपाही बड़ी भारतीय सेनाओं को हरा सकते हैं; डुप्ले की फ्रांसीसी भारतीय साम्राज्य की महत्वाकांक्षा को बल मिला", "type": "leaf"}
            ]}
        ]
    },
    "portuguese-albuquerque": {
        "en": [
            {"label": "Conquests", "type": "branch", "date": "1509-1515", "children": [
                {"label": "Alfonso de Albuquerque: Second Portuguese Governor (1509-15); architect of Portuguese empire in Asia — transformed EIC from trading posts to territorial power", "type": "leaf"},
                {"label": "Captured Goa from Bijapur Sultanate (1510): became permanent capital of Portuguese India; gave control over the pepper and spice trade route", "type": "leaf"},
                {"label": "Captured Malacca (1511): controlled the Strait of Malacca; monopolised spice trade from Moluccas (Spice Islands) to Europe", "type": "leaf"}
            ]},
            {"label": "Strategic Vision", "type": "branch", "date": "1509-1515", "children": [
                {"label": "Three-point strategy: control Hormuz (Persian Gulf), Aden (Red Sea), Malacca (East Indies) — choke all trade routes bypassing Portuguese", "type": "leaf"},
                {"label": "Failed to capture Aden (1513): this failure meant Arab merchants continued using Red Sea route; Portuguese monopoly never complete", "type": "leaf"},
                {"label": "Encouraged Portuguese men to marry local Indian women — policy of racial integration to create loyal mixed-race community in Goa", "type": "leaf"}
            ]},
            {"label": "Legacy", "type": "branch", "date": "Post-1515", "children": [
                {"label": "Died at sea near Goa (1515); built Portuguese Estado da India (State of India) that lasted until Indian annexation of Goa in 1961", "type": "leaf"},
                {"label": "Established Portuguese as dominant Indian Ocean power for nearly a century; his policies shaped all subsequent European colonial strategies in Asia", "type": "leaf"}
            ]}
        ],
        "hi": [
            {"label": "विजयें", "type": "branch", "date": "1509-1515", "children": [
                {"label": "एफोंसो डी अल्बुकर्क: दूसरे पुर्तगाली गवर्नर (1509-15); एशिया में पुर्तगाली साम्राज्य के वास्तुकार — व्यापारिक चौकियों से क्षेत्रीय शक्ति में परिवर्तन", "type": "leaf"},
                {"label": "बीजापुर सल्तनत से गोवा पर विजय (1510): पुर्तगाली भारत की स्थायी राजधानी; काली मिर्च और मसाले व्यापार मार्ग पर नियंत्रण", "type": "leaf"},
                {"label": "मलक्का पर विजय (1511): मलक्का जलडमरूमध्य नियंत्रित; मसाला द्वीप समूह से यूरोप तक मसाला व्यापार का एकाधिकार", "type": "leaf"}
            ]},
            {"label": "रणनीतिक दृष्टि", "type": "branch", "date": "1509-1515", "children": [
                {"label": "तीन-बिंदु रणनीति: होर्मुज (फारस की खाड़ी), अदन (लाल सागर), मलक्का (पूर्वी द्वीप) नियंत्रित करना — पुर्तगालियों को बायपास करने वाले सभी व्यापार मार्गों को अवरुद्ध करना", "type": "leaf"},
                {"label": "अदन को जीतने में विफल (1513): इस विफलता से अरब व्यापारी लाल सागर मार्ग का उपयोग जारी रखा; पुर्तगाली एकाधिकार कभी पूर्ण नहीं हुआ", "type": "leaf"},
                {"label": "पुर्तगाली पुरुषों को स्थानीय भारतीय महिलाओं से विवाह के लिए प्रोत्साहित किया — गोवा में वफादार मिश्रित-नस्ल समुदाय बनाने की नीति", "type": "leaf"}
            ]},
            {"label": "विरासत", "type": "branch", "date": "1515 के बाद", "children": [
                {"label": "गोवा के पास समुद्र में मृत्यु (1515); पुर्तगाली एस्टाडो दा इंडिया (भारत राज्य) बनाया जो 1961 में भारत के गोवा विलय तक चला", "type": "leaf"},
                {"label": "लगभग एक शताब्दी तक पुर्तगालियों को प्रमुख हिंद महासागर शक्ति के रूप में स्थापित किया; उनकी नीतियों ने एशिया में सभी बाद की यूरोपीय औपनिवेशिक रणनीतियों को आकार दिया", "type": "leaf"}
            ]}
        ]
    },
    "portuguese-de-almeida": {
        "en": [
            {"label": "Governorship (1505-09)", "type": "branch", "date": "1505-1509", "children": [
                {"label": "Francisco de Almeida: First Viceroy (Governor) of Portuguese India; advocated 'Blue Water Policy' (Cartaz System) — control the sea, not land", "type": "leaf"},
                {"label": "Blue Water Policy: Portuguese naval supremacy at sea would be enough to control trade; no need for large territorial empire inland", "type": "leaf"},
                {"label": "This policy was later reversed by Albuquerque who captured Goa (1510) — shift from sea-based to land-based empire", "type": "leaf"}
            ]},
            {"label": "Battle of Diu (1509)", "type": "branch", "date": "1509", "children": [
                {"label": "Combined Egyptian-Gujarat fleet (backed by Venetians) challenged Portuguese naval monopoly; threatened spice trade control", "type": "leaf"},
                {"label": "De Almeida's fleet decisively defeated the combined fleet at Battle of Diu (February 1509); established Portuguese naval dominance in Indian Ocean", "type": "leaf"},
                {"label": "This victory ensured Portuguese monopoly over spice trade for the next century; all rival powers had to accept Portuguese sea power", "type": "leaf"}
            ]},
            {"label": "Significance", "type": "branch", "date": "Post-1509", "children": [
                {"label": "De Almeida was recalled but killed at Cape of Good Hope (1510) by Khoikhoi people; never returned to Portugal", "type": "leaf"},
                {"label": "Battle of Diu (1509) is as significant as Vasco da Gama's voyage — secured Portuguese command of Indian Ocean trade for a century", "type": "leaf"}
            ]}
        ],
        "hi": [
            {"label": "गवर्नरशिप (1505-09)", "type": "branch", "date": "1505-1509", "children": [
                {"label": "फ्रांसिस्को डी अल्मेइडा: पुर्तगाली भारत के पहले वायसराय (गवर्नर); 'ब्लू वाटर पॉलिसी' (कारताज़ प्रणाली) के समर्थक — भूमि नहीं, समुद्र पर नियंत्रण", "type": "leaf"},
                {"label": "ब्लू वाटर पॉलिसी: समुद्र पर पुर्तगाली नौसैनिक वर्चस्व व्यापार नियंत्रण के लिए पर्याप्त होगा; अंतर्देशीय बड़े क्षेत्रीय साम्राज्य की आवश्यकता नहीं", "type": "leaf"},
                {"label": "यह नीति बाद में अल्बुकर्क ने पलट दी जिसने गोवा (1510) जीता — समुद्र-आधारित से भूमि-आधारित साम्राज्य में बदलाव", "type": "leaf"}
            ]},
            {"label": "दीव की लड़ाई (1509)", "type": "branch", "date": "1509", "children": [
                {"label": "संयुक्त मिस्री-गुजरात बेड़े (वेनेशियनों द्वारा समर्थित) ने पुर्तगाली नौसैनिक एकाधिकार को चुनौती दी; मसाला व्यापार नियंत्रण को खतरा", "type": "leaf"},
                {"label": "डी अल्मेइडा के बेड़े ने दीव की लड़ाई (फरवरी 1509) में संयुक्त बेड़े को निर्णायक रूप से हराया; हिंद महासागर में पुर्तगाली नौसैनिक वर्चस्व स्थापित", "type": "leaf"},
                {"label": "इस जीत ने अगली शताब्दी के लिए मसाला व्यापार पर पुर्तगाली एकाधिकार सुनिश्चित किया; सभी प्रतिद्वंद्वी शक्तियों को पुर्तगाली समुद्री शक्ति स्वीकार करनी पड़ी", "type": "leaf"}
            ]},
            {"label": "महत्व", "type": "branch", "date": "1509 के बाद", "children": [
                {"label": "डी अल्मेइडा को वापस बुलाया गया लेकिन केप ऑफ गुड होप (1510) पर खोइखोई लोगों द्वारा मारा गया; कभी पुर्तगाल नहीं लौटा", "type": "leaf"},
                {"label": "दीव की लड़ाई (1509) वास्को डी गामा की यात्रा जितनी महत्वपूर्ण है — एक शताब्दी के लिए हिंद महासागर व्यापार पर पुर्तगाली नियंत्रण सुनिश्चित किया", "type": "leaf"}
            ]}
        ]
    },
    "portuguese-nino-da-cunha": {
        "en": [
            {"label": "Governorship (1529-38)", "type": "branch", "date": "1529-1538", "children": [
                {"label": "Nuno da Cunha: Portuguese Governor of India 1529-38; consolidated Portuguese power in western India", "type": "leaf"},
                {"label": "Captured Diu (1535) from Gujarat Sultanate with help of Mughal Emperor Humayun's threat to Gujarat — used Mughal-Gujarat rivalry skillfully", "type": "leaf"},
                {"label": "Captured Bassein (1534) from Gujarat Sultanate; Daman leased from Gujarat ruler — expanded Portuguese control over Gujarat coast", "type": "leaf"}
            ]},
            {"label": "Significance", "type": "branch", "date": "1529-1538", "children": [
                {"label": "Diu fort became one of the most important Portuguese strongholds in India — controlled entrance to Gulf of Khambhat and Gujarat spice trade", "type": "leaf"},
                {"label": "His acquisitions (Diu, Bassein, Daman) formed the nucleus of Portuguese India's western coastal empire that survived until 1961", "type": "leaf"}
            ]},
            {"label": "Context: Gujarat-Portuguese Relations", "type": "branch", "date": "16th Century", "children": [
                {"label": "Gujarat was major spice entrepôt; Portuguese had blockaded its ports and taxed its traders; Gujarat allied with Egypt and Ottoman Empire against Portuguese", "type": "leaf"},
                {"label": "Battle of Diu (1538): Ottoman-Gujarat fleet attacked Diu fort; Portuguese garrison held out; Ottoman withdrawal marked end of Muslim challenge to Portuguese Indian Ocean power", "type": "leaf"}
            ]}
        ],
        "hi": [
            {"label": "गवर्नरशिप (1529-38)", "type": "branch", "date": "1529-1538", "children": [
                {"label": "नुनो दा कुन्हा: भारत के पुर्तगाली गवर्नर 1529-38; पश्चिमी भारत में पुर्तगाली शक्ति मजबूत की", "type": "leaf"},
                {"label": "मुगल सम्राट हुमायूं के गुजरात को खतरे की मदद से गुजरात सल्तनत से दीव (1535) पर कब्जा — मुगल-गुजरात प्रतिद्वंद्विता का कुशल उपयोग", "type": "leaf"},
                {"label": "गुजरात सल्तनत से बसीन (1534) पर कब्जा; गुजरात शासक से दमन पट्टे पर — पुर्तगाली गुजरात तट नियंत्रण का विस्तार", "type": "leaf"}
            ]},
            {"label": "महत्व", "type": "branch", "date": "1529-1538", "children": [
                {"label": "दीव किला भारत में सबसे महत्वपूर्ण पुर्तगाली किलों में से एक बना — खंभात की खाड़ी के प्रवेश द्वार और गुजरात मसाला व्यापार को नियंत्रित किया", "type": "leaf"},
                {"label": "उनके अधिग्रहण (दीव, बसीन, दमन) ने 1961 तक जीवित पुर्तगाली भारत के पश्चिमी तटीय साम्राज्य का केंद्र बनाया", "type": "leaf"}
            ]},
            {"label": "संदर्भ: गुजरात-पुर्तगाली संबंध", "type": "branch", "date": "16वीं सदी", "children": [
                {"label": "गुजरात प्रमुख मसाला केंद्र था; पुर्तगालियों ने इसके बंदरगाहों को बंद कर दिया और व्यापारियों पर कर लगाया; गुजरात ने पुर्तगालियों के खिलाफ मिस्र और ओटोमन साम्राज्य से गठबंधन किया", "type": "leaf"},
                {"label": "दीव की लड़ाई (1538): ओटोमन-गुजरात बेड़े ने दीव किले पर हमला किया; पुर्तगाली गैरिसन डटा रहा; ओटोमन वापसी ने पुर्तगाली हिंद महासागर शक्ति को मुस्लिम चुनौती का अंत किया", "type": "leaf"}
            ]}
        ]
    },
    "portuguese-pedro-alvarez-cabral": {
        "en": [
            {"label": "Second Portuguese Voyage to India (1500)", "type": "branch", "date": "1500-1501", "children": [
                {"label": "Pedro Álvares Cabral led 13-ship fleet; 'accidentally' discovered Brazil on the way south (April 1500) — most significant unintended discovery in history", "type": "leaf"},
                {"label": "Arrived Calicut (Kozhikode) May 1500; Zamorin initially friendly; spice cargo loaded; conflict erupted over Arab merchants' influence", "type": "leaf"},
                {"label": "Arab merchants incited Zamorin against Portuguese; Cabral's factory at Calicut attacked; 50 Portuguese killed; Cabral bombarded Calicut in retaliation", "type": "leaf"}
            ]},
            {"label": "Cochin & Results", "type": "branch", "date": "1500-1501", "children": [
                {"label": "Cabral established first permanent Portuguese factory at Cochin (Kochi) — Cochin Raja was rival of Zamorin and welcomed Portuguese alliance", "type": "leaf"},
                {"label": "Returned to Portugal with spice cargo; proved Vasco da Gama's route commercially viable; established Portuguese-Cochin alliance that lasted decades", "type": "leaf"}
            ]},
            {"label": "Significance", "type": "branch", "date": "Post-1501", "children": [
                {"label": "Cabral's voyage established Portugal's dual empire: India (spice trade) and Brazil (sugar trade) — two pillars of Portuguese imperial wealth", "type": "leaf"},
                {"label": "Pattern established: Portuguese would ally with Indian rulers hostile to their rivals; used local rivalries to gain footholds", "type": "leaf"}
            ]}
        ],
        "hi": [
            {"label": "भारत की दूसरी पुर्तगाली यात्रा (1500)", "type": "branch", "date": "1500-1501", "children": [
                {"label": "पेड्रो अल्वारेज़ काब्राल ने 13 जहाजों के बेड़े का नेतृत्व किया; दक्षिण की ओर जाते समय 'अनजाने में' ब्राज़ील की खोज की (अप्रैल 1500) — इतिहास की सबसे महत्वपूर्ण अनपेक्षित खोज", "type": "leaf"},
                {"label": "मई 1500 में कालीकट (कोझिकोड) पहुंचे; ज़मोरिन शुरू में मैत्रीपूर्ण; मसाला माल लोड; अरब व्यापारियों के प्रभाव पर संघर्ष भड़का", "type": "leaf"},
                {"label": "अरब व्यापारियों ने ज़मोरिन को पुर्तगालियों के खिलाफ उकसाया; कालीकट में काब्राल की फैक्ट्री पर हमला; 50 पुर्तगाली मारे; काब्राल ने प्रतिशोध में कालीकट पर गोलाबारी की", "type": "leaf"}
            ]},
            {"label": "कोचीन और परिणाम", "type": "branch", "date": "1500-1501", "children": [
                {"label": "काब्राल ने कोचीन (कोच्चि) में पहली स्थायी पुर्तगाली फैक्ट्री स्थापित की — कोचीन राजा ज़मोरिन का प्रतिद्वंद्वी था और पुर्तगाली गठबंधन का स्वागत किया", "type": "leaf"},
                {"label": "मसाले के माल के साथ पुर्तगाल लौटे; वास्को डी गामा के मार्ग को व्यावसायिक रूप से व्यवहार्य साबित किया; दशकों तक चलने वाला पुर्तगाली-कोचीन गठबंधन स्थापित", "type": "leaf"}
            ]},
            {"label": "महत्व", "type": "branch", "date": "1501 के बाद", "children": [
                {"label": "काब्राल की यात्रा ने पुर्तगाल का दोहरा साम्राज्य स्थापित किया: भारत (मसाला व्यापार) और ब्राज़ील (चीनी व्यापार) — पुर्तगाली शाही संपदा के दो स्तंभ", "type": "leaf"},
                {"label": "पैटर्न स्थापित: पुर्तगाली अपने प्रतिद्वंद्वियों के शत्रु भारतीय शासकों से गठबंधन करेंगे; पैर जमाने के लिए स्थानीय प्रतिद्वंद्विताओं का इस्तेमाल किया", "type": "leaf"}
            ]}
        ]
    },
    "portuguese-vasco-da-gama": {
        "en": [
            {"label": "First Voyage (1497-99)", "type": "branch", "date": "1497-1499", "children": [
                {"label": "Left Lisbon July 1497; rounded Cape of Good Hope (November 1497); crossed Indian Ocean with help of Arab navigator Ahmad ibn Majid", "type": "leaf"},
                {"label": "Arrived Calicut (Kozhikode) May 1498 — first European to reach India by sea; met Zamorin (local ruler); initial trade relations established", "type": "leaf"},
                {"label": "Returned to Lisbon September 1499 with spices; profit of 60x voyage cost; proved sea route to India commercially viable; ended Arab-Venetian spice monopoly", "type": "leaf"}
            ]},
            {"label": "Second Voyage (1502-03)", "type": "branch", "date": "1502-1503", "children": [
                {"label": "Returned with 20 armed ships; bombarded Calicut when Zamorin refused to expel Arab traders; signed treaty with Cochin Raja", "type": "leaf"},
                {"label": "Intercepted Arab ship 'Miri' near Calicut; burned it with 400 Muslim pilgrims on board — established Portuguese brutality as deliberate policy", "type": "leaf"},
                {"label": "Established Mozambique, Mombasa as supply stations; created framework for Portuguese Indian Ocean empire", "type": "leaf"}
            ]},
            {"label": "Third Voyage & Death (1524)", "type": "branch", "date": "1524", "children": [
                {"label": "Appointed Viceroy of India 1524; died at Cochin (Kochi) December 1524; his grave was later moved to Portugal", "type": "leaf"},
                {"label": "His 1498 voyage opened the Age of Exploration; ended the overland Silk Road's dominance; began European seaborne empire era", "type": "leaf"}
            ]}
        ],
        "hi": [
            {"label": "प्रथम यात्रा (1497-99)", "type": "branch", "date": "1497-1499", "children": [
                {"label": "जुलाई 1497 में लिस्बन से रवाना; केप ऑफ गुड होप का चक्कर लगाया (नवंबर 1497); अरब नाविक अहमद इब्न माजिद की मदद से हिंद महासागर पार किया", "type": "leaf"},
                {"label": "मई 1498 में कालीकट (कोझिकोड) पहुंचे — समुद्री मार्ग से भारत पहुंचने वाले पहले यूरोपीय; ज़मोरिन (स्थानीय शासक) से मिले; प्रारंभिक व्यापार संबंध स्थापित", "type": "leaf"},
                {"label": "मसालों के साथ सितंबर 1499 में लिस्बन लौटे; यात्रा लागत का 60 गुना लाभ; भारत का समुद्री मार्ग व्यावसायिक रूप से व्यवहार्य साबित; अरब-वेनेशियन मसाला एकाधिकार समाप्त", "type": "leaf"}
            ]},
            {"label": "द्वितीय यात्रा (1502-03)", "type": "branch", "date": "1502-1503", "children": [
                {"label": "20 सशस्त्र जहाजों के साथ लौटे; जब ज़मोरिन ने अरब व्यापारियों को बाहर निकालने से इनकार किया तो कालीकट पर गोलाबारी; कोचीन राजा के साथ संधि", "type": "leaf"},
                {"label": "कालीकट के पास अरब जहाज 'मिरी' को रोका; 400 मुस्लिम तीर्थयात्रियों सहित जला दिया — पुर्तगाली क्रूरता को जानबूझकर नीति के रूप में स्थापित किया", "type": "leaf"},
                {"label": "मोजाम्बिक, मोम्बासा को आपूर्ति स्टेशन के रूप में स्थापित; पुर्तगाली हिंद महासागर साम्राज्य का ढांचा बनाया", "type": "leaf"}
            ]},
            {"label": "तृतीय यात्रा और मृत्यु (1524)", "type": "branch", "date": "1524", "children": [
                {"label": "1524 में भारत के वायसराय नियुक्त; दिसंबर 1524 में कोचीन (कोच्चि) में मृत्यु; उनकी कब्र बाद में पुर्तगाल स्थानांतरित की गई", "type": "leaf"},
                {"label": "उनकी 1498 यात्रा ने अन्वेषण का युग खोला; ओवरलैंड सिल्क रोड का वर्चस्व समाप्त किया; यूरोपीय समुद्री साम्राज्य युग की शुरुआत", "type": "leaf"}
            ]}
        ]
    },
    "responsible-factors-for-arrival-of-europeans": {
        "en": [
            {"label": "Commercial Motivations", "type": "branch", "date": "15th Century", "children": [
                {"label": "Spice trade demand: pepper, cinnamon, cloves, nutmeg worth more than gold in Europe; middlemen (Arabs, Venetians) added enormous markups", "type": "leaf"},
                {"label": "Fall of Constantinople (1453): Ottoman Turks controlled overland trade routes; Europeans needed alternative sea routes to Asia", "type": "leaf"},
                {"label": "Desire for direct trade access eliminated Arab and Italian middlemen; Portuguese Crown backed explorers to break this monopoly", "type": "leaf"}
            ]},
            {"label": "Technological Factors", "type": "branch", "date": "15th Century", "children": [
                {"label": "Advances in ship design: Caravel (light, maneuverable) and Carrack (large, ocean-going) ships enabled long ocean voyages", "type": "leaf"},
                {"label": "Magnetic compass, astrolabe, cross-staff: navigational instruments enabled precise positioning far from coastlines", "type": "leaf"},
                {"label": "Improved cartography: Ptolemy's Geography rediscovered; portolan charts (detailed coastal maps) available; though Indian Ocean largely unknown", "type": "leaf"}
            ]},
            {"label": "Political & Religious Factors", "type": "branch", "date": "15th Century", "children": [
                {"label": "Reconquista spirit: Portugal and Spain completed reconquest of Iberian Peninsula from Muslims (1492); crusading spirit extended overseas", "type": "leaf"},
                {"label": "Prince Henry the Navigator (1394-1460): Organised Portuguese systematic exploration of African coast; established school of navigation at Sagres", "type": "leaf"},
                {"label": "Papal support: Treaty of Tordesillas (1494) divided the world between Portugal and Spain — legitimised European colonial claims", "type": "leaf"}
            ]}
        ],
        "hi": [
            {"label": "व्यावसायिक प्रेरणाएं", "type": "branch", "date": "15वीं सदी", "children": [
                {"label": "मसाला व्यापार की मांग: यूरोप में काली मिर्च, दालचीनी, लौंग, जायफल सोने से अधिक मूल्यवान; बिचौलियों (अरब, वेनेशियन) ने भारी मार्कअप जोड़े", "type": "leaf"},
                {"label": "कॉन्स्टेंटिनोपल का पतन (1453): ओटोमन तुर्कों ने ओवरलैंड व्यापार मार्गों पर नियंत्रण किया; यूरोपीयों को एशिया के वैकल्पिक समुद्री मार्गों की जरूरत पड़ी", "type": "leaf"},
                {"label": "प्रत्यक्ष व्यापार पहुंच की इच्छा ने अरब और इतालवी बिचौलियों को समाप्त किया; पुर्तगाली क्राउन ने इस एकाधिकार तोड़ने के लिए खोजकर्ताओं का समर्थन किया", "type": "leaf"}
            ]},
            {"label": "तकनीकी कारक", "type": "branch", "date": "15वीं सदी", "children": [
                {"label": "जहाज डिजाइन में प्रगति: कारवेल (हल्का, चलायमान) और कैरेक (बड़ा, महासागर-गामी) जहाजों ने लंबी महासागर यात्राएं संभव कीं", "type": "leaf"},
                {"label": "चुंबकीय कम्पास, एस्ट्रोलेब, क्रॉस-स्टाफ: नेविगेशनल उपकरणों ने तटरेखाओं से दूर सटीक स्थिति-निर्धारण सक्षम किया", "type": "leaf"},
                {"label": "बेहतर कार्टोग्राफी: टॉलेमी का भूगोल पुनः खोजा; पोर्टोलन चार्ट (विस्तृत तटीय नक्शे) उपलब्ध; हालांकि हिंद महासागर काफी हद तक अज्ञात था", "type": "leaf"}
            ]},
            {"label": "राजनीतिक और धार्मिक कारक", "type": "branch", "date": "15वीं सदी", "children": [
                {"label": "रिकॉन्किस्टा भावना: पुर्तगाल और स्पेन ने मुसलमानों से इबेरियन प्रायद्वीप की पुनः विजय पूरी की (1492); धर्मयुद्ध की भावना विदेशों तक विस्तारित", "type": "leaf"},
                {"label": "प्रिंस हेनरी द नेविगेटर (1394-1460): पुर्तगाली व्यवस्थित अफ्रीकी तट अन्वेषण का आयोजन किया; सेगरेस में नेविगेशन स्कूल स्थापित", "type": "leaf"},
                {"label": "पापल समर्थन: टॉर्डेसिलास की संधि (1494) ने पुर्तगाल और स्पेन के बीच दुनिया को विभाजित किया — यूरोपीय औपनिवेशिक दावों को वैध बनाया", "type": "leaf"}
            ]}
        ]
    },
    "rise-of-the-hyderabad-state": {
        "en": [
            {"label": "Foundation", "type": "branch", "date": "1724", "children": [
                {"label": "Nizam ul Mulk Asaf Jah I (Qamaruddin Khan): Mughal viceroy who declared independence from weakening Mughal Empire after 1724", "type": "leaf"},
                {"label": "Battle of Shakhar Kheda (1724): Nizam defeated rival Mubariz Khan; established effective independence of Deccan under Asaf Jah dynasty", "type": "leaf"},
                {"label": "Made Aurangabad his capital initially; later moved capital to Hyderabad (founded by Quli Qutb Shah in 1591)", "type": "leaf"}
            ]},
            {"label": "Relations with EIC", "type": "branch", "date": "18th Century", "children": [
                {"label": "Hyderabad's strategic position between Maratha north and Mysore south made it crucial for EIC's Deccan policy", "type": "leaf"},
                {"label": "First Subsidiary Alliance (1798): Hyderabad was first state to accept Wellesley's system; ceded northern districts to EIC to pay for subsidiary troops", "type": "leaf"},
                {"label": "Nizam supported EIC against Tipu Sultan (4th Mysore War) and Marathas — became reliable ally against both", "type": "leaf"}
            ]},
            {"label": "Dynasty & Legacy", "type": "branch", "date": "1724-1948", "children": [
                {"label": "Seven Nizams of Hyderabad ruled 1724-1948; the largest princely state in area (82,698 sq miles) and wealthiest in British India", "type": "leaf"},
                {"label": "Last Nizam (Mir Osman Ali Khan): richest man in the world in 1940s; acceded to India only after Operation Polo (Police Action) in September 1948", "type": "leaf"}
            ]}
        ],
        "hi": [
            {"label": "स्थापना", "type": "branch", "date": "1724", "children": [
                {"label": "निज़ाम उल मुल्क आसफ जाह I (कमरुद्दीन खान): मुगल वायसराय जिन्होंने 1724 के बाद कमजोर पड़ते मुगल साम्राज्य से स्वतंत्रता घोषित की", "type": "leaf"},
                {"label": "शकर खेड़ा की लड़ाई (1724): निज़ाम ने प्रतिद्वंद्वी मुबारिज खान को हराया; आसफ जाह वंश के तहत दक्कन की प्रभावी स्वतंत्रता स्थापित", "type": "leaf"},
                {"label": "शुरू में औरंगाबाद को राजधानी बनाया; बाद में हैदराबाद (1591 में कुली कुतुब शाह द्वारा स्थापित) को राजधानी बनाया", "type": "leaf"}
            ]},
            {"label": "EIC के साथ संबंध", "type": "branch", "date": "18वीं सदी", "children": [
                {"label": "मराठा उत्तर और मैसूर दक्षिण के बीच हैदराबाद की रणनीतिक स्थिति ने इसे EIC की दक्कन नीति के लिए महत्वपूर्ण बनाया", "type": "leaf"},
                {"label": "प्रथम सहायक संधि (1798): हैदराबाद वेलेजली की प्रणाली स्वीकार करने वाला पहला राज्य; सहायक सैनिकों के भुगतान के लिए उत्तरी जिले EIC को सौंपे", "type": "leaf"},
                {"label": "निजाम ने टीपू सुल्तान (चौथे मैसूर युद्ध) और मराठों के खिलाफ EIC का समर्थन किया — दोनों के खिलाफ विश्वसनीय सहयोगी बने", "type": "leaf"}
            ]},
            {"label": "वंश और विरासत", "type": "branch", "date": "1724-1948", "children": [
                {"label": "हैदराबाद के सात निजामों ने 1724-1948 तक शासन किया; क्षेत्रफल (82,698 वर्ग मील) में सबसे बड़ा और ब्रिटिश भारत में सबसे धनी रियासत", "type": "leaf"},
                {"label": "अंतिम निज़ाम (मीर उस्मान अली खान): 1940 के दशक में दुनिया के सबसे अमीर व्यक्ति; सितंबर 1948 में ऑपरेशन पोलो (पुलिस कार्रवाई) के बाद ही भारत में विलय", "type": "leaf"}
            ]}
        ]
    },
    "the-columbian-exchange": {
        "en": [
            {"label": "From Americas to India/Asia", "type": "branch", "date": "Post-1492", "children": [
                {"label": "Crops introduced to India via Portuguese: maize (corn), potato, sweet potato, tomato, chilli pepper, tobacco, cashew, pineapple, papaya", "type": "leaf"},
                {"label": "Chilli became integral to Indian cuisine within 100 years of Portuguese arrival — transformed South Asian food culture permanently", "type": "leaf"},
                {"label": "Tobacco: introduced by Portuguese in 16th century; spread rapidly across India; Mughal emperors tried (and failed) to ban it", "type": "leaf"}
            ]},
            {"label": "From Asia to Europe", "type": "branch", "date": "Post-1498", "children": [
                {"label": "Indian Ocean spices (pepper, cinnamon, cloves, nutmeg, cardamom) now accessible directly — ended Arab-Venetian monopoly; prices fell in Europe", "type": "leaf"},
                {"label": "Indian cotton textiles (calico, muslin, chintz): flooded European markets; created demand that later drove Industrial Revolution's textile sector", "type": "leaf"},
                {"label": "Indigo from India became primary European blue dye; replaced European woad; 17th-century indigo trade was enormously profitable", "type": "leaf"}
            ]},
            {"label": "Demographic Impact", "type": "branch", "date": "16th-18th Century", "children": [
                {"label": "New World crops (potato, maize) increased caloric production in Europe and Asia — contributed to population growth in 18th century", "type": "leaf"},
                {"label": "European diseases (smallpox, measles) had catastrophic impact on Americas — but India had some immunity through earlier contact with similar pathogens", "type": "leaf"}
            ]}
        ],
        "hi": [
            {"label": "अमेरिका से भारत/एशिया", "type": "branch", "date": "1492 के बाद", "children": [
                {"label": "पुर्तगालियों के माध्यम से भारत में पेश फसलें: मक्का, आलू, शकरकंद, टमाटर, मिर्च, तंबाकू, काजू, अनानास, पपीता", "type": "leaf"},
                {"label": "पुर्तगालियों के आगमन के 100 वर्षों में मिर्च भारतीय व्यंजन का अभिन्न अंग बनी — दक्षिण एशियाई खान-पान संस्कृति को स्थायी रूप से बदला", "type": "leaf"},
                {"label": "तंबाकू: 16वीं सदी में पुर्तगालियों द्वारा पेश; पूरे भारत में तेजी से फैला; मुगल सम्राटों ने इसे प्रतिबंधित करने की (असफल) कोशिश की", "type": "leaf"}
            ]},
            {"label": "एशिया से यूरोप", "type": "branch", "date": "1498 के बाद", "children": [
                {"label": "हिंद महासागर के मसाले (काली मिर्च, दालचीनी, लौंग, जायफल, इलायची) अब सीधे उपलब्ध — अरब-वेनेशियन एकाधिकार समाप्त; यूरोप में कीमतें गिरीं", "type": "leaf"},
                {"label": "भारतीय सूती कपड़े (कैलिको, मलमल, चिंट्ज़): यूरोपीय बाजारों में भर गए; मांग ने बाद में औद्योगिक क्रांति के कपड़ा क्षेत्र को संचालित किया", "type": "leaf"},
                {"label": "भारत से नील यूरोप का प्राथमिक नीला रंजक बना; यूरोपीय वोड को प्रतिस्थापित किया; 17वीं सदी का नील व्यापार अत्यंत लाभदायक था", "type": "leaf"}
            ]},
            {"label": "जनसांख्यिकीय प्रभाव", "type": "branch", "date": "16वीं-18वीं सदी", "children": [
                {"label": "नई दुनिया की फसलें (आलू, मक्का) ने यूरोप और एशिया में कैलोरी उत्पादन बढ़ाया — 18वीं सदी में जनसंख्या वृद्धि में योगदान", "type": "leaf"},
                {"label": "यूरोपीय बीमारियों (चेचक, खसरा) का अमेरिका में विनाशकारी प्रभाव — लेकिन समान रोगाणुओं के पहले संपर्क से भारत को कुछ प्रतिरक्षा थी", "type": "leaf"}
            ]}
        ]
    },
    "the-danes-in-india": {
        "en": [
            {"label": "Danish East India Company", "type": "branch", "date": "1616-1845", "children": [
                {"label": "Danish East India Company (Dansk Ostindisk Kompagni) founded 1616; arrived India 1620; established settlement at Tranquebar (Tarangambadi) on Coromandel Coast", "type": "leaf"},
                {"label": "Also established Serampore (Frederiksnagore) in Bengal (1755) — became famous as centre of Christian missionary activity", "type": "leaf"},
                {"label": "Danes were minor traders in India; never had military power or territorial ambitions; primarily interested in pepper and textile trade", "type": "leaf"}
            ]},
            {"label": "Serampore Mission", "type": "branch", "date": "1800-1845", "children": [
                {"label": "William Carey, Joshua Marshman, William Ward — Baptist missionaries at Serampore; printed Bible in Bengali, Sanskrit, and 40+ languages", "type": "leaf"},
                {"label": "Serampore College (1818): First degree-granting institution in Asia; still functioning today as Serampore College (University)", "type": "leaf"},
                {"label": "Danish territory allowed missionaries to operate when EIC banned missionary activity in British India before 1813", "type": "leaf"}
            ]},
            {"label": "Decline", "type": "branch", "date": "1845", "children": [
                {"label": "Sold Serampore to EIC in 1845; sold Tranquebar to EIC in 1845 — effectively ended Danish presence in India after 225 years", "type": "leaf"}
            ]}
        ],
        "hi": [
            {"label": "डैनिश ईस्ट इंडिया कंपनी", "type": "branch", "date": "1616-1845", "children": [
                {"label": "डैनिश ईस्ट इंडिया कंपनी (Dansk Ostindisk Kompagni) की स्थापना 1616; 1620 में भारत आई; कोरोमंडल तट पर ट्रांकेबार (तरंगाम्बाडी) में बस्ती स्थापित", "type": "leaf"},
                {"label": "बंगाल में श्रीरामपुर (फ्रेडरिकनागोर) की भी स्थापना (1755) — ईसाई मिशनरी गतिविधि के केंद्र के रूप में प्रसिद्ध हुआ", "type": "leaf"},
                {"label": "डेन भारत में मामूली व्यापारी थे; कभी सैन्य शक्ति या क्षेत्रीय महत्वाकांक्षाएं नहीं; मुख्यतः काली मिर्च और कपड़ा व्यापार में रुचि", "type": "leaf"}
            ]},
            {"label": "श्रीरामपुर मिशन", "type": "branch", "date": "1800-1845", "children": [
                {"label": "विलियम केरी, जोशुआ मार्शमैन, विलियम वार्ड — श्रीरामपुर में बैपटिस्ट मिशनरी; बाइबिल बंगाली, संस्कृत और 40+ भाषाओं में मुद्रित", "type": "leaf"},
                {"label": "श्रीरामपुर कॉलेज (1818): एशिया में पहली डिग्री देने वाली संस्था; आज भी श्रीरामपुर कॉलेज (विश्वविद्यालय) के रूप में कार्यरत", "type": "leaf"},
                {"label": "डैनिश क्षेत्र ने मिशनरियों को तब काम करने दिया जब EIC ने 1813 से पहले ब्रिटिश भारत में मिशनरी गतिविधि पर प्रतिबंध लगाया था", "type": "leaf"}
            ]},
            {"label": "पतन", "type": "branch", "date": "1845", "children": [
                {"label": "1845 में EIC को श्रीरामपुर बेचा; 1845 में EIC को ट्रांकेबार बेचा — 225 वर्षों के बाद भारत में डैनिश उपस्थिति प्रभावी रूप से समाप्त", "type": "leaf"}
            ]}
        ]
    },
    "the-danes-in-india-settlements-personalities-decline": {
        "en": [
            {"label": "Key Settlements", "type": "branch", "date": "1620-1845", "children": [
                {"label": "Tranquebar (1620): First Danish settlement on Coromandel Coast; Fort Dansborg built; primary trading base for pepper and textiles", "type": "leaf"},
                {"label": "Serampore/Frederiksnagore (1755): Bengal settlement on Hooghly River; became famous for Serampore Mission (1800) and Serampore College (1818)", "type": "leaf"},
                {"label": "Minor posts: Balasore (Odisha) and Calicut — never developed into major settlements due to lack of military and financial backing", "type": "leaf"}
            ]},
            {"label": "Key Personalities", "type": "branch", "date": "Danish India", "children": [
                {"label": "William Carey (1761-1834): Baptist missionary at Serampore; 'Father of Modern Missions'; translated Bible into Bengali; founded Serampore College", "type": "leaf"},
                {"label": "Ove Gjedde: Led first Danish expedition to India (1620); negotiated treaty with King of Tanjore for Tranquebar settlement", "type": "leaf"}
            ]},
            {"label": "Decline Factors", "type": "branch", "date": "17th-19th Century", "children": [
                {"label": "Denmark's small size and limited naval power; never able to compete militarily with Dutch, English, or French in Indian Ocean", "type": "leaf"},
                {"label": "Napoleonic Wars: Denmark allied with Napoleon; British captured Danish ships and territories 1807; weakened Danish trading position further", "type": "leaf"},
                {"label": "Both settlements sold to EIC in 1845 for £125,000; peaceful exit from India — no wars, no major conflicts with EIC", "type": "leaf"}
            ]}
        ],
        "hi": [
            {"label": "प्रमुख बस्तियाँ", "type": "branch", "date": "1620-1845", "children": [
                {"label": "ट्रांकेबार (1620): कोरोमंडल तट पर पहली डैनिश बस्ती; फोर्ट डांसबोर्ग बनाया; काली मिर्च और कपड़ों के लिए प्राथमिक व्यापारिक आधार", "type": "leaf"},
                {"label": "श्रीरामपुर/फ्रेडरिकनागोर (1755): हुगली नदी पर बंगाल बस्ती; श्रीरामपुर मिशन (1800) और श्रीरामपुर कॉलेज (1818) के लिए प्रसिद्ध हुआ", "type": "leaf"},
                {"label": "मामूली चौकियाँ: बालासोर (ओडिशा) और कालीकट — सैन्य और वित्तीय समर्थन की कमी के कारण कभी प्रमुख बस्तियों में नहीं बढ़ीं", "type": "leaf"}
            ]},
            {"label": "प्रमुख व्यक्तित्व", "type": "branch", "date": "डैनिश भारत", "children": [
                {"label": "विलियम केरी (1761-1834): श्रीरामपुर में बैपटिस्ट मिशनरी; 'आधुनिक मिशनों के पिता'; बाइबिल का बंगाली में अनुवाद; श्रीरामपुर कॉलेज की स्थापना", "type": "leaf"},
                {"label": "ओवे ग्जेडे: भारत के लिए पहले डैनिश अभियान का नेतृत्व (1620); ट्रांकेबार बस्ती के लिए तंजौर के राजा के साथ संधि पर वार्ता", "type": "leaf"}
            ]},
            {"label": "पतन के कारक", "type": "branch", "date": "17वीं-19वीं सदी", "children": [
                {"label": "डेनमार्क का छोटा आकार और सीमित नौसैनिक शक्ति; हिंद महासागर में डच, अंग्रेज या फ्रांसीसी से सैन्य रूप से कभी प्रतिस्पर्धा नहीं कर सका", "type": "leaf"},
                {"label": "नेपोलियन युद्ध: डेनमार्क ने नेपोलियन से गठबंधन किया; ब्रिटिश ने 1807 में डैनिश जहाज और क्षेत्र जब्त किए; डैनिश व्यापारिक स्थिति और कमजोर हुई", "type": "leaf"},
                {"label": "दोनों बस्तियां 1845 में £1,25,000 में EIC को बेची गईं; भारत से शांतिपूर्ण निकास — EIC के साथ कोई युद्ध नहीं, कोई बड़ा संघर्ष नहीं", "type": "leaf"}
            ]}
        ]
    },
    "the-dutch-in-india": {
        "en": [
            {"label": "Dutch East India Company (VOC)", "type": "branch", "date": "1602-1795", "children": [
                {"label": "VOC (Vereenigde Oostindische Compagnie) established 1602; world's first multinational corporation with shareholders; issued bonds — pioneered modern capitalism", "type": "leaf"},
                {"label": "Dutch focused on spice trade from Moluccas (Indonesia) not India; India was secondary market for textiles needed to buy spices", "type": "leaf"},
                {"label": "Drove Portuguese out of many positions: Malacca (1641), Cochin (1663), Ceylon/Sri Lanka (1658); dominant Indian Ocean power 1620-1740", "type": "leaf"}
            ]},
            {"label": "Indian Settlements", "type": "branch", "date": "1605-1795", "children": [
                {"label": "Masulipatnam (1605): First Dutch factory in India; Pulicat (1610): capital of Dutch India; Nagapatnam (1659): replaced Pulicat as main base", "type": "leaf"},
                {"label": "Bengal: Chinsura (Chinsurah) 1653; Surat, Ahmedabad, Agra — extensive commercial network across India", "type": "leaf"},
                {"label": "Battle of Bedara/Chinsura (1759): EIC defeated Dutch at Chinsura; ended Dutch military power in Bengal; Dutch reduced to trading posts only", "type": "leaf"}
            ]},
            {"label": "Decline", "type": "branch", "date": "18th Century", "children": [
                {"label": "Fourth Anglo-Dutch War (1780-84) destroyed Dutch naval power; VOC went bankrupt 1799; Dutch India passed to Batavian Republic then to France", "type": "leaf"},
                {"label": "Sold Chinsura to EIC (1824); Nagapatnam to EIC (1781); effectively exited India by early 19th century", "type": "leaf"}
            ]}
        ],
        "hi": [
            {"label": "डच ईस्ट इंडिया कंपनी (VOC)", "type": "branch", "date": "1602-1795", "children": [
                {"label": "VOC (Vereenigde Oostindische Compagnie) की स्थापना 1602; शेयरधारकों के साथ दुनिया की पहली बहुराष्ट्रीय कंपनी; बॉन्ड जारी किए — आधुनिक पूंजीवाद का अग्रदूत", "type": "leaf"},
                {"label": "डच ने भारत नहीं बल्कि मोलुकास (इंडोनेशिया) से मसाला व्यापार पर ध्यान केंद्रित किया; मसाले खरीदने के लिए जरूरी कपड़ों के लिए भारत माध्यमिक बाजार था", "type": "leaf"},
                {"label": "कई स्थानों से पुर्तगालियों को निकाला: मलक्का (1641), कोचीन (1663), सीलोन/श्रीलंका (1658); 1620-1740 प्रमुख हिंद महासागर शक्ति", "type": "leaf"}
            ]},
            {"label": "भारतीय बस्तियाँ", "type": "branch", "date": "1605-1795", "children": [
                {"label": "मसूलीपट्टनम (1605): भारत में पहली डच फैक्ट्री; पुलिकट (1610): डच भारत की राजधानी; नागपट्टनम (1659): मुख्य आधार के रूप में पुलिकट की जगह ली", "type": "leaf"},
                {"label": "बंगाल: चिनसुरा (चिनसूरा) 1653; सूरत, अहमदाबाद, आगरा — पूरे भारत में व्यापक वाणिज्यिक नेटवर्क", "type": "leaf"},
                {"label": "बेडारा/चिनसुरा की लड़ाई (1759): EIC ने चिनसुरा में डच को हराया; बंगाल में डच सैन्य शक्ति का अंत; डच केवल व्यापारिक चौकियों तक सीमित", "type": "leaf"}
            ]},
            {"label": "पतन", "type": "branch", "date": "18वीं सदी", "children": [
                {"label": "चतुर्थ आंग्ल-डच युद्ध (1780-84) ने डच नौसैनिक शक्ति नष्ट की; VOC 1799 में दिवालिया; डच भारत बटावियन गणराज्य फिर फ्रांस को गया", "type": "leaf"},
                {"label": "EIC को चिनसुरा बेचा (1824); EIC को नागपट्टनम बेचा (1781); 19वीं सदी की शुरुआत तक प्रभावी रूप से भारत से बाहर", "type": "leaf"}
            ]}
        ]
    },
    "the-dutch-in-india-settlements-personalities-decline": {
        "en": [
            {"label": "Major Settlements", "type": "branch", "date": "1605-1824", "children": [
                {"label": "Pulicat (1610): First major Dutch factory; Fort Geldria built; centre of VOC operations in South India; exported cloth, pepper, indigo", "type": "leaf"},
                {"label": "Masulipatnam (1605), Nagapatnam (1659), Chinsura (1653), Surat, Cochin (1663-1795), Quilon, Cannanore — extensive but ultimately unsustainable network", "type": "leaf"},
                {"label": "Ceylon (Sri Lanka): Most profitable Dutch possession; cinnamon monopoly; Dutch Reformed Church established; sold to British 1796", "type": "leaf"}
            ]},
            {"label": "Key Personalities", "type": "branch", "date": "VOC Era", "children": [
                {"label": "Jan Pieterszoon Coen: VOC Governor-General who established Batavia (Jakarta) as Dutch headquarters in Asia (1619); brutal but effective administrator", "type": "leaf"},
                {"label": "Rijklof van Goens: Dutch Admiral who captured Portuguese Cochin (1663) and dominated Indian Ocean trade in 1660s", "type": "leaf"}
            ]},
            {"label": "Decline Factors", "type": "branch", "date": "18th Century", "children": [
                {"label": "Primary cause: VOC's focus on Southeast Asia (Indonesia) left India secondary; resources spread too thin across vast Asian empire", "type": "leaf"},
                {"label": "Battle of Bedara (1759): EIC's decisive defeat of Dutch fleet — ended any Dutch military threat to English position in Bengal", "type": "leaf"},
                {"label": "VOC bankruptcy (1799); all assets nationalised by Dutch state; sold remaining Indian possessions to EIC by 1824", "type": "leaf"}
            ]}
        ],
        "hi": [
            {"label": "प्रमुख बस्तियाँ", "type": "branch", "date": "1605-1824", "children": [
                {"label": "पुलिकट (1610): पहली प्रमुख डच फैक्ट्री; फोर्ट गेल्ड्रिया बनाया; दक्षिण भारत में VOC संचालन का केंद्र; कपड़ा, काली मिर्च, नील निर्यात", "type": "leaf"},
                {"label": "मसूलीपट्टनम (1605), नागपट्टनम (1659), चिनसुरा (1653), सूरत, कोचीन (1663-1795), क्विलोन, कन्नानोर — व्यापक लेकिन अंततः अटिकाऊ नेटवर्क", "type": "leaf"},
                {"label": "सीलोन (श्रीलंका): सबसे लाभदायक डच संपत्ति; दालचीनी एकाधिकार; डच रिफॉर्म्ड चर्च स्थापित; 1796 में ब्रिटिश को बेचा", "type": "leaf"}
            ]},
            {"label": "प्रमुख व्यक्तित्व", "type": "branch", "date": "VOC काल", "children": [
                {"label": "जान पीटर्सजून कोएन: VOC गवर्नर-जनरल जिसने एशिया में डच मुख्यालय के रूप में बटाविया (जकार्ता) की स्थापना की (1619); क्रूर लेकिन प्रभावी प्रशासक", "type": "leaf"},
                {"label": "रिजक्लोफ वान गोएन्स: डच एडमिरल जिसने पुर्तगाली कोचीन (1663) जीता और 1660 के दशक में हिंद महासागर व्यापार पर वर्चस्व किया", "type": "leaf"}
            ]},
            {"label": "पतन के कारक", "type": "branch", "date": "18वीं सदी", "children": [
                {"label": "प्राथमिक कारण: VOC का दक्षिण पूर्व एशिया (इंडोनेशिया) पर ध्यान केंद्रित होने से भारत माध्यमिक रहा; विशाल एशियाई साम्राज्य में संसाधन बहुत पतले फैले", "type": "leaf"},
                {"label": "बेडारा की लड़ाई (1759): EIC की डच बेड़े पर निर्णायक जीत — बंगाल में अंग्रेजी स्थिति को किसी भी डच सैन्य खतरे का अंत", "type": "leaf"},
                {"label": "VOC दिवालिया (1799); सभी संपत्तियां डच राज्य द्वारा राष्ट्रीयकृत; 1824 तक शेष भारतीय संपत्तियां EIC को बेचीं", "type": "leaf"}
            ]}
        ]
    },
    "the-english-causes-of-english-success": {
        "en": [
            {"label": "Institutional Advantages", "type": "branch", "date": "17th-18th Century", "children": [
                {"label": "EIC had private merchant backing and Parliamentary support; flexible commercial structure vs Portuguese Crown monopoly", "type": "leaf"},
                {"label": "Consistent policy continuity: EIC Directors in London maintained long-term strategy; Governors-General implemented it militarily", "type": "leaf"},
                {"label": "Bengal revenues: After Plassey (1757), Bengal's revenues financed all subsequent British wars across India — self-financing empire", "type": "leaf"}
            ]},
            {"label": "Military & Diplomatic Factors", "type": "branch", "date": "18th Century", "children": [
                {"label": "Sepoy system: EIC trained Indian soldiers (sepoys) in European discipline; created cost-effective, large armies without European manpower", "type": "leaf"},
                {"label": "Naval superiority: Royal Navy protected EIC shipping; no Indian state had comparable blue-water naval capability", "type": "leaf"},
                {"label": "Subsidiary Alliance diplomacy: Wellesley's system made Indian rulers pay for their own subjugation through subsidiary forces", "type": "leaf"}
            ]},
            {"label": "Indian Internal Factors", "type": "branch", "date": "18th Century", "children": [
                {"label": "Mughal decline post-Aurangzeb (1707): No central power to coordinate Indian resistance; regional powers fought each other", "type": "leaf"},
                {"label": "Maratha disunity: Five sardars unable to form unified command; Peshwa's Treaty of Bassein (1802) split confederacy", "type": "leaf"},
                {"label": "Local collaborators: Mir Jafar (Bengal), Raja of Benaras, many zamindars chose to collaborate with EIC for personal gain", "type": "leaf"}
            ]}
        ],
        "hi": [
            {"label": "संस्थागत लाभ", "type": "branch", "date": "17वीं-18वीं सदी", "children": [
                {"label": "EIC को निजी व्यापारी समर्थन और संसदीय समर्थन था; पुर्तगाली क्राउन एकाधिकार की तुलना में लचीला वाणिज्यिक ढांचा", "type": "leaf"},
                {"label": "सुसंगत नीति निरंतरता: लंदन में EIC डायरेक्टरों ने दीर्घकालिक रणनीति बनाए रखी; गवर्नर-जनरलों ने इसे सैन्य रूप से लागू किया", "type": "leaf"},
                {"label": "बंगाल राजस्व: प्लासी (1757) के बाद, बंगाल के राजस्व ने पूरे भारत में बाद के सभी ब्रिटिश युद्धों को वित्तपोषित किया — स्व-वित्तपोषित साम्राज्य", "type": "leaf"}
            ]},
            {"label": "सैन्य और कूटनीतिक कारक", "type": "branch", "date": "18वीं सदी", "children": [
                {"label": "सिपाही प्रणाली: EIC ने भारतीय सैनिकों (सिपाहियों) को यूरोपीय अनुशासन में प्रशिक्षित किया; यूरोपीय जनशक्ति के बिना किफायती, बड़ी सेनाएं बनाईं", "type": "leaf"},
                {"label": "नौसैनिक श्रेष्ठता: रॉयल नेवी ने EIC शिपिंग की रक्षा की; किसी भी भारतीय राज्य के पास तुलनीय समुद्री नौसैनिक क्षमता नहीं थी", "type": "leaf"},
                {"label": "सहायक संधि कूटनीति: वेलेजली की प्रणाली ने भारतीय शासकों को सहायक बलों के माध्यम से अपनी ही अधीनता का भुगतान करवाया", "type": "leaf"}
            ]},
            {"label": "भारतीय आंतरिक कारक", "type": "branch", "date": "18वीं सदी", "children": [
                {"label": "औरंगज़ेब (1707) के बाद मुगल पतन: भारतीय प्रतिरोध को समन्वित करने वाली कोई केंद्रीय शक्ति नहीं; क्षेत्रीय शक्तियां आपस में लड़ीं", "type": "leaf"},
                {"label": "मराठा विभाजन: पाँच सरदार एकीकृत कमान नहीं बना सके; पेशवा की बसई संधि (1802) ने परिसंघ को विभाजित किया", "type": "leaf"},
                {"label": "स्थानीय सहयोगी: मीर जाफर (बंगाल), बनारस के राजा, कई जमींदारों ने व्यक्तिगत लाभ के लिए EIC के साथ सहयोग चुना", "type": "leaf"}
            ]}
        ]
    },
    "the-english-farrukhsiyar-s-farman": {
        "en": [
            {"label": "Background", "type": "branch", "date": "1717", "children": [
                {"label": "EIC sought renewal of its trading privileges from Mughal Emperor Farrukhsiyar; sent diplomatic mission with physician William Hamilton who cured the emperor's illness", "type": "leaf"},
                {"label": "William Hamilton cured Farrukhsiyar of a painful abscess — in gratitude, emperor granted sweeping trade concessions to EIC", "type": "leaf"}
            ]},
            {"label": "Key Provisions of Farman (1717)", "type": "branch", "date": "1717", "children": [
                {"label": "Bengal: EIC granted duty-free trade throughout Bengal in exchange for annual payment of Rs 3,000; right to issue dastaks (passes) for goods", "type": "leaf"},
                {"label": "Bombay: EIC's coins to be accepted as legal tender throughout Mughal Empire; Bombay rent fixed at Rs 10,000 annually", "type": "leaf"},
                {"label": "Madras: EIC granted right to purchase 38 additional villages around Madras; rent exemptions for EIC lands near Madras", "type": "leaf"}
            ]},
            {"label": "Significance", "type": "branch", "date": "Post-1717", "children": [
                {"label": "Called the 'Magna Carta of EIC in India' — gave EIC unprecedented trade privileges across the empire; exploited by private British traders using dastaks", "type": "leaf"},
                {"label": "Abuse of dastaks (duty-free passes) by private EIC servants for their own trade was a major grievance leading to conflicts with Bengal Nawabs including Siraj ud Daula", "type": "leaf"}
            ]}
        ],
        "hi": [
            {"label": "पृष्ठभूमि", "type": "branch", "date": "1717", "children": [
                {"label": "EIC ने मुगल सम्राट फर्रुखसियर से अपने व्यापारिक विशेषाधिकारों के नवीनीकरण की मांग की; चिकित्सक विलियम हैमिल्टन के साथ राजनयिक मिशन भेजा जिसने सम्राट की बीमारी ठीक की", "type": "leaf"},
                {"label": "विलियम हैमिल्टन ने फर्रुखसियर के दर्दनाक फोड़े को ठीक किया — कृतज्ञता में, सम्राट ने EIC को व्यापक व्यापार रियायतें दीं", "type": "leaf"}
            ]},
            {"label": "फरमान के प्रमुख प्रावधान (1717)", "type": "branch", "date": "1717", "children": [
                {"label": "बंगाल: EIC को 3,000 रु. वार्षिक भुगतान के बदले पूरे बंगाल में शुल्क-मुक्त व्यापार; माल के लिए दस्तकें (पास) जारी करने का अधिकार", "type": "leaf"},
                {"label": "बॉम्बे: EIC के सिक्के पूरे मुगल साम्राज्य में कानूनी निविदा के रूप में स्वीकार किए जाएं; बॉम्बे का किराया 10,000 रु. वार्षिक निर्धारित", "type": "leaf"},
                {"label": "मद्रास: EIC को मद्रास के पास 38 अतिरिक्त गाँव खरीदने का अधिकार; मद्रास के पास EIC भूमि के लिए किराया छूट", "type": "leaf"}
            ]},
            {"label": "महत्व", "type": "branch", "date": "1717 के बाद", "children": [
                {"label": "'भारत में EIC का मैग्ना कार्टा' कहलाया — EIC को साम्राज्य भर में अभूतपूर्व व्यापार विशेषाधिकार दिए; निजी ब्रिटिश व्यापारियों द्वारा दस्तकों का शोषण", "type": "leaf"},
                {"label": "निजी EIC सेवकों द्वारा अपने व्यापार के लिए दस्तकों (शुल्क-मुक्त पास) का दुरुपयोग सिराज उद दौला सहित बंगाल नवाबों के साथ संघर्ष का प्रमुख कारण था", "type": "leaf"}
            ]}
        ]
    },
    "the-french": {
        "en": [
            {"label": "French East India Company", "type": "branch", "date": "1664-1769", "children": [
                {"label": "Compagnie des Indes Orientales founded by Colbert (1664) under Louis XIV; state-backed unlike EIC which was private", "type": "leaf"},
                {"label": "First settlement at Surat (1668); Pondicherry founded 1674 — became capital of French India; Chandernagore (Bengal) 1692", "type": "leaf"},
                {"label": "Dupleix (Governor 1742-54): transformed French India from trading posts to political force; pioneered sepoy warfare and Indian state-building", "type": "leaf"}
            ]},
            {"label": "Rise & Fall of French Power", "type": "branch", "date": "1742-1761", "children": [
                {"label": "Dupleix installed French-backed rulers in Hyderabad and Carnatic; demonstrated Europeans could control Indian politics through proxies", "type": "leaf"},
                {"label": "Robert Clive's capture of Arcot (1751): shifted tide against French; Dupleix's recalled to France in disgrace (1754)", "type": "leaf"},
                {"label": "Battle of Wandiwash (1760): Eyre Coote defeated Lally; French military power in India destroyed; Pondicherry captured 1761", "type": "leaf"}
            ]},
            {"label": "Legacy", "type": "branch", "date": "Post-1763", "children": [
                {"label": "Treaty of Paris (1763): France kept 5 stations (Pondicherry, Chandernagore, Mahe, Karikal, Yanam) but no military or political power", "type": "leaf"},
                {"label": "French retained Pondicherry until it merged with India in 1954; Chandernagore merged in 1950 — last European territories to join India", "type": "leaf"}
            ]}
        ],
        "hi": [
            {"label": "फ्रांसीसी ईस्ट इंडिया कंपनी", "type": "branch", "date": "1664-1769", "children": [
                {"label": "कोलबर्ट द्वारा लुई XIV के अधीन Compagnie des Indes Orientales की स्थापना (1664); EIC के विपरीत राज्य-समर्थित", "type": "leaf"},
                {"label": "सूरत में पहली बस्ती (1668); पांडिचेरी की स्थापना 1674 — फ्रांसीसी भारत की राजधानी; चंद्रनगर (बंगाल) 1692", "type": "leaf"},
                {"label": "डुप्ले (गवर्नर 1742-54): फ्रांसीसी भारत को व्यापारिक चौकियों से राजनीतिक शक्ति में परिवर्तित किया; सिपाही युद्ध और भारतीय राज्य-निर्माण का अग्रदूत", "type": "leaf"}
            ]},
            {"label": "फ्रांसीसी शक्ति का उत्थान और पतन", "type": "branch", "date": "1742-1761", "children": [
                {"label": "डुप्ले ने हैदराबाद और कर्नाटक में फ्रांसीसी-समर्थित शासक स्थापित किए; प्रदर्शित किया कि यूरोपीय प्रतिनिधियों के माध्यम से भारतीय राजनीति नियंत्रित कर सकते हैं", "type": "leaf"},
                {"label": "रॉबर्ट क्लाइव का अर्काट पर कब्जा (1751): फ्रांसीसी के खिलाफ ज्वार बदला; डुप्ले को 1754 में अपमान के साथ फ्रांस वापस बुलाया", "type": "leaf"},
                {"label": "वांडीवाश की लड़ाई (1760): आयर कूट ने लाली को हराया; भारत में फ्रांसीसी सैन्य शक्ति नष्ट; 1761 में पांडिचेरी पर कब्जा", "type": "leaf"}
            ]},
            {"label": "विरासत", "type": "branch", "date": "1763 के बाद", "children": [
                {"label": "पेरिस की संधि (1763): फ्रांस ने 5 स्टेशन (पांडिचेरी, चंद्रनगर, माहे, करिकल, यनम) रखे लेकिन कोई सैन्य या राजनीतिक शक्ति नहीं", "type": "leaf"},
                {"label": "फ्रांस ने पांडिचेरी 1954 में भारत में विलय तक बनाए रखा; चंद्रनगर 1950 में विलय — भारत में शामिल होने वाले अंतिम यूरोपीय क्षेत्र", "type": "leaf"}
            ]}
        ]
    },
    "the-french-settlements-personalities-decline": {
        "en": [
            {"label": "Key Settlements", "type": "branch", "date": "1668-1763", "children": [
                {"label": "Pondicherry (1674): Capital of French India; fortified; seat of Governor-General; population 100,000+ at peak under Dupleix", "type": "leaf"},
                {"label": "Chandernagore/Chandannagar (1692): Bengal settlement on Hooghly; second most important French base; captured by Clive in 1757", "type": "leaf"},
                {"label": "Mahe (Malabar coast), Karikal (Coromandel), Yanam (Andhra) — minor stations that survived Treaty of Paris and remained French until 1954", "type": "leaf"}
            ]},
            {"label": "Key Personalities", "type": "branch", "date": "French India Era", "children": [
                {"label": "Dupleix (1697-1763): Greatest French imperialist; invented the strategy of using Indian proxies; recalled in disgrace 1754; died in poverty in France", "type": "leaf"},
                {"label": "Lally (Thomas Arthur de Lally, 1758-61): Last major French commander in India; captured Fort St David but lost Wandiwash; executed in France for cowardice", "type": "leaf"},
                {"label": "Bussy: Dupleix's general who controlled Hyderabad for French for years — demonstrated how European officers could dominate Indian courts", "type": "leaf"}
            ]},
            {"label": "Decline Factors", "type": "branch", "date": "Mid-18th Century", "children": [
                {"label": "French government failed to provide consistent support; Compagnie des Indes repeatedly went bankrupt; private investment discouraged", "type": "leaf"},
                {"label": "France prioritised European wars over Indian empire; India was always secondary to French continental interests", "type": "leaf"},
                {"label": "Seven Years War (1756-63) brought English naval supremacy; French reinforcements unable to reach India — decisive strategic disadvantage", "type": "leaf"}
            ]}
        ],
        "hi": [
            {"label": "प्रमुख बस्तियाँ", "type": "branch", "date": "1668-1763", "children": [
                {"label": "पांडिचेरी (1674): फ्रांसीसी भारत की राजधानी; किलेबंद; गवर्नर-जनरल की सीट; डुप्ले के अधीन चरम पर 1 लाख+ जनसंख्या", "type": "leaf"},
                {"label": "चंद्रनगर/चंद्ननगर (1692): हुगली पर बंगाल बस्ती; दूसरा सबसे महत्वपूर्ण फ्रांसीसी आधार; 1757 में क्लाइव ने जीता", "type": "leaf"},
                {"label": "माहे (मलाबार तट), करिकल (कोरोमंडल), यनम (आंध्र) — मामूली स्टेशन जो पेरिस की संधि से बचे और 1954 तक फ्रांसीसी रहे", "type": "leaf"}
            ]},
            {"label": "प्रमुख व्यक्तित्व", "type": "branch", "date": "फ्रांसीसी भारत काल", "children": [
                {"label": "डुप्ले (1697-1763): सबसे महान फ्रांसीसी साम्राज्यवादी; भारतीय प्रतिनिधियों का उपयोग करने की रणनीति ईजाद की; 1754 में अपमान के साथ वापस बुलाया; फ्रांस में गरीबी में मृत्यु", "type": "leaf"},
                {"label": "लाली (थॉमस आर्थर डी लाली, 1758-61): भारत में अंतिम प्रमुख फ्रांसीसी कमांडर; फोर्ट सेंट डेविड जीता लेकिन वांडीवाश हारा; कायरता के लिए फ्रांस में फांसी", "type": "leaf"},
                {"label": "बुसी: डुप्ले का जनरल जिसने वर्षों तक फ्रांसीसियों के लिए हैदराबाद नियंत्रित किया — प्रदर्शित किया कि यूरोपीय अधिकारी भारतीय दरबारों पर कैसे हावी हो सकते हैं", "type": "leaf"}
            ]},
            {"label": "पतन के कारक", "type": "branch", "date": "18वीं सदी के मध्य", "children": [
                {"label": "फ्रांसीसी सरकार लगातार समर्थन देने में विफल; Compagnie des Indes बार-बार दिवालिया हुई; निजी निवेश हतोत्साहित", "type": "leaf"},
                {"label": "फ्रांस ने भारतीय साम्राज्य की बजाय यूरोपीय युद्धों को प्राथमिकता दी; भारत हमेशा फ्रांसीसी महाद्वीपीय हितों के लिए माध्यमिक था", "type": "leaf"},
                {"label": "सप्तवर्षीय युद्ध (1756-63) ने अंग्रेजी नौसैनिक वर्चस्व लाया; फ्रांसीसी सुदृढीकरण भारत नहीं पहुंच सका — निर्णायक रणनीतिक नुकसान", "type": "leaf"}
            ]}
        ]
    },
    "the-portuguese-in-india": {
        "en": [
            {"label": "Establishment of Empire (1498-1530)", "type": "branch", "date": "1498-1530", "children": [
                {"label": "Vasco da Gama (1498): First European to reach India by sea; established Calicut and Cochin as trading bases", "type": "leaf"},
                {"label": "Albuquerque (1510): Captured Goa; established Estado da India (State of India) as administrative framework for Portuguese Indian empire", "type": "leaf"},
                {"label": "Cartaz system: All Indian Ocean traders required to buy Portuguese naval passes; revolutionised Indian Ocean trade control", "type": "leaf"}
            ]},
            {"label": "Peak Period (1530-1600)", "type": "branch", "date": "1530-1600", "children": [
                {"label": "Goa (1510), Diu (1535), Daman (1559), Bassein (1534), Cochin, Calicut, Quilon: network of forts and factories controlling western India trade", "type": "leaf"},
                {"label": "Portuguese controlled spice trade from Moluccas to Europe for nearly a century — enormous profits flowed to Lisbon", "type": "leaf"},
                {"label": "Goa Inquisition (1561-1812): Most notorious aspect; forced conversions; burned heretics; created lasting hostility among Hindus and Muslims", "type": "leaf"}
            ]},
            {"label": "Decline & Legacy", "type": "branch", "date": "17th Century onwards", "children": [
                {"label": "Dutch and English displaced Portuguese from Malacca, Cochin, Ceylon by mid-17th century; retained only Goa, Diu, Daman", "type": "leaf"},
                {"label": "Goa remained Portuguese until Indian military annexation (Operation Vijay) in December 1961 — 451 years of Portuguese presence", "type": "leaf"},
                {"label": "Legacy: Konkani language influence; Catholic churches; Indo-Portuguese architecture; genetic admixture in coastal populations", "type": "leaf"}
            ]}
        ],
        "hi": [
            {"label": "साम्राज्य की स्थापना (1498-1530)", "type": "branch", "date": "1498-1530", "children": [
                {"label": "वास्को डी गामा (1498): समुद्री मार्ग से भारत पहुंचने वाले पहले यूरोपीय; कालीकट और कोचीन को व्यापारिक आधार के रूप में स्थापित किया", "type": "leaf"},
                {"label": "अल्बुकर्क (1510): गोवा पर विजय; पुर्तगाली भारतीय साम्राज्य के प्रशासनिक ढांचे के रूप में एस्टाडो दा इंडिया (भारत राज्य) स्थापित", "type": "leaf"},
                {"label": "कारताज़ प्रणाली: सभी हिंद महासागर व्यापारियों को पुर्तगाली नौसैनिक पास खरीदने की आवश्यकता; हिंद महासागर व्यापार नियंत्रण में क्रांति", "type": "leaf"}
            ]},
            {"label": "चरम काल (1530-1600)", "type": "branch", "date": "1530-1600", "children": [
                {"label": "गोवा (1510), दीव (1535), दमन (1559), बसीन (1534), कोचीन, कालीकट, क्विलोन: पश्चिमी भारत व्यापार नियंत्रण करने वाले किलों और कारखानों का नेटवर्क", "type": "leaf"},
                {"label": "पुर्तगालियों ने लगभग एक शताब्दी तक मोलुकास से यूरोप तक मसाला व्यापार नियंत्रित किया — लिस्बन में भारी लाभ", "type": "leaf"},
                {"label": "गोवा इन्क्विज़िशन (1561-1812): सबसे कुख्यात पहलू; जबरन धर्मांतरण; विधर्मियों को जलाया; हिंदुओं और मुसलमानों में स्थायी शत्रुता पैदा की", "type": "leaf"}
            ]},
            {"label": "पतन और विरासत", "type": "branch", "date": "17वीं सदी से", "children": [
                {"label": "17वीं सदी के मध्य तक डच और अंग्रेजों ने पुर्तगालियों को मलक्का, कोचीन, सीलोन से विस्थापित किया; केवल गोवा, दीव, दमन बचे", "type": "leaf"},
                {"label": "गोवा दिसंबर 1961 में भारतीय सैन्य विलय (ऑपरेशन विजय) तक पुर्तगाली रहा — 451 वर्षों की पुर्तगाली उपस्थिति", "type": "leaf"},
                {"label": "विरासत: कोंकणी भाषा का प्रभाव; कैथोलिक चर्च; इंडो-पुर्तगाली वास्तुकला; तटीय आबादी में आनुवंशिक मिश्रण", "type": "leaf"}
            ]}
        ]
    },
    "the-second-carnatic-war": {
        "en": [
            {"label": "Background & Succession Dispute", "type": "branch", "date": "1749-1754", "children": [
                {"label": "Two succession disputes: Hyderabad (Nizam) and Carnatic (Nawab) — French backed one claimant each; English backed rivals", "type": "leaf"},
                {"label": "Hyderabad: French supported Muzaffar Jung; English supported Nasir Jung — Muzaffar Jung won with French help", "type": "leaf"},
                {"label": "Carnatic: French supported Chanda Sahib; English supported Muhammad Ali — Dupleix made Chanda Sahib Nawab of Carnatic", "type": "leaf"}
            ]},
            {"label": "Siege of Arcot (1751)", "type": "branch", "date": "1751", "children": [
                {"label": "Robert Clive (24 years old) captured Arcot, capital of Carnatic, with 200 men (Sept 1751) — bold stroke diverted Chanda Sahib's forces", "type": "leaf"},
                {"label": "Clive held Arcot for 53 days against 10,000 Chanda Sahib forces; brilliant defence made Clive's reputation", "type": "leaf"},
                {"label": "Muhammad Ali (English-backed) defeated Chanda Sahib; French influence in Carnatic collapsed; Dupleix's strategy failed", "type": "leaf"}
            ]},
            {"label": "Dupleix's Recall (1754)", "type": "branch", "date": "1754", "children": [
                {"label": "French East India Company, fearing war costs, recalled Dupleix in 1754; signed Convention of Pondicherry — both sides agreed to non-interference in Indian politics", "type": "leaf"},
                {"label": "Dupleix's recall was a fatal strategic blunder — abandoned French empire-building in India when close to success; cleared way for English dominance", "type": "leaf"}
            ]}
        ],
        "hi": [
            {"label": "पृष्ठभूमि और उत्तराधिकार विवाद", "type": "branch", "date": "1749-1754", "children": [
                {"label": "दो उत्तराधिकार विवाद: हैदराबाद (निजाम) और कर्नाटक (नवाब) — फ्रांसीसियों ने प्रत्येक में एक दावेदार का समर्थन किया; अंग्रेजों ने प्रतिद्वंद्वियों का", "type": "leaf"},
                {"label": "हैदराबाद: फ्रांसीसियों ने मुजफ्फर जंग का समर्थन किया; अंग्रेजों ने नासिर जंग का — मुजफ्फर जंग फ्रांसीसी मदद से जीते", "type": "leaf"},
                {"label": "कर्नाटक: फ्रांसीसियों ने चंदा साहब का समर्थन किया; अंग्रेजों ने मुहम्मद अली का — डुप्ले ने चंदा साहब को कर्नाटक का नवाब बनाया", "type": "leaf"}
            ]},
            {"label": "अर्काट का घेरा (1751)", "type": "branch", "date": "1751", "children": [
                {"label": "रॉबर्ट क्लाइव (24 वर्ष) ने 200 सैनिकों के साथ कर्नाटक की राजधानी अर्काट जीती (सितं. 1751) — साहसी कदम ने चंदा साहब की सेनाओं का ध्यान भटकाया", "type": "leaf"},
                {"label": "क्लाइव ने 10,000 चंदा साहब सेनाओं के खिलाफ 53 दिन अर्काट पर कब्जा बनाए रखा; शानदार रक्षा ने क्लाइव की प्रतिष्ठा बनाई", "type": "leaf"},
                {"label": "मुहम्मद अली (अंग्रेजी-समर्थित) ने चंदा साहब को हराया; कर्नाटक में फ्रांसीसी प्रभाव ध्वस्त; डुप्ले की रणनीति विफल", "type": "leaf"}
            ]},
            {"label": "डुप्ले की वापसी (1754)", "type": "branch", "date": "1754", "children": [
                {"label": "युद्ध की लागत से डरकर फ्रांसीसी ईस्ट इंडिया कंपनी ने 1754 में डुप्ले को वापस बुलाया; पांडिचेरी की संधि — दोनों पक्षों ने भारतीय राजनीति में गैर-हस्तक्षेप पर सहमति जताई", "type": "leaf"},
                {"label": "डुप्ले की वापसी घातक रणनीतिक भूल थी — सफलता के करीब होने पर भारत में फ्रांसीसी साम्राज्य-निर्माण छोड़ा; अंग्रेजी वर्चस्व का रास्ता साफ", "type": "leaf"}
            ]}
        ]
    },
    "the-third-carnatic-war": {
        "en": [
            {"label": "Seven Years War Context (1756-63)", "type": "branch", "date": "1756-1763", "children": [
                {"label": "Third Carnatic War was the Indian theatre of the Seven Years War (1756-63); France and England fighting globally — America, Europe, India simultaneously", "type": "leaf"},
                {"label": "French sent Count de Lally with reinforcements (1758); captured Fort St David from English; besieged Madras unsuccessfully", "type": "leaf"},
                {"label": "English forces under Eyre Coote reinforced; French ally Bussy recalled from Hyderabad — weakened French inland position critically", "type": "leaf"}
            ]},
            {"label": "Battle of Wandiwash (1760)", "type": "branch", "date": "22 January 1760", "children": [
                {"label": "Decisive engagement at Wandiwash (Jan 22, 1760): Eyre Coote's EIC forces defeated Lally's French army decisively", "type": "leaf"},
                {"label": "French commander Bussy captured; Lally retreated to Pondicherry; EIC besieged Pondicherry which fell January 1761", "type": "leaf"},
                {"label": "French power in India effectively destroyed; all French factories and forts fell to EIC by 1761", "type": "leaf"}
            ]},
            {"label": "Treaty of Paris (1763) & Aftermath", "type": "branch", "date": "1763", "children": [
                {"label": "France received back Pondicherry, Chandernagore, Karikal, Mahe, Yanam — but as unfortified trading posts with no military establishment", "type": "leaf"},
                {"label": "Lally executed in France (1766) for treachery and incompetence — scapegoated for French failure; Voltaire defended him", "type": "leaf"},
                {"label": "English unchallenged supremacy in India established; road to British Indian Empire fully open; Carnatic Wars were the pivotal contest", "type": "leaf"}
            ]}
        ],
        "hi": [
            {"label": "सप्तवर्षीय युद्ध संदर्भ (1756-63)", "type": "branch", "date": "1756-1763", "children": [
                {"label": "तृतीय कर्नाटक युद्ध सप्तवर्षीय युद्ध (1756-63) का भारतीय रंगमंच था; फ्रांस और इंग्लैंड एक साथ वैश्विक स्तर पर लड़ रहे थे — अमेरिका, यूरोप, भारत में", "type": "leaf"},
                {"label": "फ्रांसीसियों ने काउंट डी लाली को सुदृढीकरण के साथ भेजा (1758); अंग्रेजों से फोर्ट सेंट डेविड जीता; मद्रास को असफलतापूर्वक घेरा", "type": "leaf"},
                {"label": "आयर कूट के नेतृत्व में अंग्रेजी सेना को सुदृढीकरण; फ्रांसीसी सहयोगी बुसी को हैदराबाद से वापस बुलाया — फ्रांसीसी अंतर्देशीय स्थिति गंभीर रूप से कमजोर", "type": "leaf"}
            ]},
            {"label": "वांडीवाश की लड़ाई (1760)", "type": "branch", "date": "22 जनवरी 1760", "children": [
                {"label": "वांडीवाश में निर्णायक मुठभेड़ (22 जन. 1760): आयर कूट की EIC सेनाओं ने लाली की फ्रांसीसी सेना को निर्णायक रूप से हराया", "type": "leaf"},
                {"label": "फ्रांसीसी कमांडर बुसी को पकड़ा गया; लाली पांडिचेरी भागा; EIC ने पांडिचेरी को घेरा जो जनवरी 1761 में गिरा", "type": "leaf"},
                {"label": "भारत में फ्रांसीसी शक्ति प्रभावी रूप से नष्ट; 1761 तक सभी फ्रांसीसी कारखाने और किले EIC को मिले", "type": "leaf"}
            ]},
            {"label": "पेरिस की संधि (1763) और बाद में", "type": "branch", "date": "1763", "children": [
                {"label": "फ्रांस को पांडिचेरी, चंद्रनगर, करिकल, माहे, यनम वापस मिले — लेकिन बिना किलेबंदी और सैन्य प्रतिष्ठान के व्यापारिक चौकियों के रूप में", "type": "leaf"},
                {"label": "लाली को फ्रांस में (1766) विश्वासघात और अक्षमता के लिए फांसी — फ्रांसीसी विफलता के लिए बलि का बकरा; वोल्टेयर ने उसका बचाव किया", "type": "leaf"},
                {"label": "भारत में अंग्रेजी का निर्विवाद वर्चस्व स्थापित; ब्रिटिश भारतीय साम्राज्य का रास्ता पूरी तरह खुला; कर्नाटक युद्ध निर्णायक प्रतिस्पर्धा थी", "type": "leaf"}
            ]}
        ]
    }
}

MINDMAP_MAPPINGS = {
    "anglo-french-rivalry": "anglo-french-rivalry",
    "causes-of-failure-of-portuguese-empire-in-india": "causes-of-failure-of-portuguese-empire-in-india",
    "first-carnatic-war": "first-carnatic-war",
    "portuguese-albuquerque": "portuguese-albuquerque",
    "portuguese-de-almeida": "portuguese-de-almeida",
    "portuguese-nino-da-cunha": "portuguese-nino-da-cunha",
    "portuguese-pedro-alvarez-cabral": "portuguese-pedro-alvarez-cabral",
    "portuguese-vasco-da-gama": "portuguese-vasco-da-gama",
    "responsible-factors-for-arrival-of-europeans": "responsible-factors-for-arrival-of-europeans",
    "rise-of-the-hyderabad-state": "rise-of-the-hyderabad-state",
    "the-columbian-exchange": "the-columbian-exchange",
    "the-danes-in-india": "the-danes-in-india",
    "the-danes-in-india-settlements-personalities-decline": "the-danes-in-india-settlements-personalities-decline",
    "the-dutch-in-india": "the-dutch-in-india",
    "the-dutch-in-india-settlements-personalities-decline": "the-dutch-in-india-settlements-personalities-decline",
    "the-english-causes-of-english-success": "the-english-causes-of-english-success",
    "the-english-farrukhsiyar-s-farman": "the-english-farrukhsiyar-s-farman",
    "the-french": "the-french",
    "the-french-settlements-personalities-decline": "the-french-settlements-personalities-decline",
    "the-portuguese-in-india": "the-portuguese-in-india",
    "the-second-carnatic-war": "the-second-carnatic-war",
    "the-third-carnatic-war": "the-third-carnatic-war"
}

def get_clean_title(folder_name):
    title = folder_name.replace('-', ' ').replace("'", "'")
    skip = {'of', 'and', 'the', 'for', 'in', 'with', 'to', 'on', 'by', 'or', 'a', 'an', 'at', 'its', 'from', 'da', 's'}
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
    canonical_key = MINDMAP_MAPPINGS.get(key, "responsible-factors-for-arrival-of-europeans")

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
