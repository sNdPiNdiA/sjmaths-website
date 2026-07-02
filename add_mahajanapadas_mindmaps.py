#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script to add detailed unique mindmaps for Age-of-Mahajanapadas topics in both English and Hindi.
It creates the hi/index.html stub if it doesn't exist, then injects the mindmap.
"""

import os, re, json, shutil

BASE = r"upsc/ancient_history/Age-of-Mahajanapadas"

# ─── DATA: ENGLISH AND HINDI BRANCHES ───────────────────────────────────────

MINDMAP_DATA = {

"administrative-setup": {
    "en": [
        {"label": "Monarchies (Rajyas)", "type": "branch", "date": "Monarchy", "children": [
            {"label": "King (Rajan): Absolute power, maintained regular army (Senani)", "type": "leaf"},
            {"label": "Officials: Amatyas (Ministers), Mahamatras (High officials), Ayuktas", "type": "leaf"},
            {"label": "Taxation: Bhaga (1/6th of produce) collected by Bhāgadugha/Balisadhakas", "type": "leaf"}]},
        {"label": "Republics (Ganas/Sanghas)", "type": "branch", "date": "Republics", "children": [
            {"label": "Oligarchy: Ruled by an assembly of Kshatriya elders (Rajas)", "type": "leaf"},
            {"label": "Assembly Hall (Santhagara): Place for democratic discussions and voting (Salaka)", "type": "leaf"}]}
    ],
    "hi": [
        {"label": "राजतंत्र (Monarchy)", "type": "branch", "date": "राजतंत्र", "children": [
            {"label": "राजा: पूर्ण शक्ति, नियमित सेना (सेनानी) रखता था", "type": "leaf"},
            {"label": "अधिकारी: अमात्य (मंत्री), महामात्र (उच्च अधिकारी), आयुक्त", "type": "leaf"},
            {"label": "कराधान: भागदुघ/बलिसाधक द्वारा भाग (उपज का 1/6) वसूला जाता था", "type": "leaf"}]},
        {"label": "गणतंत्र (गण/संघ)", "type": "branch", "date": "गणतंत्र", "children": [
            {"label": "कुलीनतंत्र: क्षत्रिय कुलीनों (राजाओं) की सभा द्वारा शासन", "type": "leaf"},
            {"label": "संथागार (सभागार): लोकतांत्रिक चर्चा और मतदान (शलाका) का स्थान", "type": "leaf"}]}
    ]
},

"alexanders-invasion": {
    "en": [
        {"label": "The Invasion (326 BCE)", "type": "branch", "date": "Invasion", "children": [
            {"label": "Ambhi of Taxila: Submitted without a fight and allied with Alexander", "type": "leaf"},
            {"label": "Battle of Hydaspes (Jhelum): Fought against Porus; Alexander won but restored Porus' kingdom", "type": "leaf"}]},
        {"label": "Retreat and Impact", "type": "branch", "date": "Impact", "children": [
            {"label": "Mutiny at Beas (Hyphasis): Greek soldiers refused to march further east (feared Nanda army)", "type": "leaf"},
            {"label": "Political Impact: Destroyed small republics in NW, paving the way for Mauryan expansion", "type": "leaf"},
            {"label": "Cultural Impact: Opened new trade routes; Hellenistic art influence (Gandhara art later)", "type": "leaf"}]}
    ],
    "hi": [
        {"label": "आक्रमण (326 ई.पू.)", "type": "branch", "date": "आक्रमण", "children": [
            {"label": "तक्षशिला का आम्भी: बिना लड़े आत्मसमर्पण किया और सिकंदर का सहयोगी बना", "type": "leaf"},
            {"label": "हाइडस्पेस (झेलम) का युद्ध: पोरस के विरुद्ध; सिकंदर जीता लेकिन पोरस का राज्य लौटा दिया", "type": "leaf"}]},
        {"label": "वापसी और प्रभाव", "type": "branch", "date": "प्रभाव", "children": [
            {"label": "व्यास नदी (हाइफैसिस) पर विद्रोह: यूनानी सैनिकों ने आगे बढ़ने से मना किया (नंद सेना का डर)", "type": "leaf"},
            {"label": "राजनीतिक प्रभाव: उत्तर-पश्चिम के छोटे गणराज्यों को नष्ट किया; मौर्य विस्तार का मार्ग प्रशस्त", "type": "leaf"},
            {"label": "सांस्कृतिक प्रभाव: नए व्यापार मार्ग खुले; हेलेनिस्टिक कला का प्रभाव (बाद में गांधार कला)", "type": "leaf"}]}
    ]
},

"economy-during-mahajanapadas-period": {
    "en": [
        {"label": "Agriculture (Second Urbanization)", "type": "branch", "date": "Agriculture", "children": [
            {"label": "Iron Plowshare: Extensive forest clearing in Gangetic valley; surplus production", "type": "leaf"},
            {"label": "Paddy Transplantation: Increased rice yields", "type": "leaf"}]},
        {"label": "Trade and Urbanization", "type": "branch", "date": "Trade", "children": [
            {"label": "Guilds (Shrenis): Merchants and artisans organized into powerful guilds headed by a Jesthaka/Sreshthi", "type": "leaf"},
            {"label": "Currency: Punch-marked coins (Karshapanas) of silver and copper became common", "type": "leaf"},
            {"label": "Trade Routes: Uttarapatha (North-West to Bengal) and Dakshinapatha (North to South)", "type": "leaf"}]}
    ],
    "hi": [
        {"label": "कृषि (द्वितीय नगरीकरण)", "type": "branch", "date": "कृषि", "children": [
            {"label": "लोहे का फाल: गंगा घाटी में जंगलों की कटाई; अधिशेष उत्पादन", "type": "leaf"},
            {"label": "धान की रोपाई: चावल की पैदावार में वृद्धि", "type": "leaf"}]},
        {"label": "व्यापार और नगरीकरण", "type": "branch", "date": "व्यापार", "children": [
            {"label": "श्रेणी (Guilds): व्यापारियों और कारीगरों के संघ (प्रमुख: श्रेष्ठिन/जेठक)", "type": "leaf"},
            {"label": "मुद्रा: चाँदी और ताँबे के आहत सिक्के (कार्षापण) का व्यापक प्रयोग", "type": "leaf"},
            {"label": "व्यापारिक मार्ग: उत्तरापथ (उत्तर-पश्चिम से बंगाल) और दक्षिणापथ (उत्तर से दक्षिण)", "type": "leaf"}]}
    ]
},

"haryanka-dynasty": {
    "en": [
        {"label": "Bimbisara (c. 544–492 BCE)", "type": "branch", "date": "Bimbisara", "children": [
            {"label": "Founder of Magadhan imperial power; Title: Shrenika", "type": "leaf"},
            {"label": "Matrimonial Alliances: Married Kosala Devi (dowry: Kashi), Chellana (Lichchhavi), Khema (Madra)", "type": "leaf"},
            {"label": "Conquests: Annexed Anga (ruled by Brahmadatta); contemporary of Buddha and Mahavira", "type": "leaf"}]},
        {"label": "Ajatashatru (c. 492–460 BCE)", "type": "branch", "date": "Ajatashatru", "children": [
            {"label": "Killed his father; Title: Kunika", "type": "leaf"},
            {"label": "Wars: Defeated Kosala and the Vajjian confederacy (used new weapons: Mahashilakantaka and Rathamusala)", "type": "leaf"},
            {"label": "1st Buddhist Council: Patronized it at Rajagriha after Buddha's death", "type": "leaf"}]},
        {"label": "Udayin", "type": "branch", "date": "Udayin", "children": [
            {"label": "Shifted capital from Rajagriha to Pataliputra (confluence of Ganga and Son)", "type": "leaf"}]}
    ],
    "hi": [
        {"label": "बिम्बिसार (लगभग 544–492 ई.पू.)", "type": "branch", "date": "बिम्बिसार", "children": [
            {"label": "मगध साम्राज्य का वास्तविक संस्थापक; उपाधि: श्रेणिक", "type": "leaf"},
            {"label": "वैवाहिक संबंध: कोसल देवी (दहेज: काशी), चेलना (लिच्छवि), खेमा (मद्र) से विवाह", "type": "leaf"},
            {"label": "विजय: अंग को जीता; बुद्ध और महावीर के समकालीन", "type": "leaf"}]},
        {"label": "अजातशत्रु (लगभग 492–460 ई.पू.)", "type": "branch", "date": "अजातशत्रु", "children": [
            {"label": "पिता की हत्या की; उपाधि: कुणिक", "type": "leaf"},
            {"label": "युद्ध: कोसल और वज्जि संघ को हराया (नए हथियार: महाशिलाकंटक और रथमूसल)", "type": "leaf"},
            {"label": "प्रथम बौद्ध संगीति: राजगृह में संरक्षण दिया", "type": "leaf"}]},
        {"label": "उदयिन", "type": "branch", "date": "उदयिन", "children": [
            {"label": "राजधानी को राजगृह से पाटलिपुत्र (गंगा और सोन के संगम) स्थानांतरित किया", "type": "leaf"}]}
    ]
},

"important-dynasties": {
    "en": [
        {"label": "Haryanka Dynasty (c. 544–412 BCE)", "type": "branch", "date": "Haryanka", "children": [
            {"label": "Bimbisara, Ajatashatru, Udayin (Shifted capital to Pataliputra)", "type": "leaf"}]},
        {"label": "Shishunaga Dynasty (c. 412–344 BCE)", "type": "branch", "date": "Shishunaga", "children": [
            {"label": "Shishunaga (destroyed Avanti), Kalashoka (2nd Buddhist Council)", "type": "leaf"}]},
        {"label": "Nanda Dynasty (c. 344–322 BCE)", "type": "branch", "date": "Nanda", "children": [
            {"label": "Mahapadma Nanda ('Ugrasena', 'Ekarat'), Dhana Nanda (Contemporary of Alexander)", "type": "leaf"}]}
    ],
    "hi": [
        {"label": "हर्यक वंश (लगभग 544–412 ई.पू.)", "type": "branch", "date": "हर्यक", "children": [
            {"label": "बिम्बिसार, अजातशत्रु, उदयिन (राजधानी पाटलिपुत्र ले गया)", "type": "leaf"}]},
        {"label": "शिशुनाग वंश (लगभग 412–344 ई.पू.)", "type": "branch", "date": "शिशुनाग", "children": [
            {"label": "शिशुनाग (अवंति को नष्ट किया), कालाशोक (द्वितीय बौद्ध संगीति)", "type": "leaf"}]},
        {"label": "नंद वंश (लगभग 344–322 ई.पू.)", "type": "branch", "date": "नंद", "children": [
            {"label": "महापद्म नंद ('उग्रसेन', 'एकराट्'), धनानंद (सिकंदर का समकालीन)", "type": "leaf"}]}
    ]
},

"nanda-dynasty": {
    "en": [
        {"label": "Mahapadma Nanda", "type": "branch", "date": "Mahapadma", "children": [
            {"label": "First non-Kshatriya (Shudra) dynasty; Title: 'Ekarat', 'Sarvakshatrantaka' (Uprooter of Kshatriyas)", "type": "leaf"},
            {"label": "Conquests: Conquered Kalinga (brought Jina image as trophy, mentioned in Hathigumpha inscription)", "type": "leaf"}]},
        {"label": "Dhana Nanda", "type": "branch", "date": "Dhana Nanda", "children": [
            {"label": "Last ruler; deeply unpopular due to oppressive taxation", "type": "leaf"},
            {"label": "Alexander's Invasion: Greek army refused to face his huge army of 200,000 infantry and 3,000 elephants", "type": "leaf"},
            {"label": "Overthrow: Defeated by Chandragupta Maurya and Chanakya", "type": "leaf"}]}
    ],
    "hi": [
        {"label": "महापद्म नंद", "type": "branch", "date": "महापद्म", "children": [
            {"label": "पहला गैर-क्षत्रिय (शूद्र) वंश; उपाधि: 'एकराट्', 'सर्वक्षत्रांतक' (क्षत्रियों का नाश करने वाला)", "type": "leaf"},
            {"label": "विजय: कलिंग को जीता (जैन मूर्ति मगध लाया, जिसका उल्लेख हाथीगुम्फा अभिलेख में है)", "type": "leaf"}]},
        {"label": "धनानंद", "type": "branch", "date": "धनानंद", "children": [
            {"label": "अंतिम शासक; दमनकारी कराधान के कारण अत्यधिक अलोकप्रिय", "type": "leaf"},
            {"label": "सिकंदर का आक्रमण: यूनानी सेना ने इसकी विशाल सेना (2 लाख पैदल, 3000 हाथी) का सामना करने से मना किया", "type": "leaf"},
            {"label": "पतन: चंद्रगुप्त मौर्य और चाणक्य द्वारा पराजित", "type": "leaf"}]}
    ]
},

"persian-invasions": {
    "en": [
        {"label": "Achaemenid Empire", "type": "branch", "date": "Persia", "children": [
            {"label": "Cyrus the Great (558–530 BCE): First foreign conqueror to penetrate NW India (destroyed Kapisha)", "type": "leaf"},
            {"label": "Darius I (516 BCE): Annexed Punjab, west of Indus, and Sindh; made it the 20th Satrapy of Persia (most fertile/populated)", "type": "leaf"}]},
        {"label": "Impact", "type": "branch", "date": "Impact", "children": [
            {"label": "Script: Introduced Kharoshthi script (written right to left) in NW India", "type": "leaf"},
            {"label": "Architecture: Persian influence on Ashokan pillars (bell-shaped capitals, smooth polish)", "type": "leaf"},
            {"label": "Trade: Boosted Indo-Iranian trade networks", "type": "leaf"}]}
    ],
    "hi": [
        {"label": "हखामनी (Achaemenid) साम्राज्य", "type": "branch", "date": "फारस", "children": [
            {"label": "साइरस महान (558–530 ई.पू.): उत्तर-पश्चिम भारत में प्रवेश करने वाला पहला विदेशी (कपिशा को नष्ट किया)", "type": "leaf"},
            {"label": "डेरियस प्रथम (516 ई.पू.): पंजाब और सिंध को जीता; इसे फारस का 20वाँ प्रांत (क्षत्रपी) बनाया (सबसे उपजाऊ)", "type": "leaf"}]},
        {"label": "प्रभाव", "type": "branch", "date": "प्रभाव", "children": [
            {"label": "लिपि: उत्तर-पश्चिम भारत में खरोष्ठी लिपि (दाएँ से बाएँ) की शुरुआत", "type": "leaf"},
            {"label": "वास्तुकला: अशोक के स्तंभों पर फारसी प्रभाव (घंटी के आकार का शीर्ष, पॉलिश)", "type": "leaf"},
            {"label": "व्यापार: भारत-ईरानी व्यापार संबंधों को बढ़ावा मिला", "type": "leaf"}]}
    ]
},

"polity-republics-and-monarchies": {
    "en": [
        {"label": "Monarchies (Rajyas)", "type": "branch", "date": "Monarchies", "children": [
            {"label": "Power concentrated in King; supported by orthodox Brahmanism", "type": "leaf"},
            {"label": "Key States: Magadha, Kosala, Vatsa, Avanti", "type": "leaf"}]},
        {"label": "Republics (Ganas/Sanghas)", "type": "branch", "date": "Republics", "children": [
            {"label": "Ruled by tribal councils (Rajas); rejected Vedic orthodoxy and caste system", "type": "leaf"},
            {"label": "Key States: Vajji (Lichchhavis), Malla, Shakyas (Buddha's clan), Jnatrikas (Mahavira's clan)", "type": "leaf"},
            {"label": "Vajji Confederacy: Capital at Vaishali; 8 clans joined together (Lichchhavis were the most powerful)", "type": "leaf"}]}
    ],
    "hi": [
        {"label": "राजतंत्र (राज्या)", "type": "branch", "date": "राजतंत्र", "children": [
            {"label": "सत्ता राजा में केंद्रित; रूढ़िवादी ब्राह्मणवाद द्वारा समर्थित", "type": "leaf"},
            {"label": "प्रमुख राज्य: मगध, कोसल, वत्स, अवंति", "type": "leaf"}]},
        {"label": "गणतंत्र (गण/संघ)", "type": "branch", "date": "गणतंत्र", "children": [
            {"label": "जनजातीय परिषदों (राजाओं) द्वारा शासित; वैदिक कर्मकांड और जाति व्यवस्था को अस्वीकार किया", "type": "leaf"},
            {"label": "प्रमुख राज्य: वज्जि (लिच्छवि), मल्ल, शाक्य (बुद्ध का कुल), ज्ञातृक (महावीर का कुल)", "type": "leaf"},
            {"label": "वज्जि संघ: राजधानी वैशाली; 8 कुलों का संघ (लिच्छवि सबसे शक्तिशाली थे)", "type": "leaf"}]}
    ]
},

"rise-of-magadha": {
    "en": [
        {"label": "Geographical & Economic Causes", "type": "branch", "date": "Geography", "children": [
            {"label": "Iron Ore Deposits: Easy access to rich iron ores (Rajgir) for superior weapons and clearing forests", "type": "leaf"},
            {"label": "Strategic Capitals: Rajagriha (surrounded by 5 hills - Jaladurga), Pataliputra (at confluence of rivers - water fort)", "type": "leaf"},
            {"label": "Fertile Land: Gangetic plains produced agricultural surplus; control over trade routes", "type": "leaf"}]},
        {"label": "Military & Political Causes", "type": "branch", "date": "Military", "children": [
            {"label": "Use of Elephants: First to use elephants on a large scale in warfare", "type": "leaf"},
            {"label": "Ambitious Rulers: Bimbisara, Ajatashatru, Mahapadma Nanda pursued aggressive expansion", "type": "leaf"},
            {"label": "Unorthodox Society: Less brahmanical dominance allowed innovative and practical statecraft", "type": "leaf"}]}
    ],
    "hi": [
        {"label": "भौगोलिक और आर्थिक कारण", "type": "branch", "date": "भूगोल", "children": [
            {"label": "लौह अयस्क: बेहतर हथियारों और जंगलों की कटाई के लिए लौह खदानों (राजगीर) तक आसान पहुँच", "type": "leaf"},
            {"label": "रणनीतिक राजधानियाँ: राजगृह (5 पहाड़ियों से घिरा - गिरिदुर्ग), पाटलिपुत्र (नदियों के संगम पर - जलदुर्ग)", "type": "leaf"},
            {"label": "उपजाऊ भूमि: गंगा के मैदानों में कृषि अधिशेष; व्यापार मार्गों पर नियंत्रण", "type": "leaf"}]},
        {"label": "सैन्य और राजनीतिक कारण", "type": "branch", "date": "सैन्य", "children": [
            {"label": "हाथियों का उपयोग: युद्ध में बड़े पैमाने पर हाथियों का उपयोग करने वाले पहले", "type": "leaf"},
            {"label": "महत्वाकांक्षी शासक: बिम्बिसार, अजातशत्रु, महापद्म नंद ने आक्रामक विस्तार किया", "type": "leaf"},
            {"label": "गैर-रूढ़िवादी समाज: ब्राह्मणवादी वर्चस्व कम होने से नवीन और व्यावहारिक कूटनीति को बढ़ावा", "type": "leaf"}]}
    ]
},

"shishunaga-dynasty": {
    "en": [
        {"label": "Shishunaga (c. 412–394 BCE)", "type": "branch", "date": "Shishunaga", "children": [
            {"label": "A former Amatya (minister) chosen by the people to replace the last Haryanka king", "type": "leaf"},
            {"label": "Avanti Conquest: Defeated the Pradyota dynasty of Avanti, ending the 100-year rivalry with Magadha", "type": "leaf"},
            {"label": "Capital: Shifted capital temporarily to Vaishali", "type": "leaf"}]},
        {"label": "Kalashoka (Kakavarna)", "type": "branch", "date": "Kalashoka", "children": [
            {"label": "Shifted capital back to Pataliputra", "type": "leaf"},
            {"label": "2nd Buddhist Council: Held at Vaishali (383 BCE)", "type": "leaf"},
            {"label": "Death: Assassinated by the founder of the Nanda dynasty", "type": "leaf"}]}
    ],
    "hi": [
        {"label": "शिशुनाग (लगभग 412–394 ई.पू.)", "type": "branch", "date": "शिशुनाग", "children": [
            {"label": "अंतिम हर्यक राजा के स्थान पर जनता द्वारा चुना गया एक अमात्य (मंत्री)", "type": "leaf"},
            {"label": "अवंति विजय: अवंति के प्रद्योत वंश को हराया, मगध के साथ 100 साल की दुश्मनी समाप्त", "type": "leaf"},
            {"label": "राजधानी: अस्थायी रूप से राजधानी वैशाली स्थानांतरित की", "type": "leaf"}]},
        {"label": "कालाशोक (काकवर्ण)", "type": "branch", "date": "कालाशोक", "children": [
            {"label": "राजधानी वापस पाटलिपुत्र ले गया", "type": "leaf"},
            {"label": "द्वितीय बौद्ध संगीति: वैशाली में (383 ई.पू.) आयोजित", "type": "leaf"},
            {"label": "मृत्यु: नंद वंश के संस्थापक द्वारा हत्या", "type": "leaf"}]}
    ]
},

"society-and-rise-of-cities-towns": {
    "en": [
        {"label": "Second Urbanization", "type": "branch", "date": "Urbanization", "children": [
            {"label": "Urban Centers: 60 towns mentioned in Pali texts (e.g., Kausambi, Sravasti, Ayodhya, Kapilavastu, Varanasi)", "type": "leaf"},
            {"label": "NBPW: Introduction of Northern Black Polished Ware pottery marks the urban phase", "type": "leaf"},
            {"label": "Burnt Bricks: Used in housing and fortifications for the first time since Harappan era", "type": "leaf"}]},
        {"label": "Social Structure", "type": "branch", "date": "Society", "children": [
            {"label": "Varna System: Became more rigid; Dharmasutras laid down rules for the 4 varnas", "type": "leaf"},
            {"label": "Untouchability: Emergence of Chandalas (social outcasts)", "type": "leaf"},
            {"label": "Gahapati: Rise of the wealthy land-owning class / influential merchants", "type": "leaf"}]}
    ],
    "hi": [
        {"label": "द्वितीय नगरीकरण", "type": "branch", "date": "नगरीकरण", "children": [
            {"label": "शहरी केंद्र: पाली ग्रंथों में 60 शहरों का उल्लेख (उदा. कौशांबी, श्रावस्ती, अयोध्या, वाराणसी)", "type": "leaf"},
            {"label": "NBPW: उत्तरी काले पॉलिश वाले मृदभांड का उद्भव शहरी चरण को दर्शाता है", "type": "leaf"},
            {"label": "पकी ईंटें: हड़प्पा काल के बाद पहली बार मकानों और किलों में प्रयोग", "type": "leaf"}]},
        {"label": "सामाजिक संरचना", "type": "branch", "date": "समाज", "children": [
            {"label": "वर्ण व्यवस्था: अधिक कठोर हुई; धर्मसूत्रों ने 4 वर्णों के लिए नियम बनाए", "type": "leaf"},
            {"label": "अस्पृश्यता: चांडालों (समाज से बहिष्कृत) का उदय", "type": "leaf"},
            {"label": "गहपति: धनी भू-स्वामी वर्ग / प्रभावशाली व्यापारियों का उदय", "type": "leaf"}]}
    ]
},

"society-and-rise-of-citiestowns": {
    "en": [
        {"label": "Second Urbanization", "type": "branch", "date": "Urbanization", "children": [
            {"label": "Urban Centers: 60 towns mentioned in Pali texts (e.g., Kausambi, Sravasti, Ayodhya, Kapilavastu, Varanasi)", "type": "leaf"},
            {"label": "NBPW: Introduction of Northern Black Polished Ware pottery marks the urban phase", "type": "leaf"},
            {"label": "Burnt Bricks: Used in housing and fortifications for the first time since Harappan era", "type": "leaf"}]},
        {"label": "Social Structure", "type": "branch", "date": "Society", "children": [
            {"label": "Varna System: Became more rigid; Dharmasutras laid down rules for the 4 varnas", "type": "leaf"},
            {"label": "Untouchability: Emergence of Chandalas (social outcasts)", "type": "leaf"},
            {"label": "Gahapati: Rise of the wealthy land-owning class / influential merchants", "type": "leaf"}]}
    ],
    "hi": [
        {"label": "द्वितीय नगरीकरण", "type": "branch", "date": "नगरीकरण", "children": [
            {"label": "शहरी केंद्र: पाली ग्रंथों में 60 शहरों का उल्लेख (उदा. कौशांबी, श्रावस्ती, अयोध्या, वाराणसी)", "type": "leaf"},
            {"label": "NBPW: उत्तरी काले पॉलिश वाले मृदभांड का उद्भव शहरी चरण को दर्शाता है", "type": "leaf"},
            {"label": "पकी ईंटें: हड़प्पा काल के बाद पहली बार मकानों और किलों में प्रयोग", "type": "leaf"}]},
        {"label": "सामाजिक संरचना", "type": "branch", "date": "समाज", "children": [
            {"label": "वर्ण व्यवस्था: अधिक कठोर हुई; धर्मसूत्रों ने 4 वर्णों के लिए नियम बनाए", "type": "leaf"},
            {"label": "अस्पृश्यता: चांडालों (समाज से बहिष्कृत) का उदय", "type": "leaf"},
            {"label": "गहपति: धनी भू-स्वामी वर्ग / प्रभावशाली व्यापारियों का उदय", "type": "leaf"}]}
    ]
},

"the-16-mahajanapadas": {
    "en": [
        {"label": "Key Sources", "type": "branch", "date": "Sources", "children": [
            {"label": "Buddhist Text: Anguttara Nikaya and Mahavastu mention 16 states", "type": "leaf"},
            {"label": "Jain Text: Bhagavati Sutra", "type": "leaf"}]},
        {"label": "Important Mahajanapadas & Capitals", "type": "branch", "date": "States", "children": [
            {"label": "Magadha (Girivraja / Rajagriha): Most powerful, modern Bihar", "type": "leaf"},
            {"label": "Anga (Champa): Famous for trade; annexed by Bimbisara", "type": "leaf"},
            {"label": "Kosala (Shravasti / Ayodhya): Modern Awadh; King Prasenajit", "type": "leaf"},
            {"label": "Vajji (Vaishali): A powerful republic of 8 clans (Lichchhavis)", "type": "leaf"},
            {"label": "Avanti (Ujjain / Mahishmati): Malwa region; King Pradyota; patron of Buddhism", "type": "leaf"},
            {"label": "Vatsa (Kausambi): Allahabad area; King Udayana", "type": "leaf"},
            {"label": "Ashmaka / Assaka (Potali / Paudanya): Only Mahajanapada situated on the banks of Godavari (South India)", "type": "leaf"},
            {"label": "Gandhara (Taxila): NW India; famous for education and trade", "type": "leaf"},
            {"label": "Kamboja (Poonch / Rajori): Famous for excellent horses", "type": "leaf"},
            {"label": "Malla (Kushinagar / Pava): Republic where Buddha and Mahavira attained Nirvana", "type": "leaf"}]}
    ],
    "hi": [
        {"label": "प्रमुख स्रोत", "type": "branch", "date": "स्रोत", "children": [
            {"label": "बौद्ध ग्रंथ: अंगुत्तर निकाय और महावस्तु में 16 राज्यों का उल्लेख", "type": "leaf"},
            {"label": "जैन ग्रंथ: भगवती सूत्र", "type": "leaf"}]},
        {"label": "महत्वपूर्ण महाजनपद और राजधानियाँ", "type": "branch", "date": "राज्य", "children": [
            {"label": "मगध (गिरिव्रज / राजगृह): सबसे शक्तिशाली, आधुनिक बिहार", "type": "leaf"},
            {"label": "अंग (चंपा): व्यापार के लिए प्रसिद्ध; बिम्बिसार द्वारा जीता गया", "type": "leaf"},
            {"label": "कोसल (श्रावस्ती / अयोध्या): आधुनिक अवध; राजा प्रसेनजित", "type": "leaf"},
            {"label": "वज्जि (वैशाली): 8 कुलों (लिच्छवि) का शक्तिशाली गणतंत्र", "type": "leaf"},
            {"label": "अवंति (उज्जैन / माहिष्मती): मालवा क्षेत्र; राजा प्रद्योत", "type": "leaf"},
            {"label": "वत्स (कौशांबी): इलाहाबाद क्षेत्र; राजा उदयन", "type": "leaf"},
            {"label": "अश्मक (पोतलि / पोदन): गोदावरी तट पर स्थित एकमात्र महाजनपद (दक्षिण भारत)", "type": "leaf"},
            {"label": "गांधार (तक्षशिला): शिक्षा और व्यापार के लिए प्रसिद्ध", "type": "leaf"},
            {"label": "कम्बोज (हाटक / राजौरी): उत्कृष्ट घोड़ों के लिए प्रसिद्ध", "type": "leaf"},
            {"label": "मल्ल (कुशीनगर / पावा): गणतंत्र जहाँ बुद्ध और महावीर को निर्वाण प्राप्त हुआ", "type": "leaf"}]}
    ]
}

}

# ─── HELPERS ────────────────────────────────────────────────────────────────

def get_clean_title(folder_name):
    title = folder_name.replace('-', ' ')
    skip = {'of', 'and', 'the', 'for', 'in', 'with', 'to', 'on', 'by', 'or', 'a', 'an', 'about'}
    return ' '.join(w if w.lower() in skip else w.capitalize() for w in title.split())

def create_hi_stub(en_html_path, hi_html_path, folder_name):
    with open(en_html_path, 'r', encoding='utf-8') as f:
        html = f.read()
    html = html.replace('\r\n', '\n')
    html = html.replace('<html lang="en">', '<html lang="hi">', 1)
    
    html = re.sub(
        r'<link rel="canonical" href="([^"]+)"',
        lambda m: f'<link rel="canonical" href="{m.group(1).rstrip("/")}/hi/"',
        html, count=1
    )
    
    clean_title = get_clean_title(folder_name)
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

    for old in ['    <link rel="stylesheet" href="/assets/css/mindmap.min.css?v=2">\n',
                '    <link rel="stylesheet" href="/assets/css/mindmap.min.css?v=1">\n']:
        html = html.replace(old, '')
    html = re.sub(r'\s*<!-- Interactive Mindmap -->.*?<!-- Deep-Dive Study Guide \(Dynamically Rendered\) -->', '\n            <!-- Deep-Dive Study Guide (Dynamically Rendered) -->', html, flags=re.DOTALL)
    html = re.sub(r'\s*<!-- Interactive Mindmap -->.*?renderMindmap\(.*?\);\s*</script>', '', html, flags=re.DOTALL)

    clean_title = get_clean_title(folder_name)
    key = folder_name.lower()
    branches = MINDMAP_DATA.get(key, {}).get(lang, [])
    if not branches:
        branches = [{"label": clean_title, "type": "branch", "date": "UPSC", "children": [{"label": "Content coming soon", "type": "leaf"}]}]
        
    mindmap_data = {"label": clean_title, "type": "root", "children": branches}

    css_link = '    <link rel="stylesheet" href="/assets/css/mindmap.min.css?v=2">\n'
    if css_link not in html:
        html = html.replace('</head>', css_link + '</head>')

    if lang == 'hi':
        instr = 'किसी <strong style="color:#a78bfa;">बैंगनी</strong> या <strong style="color:#2ecc71;">हरे</strong> <strong>+</strong> पर क्लिक करें।'
        title_text = f"{clean_title} &mdash; इंटरैक्टिव माइंडमैप"
    else:
        instr = 'Tap a <strong style="color:#a78bfa;">purple</strong> or <strong style="color:#2ecc71;">green</strong> <strong>+</strong> to expand.'
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
    else:
        marker = '<div class="tab-panel active" id="notes-panel" role="tabpanel" aria-labelledby="notes-panel">'
        if marker in html:
            html = html.replace(marker, marker + '\n' + mindmap_card, 1)

    tree_json = json.dumps(mindmap_data, ensure_ascii=False)
    inline_script = f'''
    <!-- Interactive Mindmap -->
    <script src="/assets/js/mindmap-engine.min.js?v=2"></script>
    <script>
    renderMindmap({tree_json}, undefined, '{lang}');
    </script>
'''
    html = html.replace('</body>', inline_script + '\n</body>')
    with open(html_path, 'w', encoding='utf-8') as f:
        f.write(html)

def main():
    total_en = 0
    total_hi = 0

    for root_dir, dirs, files in os.walk(BASE):
        dirs[:] = [d for d in dirs if d != 'hi']
        if 'index.html' not in files:
            continue

        folder_name = os.path.basename(root_dir)
        en_path = os.path.join(root_dir, 'index.html')
        hi_dir = os.path.join(root_dir, 'hi')
        hi_path = os.path.join(hi_dir, 'index.html')

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
