#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script to add detailed unique mindmaps for Mauryan-Empire topics in both English and Hindi.
It creates the hi/index.html stub if it doesn't exist, then injects the mindmap.
"""

import os, re, json, shutil

BASE = r"upsc/ancient_history/Mauryan-Empire"

# ─── DATA: ENGLISH AND HINDI BRANCHES ───────────────────────────────────────

MINDMAP_DATA = {

"administration": {
    "en": [
        {"label": "Central Administration", "type": "branch", "date": "Central", "children": [
            {"label": "King: Absolute power, paternal despotism; assisted by Mantriparishad", "type": "leaf"},
            {"label": "Tirthas (18 Top Officials): Mantrin (Chief Minister), Purohita (Chief Priest), Senapati (Commander)", "type": "leaf"},
            {"label": "Adhyakshas (Superintendents): 27 mentioned in Arthashastra (e.g., Sitadhyaksha for agriculture)", "type": "leaf"}]},
        {"label": "Provincial & Local", "type": "branch", "date": "Local", "children": [
            {"label": "5 Provinces: Uttarapatha (Taxila), Dakshinapatha (Suvarnagiri), Prachyapatha (Tosali), Avantiratha (Ujjain), Magadha (Pataliputra)", "type": "leaf"},
            {"label": "City Administration: 6 boards of 5 members each (Megasthenes account)", "type": "leaf"}]}
    ],
    "hi": [
        {"label": "केंद्रीय प्रशासन", "type": "branch", "date": "केंद्र", "children": [
            {"label": "राजा: सर्वोच्च शक्ति, पैतृक निरंकुशता; मंत्रिपरिषद द्वारा सहायता", "type": "leaf"},
            {"label": "तीर्थ (18 शीर्ष अधिकारी): मंत्री, पुरोहित, सेनापति, युवराज", "type": "leaf"},
            {"label": "अध्यक्ष (27): अर्थशास्त्र में वर्णित (उदा. सीताध्यक्ष - कृषि, लक्षणाध्यक्ष - मुद्रा)", "type": "leaf"}]},
        {"label": "प्रांतीय और स्थानीय", "type": "branch", "date": "स्थानीय", "children": [
            {"label": "5 प्रांत: उत्तरापथ (तक्षशिला), दक्षिणापथ (सुवर्णगिरि), प्राच्यपथ (तोसाली), अवंति (उज्जैन), मगध (पाटलिपुत्र)", "type": "leaf"},
            {"label": "नगर प्रशासन: 6 समितियाँ (प्रत्येक में 5 सदस्य) — मेगस्थनीज का विवरण", "type": "leaf"}]}
    ]
},

"administration-important-offices": {
    "en": [
        {"label": "Key Tirthas (Top Officials)", "type": "branch", "date": "Tirthas", "children": [
            {"label": "Samaharta: Chief Revenue Collector", "type": "leaf"},
            {"label": "Sannidhata: Treasurer / Keeper of Royal Store", "type": "leaf"},
            {"label": "Pradeshtri: Chief Justice of Criminal Court (Kantakasodhana)", "type": "leaf"},
            {"label": "Karmantika: Head of Industries and Factories", "type": "leaf"}]},
        {"label": "Key Adhyakshas", "type": "branch", "date": "Adhyakshas", "children": [
            {"label": "Sitadhyaksha: Superintendent of Crown Lands (Agriculture)", "type": "leaf"},
            {"label": "Panyadhyaksha: Superintendent of Commerce/Trade", "type": "leaf"},
            {"label": "Rupadarshaka: Inspector of Coins", "type": "leaf"}]}
    ],
    "hi": [
        {"label": "प्रमुख तीर्थ (शीर्ष अधिकारी)", "type": "branch", "date": "तीर्थ", "children": [
            {"label": "समाहर्ता: मुख्य राजस्व संग्रहकर्ता", "type": "leaf"},
            {"label": "सन्निधाता: कोषाध्यक्ष (राजकीय भंडार का रक्षक)", "type": "leaf"},
            {"label": "प्रदेष्टा: फौजदारी न्यायालय (कंटकशोधन) का मुख्य न्यायाधीश", "type": "leaf"},
            {"label": "कर्मांतिक: उद्योगों और कारखानों का प्रमुख", "type": "leaf"}]},
        {"label": "प्रमुख अध्यक्ष", "type": "branch", "date": "अध्यक्ष", "children": [
            {"label": "सीताध्यक्ष: राजकीय कृषि भूमि का अधीक्षक", "type": "leaf"},
            {"label": "पण्याध्यक्ष: व्यापार और वाणिज्य का अधीक्षक", "type": "leaf"},
            {"label": "रूपदर्शक: मुद्राओं (सिक्कों) का निरीक्षक", "type": "leaf"}]}
    ]
},

"administrative-setup": {
    "en": [
        {"label": "Hierarchy", "type": "branch", "date": "Hierarchy", "children": [
            {"label": "Empire → Province (Chakra) → District (Ahara/Vishaya) → Village Group (Sangrahana) → Village (Grama)", "type": "leaf"},
            {"label": "Rajukas: District administrators (like modern DMs), later given judicial powers by Ashoka", "type": "leaf"},
            {"label": "Gopa: Accountant for 10-15 villages", "type": "leaf"}]},
        {"label": "Espionage System", "type": "branch", "date": "Espionage", "children": [
            {"label": "Gudha Purushas: Spies mentioned by Chanakya", "type": "leaf"},
            {"label": "Sanstha (Stationary spies) and Sanchari (Wandering spies)", "type": "leaf"}]}
    ],
    "hi": [
        {"label": "प्रशासनिक पदानुक्रम", "type": "branch", "date": "पदानुक्रम", "children": [
            {"label": "साम्राज्य → प्रांत (चक्र) → जिला (आहार/विषय) → ग्राम समूह (संग्रहण) → ग्राम", "type": "leaf"},
            {"label": "रज्जुक: जिला अधिकारी (आधुनिक DM के समान), अशोक ने न्यायिक अधिकार दिए", "type": "leaf"},
            {"label": "गोप: 10-15 गाँवों का लेखापाल", "type": "leaf"}]},
        {"label": "गुप्तचर व्यवस्था", "type": "branch", "date": "गुप्तचर", "children": [
            {"label": "गूढ़ पुरुष: चाणक्य द्वारा वर्णित गुप्तचर प्रणाली", "type": "leaf"},
            {"label": "संस्था (स्थायी गुप्तचर) और संचार (भ्रमणशील गुप्तचर)", "type": "leaf"}]}
    ]
},

"ashoka-policy-of-dhamma": {
    "en": [
        {"label": "Nature of Dhamma", "type": "branch", "date": "Concept", "children": [
            {"label": "Not a religion: A moral code of conduct (Prakrit 'Dhamma' = Sanskrit 'Dharma')", "type": "leaf"},
            {"label": "Focus: Social harmony, non-violence (Ahimsa), tolerance, respect for elders and slaves", "type": "leaf"},
            {"label": "Aim: To unify the vast empire through a common ethical framework", "type": "leaf"}]},
        {"label": "Propagation", "type": "branch", "date": "Propagation", "children": [
            {"label": "Dhamma Mahamattas: Special officers appointed to spread Dhamma (Major Rock Edict V)", "type": "leaf"},
            {"label": "Rock & Pillar Edicts: Inscribed messages in local scripts (Brahmi, Kharoshthi, Aramaic, Greek)", "type": "leaf"}]}
    ],
    "hi": [
        {"label": "धम्म की प्रकृति", "type": "branch", "date": "अवधारणा", "children": [
            {"label": "कोई धर्म नहीं: आचार संहिता (प्राकृत 'धम्म' = संस्कृत 'धर्म')", "type": "leaf"},
            {"label": "केंद्र: सामाजिक सद्भाव, अहिंसा, सहिष्णुता, बड़ों और दासों का सम्मान", "type": "leaf"},
            {"label": "उद्देश्य: एक सामान्य नैतिक ढांचे के माध्यम से विशाल साम्राज्य को एकजुट करना", "type": "leaf"}]},
        {"label": "प्रचार-प्रसार", "type": "branch", "date": "प्रचार", "children": [
            {"label": "धम्म महामात्र: धम्म के प्रचार के लिए विशेष अधिकारी (5वाँ शिलालेख)", "type": "leaf"},
            {"label": "शिलालेख और स्तंभ लेख: स्थानीय लिपियों (ब्राह्मी, खरोष्ठी, अरामी) में उत्कीर्ण संदेश", "type": "leaf"}]}
    ]
},

"ashoka-and-buddhism": {
    "en": [
        {"label": "Conversion", "type": "branch", "date": "Conversion", "children": [
            {"label": "Kalinga War (261 BCE): Shocked by bloodshed, Ashoka embraced Buddhism (Major Rock Edict XIII)", "type": "leaf"},
            {"label": "Upagupta: The Buddhist monk who influenced/converted Ashoka", "type": "leaf"},
            {"label": "Bhabru Inscription: Ashoka expresses faith in Buddha, Dhamma, and Sangha", "type": "leaf"}]},
        {"label": "Buddhist Activities", "type": "branch", "date": "Activities", "children": [
            {"label": "3rd Buddhist Council: Held at Pataliputra (250 BCE); presided by Moggaliputta Tissa", "type": "leaf"},
            {"label": "Missions: Sent Mahendra (son) and Sanghamitra (daughter) to Ceylon (Sri Lanka) with Bodhi tree branch", "type": "leaf"}]}
    ],
    "hi": [
        {"label": "बौद्ध धर्म ग्रहण", "type": "branch", "date": "स्वीकार", "children": [
            {"label": "कलिंग युद्ध (261 BCE): रक्तपात से दुखी होकर बौद्ध धर्म अपनाया (13वाँ शिलालेख)", "type": "leaf"},
            {"label": "उपगुप्त: वह बौद्ध भिक्षु जिसने अशोक को प्रभावित/दीक्षित किया", "type": "leaf"},
            {"label": "भाब्रू अभिलेख: अशोक ने बुद्ध, धम्म और संघ में आस्था व्यक्त की", "type": "leaf"}]},
        {"label": "बौद्ध गतिविधियाँ", "type": "branch", "date": "गतिविधियाँ", "children": [
            {"label": "तीसरी बौद्ध संगीति: पाटलिपुत्र (250 BCE); मोग्गलिपुत्त तिस्स की अध्यक्षता में", "type": "leaf"},
            {"label": "धर्म प्रचारक: महेंद्र (पुत्र) और संघमित्रा (पुत्री) को बोधि वृक्ष की शाखा के साथ सीलोन (श्रीलंका) भेजा", "type": "leaf"}]}
    ]
},

"ashoka-and-his-successors": {
    "en": [
        {"label": "Ashoka's Later Years", "type": "branch", "date": "Later Years", "children": [
            {"label": "Ruled for ~40 years; empire covered almost entire subcontinent except extreme south (Cholas, Pandyas, Cheras)", "type": "leaf"}]},
        {"label": "Successors", "type": "branch", "date": "Successors", "children": [
            {"label": "Empire Partitioned: Western part (Kunala), Eastern part (Dasaratha)", "type": "leaf"},
            {"label": "Dasaratha: Patronized Ajivikas (Nagarjuni caves)", "type": "leaf"},
            {"label": "Brihadratha: Last Mauryan king, assassinated by his general Pushyamitra Shunga in 185 BCE", "type": "leaf"}]}
    ],
    "hi": [
        {"label": "अशोक का अंतिम समय", "type": "branch", "date": "अंतिम काल", "children": [
            {"label": "~40 वर्ष शासन किया; साम्राज्य पूरे उपमहाद्वीप में फैला था (सुदूर दक्षिण - चोल, पांड्य, चेर को छोड़कर)", "type": "leaf"}]},
        {"label": "उत्तराधिकारी", "type": "branch", "date": "उत्तराधिकारी", "children": [
            {"label": "साम्राज्य का विभाजन: पश्चिमी भाग (कुणाल), पूर्वी भाग (दशरथ)", "type": "leaf"},
            {"label": "दशरथ: आजीवक संप्रदाय को संरक्षण दिया (नागार्जुनी गुफाएँ)", "type": "leaf"},
            {"label": "बृहद्रथ: अंतिम मौर्य राजा, 185 ई.पू. में सेनापति पुष्यमित्र शुंग द्वारा हत्या", "type": "leaf"}]}
    ]
},

"ashokan-reign": {
    "en": [
        {"label": "Early Reign", "type": "branch", "date": "Early", "children": [
            {"label": "Ascension: Defeated brothers (legend says 99 brothers) to claim throne; 4-year succession war", "type": "leaf"},
            {"label": "Title: 'Devanampiya Piyadasi' (Beloved of the Gods, He who looks with affection)", "type": "leaf"}]},
        {"label": "Key Events", "type": "branch", "date": "Events", "children": [
            {"label": "Kalinga War (Year 8): Massive casualties; turning point of his life", "type": "leaf"},
            {"label": "Welfare State: Built hospitals, dug wells, planted trees along roads", "type": "leaf"}]}
    ],
    "hi": [
        {"label": "प्रारंभिक शासन", "type": "branch", "date": "प्रारंभिक", "children": [
            {"label": "राज्यारोहण: भाइयों को हराकर सत्ता प्राप्त की; 4 वर्ष का उत्तराधिकार युद्ध", "type": "leaf"},
            {"label": "उपाधि: 'देवानांपिय पियदस्सी' (देवताओं का प्रिय)", "type": "leaf"}]},
        {"label": "प्रमुख घटनाएँ", "type": "branch", "date": "घटनाएँ", "children": [
            {"label": "कलिंग युद्ध (8वें वर्ष): भारी रक्तपात; जीवन का टर्निंग पॉइंट", "type": "leaf"},
            {"label": "कल्याणकारी राज्य: अस्पताल बनवाए, कुएं खुदवाए, सड़कों के किनारे पेड़ लगाए", "type": "leaf"}]}
    ]
},

"ashokas-inscriptions-and-sites": {
    "en": [
        {"label": "Types of Edicts", "type": "branch", "date": "Types", "children": [
            {"label": "14 Major Rock Edicts: Moral principles; Edict XIII mentions Kalinga war", "type": "leaf"},
            {"label": "7 Pillar Edicts: Appendix to rock edicts; found in Gangetic valley", "type": "leaf"},
            {"label": "Minor Rock Edicts: Personal history of Ashoka; Maski and Gujarra mention his name 'Ashoka'", "type": "leaf"}]},
        {"label": "Languages & Scripts", "type": "branch", "date": "Scripts", "children": [
            {"label": "Prakrit language in Brahmi script (Majority of India)", "type": "leaf"},
            {"label": "Kharoshthi script (North-West: Mansehra, Shahbazgarhi)", "type": "leaf"},
            {"label": "Aramaic & Greek (Afghanistan: Kandahar bilingual edict)", "type": "leaf"}]}
    ],
    "hi": [
        {"label": "अभिलेखों के प्रकार", "type": "branch", "date": "प्रकार", "children": [
            {"label": "14 बृहत् शिलालेख: नैतिक सिद्धांत; 13वें में कलिंग युद्ध का वर्णन", "type": "leaf"},
            {"label": "7 स्तंभ लेख: गंगा घाटी में पाए गए; शिलालेखों के परिशिष्ट", "type": "leaf"},
            {"label": "लघु शिलालेख: अशोक का व्यक्तिगत इतिहास; मास्की और गुर्जरा में 'अशोक' नाम का उल्लेख", "type": "leaf"}]},
        {"label": "भाषा और लिपियाँ", "type": "branch", "date": "लिपियाँ", "children": [
            {"label": "ब्राह्मी लिपि में प्राकृत भाषा (अधिकांश भारत में)", "type": "leaf"},
            {"label": "खरोष्ठी लिपि (उत्तर-पश्चिम: मानसेहरा, शाहबाजगढ़ी)", "type": "leaf"},
            {"label": "अरामी और ग्रीक (अफगानिस्तान: कंधार द्विभाषी अभिलेख)", "type": "leaf"}]}
    ]
},

"aspects-of-mauryan-economy": {
    "en": [
        {"label": "Agriculture", "type": "branch", "date": "Agriculture", "children": [
            {"label": "State-controlled farms (Sita lands) managed by Sitadhyaksha", "type": "leaf"},
            {"label": "Taxes: Bhaga (1/6 to 1/4 of produce), Bali (religious/additional tax), Udakabhaga (irrigation tax)", "type": "leaf"}]},
        {"label": "Trade and Currency", "type": "branch", "date": "Trade", "children": [
            {"label": "State monopolies: Mining, liquor, salt, arms manufacture", "type": "leaf"},
            {"label": "Currency: Punch-marked silver coins (Karshapana/Pana); managed by Rupadarshaka", "type": "leaf"},
            {"label": "Guilds (Shrenis): Organized craft associations", "type": "leaf"}]}
    ],
    "hi": [
        {"label": "कृषि", "type": "branch", "date": "कृषि", "children": [
            {"label": "राज्य नियंत्रित खेत (सीता भूमि); सीताध्यक्ष द्वारा प्रबंधित", "type": "leaf"},
            {"label": "कर: भाग (उपज का 1/6 से 1/4), बलि (अतिरिक्त कर), उदकभाग (सिंचाई कर)", "type": "leaf"}]},
        {"label": "व्यापार और मुद्रा", "type": "branch", "date": "व्यापार", "children": [
            {"label": "राज्य एकाधिकार: खनन, शराब, नमक, हथियार निर्माण", "type": "leaf"},
            {"label": "मुद्रा: आहत चाँदी के सिक्के (कार्षापण/पण); रूपदर्शक द्वारा प्रबंधित", "type": "leaf"},
            {"label": "श्रेणी (Guilds): संगठित शिल्प संघ", "type": "leaf"}]}
    ]
},

"aspects-of-mauryan-polity": {
    "en": [
        {"label": "Saptanga Theory", "type": "branch", "date": "Theory", "children": [
            {"label": "Chanakya's 7 elements of state: Swami (King), Amatya (Minister), Janapada (Territory), Durga (Fort), Kosha (Treasury), Danda (Army), Mitra (Ally)", "type": "leaf"}]},
        {"label": "Judiciary & Military", "type": "branch", "date": "Law", "children": [
            {"label": "Courts: Dharmasthiya (Civil) and Kantakasodhana (Criminal)", "type": "leaf"},
            {"label": "Military: War Office of 30 members (6 boards of 5); Senapati was the head", "type": "leaf"}]}
    ],
    "hi": [
        {"label": "सप्तांग सिद्धांत", "type": "branch", "date": "सिद्धांत", "children": [
            {"label": "चाणक्य के राज्य के 7 अंग: स्वामी (राजा), अमात्य (मंत्री), जनपद (क्षेत्र), दुर्ग (किला), कोष (खजाना), दंड (सेना), मित्र", "type": "leaf"}]},
        {"label": "न्यायपालिका और सेना", "type": "branch", "date": "न्याय", "children": [
            {"label": "न्यायालय: धर्मस्थानीय (दीवानी) और कंटकशोधन (फौजदारी)", "type": "leaf"},
            {"label": "सेना: 30 सदस्यों का युद्ध कार्यालय (5-5 की 6 समितियाँ); सेनापति प्रमुख था", "type": "leaf"}]}
    ]
},

"bindusara": {
    "en": [
        {"label": "Bindusara (298-273 BCE)", "type": "branch", "date": "Reign", "children": [
            {"label": "Titles: 'Amitraghata' (Slayer of foes) by Greeks, 'Simhasena' in Jain texts", "type": "leaf"},
            {"label": "Expansion: Conquered 'the land between the two seas' (Deccan/South India)", "type": "leaf"}]},
        {"label": "Foreign Relations & Religion", "type": "branch", "date": "Relations", "children": [
            {"label": "Syrian King Antiochus I sent ambassador Deimachus", "type": "leaf"},
            {"label": "Requested sweet wine, dried figs, and a sophist from Syria (Sophist was denied)", "type": "leaf"},
            {"label": "Religion: Patronized the Ajivika sect", "type": "leaf"}]}
    ],
    "hi": [
        {"label": "बिंदुसार (298-273 BCE)", "type": "branch", "date": "शासन", "children": [
            {"label": "उपाधियाँ: यूनानियों द्वारा 'अमित्रघात' (शत्रुओं का नाशक), जैन ग्रंथों में 'सिंहसेन'", "type": "leaf"},
            {"label": "विस्तार: 'दो समुद्रों के बीच की भूमि' (दक्कन/दक्षिण भारत) पर विजय प्राप्त की", "type": "leaf"}]},
        {"label": "विदेशी संबंध और धर्म", "type": "branch", "date": "संबंध", "children": [
            {"label": "सीरियाई राजा एंटिओकस प्रथम ने राजदूत डाइमेकस को भेजा", "type": "leaf"},
            {"label": "सीरिया से मीठी शराब, सूखे अंजीर और एक दार्शनिक माँगा (दार्शनिक देने से मना कर दिया गया)", "type": "leaf"},
            {"label": "धर्म: आजीवक संप्रदाय को संरक्षण दिया", "type": "leaf"}]}
    ]
},

"chandragupta": {
    "en": [
        {"label": "Chandragupta Maurya (322-298 BCE)", "type": "branch", "date": "Reign", "children": [
            {"label": "Foundation: Defeated Dhana Nanda (last Nanda king) with Chanakya's help", "type": "leaf"},
            {"label": "Greek Conflict: Defeated Seleucus Nicator (305 BCE); gained Kabul, Kandahar, Herat, Makran", "type": "leaf"},
            {"label": "Marriage Alliance: Married Helena, daughter of Seleucus; Megasthenes sent as ambassador", "type": "leaf"}]},
        {"label": "Later Life", "type": "branch", "date": "Later Life", "children": [
            {"label": "Religion: Embraced Jainism under Bhadrabahu", "type": "leaf"},
            {"label": "Death: Migrated to Shravanabelagola (Karnataka); died by Sallekhana (fasting to death)", "type": "leaf"}]}
    ],
    "hi": [
        {"label": "चंद्रगुप्त मौर्य (322-298 BCE)", "type": "branch", "date": "शासन", "children": [
            {"label": "स्थापना: चाणक्य की मदद से धनानंद (अंतिम नंद राजा) को हराया", "type": "leaf"},
            {"label": "यूनानी संघर्ष: सेल्यूकस निकेटर को हराया (305 BCE); काबुल, कंधार, हेरात, मकरान प्राप्त किया", "type": "leaf"},
            {"label": "वैवाहिक संबंध: सेल्यूकस की पुत्री हेलेना से विवाह; मेगस्थनीज राजदूत बनकर आया", "type": "leaf"}]},
        {"label": "अंतिम जीवन", "type": "branch", "date": "अंतिम", "children": [
            {"label": "धर्म: भद्रबाहु के प्रभाव में जैन धर्म अपनाया", "type": "leaf"},
            {"label": "मृत्यु: श्रवणबेलगोला (कर्नाटक) गए; संलेखना (उपवास) द्वारा प्राण त्यागे", "type": "leaf"}]}
    ]
},

"decline-of-the-mauryas": {
    "en": [
        {"label": "Causes of Decline", "type": "branch", "date": "Causes", "children": [
            {"label": "Brahmanical Reaction: Pushyamitra Shunga's revolt against pro-Buddhist policies (H.P. Sastri theory)", "type": "leaf"},
            {"label": "Financial Crisis: Huge expenditure on army, bureaucracy, and Ashoka's donations (D.D. Kosambi theory)", "type": "leaf"},
            {"label": "Oppressive Rule: Revolts in provinces like Taxila (Bindusara and Ashoka's time)", "type": "leaf"}]},
        {"label": "Weak Successors & Invasions", "type": "branch", "date": "Aftermath", "children": [
            {"label": "Partition of Empire: Weakened central authority after Ashoka", "type": "leaf"},
            {"label": "Foreign Invasions: Bactrian Greeks invaded the North-West", "type": "leaf"}]}
    ],
    "hi": [
        {"label": "पतन के कारण", "type": "branch", "date": "कारण", "children": [
            {"label": "ब्राह्मण प्रतिक्रिया: बौद्ध समर्थक नीतियों के खिलाफ पुष्यमित्र शुंग का विद्रोह (एच.पी. शास्त्री)", "type": "leaf"},
            {"label": "वित्तीय संकट: सेना, नौकरशाही और अशोक के दान पर भारी खर्च (डी.डी. कोसांबी)", "type": "leaf"},
            {"label": "दमनकारी शासन: तक्षशिला जैसे प्रांतों में विद्रोह (अमात्यों का अत्याचार)", "type": "leaf"}]},
        {"label": "कमजोर उत्तराधिकारी", "type": "branch", "date": "परिणाम", "children": [
            {"label": "साम्राज्य का विभाजन: अशोक के बाद केंद्रीय सत्ता कमजोर हुई", "type": "leaf"},
            {"label": "विदेशी आक्रमण: उत्तर-पश्चिम में बैक्ट्रियन ग्रीक (यवन) आक्रमण", "type": "leaf"}]}
    ]
},

"foreign-relations": {
    "en": [
        {"label": "Greeks and West Asia", "type": "branch", "date": "West", "children": [
            {"label": "Seleucus Nicator: Treaty with Chandragupta; exchanged 500 elephants for territories", "type": "leaf"},
            {"label": "Ambassadors: Megasthenes (from Seleucus), Deimachus (from Antiochus to Bindusara), Dionysius (from Ptolemy Philadelphus to Ashoka)", "type": "leaf"}]},
        {"label": "Ashoka's Dhamma Missions", "type": "branch", "date": "Missions", "children": [
            {"label": "Rock Edict XIII: Mentions Greek kings (Antiochus, Ptolemy, Antigonus, Magas, Alexander)", "type": "leaf"},
            {"label": "Sri Lanka (Ceylon): Sent Mahendra and Sanghamitra; King Tissa adopted Buddhism", "type": "leaf"}]}
    ],
    "hi": [
        {"label": "यूनानी और पश्चिम एशिया", "type": "branch", "date": "पश्चिम", "children": [
            {"label": "सेल्यूकस निकेटर: चंद्रगुप्त के साथ संधि; 500 हाथियों के बदले 4 प्रांत दिए", "type": "leaf"},
            {"label": "राजदूत: मेगस्थनीज (सेल्यूकस से), डाइमेकस (एंटिओकस से बिंदुसार के दरबार में), डायोनिसियस (अशोक के दरबार में)", "type": "leaf"}]},
        {"label": "अशोक के धम्म मिशन", "type": "branch", "date": "मिशन", "children": [
            {"label": "13वाँ शिलालेख: 5 यूनानी राजाओं का उल्लेख (एंटिओकस, टॉलेमी, एंटीगोनस, मागस, अलेक्जेंडर)", "type": "leaf"},
            {"label": "श्रीलंका (सीलोन): महेंद्र और संघमित्रा को भेजा; राजा तिस्स ने बौद्ध धर्म अपनाया", "type": "leaf"}]}
    ]
},

"political-history-of-the-mauryas": {
    "en": [
        {"label": "Chronology", "type": "branch", "date": "Timeline", "children": [
            {"label": "Chandragupta Maurya (322-298 BCE): Founder, defeated Nandas and Greeks", "type": "leaf"},
            {"label": "Bindusara (298-273 BCE): Expanded into the Deccan", "type": "leaf"},
            {"label": "Ashoka (268-232 BCE): Kalinga war, Dhamma, peak of empire", "type": "leaf"},
            {"label": "Later Mauryas (232-185 BCE): Weak kings, ending with Brihadratha", "type": "leaf"}]}
    ],
    "hi": [
        {"label": "कालक्रम (Chronology)", "type": "branch", "date": "कालक्रम", "children": [
            {"label": "चंद्रगुप्त मौर्य (322-298 ई.पू.): संस्थापक, नंदों और यूनानियों को हराया", "type": "leaf"},
            {"label": "बिंदुसार (298-273 ई.पू.): दक्कन में विस्तार किया", "type": "leaf"},
            {"label": "अशोक (268-232 ई.पू.): कलिंग युद्ध, धम्म, साम्राज्य का चरमोत्कर्ष", "type": "leaf"},
            {"label": "उत्तर मौर्य (232-185 ई.पू.): कमजोर राजा, बृहद्रथ अंतिम शासक", "type": "leaf"}]}
    ]
},

"society": {
    "en": [
        {"label": "Megasthenes' Observations", "type": "branch", "date": "Megasthenes", "children": [
            {"label": "7 Castes: Philosophers, Farmers, Herdsmen, Artisans, Military, Overseers, Councillors (He confused occupation with varna)", "type": "leaf"},
            {"label": "Slavery: Claimed no slavery existed in India (contradicted by Indian texts)", "type": "leaf"},
            {"label": "Famines: Claimed no famines occurred (contradicted by Sohgaura and Mahasthan inscriptions)", "type": "leaf"}]},
        {"label": "Social Conditions", "type": "branch", "date": "Conditions", "children": [
            {"label": "Women: Employed as spies (Vishkanyas), royal bodyguards; widow remarriage allowed (Niyoga)", "type": "leaf"},
            {"label": "Varna System: Rigid, but Shudras were involved in agriculture for the first time on a large scale", "type": "leaf"}]}
    ],
    "hi": [
        {"label": "मेगस्थनीज का विवरण", "type": "branch", "date": "मेगस्थनीज", "children": [
            {"label": "7 जातियाँ: दार्शनिक, किसान, अहीर, शिल्पी, सैनिक, निरीक्षक, सभासद (उसने व्यवसाय को वर्ण समझ लिया)", "type": "leaf"},
            {"label": "दास प्रथा: कहा कि भारत में दास प्रथा नहीं थी (भारतीय ग्रंथों के विपरीत)", "type": "leaf"},
            {"label": "अकाल: कहा कि अकाल नहीं पड़ते थे (सोहगौरा और महास्थान अभिलेख इसके विपरीत हैं)", "type": "leaf"}]},
        {"label": "सामाजिक स्थिति", "type": "branch", "date": "स्थिति", "children": [
            {"label": "महिलाएँ: जासूस (विषकन्या), अंगरक्षक के रूप में कार्यरत; विधवा विवाह (नियोग) की अनुमति", "type": "leaf"},
            {"label": "वर्ण व्यवस्था: कठोर थी, लेकिन शूद्र पहली बार बड़े पैमाने पर कृषि में शामिल हुए", "type": "leaf"}]}
    ]
},

"sources-of-information": {
    "en": [
        {"label": "Literary Sources", "type": "branch", "date": "Literature", "children": [
            {"label": "Arthashastra (Kautilya): Treatise on statecraft, economy, and military strategy", "type": "leaf"},
            {"label": "Indica (Megasthenes): Greek account of Mauryan society and administration (survives in fragments)", "type": "leaf"},
            {"label": "Mudrarakshasa (Vishakhadatta): Gupta-era play about Chanakya overthrowing the Nandas", "type": "leaf"}]},
        {"label": "Archaeological Sources", "type": "branch", "date": "Archaeology", "children": [
            {"label": "Ashokan Edicts: First deciphered by James Prinsep (1837)", "type": "leaf"},
            {"label": "Material Culture: Northern Black Polished Ware (NBPW), Punch-marked coins, Wooden palace at Kumrahar", "type": "leaf"}]}
    ],
    "hi": [
        {"label": "साहित्यिक स्रोत", "type": "branch", "date": "साहित्य", "children": [
            {"label": "अर्थशास्त्र (कौटिल्य): राजनीति, अर्थव्यवस्था और सैन्य रणनीति पर ग्रंथ", "type": "leaf"},
            {"label": "इंडिका (मेगस्थनीज): मौर्य समाज और प्रशासन का यूनानी विवरण", "type": "leaf"},
            {"label": "मुद्राराक्षस (विशाखदत्त): नंदों को उखाड़ फेंकने पर गुप्तकालीन नाटक", "type": "leaf"}]},
        {"label": "पुरातात्विक स्रोत", "type": "branch", "date": "पुरातत्व", "children": [
            {"label": "अशोक के अभिलेख: 1837 में जेम्स प्रिंसेप द्वारा पहली बार पढ़े गए", "type": "leaf"},
            {"label": "भौतिक संस्कृति: NBPW (उत्तरी काले पॉलिश वाले मृदभांड), आहत सिक्के, कुम्हरार का लकड़ी का महल", "type": "leaf"}]}
    ]
},

"sources-of-information-coins-and-sites": {
    "en": [
        {"label": "Numismatics", "type": "branch", "date": "Coins", "children": [
            {"label": "Punch-Marked Coins (PMC): Mostly silver (Karshapana) and copper; symbol-stamped, no royal names", "type": "leaf"},
            {"label": "Symbols: Sun, crescent, elephant, tree-in-railing, hill", "type": "leaf"}]},
        {"label": "Archaeological Sites", "type": "branch", "date": "Sites", "children": [
            {"label": "Kumrahar (Patna): Remains of an 80-pillared Mauryan hall", "type": "leaf"},
            {"label": "Sanchi & Sarnath: Stupas and pillars built by Ashoka", "type": "leaf"},
            {"label": "Barabar Caves: Built by Ashoka for Ajivikas; oldest rock-cut caves", "type": "leaf"}]}
    ],
    "hi": [
        {"label": "मुद्राशास्त्र (सिक्के)", "type": "branch", "date": "सिक्के", "children": [
            {"label": "आहत सिक्के (Punch-marked): मुख्य रूप से चाँदी (कार्षापण) और ताँबे के; राजाओं के नाम नहीं", "type": "leaf"},
            {"label": "प्रतीक चिन्ह: सूर्य, अर्धचंद्र, हाथी, पेड़, पहाड़ी", "type": "leaf"}]},
        {"label": "पुरातात्विक स्थल", "type": "branch", "date": "स्थल", "children": [
            {"label": "कुम्हरार (पटना): 80 खंभों वाले मौर्य महल के अवशेष", "type": "leaf"},
            {"label": "साँची और सारनाथ: अशोक द्वारा निर्मित स्तूप और स्तंभ", "type": "leaf"},
            {"label": "बराबर गुफाएँ: अशोक द्वारा आजीवकों के लिए निर्मित; सबसे पुरानी रॉक-कट गुफाएँ", "type": "leaf"}]}
    ]
},

"sources-of-information-inscriptions": {
    "en": [
        {"label": "Ashokan Inscriptions", "type": "branch", "date": "Edicts", "children": [
            {"label": "Deciphered by James Prinsep (1837)", "type": "leaf"},
            {"label": "Rock Edict 13: Mentions Kalinga War and foreign kings", "type": "leaf"},
            {"label": "Rummindei Pillar Inscription: Commemorates Ashoka's visit to Buddha's birthplace; tax reduced to 1/8", "type": "leaf"}]},
        {"label": "Other Inscriptions", "type": "branch", "date": "Other", "children": [
            {"label": "Sohgaura (UP) & Mahasthan (Bengal) Copper Plates: Pre-Ashokan; mention relief measures during famine", "type": "leaf"},
            {"label": "Junagadh Rock Inscription (Rudradaman): Mentions Pushyagupta building Sudarshana lake during Chandragupta's reign", "type": "leaf"}]}
    ],
    "hi": [
        {"label": "अशोक के अभिलेख", "type": "branch", "date": "अभिलेख", "children": [
            {"label": "1837 में जेम्स प्रिंसेप द्वारा पढ़े गए", "type": "leaf"},
            {"label": "13वाँ शिलालेख: कलिंग युद्ध और विदेशी राजाओं का उल्लेख", "type": "leaf"},
            {"label": "रुम्मिन्देई स्तंभ लेख: बुद्ध की जन्मस्थली की यात्रा; कर घटाकर 1/8 किया गया", "type": "leaf"}]},
        {"label": "अन्य अभिलेख", "type": "branch", "date": "अन्य", "children": [
            {"label": "सोहगौरा और महास्थान अभिलेख: अकाल के दौरान राहत उपायों का उल्लेख (चंद्रगुप्त काल)", "type": "leaf"},
            {"label": "जूनागढ़ अभिलेख (रुद्रदामन): चंद्रगुप्त के समय पुष्यगुप्त द्वारा सुदर्शन झील के निर्माण का उल्लेख", "type": "leaf"}]}
    ]
},

"sources-of-information-literary-sources": {
    "en": [
        {"label": "Brahmanical Texts", "type": "branch", "date": "Brahmanical", "children": [
            {"label": "Arthashastra (Kautilya): 15 Adhikaranas (books); detailed statecraft", "type": "leaf"},
            {"label": "Mudrarakshasa (Vishakhadatta): Describes Chanakya's machinations against Nandas", "type": "leaf"},
            {"label": "Puranas: Provide chronology and genealogy of Mauryan kings", "type": "leaf"}]},
        {"label": "Buddhist and Jain Texts", "type": "branch", "date": "Buddhist/Jain", "children": [
            {"label": "Dipavamsa & Mahavamsa (Sri Lanka): Detail Ashoka's role in spreading Buddhism", "type": "leaf"},
            {"label": "Divyavadana (Tibetan): Stories of Ashoka and Bindusara", "type": "leaf"},
            {"label": "Parishishtaparvan (Hemachandra): Jain text detailing Chandragupta's connection to Jainism", "type": "leaf"}]}
    ],
    "hi": [
        {"label": "ब्राह्मण ग्रंथ", "type": "branch", "date": "ब्राह्मण", "children": [
            {"label": "अर्थशास्त्र (कौटिल्य): 15 अधिकरण; राज्यशिल्प का विस्तृत वर्णन", "type": "leaf"},
            {"label": "मुद्राराक्षस (विशाखदत्त): नंदों के विरुद्ध चाणक्य की कूटनीति", "type": "leaf"},
            {"label": "पुराण: मौर्य राजाओं की वंशावली और कालक्रम", "type": "leaf"}]},
        {"label": "बौद्ध और जैन ग्रंथ", "type": "branch", "date": "बौद्ध/जैन", "children": [
            {"label": "दीपवंश और महावंश (श्रीलंका): बौद्ध धर्म फैलाने में अशोक की भूमिका", "type": "leaf"},
            {"label": "दिव्यावदान: अशोक और बिंदुसार की कहानियाँ", "type": "leaf"},
            {"label": "परिशिष्टपर्वन (हेमचंद्र): चंद्रगुप्त के जैन धर्म से जुड़ाव का वर्णन", "type": "leaf"}]}
    ]
},

"sources-of-information-literary-sources-indian-texts-and-travellers-account": {
    "en": [
        {"label": "Indigenous Texts", "type": "branch", "date": "Indian", "children": [
            {"label": "Arthashastra: Key source for administration, taxation, and espionage", "type": "leaf"},
            {"label": "Jatakas: Reveal socio-economic conditions of the Mauryan period", "type": "leaf"}]},
        {"label": "Foreign Accounts", "type": "branch", "date": "Foreign", "children": [
            {"label": "Megasthenes (Indica): Greek ambassador; detailed Pataliputra (Palibothra) administration", "type": "leaf"},
            {"label": "Justin & Strabo: Greek writers who called Chandragupta 'Sandrokottos'", "type": "leaf"},
            {"label": "Pliny: Described Indian trade and geography", "type": "leaf"}]}
    ],
    "hi": [
        {"label": "स्वदेशी ग्रंथ", "type": "branch", "date": "भारतीय", "children": [
            {"label": "अर्थशास्त्र: प्रशासन, कराधान और जासूसी के लिए प्रमुख स्रोत", "type": "leaf"},
            {"label": "जातक कथाएँ: मौर्य काल की सामाजिक-आर्थिक स्थिति", "type": "leaf"}]},
        {"label": "विदेशी विवरण", "type": "branch", "date": "विदेशी", "children": [
            {"label": "मेगस्थनीज (इंडिका): यूनानी राजदूत; पाटलिपुत्र (पालिबोथ्रा) प्रशासन का विवरण", "type": "leaf"},
            {"label": "जस्टिन और स्ट्रैबो: यूनानी लेखक जिन्होंने चंद्रगुप्त को 'सैंड्रोकोट्टोस' कहा", "type": "leaf"},
            {"label": "प्लिनी: भारतीय व्यापार और भूगोल का वर्णन", "type": "leaf"}]}
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
    # Update canonical
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

    # Remove existing mindmap injection
    for old in ['    <link rel="stylesheet" href="/assets/css/mindmap.min.css?v=2">\n',
                '    <link rel="stylesheet" href="/assets/css/mindmap.min.css?v=1">\n']:
        html = html.replace(old, '')
    html = re.sub(r'\s*<!-- Interactive Mindmap -->.*?<!-- Deep-Dive Study Guide \(Dynamically Rendered\) -->', '\n            <!-- Deep-Dive Study Guide (Dynamically Rendered) -->', html, flags=re.DOTALL)
    html = re.sub(r'\s*<!-- Interactive Mindmap -->.*?renderMindmap\(.*?\);\s*</script>', '', html, flags=re.DOTALL)

    clean_title = get_clean_title(folder_name)
    
    # Get branches
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

        # 1. Inject English mindmap
        inject_mindmap(en_path, folder_name, 'en')
        total_en += 1

        # 2. Create Hindi stub if missing
        if not os.path.exists(hi_path):
            create_hi_stub(en_path, hi_path, folder_name)

        # 3. Inject Hindi mindmap
        inject_mindmap(hi_path, folder_name, 'hi')
        total_hi += 1
        
        print(f"Processed: {folder_name}")

    print(f"\nCreated+patched {total_en} English and {total_hi} Hindi pages.")

if __name__ == '__main__':
    main()
