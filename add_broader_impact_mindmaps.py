#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os, re, json

BASE_DIR = r"upsc/modern_history/Broader-Impact-of-British-Administration"

MINDMAP_DATA = {
    "abolition-of-the-dual-system": {
        "en": [
            {"label": "Background & Origins", "type": "branch", "date": "1765-1772", "children": [
                {"label": "Introduced by Robert Clive in 1765 after the Treaty of Allahabad following the Battle of Buxar", "type": "leaf"},
                {"label": "EIC held Diwani (revenue rights) while Nawab retained Nizamat (administration & law/order)", "type": "leaf"},
                {"label": "Created 'authority without responsibility' for EIC, and 'responsibility without authority' for Nawab", "type": "leaf"}]},
            {"label": "Disastrous Consequences", "type": "branch", "date": "1765-1772", "children": [
                {"label": "Led to massive administrative chaos, unchecked corruption, and severe exploitation of Bengal", "type": "leaf"},
                {"label": "Aggravated the Great Bengal Famine of 1770, causing death of one-third of Bengal's population", "type": "leaf"},
                {"label": "Private trade by Company servants flourished while official EIC revenue deteriorated", "type": "leaf"}]},
            {"label": "Abolition & Transition", "type": "branch", "date": "1772", "children": [
                {"label": "Abolished by Warren Hastings in 1772 under orders of Court of Directors", "type": "leaf"},
                {"label": "Company decided to 'stand forth as Dewan' and take direct charge of revenue administration", "type": "leaf"},
                {"label": "Board of Revenue established; treasury shifted from Murshidabad to Calcutta", "type": "leaf"}]}
        ],
        "hi": [
            {"label": "पृष्ठभूमि और उत्पत्ति", "type": "branch", "date": "1765-1772", "children": [
                {"label": "बक्सर के युद्ध के बाद इलाहाबाद की संधि के बाद 1765 में रॉबर्ट क्लाइव द्वारा शुरू किया गया", "type": "leaf"},
                {"label": "EIC के पास दीवानी (राजस्व अधिकार) थे जबकि नवाब के पास निजामत (प्रशासन और कानून/व्यवस्था) थी", "type": "leaf"},
                {"label": "EIC के लिए 'बिना जिम्मेदारी के अधिकार' और नवाब के लिए 'बिना अधिकार के जिम्मेदारी' का निर्माण किया", "type": "leaf"}]},
            {"label": "विनाशकारी परिणाम", "type": "branch", "date": "1765-1772", "children": [
                {"label": "बंगाल में बड़े पैमाने पर प्रशासनिक अराजकता, अनियंत्रित भ्रष्टाचार और गंभीर शोषण को बढ़ावा मिला", "type": "leaf"},
                {"label": "1770 के महान बंगाल अकाल को और गंभीर बना दिया, जिससे बंगाल की एक तिहाई आबादी की मृत्यु हो गई", "type": "leaf"},
                {"label": "कंपनी के सेवकों द्वारा निजी व्यापार फला-फूला जबकि आधिकारिक EIC राजस्व में गिरावट आई", "type": "leaf"}]},
            {"label": "उन्मूलन और संक्रमण", "type": "branch", "date": "1772", "children": [
                {"label": "कोर्ट ऑफ डायरेक्टर्स के आदेश पर 1772 में वारेन हेस्टिंग्स द्वारा समाप्त किया गया", "type": "leaf"},
                {"label": "कंपनी ने 'दीवान के रूप में खड़े होने' और राजस्व प्रशासन का सीधा प्रभार लेने का फैसला किया", "type": "leaf"},
                {"label": "राजस्व बोर्ड (Board of Revenue) की स्थापना; खजाना मुर्शिदाबाद से कलकत्ता स्थानांतरित किया गया", "type": "leaf"}]}
        ]
    },
    "changes-in-social-setup": {
        "en": [
            {"label": "Emergence of New Classes", "type": "branch", "date": "Social Setup", "children": [
                {"label": "Middle class intelligentsia: English-educated Indians employed in administration, law, medicine", "type": "leaf"},
                {"label": "Industrial Bourgeoisie: Indian merchants and capitalists who accumulated wealth during WWI", "type": "leaf"},
                {"label": "Modern working class: Labourers in railways, coal mines, plantations, and cotton/jute factories", "type": "leaf"}]},
            {"label": "Erosion of Village Structure", "type": "branch", "date": "Social Setup", "children": [
                {"label": "Breakdown of self-sufficient village communities due to commercialization and land saleability", "type": "leaf"},
                {"label": "Rise of rural proletariat: landless peasants forced into agricultural labor or sharecropping", "type": "leaf"}]},
            {"label": "Socio-Religious Changes", "type": "branch", "date": "Social Setup", "children": [
                {"label": "Spread of rationalist, reformist ideas leading to the challenge of rigid caste hierarchy", "type": "leaf"},
                {"label": "Rise of social mobility for English-educated elite, but widening gap with the rural masses", "type": "leaf"}]}
        ],
        "hi": [
            {"label": "नए वर्गों का उदय", "type": "branch", "date": "सामाजिक व्यवस्था", "children": [
                {"label": "मध्यम वर्ग बुद्धिजीवी: प्रशासन, कानून, चिकित्सा में कार्यरत अंग्रेजी-शिक्षित भारतीय", "type": "leaf"},
                {"label": "औद्योगिक बुर्जुआ: भारतीय व्यापारी और पूंजीपति जिन्होंने प्रथम विश्व युद्ध के दौरान धन संचित किया", "type": "leaf"},
                {"label": "आधुनिक श्रमिक वर्ग: रेलवे, कोयला खानों, बागानों और सूती/जूट कारखानों में काम करने वाले मजदूर", "type": "leaf"}]},
            {"label": "ग्रामीण संरचना का पतन", "type": "branch", "date": "सामाजिक व्यवस्था", "children": [
                {"label": "कृषि के व्यावसायीकरण और भूमि की बिक्री योग्यता के कारण आत्मनिर्भर ग्रामीण समुदायों का टूटना", "type": "leaf"},
                {"label": "ग्रामीण सर्वहारा वर्ग का उदय: भूमिहीन किसान कृषि श्रम या बटाईदारी के लिए मजबूर हुए", "type": "leaf"}]},
            {"label": "सामाजिक-धार्मिक परिवर्तन", "type": "branch", "date": "सामाजिक व्यवस्था", "children": [
                {"label": "तर्कवादी, सुधारवादी विचारों का प्रसार जिसके कारण कठोर जाति पदानुक्रम को चुनौती मिली", "type": "leaf"},
                {"label": "अंग्रेजी-शिक्षित अभिजात वर्ग के लिए सामाजिक गतिशीलता में वृद्धि, लेकिन ग्रामीण जनता के साथ अंतर बढ़ा", "type": "leaf"}]}
        ]
    },
    "commercialization-of-indian-agriculture": {
        "en": [
            {"label": "Nature of Shift", "type": "branch", "date": "19th Century", "children": [
                {"label": "Transition from subsistence food crops (rice, wheat) to commercial cash crops (indigo, cotton, opium, tea, jute)", "type": "leaf"},
                {"label": "Driven by British industrial demands for raw materials and EIC's need to balance trade with China (opium)", "type": "leaf"}]},
            {"label": "Mechanisms of Exploitation", "type": "branch", "date": "19th Century", "children": [
                {"label": "Dadni System: Forceful advance payments to peasants, locking them into low-price cultivation contracts", "type": "leaf"},
                {"label": "High land revenue obligations forced peasants to sell harvest immediately to local moneylenders at throwaway prices", "type": "leaf"}]},
            {"label": "Severe Impact", "type": "branch", "date": "19th Century", "children": [
                {"label": "Reduced availability of food grain reserves, leading to high frequency of artificial famines", "type": "leaf"},
                {"label": "Farmers became vulnerable to international price crashes (e.g. Cotton crash post American Civil War)", "type": "leaf"}]}
        ],
        "hi": [
            {"label": "बदलाव की प्रकृति", "type": "branch", "date": "19वीं सदी", "children": [
                {"label": "जीवन निर्वाह फसलों (चावल, गेहूं) से व्यावसायिक नकदी फसलों (नील, कपास, अफीम, चाय, जूट) में संक्रमण", "type": "leaf"},
                {"label": "कच्चे माल के लिए ब्रिटिश औद्योगिक मांगों और चीन के साथ व्यापार संतुलन (अफीम) की EIC की आवश्यकता से प्रेरित", "type": "leaf"}]},
            {"label": "शोषण के तंत्र", "type": "branch", "date": "19वीं सदी", "children": [
                {"label": "ददनी प्रणाली: किसानों को जबरन अग्रिम भुगतान, जिससे उन्हें कम कीमत वाले खेती के अनुबंधों में बांधा गया", "type": "leaf"},
                {"label": "उच्च भू-राजस्व बाध्यताओं ने किसानों को स्थानीय साहूकारों को औने-पौने दामों पर तुरंत फसल बेचने के लिए मजबूर किया", "type": "leaf"}]},
            {"label": "गंभीर प्रभाव", "type": "branch", "date": "19वीं सदी", "children": [
                {"label": "खाद्यान्न भंडार की उपलब्धता में कमी आई, जिससे कृत्रिम अकालों की आवृत्ति बढ़ गई", "type": "leaf"},
                {"label": "किसान अंतर्राष्ट्रीय कीमतों में गिरावट (जैसे अमेरिकी गृहयुद्ध के बाद कपास संकट) के प्रति संवेदनशील हो गए", "type": "leaf"}]}
        ]
    },
    "critique-economic-drain": {
        "en": [
            {"label": "Conceptual Origin", "type": "branch", "date": "1867 Onward", "children": [
                {"label": "Dadabhai Naoroji formulated the 'Drain of Wealth' theory in his 1867 paper 'England's Debt to India'", "type": "leaf"},
                {"label": "Detailed in book 'Poverty and Un-British Rule in India' (1901) as systematic transfer of capital", "type": "leaf"}]},
            {"label": "Channels of Drain", "type": "branch", "date": "1867 Onward", "children": [
                {"label": "Home Charges: Expenses of India Office in London, pensions of civil/military officers, and guaranteed railway interest", "type": "leaf"},
                {"label": "Unilateral trade surplus where India exported massive resources without equivalent material return", "type": "leaf"}]},
            {"label": "Consequences", "type": "branch", "date": "1867 Onward", "children": [
                {"label": "Prevented capital accumulation within India, leaving the country dependent on foreign loans", "type": "leaf"},
                {"label": "Directly caused systemic poverty, industrial backwardness, and lack of developmental resources", "type": "leaf"}]}
        ],
        "hi": [
            {"label": "वैचारिक उत्पत्ति", "type": "branch", "date": "1867 से आगे", "children": [
                {"label": "दादाभाई नौरोजी ने अपने 1867 के पत्र 'इंग्लैंड्स डेट टू इंडिया' में 'धन की निकासी' का सिद्धांत प्रतिपादित किया", "type": "leaf"},
                {"label": "पूंजी के व्यवस्थित हस्तांतरण के रूप में 'पॉवर्टी एंड अन-ब्रिटिश रूल इन इंडिया' (1901) पुस्तक में विस्तृत रूप से प्रस्तुत किया", "type": "leaf"}]},
            {"label": "निकासी के माध्यम", "type": "branch", "date": "1867 से आगे", "children": [
                {"label": "गृह प्रभार (Home Charges): लंदन में इंडिया ऑफिस के खर्च, सिविल/सैन्य अधिकारियों की पेंशन और गारंटीकृत रेलवे ब्याज", "type": "leaf"},
                {"label": "एकतरफा व्यापार अधिशेष जहां भारत ने बिना किसी समकक्ष भौतिक रिटर्न के भारी मात्रा में संसाधनों का निर्यात किया", "type": "leaf"}]},
            {"label": "दुष्परिणाम", "type": "branch", "date": "1867 से आगे", "children": [
                {"label": "भारत के भीतर पूंजी संचय को रोका, जिससे देश विदेशी ऋणों पर निर्भर हो गया", "type": "leaf"},
                {"label": "सीधे तौर पर प्रणालीगत गरीबी, औद्योगिक पिछड़ेपन और विकासात्मक संसाधनों की कमी का कारण बना", "type": "leaf"}]}
        ]
    },
    "critique-of-the-colonial-economy": {
        "en": [
            {"label": "Colonial Trade Pattern", "type": "branch", "date": "Colonial Economy", "children": [
                {"label": "Forced role as raw material supplier (cotton, jute, wheat) and captive consumer of British finished goods", "type": "leaf"},
                {"label": "One-Way Free Trade: Abolished import duties on British textiles while imposing high tariffs on Indian goods", "type": "leaf"}]},
            {"label": "Fiscal Policy", "type": "branch", "date": "Colonial Economy", "children": [
                {"label": "High land revenue taxation combined with regressive salt tax burdened the poorest populations", "type": "leaf"},
                {"label": "State expenditure skewed: over 50% spent on military campaigns, police, and administration, ignoring development", "type": "leaf"}]}
        ],
        "hi": [
            {"label": "औपनिवेशिक व्यापार प्रारूप", "type": "branch", "date": "औपनिवेशिक अर्थव्यवस्था", "children": [
                {"label": "कच्चे माल के आपूर्तिकर्ता (कपास, जूट, गेहूं) और ब्रिटिश तैयार माल के बंदी उपभोक्ता के रूप में मजबूर भूमिका", "type": "leaf"},
                {"label": "एकतरफा मुक्त व्यापार: भारतीय वस्तुओं पर उच्च शुल्क लगाते हुए ब्रिटिश वस्त्रों पर आयात शुल्क समाप्त कर दिया", "type": "leaf"}]},
            {"label": "राजकोषीय नीति", "type": "branch", "date": "औपनिवेशिक अर्थव्यवस्था", "children": [
                {"label": "दमनकारी नमक कर के साथ मिलकर उच्च भू-राजस्व कराधान ने सबसे गरीब आबादी पर बोझ डाला", "type": "leaf"},
                {"label": "राज्य का खर्च असंतुलित था: विकास की उपेक्षा करते हुए 50% से अधिक सैन्य अभियानों, पुलिस और प्रशासन पर खर्च किया गया", "type": "leaf"}]}
        ]
    },
    "development-of-modern-industry": {
        "en": [
            {"label": "Early Initiatives", "type": "branch", "date": "Modern Industry", "children": [
                {"label": "First cotton textile mill in Bombay (1854) by Kawasjee Nanabhoy Davar; first jute mill in Rishra, Bengal (1855)", "type": "leaf"},
                {"label": "Plantation industries (tea, coffee, indigo) grew early, largely owned by European capital", "type": "leaf"}]},
            {"label": "Indigenous Enterprise", "type": "branch", "date": "Modern Industry", "children": [
                {"label": "Establishment of Tata Iron and Steel Company (TISCO) in 1907 at Sakchi (Jamshedpur) by Jamsetji Tata", "type": "leaf"},
                {"label": "Swadeshi Movement (1905) gave push to Indian-owned banks, insurance companies, and soap factories", "type": "leaf"}]},
            {"label": "Colonial Constraints", "type": "branch", "date": "Modern Industry", "children": [
                {"label": "Managing Agency System: British syndicates controlled finance and operations of Indian enterprises", "type": "leaf"},
                {"label": "Complete neglect of heavy capital goods industries, keeping India technologically dependent on Britain", "type": "leaf"}]}
        ],
        "hi": [
            {"label": "प्रारंभिक पहल", "type": "branch", "date": "आधुनिक उद्योग", "children": [
                {"label": "कावसजी नानाभाई डावर द्वारा बॉम्बे में पहली सूती कपड़ा मिल (1854); बंगाल के रिशरा में पहली जूट मिल (1855)", "type": "leaf"},
                {"label": "बागान उद्योग (चाय, कॉफी, नील) जल्दी बढ़े, जिन पर मुख्य रूप से यूरोपीय पूंजी का स्वामित्व था", "type": "leaf"}]},
            {"label": "स्वदेशी उद्यम", "type": "branch", "date": "आधुनिक उद्योग", "children": [
                {"label": "जमशेदजी टाटा द्वारा 1907 में साक्षी (जमशेदपुर) में टाटा आयरन एंड स्टील कंपनी (TISCO) की स्थापना", "type": "leaf"},
                {"label": "स्वदेशी आंदोलन (1905) ने भारतीय स्वामित्व वाले बैंकों, बीमा कंपनियों और साबुन कारखानों को बढ़ावा दिया", "type": "leaf"}]},
            {"label": "औपनिवेशिक बाधाएं", "type": "branch", "date": "आधुनिक उद्योग", "children": [
                {"label": "प्रबंध एजेंसी प्रणाली (Managing Agency System): ब्रिटिश सिंडिकेट भारतीय उद्यमों के वित्त और संचालन को नियंत्रित करते थे", "type": "leaf"},
                {"label": "भारी पूंजीगत सामान उद्योगों की पूर्ण उपेक्षा की गई, जिससे भारत तकनीकी रूप से ब्रिटेन पर निर्भर रहा", "type": "leaf"}]}
        ]
    },
    "emergence-of-new-land-relations-ruin-of-old-zamindars": {
        "en": [
            {"label": "New Land Concepts", "type": "branch", "date": "Land Relations", "children": [
                {"label": "Introduced private property in land, making it alienable, mortgageable, and saleable for revenue default", "type": "leaf"},
                {"label": "Replaced customary rights of occupancy with contractual relations, weakening peasant security", "type": "leaf"}]},
            {"label": "Ruin of Traditional Elites", "type": "branch", "date": "Land Relations", "children": [
                {"label": "Sunset Law: Mandated revenue payment by sunset on due date; default led to auction of estates", "type": "leaf"},
                {"label": "Over 50% of Bengal's traditional Zamindaris changed hands in the decade following the 1793 settlement", "type": "leaf"}]},
            {"label": "Rise of Absentee Landlords", "type": "branch", "date": "Land Relations", "children": [
                {"label": "Urban merchants, moneylenders, and EIC officials bought auctioned estates", "type": "leaf"},
                {"label": "Sub-infeudation: Creation of long chains of middle-men (Patnidars) who squeezed peasants for rent", "type": "leaf"}]}
        ],
        "hi": [
            {"label": "नई भूमि अवधारणाएं", "type": "branch", "date": "भूमि संबंध", "children": [
                {"label": "भूमि में निजी संपत्ति की शुरुआत की, जिससे यह राजस्व चूक के लिए हस्तांतरणीय और बिक्री योग्य बन गई", "type": "leaf"},
                {"label": "कब्जे के पारंपरिक अधिकारों को संविदात्मक संबंधों से बदल दिया, जिससे किसानों की सुरक्षा कमजोर हुई", "type": "leaf"}]},
            {"label": "पारंपरिक अभिजात वर्ग की बर्बादी", "type": "branch", "date": "भूमि संबंध", "children": [
                {"label": "सूर्यास्त कानून (Sunset Law): नियत तिथि पर सूर्यास्त तक राजस्व भुगतान अनिवार्य; चूक होने पर जागीरों की नीलामी हुई", "type": "leaf"},
                {"label": "1793 के बंदोबस्त के बाद के दशक में बंगाल की 50% से अधिक पारंपरिक जमींदारियां अन्य हाथों में चली गईं", "type": "leaf"}]},
            {"label": "अनुपस्थित जमींदारों का उदय", "type": "branch", "date": "भूमि संबंध", "children": [
                {"label": "शहरी व्यापारियों, साहूकारों और EIC अधिकारियों ने नीलाम की गई जागीरों को खरीदा", "type": "leaf"},
                {"label": "उपनिवेशीकरण (Sub-infeudation): बिचौलियों (पटनीदारों) की लंबी श्रृंखलाओं का निर्माण जिन्होंने किराए के लिए किसानों को निचोड़ा", "type": "leaf"}]}
        ]
    },
    "famine-and-poverty": {
        "en": [
            {"label": "Famine Frequency", "type": "branch", "date": "Famines", "children": [
                {"label": "Major famines: Bengal Famine (1770), Great Famine of 1876-78 (Southern India), Bengal Famine of 1943", "type": "leaf"},
                {"label": "Famines were not due to lack of food, but lack of purchasing power and export of grain during distress", "type": "leaf"}]},
            {"label": "Famine Commissions", "type": "branch", "date": "Famines", "children": [
                {"label": "Strachey Commission (1880): Recommended Famine Code; proposed providing employment on public works", "type": "leaf"},
                {"label": "Lyall Commission (1897) & MacDonnell Commission (1901): Advocated moral check, village relief, and agricultural banks", "type": "leaf"}]},
            {"label": "Colonial Response", "type": "branch", "date": "Famines", "children": [
                {"label": "Laissez-faire policy: Refused to regulate food prices or ban food grain exports during famines", "type": "leaf"},
                {"label": "Relief works were highly punitive, offering starvation-level wages to prevent 'dependency'", "type": "leaf"}]}
        ],
        "hi": [
            {"label": "अकालों की आवृत्ति", "type": "branch", "date": "अकाल और गरीबी", "children": [
                {"label": "प्रमुख अकाल: बंगाल अकाल (1770), 1876-78 का महान अकाल (दक्षिण भारत), 1943 का बंगाल अकाल", "type": "leaf"},
                {"label": "अकाल भोजन की कमी के कारण नहीं, बल्कि क्रय शक्ति की कमी और संकट के दौरान अनाज के निर्यात के कारण थे", "type": "leaf"}]},
            {"label": "अकाल आयोग", "type": "branch", "date": "अकाल और गरीबी", "children": [
                {"label": "स्ट्रेची आयोग (1880): अकाल संहिता की सिफारिश की; सार्वजनिक कार्यों पर रोजगार प्रदान करने का प्रस्ताव दिया", "type": "leaf"},
                {"label": "लायल आयोग (1897) और मैकडोनेल आयोग (1901): ग्रामीण राहत और कृषि बैंकों की वकालत की", "type": "leaf"}]},
            {"label": "औपनिवेशिक प्रतिक्रिया", "type": "branch", "date": "अकाल और गरीबी", "children": [
                {"label": "हस्तक्षेप न करने की नीति (Laissez-faire): अकालों के दौरान खाद्य कीमतों को विनियमित करने या खाद्यान्न निर्यात पर प्रतिबंध लगाने से इनकार कर दिया", "type": "leaf"},
                {"label": "राहत कार्य अत्यधिक दंडात्मक थे, जो 'निर्भरता' को रोकने के लिए भुखमरी के स्तर की मजदूरी की पेशकश करते थे", "type": "leaf"}]}
        ]
    },
    "impoverishment-of-peasantry": {
        "en": [
            {"label": "Revenue Demands", "type": "branch", "date": "Peasantry", "children": [
                {"label": "Exorbitant initial revenue rates set under Permanent, Ryotwari, and Mahalwari systems", "type": "leaf"},
                {"label": "Cash payment requirement forced peasants to sell crops immediately when prices were lowest", "type": "leaf"}]},
            {"label": "Debt & Eviction", "type": "branch", "date": "Peasantry", "children": [
                {"label": "Peasants fell into clutches of local moneylenders (Mahajans) to pay taxes, leading to debt slavery", "type": "leaf"},
                {"label": "Widespread evictions for non-payment converted independent cultivators into landless laborers", "type": "leaf"}]}
        ],
        "hi": [
            {"label": "राजस्व मांगें", "type": "branch", "date": "कृषक वर्ग", "children": [
                {"label": "स्थायी, रैयतवाड़ी और महलवाड़ी प्रणालियों के तहत अत्यधिक प्रारंभिक राजस्व दरें निर्धारित की गईं", "type": "leaf"},
                {"label": "नकद भुगतान की आवश्यकता ने किसानों को फसल तुरंत बेचने के लिए मजबूर किया जब कीमतें सबसे कम थीं", "type": "leaf"}]},
            {"label": "ऋण और बेदखली", "type": "branch", "date": "कृषक वर्ग", "children": [
                {"label": "कर चुकाने के लिए किसान स्थानीय साहूकारों (महाजनों) के चंगुल में फंस गए, जिससे ऋण दासता शुरू हुई", "type": "leaf"},
                {"label": "भुगतान न करने पर व्यापक बेदखली ने स्वतंत्र कृषकों को भूमिहीन मजदूरों में बदल दिया", "type": "leaf"}]}
        ]
    },
    "industrializationruin-of-artisans-and-handicrafts-men": {
        "en": [
            {"label": "De-industrialization Process", "type": "branch", "date": "Artisans", "children": [
                {"label": "Influx of cheap, machine-made cotton textiles from Lancashire ruined the domestic spinning and weaving industries", "type": "leaf"},
                {"label": "Enforced export of raw cotton starved local weavers of essential raw materials", "type": "leaf"}]},
            {"label": "Demise of Urban Crafts", "type": "branch", "date": "Artisans", "children": [
                {"label": "Disappearance of native princely courts destroyed the market for luxury crafts, silk, and weaponry", "type": "leaf"},
                {"label": "British shipping and transit duties discriminated against Indian-made goods in local and foreign markets", "type": "leaf"}]}
        ],
        "hi": [
            {"label": "वि-औद्योगिकीकरण की प्रक्रिया", "type": "branch", "date": "कारीगर", "children": [
                {"label": "लंकाशायर से सस्ते, मशीन-निर्मित सूती वस्त्रों के आयात ने घरेलू कताई और बुनाई उद्योगों को नष्ट कर दिया", "type": "leaf"},
                {"label": "कच्चे कपास के जबरन निर्यात ने स्थानीय बुनकरों को आवश्यक कच्चे माल से वंचित कर दिया", "type": "leaf"}]},
            {"label": "शहरी शिल्प का पतन", "type": "branch", "date": "कारीगर", "children": [
                {"label": "देशी रियासतों के गायब होने से विलासिता के शिल्प, रेशम और हथियारों का बाजार नष्ट हो गया", "type": "leaf"},
                {"label": "ब्रिटिश नौवहन और पारगमन शुल्कों ने स्थानीय और विदेशी बाजारों में भारतीय निर्मित वस्तुओं के साथ भेदभाव किया", "type": "leaf"}]}
        ]
    },
    "nationalist-critique-of-colonial-economy": {
        "en": [
            {"label": "Economic Thinkers", "type": "branch", "date": "Nationalists", "children": [
                {"label": "Led by Dadabhai Naoroji, Mahadev Govind Ranade, and Romesh Chandra Dutt (Economic History of India)", "type": "leaf"},
                {"label": "Provided data-backed analysis exposing that India's poverty was a modern colonial construct", "type": "leaf"}]},
            {"label": "Key Demands", "type": "branch", "date": "Nationalists", "children": [
                {"label": "Advocated for high protective tariffs to safeguard infant Indian industries from foreign competition", "type": "leaf"},
                {"label": "Demanded reduction in land revenue and military expenditure to ease peasant burden", "type": "leaf"}]}
        ],
        "hi": [
            {"label": "आर्थिक विचारक", "type": "branch", "date": "राष्ट्रवादी", "children": [
                {"label": "दादाभाई नौरोजी, महादेव गोविंद रानाडे और रमेश चंद्र दत्त (इकोनॉमिक हिस्ट्री ऑफ इंडिया) के नेतृत्व में", "type": "leaf"},
                {"label": "आंकड़ों पर आधारित विश्लेषण प्रदान किया जिससे पता चला कि भारत की गरीबी एक आधुनिक औपनिवेशिक निर्माण थी", "type": "leaf"}]},
            {"label": "मुख्य मांगें", "type": "branch", "date": "राष्ट्रवादी", "children": [
                {"label": "विदेशी प्रतिस्पर्धा से नवजात भारतीय उद्योगों की रक्षा के लिए उच्च सुरक्षात्मक टैरिफ की वकालत की", "type": "leaf"},
                {"label": "किसानों का बोझ कम करने के लिए भू-राजस्व और सैन्य खर्च में कमी की मांग की", "type": "leaf"}]}
        ]
    },
    "rise-of-indian-bourgeoisie": {
        "en": [
            {"label": "Emergence", "type": "branch", "date": "Bourgeoisie", "children": [
                {"label": "Accumulated capital as brokers (Dubashes), opium traders, and cotton exporters to China and Britain", "type": "leaf"},
                {"label": "Grew significantly during WWI and WWII due to supply disruptions and shipping shortages from Europe", "type": "leaf"}]},
            {"label": "Nationalist Alliance", "type": "branch", "date": "Bourgeoisie", "children": [
                {"label": "Supported the Indian National Congress financially and aligned with Swadeshi/Boycott campaigns", "type": "leaf"},
                {"label": "Prominent leaders like G.D. Birla and Purshottamdas Thakurdas actively backed Gandhi's programs", "type": "leaf"}]}
        ],
        "hi": [
            {"label": "उदय", "type": "branch", "date": "पूंजीपति वर्ग", "children": [
                {"label": "दलालों (दुभाषियों), अफीम व्यापारियों और चीन व ब्रिटेन को कपास निर्यातकों के रूप में पूंजी संचित की", "type": "leaf"},
                {"label": "यूरोप से आपूर्ति व्यवधानों और शिपिंग की कमी के कारण WWI और WWII के दौरान महत्वपूर्ण रूप से विकसित हुआ", "type": "leaf"}]},
            {"label": "राष्ट्रवादी गठबंधन", "type": "branch", "date": "पूंजीपति वर्ग", "children": [
                {"label": "भारतीय राष्ट्रीय कांग्रेस को आर्थिक रूप से समर्थन दिया और स्वदेशी/बहिष्कार अभियानों के साथ संरेखित किया", "type": "leaf"},
                {"label": "जी.डी. बिड़ला और पुरुषोत्तमदास ठाकुरदास जैसे प्रमुख नेताओं ने गांधी के कार्यक्रमों का सक्रिय रूप से समर्थन किया", "type": "leaf"}]}
        ]
    },
    "stagnation-and-deterioration-of-agriculture": {
        "en": [
            {"label": "Structural Factors", "type": "branch", "date": "Agriculture Stagnation", "children": [
                {"label": "Total lack of capital investment by the colonial state in irrigation, seed development, and fertilizers", "type": "leaf"},
                {"label": "Extreme fragmentation of landholdings due to de-industrialization forcing people back to land", "type": "leaf"}]},
            {"label": "State Neglect", "type": "branch", "date": "Agriculture Stagnation", "children": [
                {"label": "Government spent over 90% of development budget on railways (strategic reasons) rather than irrigation", "type": "leaf"},
                {"label": "Declining agricultural productivity per acre led to persistent crop failures and mass undernourishment", "type": "leaf"}]}
        ],
        "hi": [
            {"label": "संरचनात्मक कारक", "type": "branch", "date": "कृषि ठहराव", "children": [
                {"label": "सिंचाई, बीज विकास और उर्वरकों में औपनिवेशिक राज्य द्वारा पूंजी निवेश की पूर्ण कमी", "type": "leaf"},
                {"label": "वि-औद्योगिकीकरण के कारण जोतों का अत्यधिक विखंडन जिससे लोग वापस भूमि पर लौटने को मजबूर हुए", "type": "leaf"}]},
            {"label": "राज्य की उपेक्षा", "type": "branch", "date": "कृषि ठहराव", "children": [
                {"label": "सरकार ने सिंचाई के बजाय रेलवे (रणनीतिक कारणों) पर विकास बजट का 90% से अधिक खर्च किया", "type": "leaf"},
                {"label": "प्रति एकड़ गिरती कृषि उत्पादकता के कारण लगातार फसलें खराब हुईं और बड़े पैमाने पर कुपोषण फैला", "type": "leaf"}]}
        ]
    }
}

# Mapping folder variations to canonical keys
MINDMAP_MAPPINGS = {
    "abolition-of-the-dual-system": "abolition-of-the-dual-system",
    "changes-in-social-setup": "changes-in-social-setup",
    "commercialization-of-indian-agriculture": "commercialization-of-indian-agriculture",
    "critique-economic-drain": "critique-economic-drain",
    "critique-of-the-colonial-economy": "critique-of-the-colonial-economy",
    "development-of-modern-industry": "development-of-modern-industry",
    "emergence-of-new-land-relations-ruin-of-old-zamindars": "emergence-of-new-land-relations-ruin-of-old-zamindars",
    "famine-and-poverty": "famine-and-poverty",
    "impoverishment-of-peasantry": "impoverishment-of-peasantry",
    "industrializationruin-of-artisans-and-handicrafts-men": "industrializationruin-of-artisans-and-handicrafts-men",
    "nationalist-critique-of-colonial-economy": "nationalist-critique-of-colonial-economy",
    "rise-of-indian-bourgeoisie": "rise-of-indian-bourgeoisie",
    "stagnation-and-deterioration-of-agriculture": "stagnation-and-deterioration-of-agriculture"
}

def get_clean_title(folder_name):
    title = folder_name.replace('-', ' ')
    title = title.replace('INC', 'INC (Indian National Congress)')
    title = title.replace('IndustrializationRuin', 'Industrialization & Ruin')
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
    canonical_key = MINDMAP_MAPPINGS.get(key, "abolition-of-the-dual-system")
    
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
