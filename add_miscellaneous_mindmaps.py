#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import re
import json

BASE = r"upsc/art_and_culture/Miscellaneous"

def get_clean_title(folder_name):
    title = folder_name.replace('-', ' ')
    words = []
    acronyms = {'upsc', 'ad', 'bc', 'ii', 'iii', 'unesco', 'gi', 'wto', 'trips', 'asi', 'amasr', 'gst'}
    for w in title.split():
        if w.lower() in acronyms:
            words.append(w.upper())
        elif w.lower() in ['of', 'and', 'the', 'for', 'in', 'with', 'against', 'to', 'on', 'some', 'by', 'between', 'or']:
            words.append(w.lower())
        else:
            words.append(w.capitalize())
    return ' '.join(words)

def get_custom_branches(folder_name, is_hindi):
    fl = folder_name.lower()

    # 1. GI Tags
    if fl == 'gi-tags':
        if is_hindi:
            return [
                {"label": "परिभाषा और कानूनी ढांचा", "type": "branch", "date": "अधिनियम 1999", "children": [
                    {"label": "जीआई अधिनियम: भौगोलिक संकेत (पंजीकरण और संरक्षण) अधिनियम, 1999 द्वारा शासित; डब्ल्यूटीओ (WTO) के ट्रिप्स (TRIPS) समझौते के तहत लागू", "type": "leaf"},
                    {"label": "जीआई रजिस्ट्री: इसका मुख्यालय चेन्नई में है; पंजीकरण 10 वर्षों के लिए वैध होता है (नवीकरणीय)", "type": "leaf"}
                ]},
                {"label": "प्रमुख वर्गीकरण", "type": "branch", "date": "वर्गीकरण", "children": [
                    {"label": "कृषि: दार्जिलिंग चाय (भारत का पहला जीआई उत्पाद, 2004), बासमती चावल, अलफांसो आम", "type": "leaf"},
                    {"label": "हस्तशिल्प: मैसूर सिल्क (कर्नाटक), अरनमुला कन्नड़ी (धातु दर्पण, केरल), बस्तर लौह शिल्प (छत्तीसगढ़)", "type": "leaf"},
                    {"label": "खाद्य सामग्री: हैदराबादी हलीम (तेलंगाना), धारवाड़ पेड़ा (कर्नाटक), रसगुल्ला (ओडिशा/पश्चिम बंगाल)", "type": "leaf"}
                ]}
            ]
        else:
            return [
                {"label": "Legal & Administrative Framework", "type": "branch", "date": "Act 1999", "children": [
                    {"label": "GI Act: Governed by the Geographical Indications of Goods (Registration & Protection) Act, 1999, aligned with WTO TRIPS", "type": "leaf"},
                    {"label": "GI Registry: Located in Chennai; registrations are valid for 10 years and renewable thereafter", "type": "leaf"}
                ]},
                {"label": "UPSC Core Classifications", "type": "branch", "date": "Categories", "children": [
                    {"label": "Agricultural: Darjeeling Tea (India's 1st GI, 2004), Basmati Rice, Alphonso Mangoes", "type": "leaf"},
                    {"label": "Handicrafts: Mysore Silk (Karnataka), Aranmula Kannadi (metal alloy mirrors of Kerala), Bastar Iron Craft (Chhattisgarh)", "type": "leaf"},
                    {"label": "Foodstuffs: Hyderabadi Haleem, Dharwad Pedha, Tirupati Laddu, and regional Rosogolla varieties", "type": "leaf"}
                ]}
            ]

    # 2. Government Cultural Institutions in India
    elif fl == 'government-cultural-institutions-in-india':
        if is_hindi:
            return [
                {"label": "राष्ट्रीय कला अकादमियाँ", "type": "branch", "date": "अकादमियाँ", "children": [
                    {"label": "साहित्य अकादमी: भारत की राष्ट्रीय साहित्यिक संस्था; 24 मान्यता प्राप्त भाषाओं में साहित्य का संवर्धन करती है", "type": "leaf"},
                    {"label": "संगीत नाटक अकादमी (1953): संगीत, नृत्य और नाटक की राष्ट्रीय संस्था; उस्ताद बिस्मिल्लाह खान युवा पुरस्कार देती है", "type": "leaf"},
                    {"label": "ललित कला अकादमी (1954): चित्रकला, मूर्तिकला और वास्तुकला जैसे दृश्य कला रूपों को बढ़ावा देने की राष्ट्रीय संस्था", "type": "leaf"}
                ]},
                {"label": "सर्वेक्षण और संरक्षण निकाय", "type": "branch", "date": "सरकारी विभाग", "children": [
                    {"label": "भारतीय पुरातत्व सर्वेक्षण (ASI): 1861 में अलेक्जेंडर कनिंघम द्वारा स्थापित; राष्ट्रीय महत्व के स्मारकों का संरक्षण", "type": "leaf"},
                    {"label": "राष्ट्रीय अभिलेखागार (NAI): भारत सरकार के गैर-सामयिक दस्तावेजों और पांडुलिपियों का मुख्य संरक्षक", "type": "leaf"}
                ]}
            ]
        else:
            return [
                {"label": "Three National Akademis", "type": "branch", "date": "Akademis", "children": [
                    {"label": "Sahitya Akademi: Promotes literature across 24 recognized languages (22 Scheduled + English & Rajasthani)", "type": "leaf"},
                    {"label": "Sangeet Natak Akademi: Est. 1953; apex body preserving classical music, diverse dances, and traditional puppetry", "type": "leaf"},
                    {"label": "Lalit Kala Akademi: Est. 1954; national academy of fine arts promoting sculpture, graphic arts, and painting exhibitions", "type": "leaf"}
                ]},
                {"label": "Survey & Archive Bodies", "type": "branch", "date": "Conservation", "children": [
                    {"label": "ASI (Archaeological Survey of India): Founded in 1861 by Alexander Cunningham; protects 3,600+ national monuments", "type": "leaf"},
                    {"label": "National Archives of India: Official repository of historical manuscripts, treaty logs, and public records", "type": "leaf"}
                ]}
            ]

    # 3. Personalities Related to Culture
    elif fl == 'personalities-related-to-culture':
        if is_hindi:
            return [
                {"label": "संस्कृति पुनरुद्धारकर्ता और विद्वान", "type": "branch", "date": "पुनरुद्धार", "children": [
                    {"label": "रुक्मिणी देवी अरुंडेल: भरतनाट्यम को देवदासी प्रथा से बाहर निकालकर कुलीन वर्ग में लोकप्रिय बनाया; कलाक्षेत्र (Kalakshetra) की स्थापना की", "type": "leaf"},
                    {"label": "रवींद्रनाथ टैगोर: विश्व भारती (शांतिनिकेतन) की स्थापना; पूर्वी और पश्चिमी कलाओं का एकीकरण कर आधुनिक शैलियों को बढ़ावा दिया", "type": "leaf"},
                    {"label": "पंडित भातखंडे: हिंदुस्तानी संगीत की थॉट (Thaat) पद्धति का वर्गीकरण किया, जिससे संगीत शिक्षा का मानकीकरण हुआ", "type": "leaf"}
                ]},
                {"label": "कला व सिनेमा के अग्रदूत", "type": "branch", "date": "कलाकार", "children": [
                    {"label": "राजा रवि वर्मा: लिथोग्राफी प्रेस स्थापित की; हिंदू देवी-देवताओं को तैल चित्रों (Oil Painting) के माध्यम से जन-जन तक पहुँचाया", "type": "leaf"},
                    {"label": "अमृता शेर-गिल: भारतीय ग्रामीण विषयों को पश्चिमी आधुनिक शैली (Post-Impressionism) के साथ चित्रित करने वाली महान चित्रकार", "type": "leaf"},
                    {"label": "सत्यजीत रे: यथार्थवादी समानांतर सिनेमा के जनक; 'पथेर पांचाली' के लिए ऑस्कर लाइफटाइम अचीवमेंट पुरस्कार जीता", "type": "leaf"}
                ]}
            ]
        else:
            return [
                {"label": "Cultural Revivalists & Scholars", "type": "branch", "date": "Revival", "children": [
                    {"label": "Rukmini Devi Arundale: Saved Sadir Bharatanatyam from stigma; founded Kalakshetra academy of fine arts", "type": "leaf"},
                    {"label": "Rabindranath Tagore: Blended indigenous and Western arts at Santiniketan; first Asian Nobel Laureate in Literature", "type": "leaf"},
                    {"label": "V.N. Bhatkhande: Formulated the 10-Thaat classification system, standardizing Hindustani classical notation", "type": "leaf"}
                ]},
                {"label": "Pioneering Modern Artists", "type": "branch", "date": "Artists", "children": [
                    {"label": "Raja Ravi Varma: Introduced European oil techniques to render Hindu mythological themes, setting up litho presses", "type": "leaf"},
                    {"label": "Amrita Sher-Gil: Blended Western Post-Impressionism with Ajanta-style contours, capturing rural Indian subjects", "type": "leaf"},
                    {"label": "Satyajit Ray: Brought Indian cinema to international fame through the realist social themes of the Apu Trilogy", "type": "leaf"}
                ]}
            ]

    # 4. Places of Cultural Interest
    elif fl == 'places-of-cultural-interest':
        if is_hindi:
            return [
                {"label": "प्रमुख ऐतिहासिक व स्थापत्य स्थल", "type": "branch", "date": "विरासत स्थल", "children": [
                    {"label": "महाबलीपुरम (TN): पल्लव राजवंश के एकाश्म रथ मंदिर, शोर टेंपल और प्रसिद्ध 'गंगा अवतरण' शैलकृत पैनल", "type": "leaf"},
                    {"label": "हम्पी (कर्नाटक): विजयनगर साम्राज्य के खंडहर; प्रसिद्ध विट्ठल मंदिर (पत्थर का रथ, संगीत वाले खंभे)", "type": "leaf"},
                    {"label": "खजुराहो (MP): चंदेल शासकों द्वारा निर्मित नागर शैली के मंदिर; जटिल कामुक मूर्तियां; पंचायतन विन्यास", "type": "leaf"}
                ]},
                {"label": "आध्यात्मिक और व्यापारिक नगर", "type": "branch", "date": "सांस्कृतिक नगर", "children": [
                    {"label": "वाराणसी (UP): गंगा नदी के किनारे बसा प्राचीन जीवंत शहर, जो हिंदू दर्शन, संगीत (बनारस घराना) और घाटों के लिए प्रसिद्ध है", "type": "leaf"},
                    {"label": "मदुरै (TN): मीनाक्षी सुंदरेश्वर मंदिर के चारों ओर बसा कमल के आकार का प्राचीन द्रविड़ शहर", "type": "leaf"}
                ]}
            ]
        else:
            return [
                {"label": "Architectural & Historical Hubs", "type": "branch", "date": "Heritage", "children": [
                    {"label": "Mahabalipuram (TN): Pallava rock reliefs (Descent of the Ganges) and shore temples made of granite block masonry", "type": "leaf"},
                    {"label": "Hampi (Karnataka): Capital of Vijayanagara empire; features Virupaksha temple and musical stone pillars", "type": "leaf"},
                    {"label": "Khajuraho (MP): Chandela Nagara-style temples constructed on high plinths, exhibiting intricate outer-wall friezes", "type": "leaf"}
                ]},
                {"label": "Historic Civic Centres", "type": "branch", "date": "Cities", "children": [
                    {"label": "Varanasi (UP): Ancient spiritual center on Ganges banks, home of Sanskrit learning and the Banaras musical gharana", "type": "leaf"},
                    {"label": "Madurai (TN): Plan shaped as a lotus blossom surrounding the central Meenakshi-Sundareswarar Dravidian temple complex", "type": "leaf"}
                ]}
            ]

    # 5. Protection and Promotion of Indian Culture and Heritage
    elif fl == 'protection-and-promotion-of-indian-culture-and-heritage':
        if is_hindi:
            return [
                {"label": "संवैधानिक व कानूनी प्रावधान", "type": "branch", "date": "कानून", "children": [
                    {"label": "अनुच्छेद 49 (DPSP): कलात्मक या ऐतिहासिक रुचि के स्मारकों, स्थानों और वस्तुओं के संरक्षण का राज्य का दायित्व", "type": "leaf"},
                    {"label": "अनुच्छेद 51A(f) (मौलिक कर्तव्य): हमारी मिश्रित संस्कृति की समृद्ध विरासत को महत्व देना और उसका संरक्षण करना", "type": "leaf"},
                    {"label": "AMASR अधिनियम 1958: प्राचीन स्मारकों, पुरातात्विक स्थलों और राष्ट्रीय महत्व के अवशेषों के संरक्षण का नियमन करता है", "type": "leaf"}
                ]},
                {"label": "राष्ट्रीय मिशन और योजनाएं", "type": "branch", "date": "सरकारी योजनाएं", "children": [
                    {"label": "राष्ट्रीय स्मारक और पुरावशेष मिशन (NMMA): भारत के पुरावशेषों का एक डेटाबेस तैयार करना ताकि चोरी को रोका जा सके", "type": "leaf"},
                    {"label": "अमूर्त सांस्कृतिक विरासत (ICH) योजना: लोक कलाओं, मौखिक परंपराओं और दुर्लभ शिल्पों के कलाकारों को वित्तीय अनुदान देना", "type": "leaf"}
                ]}
            ]
        else:
            return [
                {"label": "Constitutional & Legislative Safeguards", "type": "branch", "date": "Law", "children": [
                    {"label": "Article 49 (DPSP): Obligation of the state to protect national monuments, objects, and places of historical value", "type": "leaf"},
                    {"label": "Article 51A(f) (Duties): Fundamental Duty of citizens to value and preserve the rich heritage of composite culture", "type": "leaf"},
                    {"label": "AMASR Act 1958: Regulates archaeological excavations and protects ancient ruins and historic sites", "type": "leaf"}
                ]},
                {"label": "State Missions & Initiatives", "type": "branch", "date": "Initiatives", "children": [
                    {"label": "NMMA Mission: Establishes national inventory of antiquities, tracing records to prevent smuggling", "type": "leaf"},
                    {"label": "ICH Scheme: Focuses on safeguarding oral expressions, performing arts, and traditional crafts via financial grants", "type": "leaf"}
                ]}
            ]

    # 6. Recent Developments related to Art Culture
    elif fl == 'recent-developments-related-to-art-culture':
        if is_hindi:
            return [
                {"label": "नवीनतम स्मारक और संग्रहालय", "type": "branch", "date": "नवीनतम विकास", "children": [
                    {"label": "पीएम संग्रहालय (दिल्ली): भारत के सभी प्रधानमंत्रियों के जीवन और योगदान को दर्शाने वाला आधुनिक डिजिटल संग्रहालय", "type": "leaf"},
                    {"label": "होयसल पवित्र मंदिर (2023): बेलूर, हेलेबिडु और सोमनाथपुरा के होयसल मंदिरों को यूनेस्को की विश्व धरोहर सूची में शामिल किया गया", "type": "leaf"},
                    {"label": "शांतिनिकेतन (2023): रवींद्रनाथ टैगोर द्वारा स्थापित कला और शिक्षा केंद्र को यूनेस्को विरासत घोषित किया गया", "type": "leaf"}
                ]},
                {"label": "डिजिटल संरक्षण व प्राचीन वस्तुओं की घर वापसी", "type": "branch", "date": "प्रौद्योगिकी", "children": [
                    {"label": "एंटीक्विटी रिपैट्रिएशन: विदेशों (जैसे यूएसए, यूके, ऑस्ट्रेलिया) से चुराई गई प्राचीन मूर्तियों (जैसे चोल कांस्य) को भारत वापस लाया गया", "type": "leaf"},
                    {"label": "भारत की राष्ट्रीय वर्चुअल लाइब्रेरी (NVLI): सांस्कृतिक पांडुलिपियों, अभिलेखों और ऐतिहासिक दस्तावेजों का डिजिटल हब", "type": "leaf"}
                ]}
            ]
        else:
            return [
                {"label": "New Inscriptions & Museums", "type": "branch", "date": "Developments", "children": [
                    {"label": "Pradhanmantri Sangrahalaya: Interactive digital museum detailing lives of all Indian PMs since independence", "type": "leaf"},
                    {"label": "Hoysala Temples (2023): Sacred ensembles of Belur, Halebidu, and Somanathapura added to UNESCO list", "type": "leaf"},
                    {"label": "Santiniketan (2023): Rabindranath Tagore's unique open-air school and art center inscribed as UNESCO site", "type": "leaf"}
                ]},
                {"label": "Digitization & Antiquity Return", "type": "branch", "date": "Digital/Return", "children": [
                    {"label": "Repatriation: Recovery of stolen cultural icons, returning Chola bronzes and temple relics from Western collections", "type": "leaf"},
                    {"label": "National Virtual Library (NVLI): Integrates digital archives of museums, ASI logs, and libraries on one platform", "type": "leaf"}
                ]}
            ]

    # 7. Schemes and Awards
    elif fl == 'schemes-and-awards':
        if is_hindi:
            return [
                {"label": "राष्ट्रीय सांस्कृतिक पुरस्कार", "type": "branch", "date": "पुरस्कार", "children": [
                    {"label": "ज्ञानपीठ पुरस्कार: भारत का सर्वोच्च साहित्यिक सम्मान; भारतीय लेखकों को उत्कृष्ट साहित्यिक योगदान हेतु दिया जाता है", "type": "leaf"},
                    {"label": "साहित्य अकादमी पुरस्कार: 24 भाषाओं के उत्कृष्ट लेखकों को दिया जाता है; तांबे की पट्टिका प्रदान की जाती है", "type": "leaf"},
                    {"label": "संगीत नाटक अकादमी फेलोशिप: प्रदर्शन कला क्षेत्र का सर्वोच्च सम्मान; असाधारण योगदान देने वाले गुरुओं को दिया जाता है", "type": "leaf"}
                ]},
                {"label": "प्रमुख सरकारी योजनाएं", "type": "branch", "date": "योजनाएं", "children": [
                    {"label": "सेवा भोज योजना: मुफ्त भोजन (लंगर/प्रसाद) परोसने वाले धर्मार्थ धार्मिक संस्थानों को कच्चे माल पर केंद्रीय जीएसटी प्रतिपूर्ति प्रदान करना", "type": "leaf"},
                    {"label": "कला संस्कृति विकास योजना (KSVY): विभिन्न लोक नृत्य, नाटक और कला मेलों के कलाकारों को वित्तीय सहायता", "type": "leaf"}
                ]}
            ]
        else:
            return [
                {"label": "Apex National Awards", "type": "branch", "date": "Awards", "children": [
                    {"label": "Jnanpith Award: Highest literary award in India, honoring writers for their life-long contributions", "type": "leaf"},
                    {"label": "Sahitya Akademi Award: Presented annually for outstanding books of literary merit published in 24 languages", "type": "leaf"},
                    {"label": "Sangeet Natak Akademi Fellowship: Premium honor recognizing lifetime achievement in classical music, dance, and theatre", "type": "leaf"}
                ]},
                {"label": "Promotional Schemes", "type": "branch", "date": "Schemes", "children": [
                    {"label": "Seva Bhoj Yojna: Reimburses CGST/IGST paid on raw food inputs by non-profit religious organizations providing free food", "type": "leaf"},
                    {"label": "Kala Sanskriti Vikas Yojana: Umbrella scheme providing financial assistance to artists, theatres, and cultural research projects", "type": "leaf"}
                ]}
            ]

    # 8. Schemes for Monument Development
    elif fl == 'schemes-for-monument-development':
        if is_hindi:
            return [
                {"label": "धरोहर गोद लें योजना और हृदय", "type": "branch", "date": "पर्यटन विकास", "children": [
                    {"label": "धरोहर गोद लें (Adopt a Monument): निजी/सार्वजनिक कंपनियों ('स्मारक मित्र') को पर्यटन सुविधाएं (पेयजल, वाई-फाई, शौचालय) विकसित करने के लिए स्मारक सौंपना", "type": "leaf"},
                    {"label": "हृदय (HRIDAY) योजना: ऐतिहासिक शहरों की आत्मा को संरक्षित करते हुए बुनियादी ढांचे का एकीकृत विकास करना", "type": "leaf"}
                ]},
                {"label": "प्रसाद और स्वदेश दर्शन", "type": "branch", "date": "पर्यटन सर्किट", "children": [
                    {"label": "प्रसाद (PRASHAD): चुनिंदा तीर्थ स्थलों का कायाकल्प और आध्यात्मिक संवर्धन; पर्यटन मंत्रालय द्वारा वित्तपोषित", "type": "leaf"},
                    {"label": "स्वदेश दर्शन: विषय-आधारित (Theme-based) पर्यटन सर्किटों का विकास; जैसे बौद्ध सर्किट, रामायण सर्किट, हिमालयी सर्किट", "type": "leaf"}
                ]}
            ]
        else:
            return [
                {"label": "Adopt a Monument & HRIDAY", "type": "branch", "date": "Development", "children": [
                    {"label": "Adopt a Monument: Corporate entities ('Monument Mitras') build and manage tourist amenities under CSR funding", "type": "leaf"},
                    {"label": "HRIDAY Scheme: Focuses on holistic development of heritage cities, preserving urban aesthetic identity", "type": "leaf"}
                ]},
                {"label": "PRASHAD & Swadesh Darshan", "type": "branch", "date": "Circuits", "children": [
                    {"label": "PRASHAD Scheme: Aims at infrastructure development and aesthetic beautification of pilgrimage centers", "type": "leaf"},
                    {"label": "Swadesh Darshan: Promotes thematic tourism circuits across India (e.g. Buddhist, Coastal, Heritage Circuits)", "type": "leaf"}
                ]}
            ]

    # 9. Science and Technology in Ancient India
    elif fl == 'science-and-technology-in-ancient-india':
        if is_hindi:
            return [
                {"label": "गणित और खगोल विज्ञान", "type": "branch", "date": "गणित", "children": [
                    {"label": "आर्यभट्ट: 'आर्यभटीय' के लेखक; शून्य के मूल्य का प्रतिपादन, पाई (Pi) का सटीक मान (3.1416) और पृथ्वी के अपनी धुरी पर घूमने की खोज की", "type": "leaf"},
                    {"label": "ब्रह्मगुप्त: 'ब्रह्मस्फुटसिद्धांत' लिखा; शून्य के साथ गणना करने के गणितीय नियम दिए, आकर्षण बल (गुरुत्वाकर्षण) का प्रारंभिक संकेत दिया", "type": "leaf"},
                    {"label": "वराहमिहिर: 'बृहत्संहिता' और 'पंचसिद्धांतिका' के लेखक; खगोल विज्ञान, ज्योतिष और मौसम विज्ञान के अग्रणी विद्वान", "type": "leaf"}
                ]},
                {"label": "आयुर्वेद और धातु विज्ञान", "type": "branch", "date": "विज्ञान", "children": [
                    {"label": "सुश्रुत: 'सुश्रुत संहिता' के लेखक; प्लास्टिक सर्जरी और मोतियाबिंद सर्जरी के प्राचीन भारतीय जनक (शल्य चिकित्सा)", "type": "leaf"},
                    {"label": "चरक: 'चरक संहिता' के लेखक; आयुर्वेद चिकित्सा के महानतम प्रतिपादक; वात, पित्त और कफ त्रिदोष का सिद्धांत दिया", "type": "leaf"},
                    {"label": "महरौली लौह स्तंभ: गुप्त काल (चंद्रगुप्त द्वितीय) का जंग-रोधी लौह स्तंभ; प्राचीन धातु विज्ञान का नायाब नमूना", "type": "leaf"}
                ]}
            ]
        else:
            return [
                {"label": "Mathematics & Astronomy", "type": "branch", "date": "Astronomy", "children": [
                    {"label": "Aryabhata: Wrote Aryabhatiya; calculated Pi value (3.1416), explained solar/lunar eclipses, and defined Earth's rotation", "type": "leaf"},
                    {"label": "Brahmagupta: Composed Brahmasphutasiddhanta, defining mathematical rules for zero and early concepts of gravity", "type": "leaf"},
                    {"label": "Varahamihira: Wrote Brihat Samhita and Panchasiddhantika, covering astronomy, meteorology, and hydrology", "type": "leaf"}
                ]},
                {"label": "Medicine & Metallurgy", "type": "branch", "date": "Sciences", "children": [
                    {"label": "Sushruta: Author of Sushruta Samhita; pioneering plastic surgeon detailing rhinoplasty and cataract extractions", "type": "leaf"},
                    {"label": "Charaka: Author of Charaka Samhita; developed Ayurveda principles based on Tridosha (Vata, Pitta, Kapha)", "type": "leaf"},
                    {"label": "Mehrauli Iron Pillar: 4th-century Gupta column constructed of rust-resistant wrought iron, proving advanced metallurgy", "type": "leaf"}
                ]}
            ]

    # 10. The Calendar the Eras
    elif fl == 'the-calendar-the-eras':
        if is_hindi:
            return [
                {"label": "शक संवत (राष्ट्रीय कैलेंडर)", "type": "branch", "date": "राष्ट्रीय कैलेंडर", "children": [
                    {"label": "शक संवत: 78 ई. में कुषाण सम्राट कनिष्क द्वारा शुरू किया गया; 22 मार्च 1957 को भारत का राष्ट्रीय कैलेंडर घोषित किया गया", "type": "leaf"},
                    {"label": "संरचना: प्रथम महीना चैत्र (22 मार्च, लीप वर्ष में 21 मार्च); कुल 365 दिन; सौर कैलेंडर प्रणाली", "type": "leaf"}
                ]},
                {"label": "अन्य प्रमुख ऐतिहासिक संवत", "type": "branch", "date": "संवत", "children": [
                    {"label": "विक्रम संवत: 57 ई.पू. में शकों पर उज्जैन के राजा विक्रमादित्य की विजय की याद में शुरू किया गया चंद्र-सौर कैलेंडर", "type": "leaf"},
                    {"label": "कोल्लम संवत: केरल में प्रयुक्त सौर कैलेंडर, जो 825 ई. से शुरू होता है", "type": "leaf"},
                    {"label": "हिजरी संवत: 622 ई. में पैगंबर मोहम्मद के मक्का से मदीना प्रवास (हिजरत) से शुरू होने वाला इस्लामी चंद्र कैलेंडर", "type": "leaf"}
                ]}
            ]
        else:
            return [
                {"label": "Saka Samvat & National Calendar", "type": "branch", "date": "Saka Era", "children": [
                    {"label": "Saka Era: Est. 78 AD by Kushan King Kanishka; adopted as India's National Calendar on March 22, 1957", "type": "leaf"},
                    {"label": "Layout: Month Chaitra begins the year (March 22, or March 21 in leap years); strictly solar-based calendar", "type": "leaf"}
                ]},
                {"label": "Alternative Historical Eras", "type": "branch", "date": "Eras", "children": [
                    {"label": "Vikram Samvat: Est. 57 BCE commemorating King Vikramaditya's victory over Sakas; follows lunisolar cycles", "type": "leaf"},
                    {"label": "Kollam Era: Solar calendar used in Kerala, beginning in 825 AD, linked to royal trading updates", "type": "leaf"},
                    {"label": "Hijri Calendar: Lunar Islamic calendar dating from the emigration (Hijrah) of Prophet Muhammad in 622 AD", "type": "leaf"}
                ]}
            ]

    # 11. UNESCOs List of Cultural Heritage in India
    elif 'unesco' in fl:
        if is_hindi:
            return [
                {"label": "विश्व धरोहर स्थल (मूर्त धरोहर)", "type": "branch", "date": "मूर्त स्थल", "children": [
                    {"label": "वर्गीकरण: तीन श्रेणियों में विभाजित: सांस्कृतिक (जैसे ताज महल, सांची स्तूप, महाबलीपुरम), प्राकृतिक (जैसे सुंदरवन, काजीरंगा), और मिश्रित (कंचनजंगा)", "type": "leaf"},
                    {"label": "नवीनतम स्थल: होयसल के पवित्र मंदिर (2023 - 42वां स्थल) और शांतिनिकेतन (2023 - 41वां स्थल)", "type": "leaf"}
                ]},
                {"label": "अमूर्त सांस्कृतिक विरासत (ICH)", "type": "branch", "date": "अमूर्त विरासत", "children": [
                    {"label": "यूनेस्को सूची: भारत के 15 सांस्कृतिक तत्वों को अमूर्त विरासत घोषित किया गया है, जो जीवित परंपराओं को दर्शाते हैं", "type": "leaf"},
                    {"label": "प्रमुख तत्व: कुटियाट्टम (संस्कृत थियेटर), रामलीला, वैदिक मंत्रोच्चार, कालबेलिया नृत्य, योग, कुंभ मेला", "type": "leaf"},
                    {"label": "नवीनतम प्रविष्टियां: कोलकाता की दुर्गा पूजा (2021) और गुजरात का गरबा नृत्य (2023)", "type": "leaf"}
                ]}
            ]
        else:
            return [
                {"label": "UNESCO World Heritage Sites", "type": "branch", "date": "Tangible", "children": [
                    {"label": "Three Groups: Cultural (Taj Mahal, Sanchi Stupa, Red Fort), Natural (Kaziranga, Western Ghats), Mixed (Khangchendzonga)", "type": "leaf"},
                    {"label": "Latest Sites: Santiniketan (41st site) and the Sacred Ensembles of the Hoysalas (42nd site, 2023)", "type": "leaf"}
                ]},
                {"label": "Intangible Cultural Heritage (ICH)", "type": "branch", "date": "Intangible", "children": [
                    {"label": "Living Traditions: 15 Indian elements inscribed representing social rituals, oral scripts, and folk arts", "type": "leaf"},
                    {"label": "Inscribed elements: Vedic chanting, Kutiyattam, Ramlila, Ramman festivals, Kalbelia, Yoga, Kumbh Mela", "type": "leaf"},
                    {"label": "Recent Entries: Durga Puja of Kolkata (2021) and the traditional Garba dance of Gujarat (2023)", "type": "leaf"}
                ]}
            ]

    # Fallback
    else:
        if is_hindi:
            return [
                {"label": "विविध विषय", "type": "branch", "date": "विविध", "children": [
                    {"label": "भारतीय कैलेंडर, प्राचीन विज्ञान और तकनीक, यूनेस्को धरोहर और जीआई टैग का परिचय", "type": "leaf"},
                    {"label": "संस्कृति मंत्रालय की विभिन्न स्मारक विकास योजनाएं और राष्ट्रीय पुरस्कारों का विवरण", "type": "leaf"}
                ]}
            ]
        else:
            return [
                {"label": "Miscellaneous Topics", "type": "branch", "date": "Overview", "children": [
                    {"label": "Covers Indian calendar systems, ancient scientific achievements, and UNESCO list details", "type": "leaf"},
                    {"label": "Includes ministry policies on monument development, GI registries, and apex awards", "type": "leaf"}
                ]}
            ]

def process_file(html_path, is_hindi):
    print(f"Processing: {html_path} (is_hindi={is_hindi})")
    
    with open(html_path, 'r', encoding='utf-8') as f:
        html = f.read()

    # Normalize newlines
    html = html.replace('\r\n', '\n')

    # Remove any existing mindmap CSS/container/script tags
    html = html.replace('    <link rel="stylesheet" href="/assets/css/mindmap.min.css?v=2">\n', '')
    html = html.replace('    <link rel="stylesheet" href="/assets/css/mindmap.min.css?v=1">\n', '')
    html = html.replace('    <link rel="stylesheet" href="/assets/css/mindmap.min.css">\n', '')
    
    # Match and clean existing interactive mindmap card
    mindmap_div_pattern = r'\s*<!-- Interactive Mindmap -->.*?<!-- Deep-Dive Study Guide \(Dynamically Rendered\) -->'
    html = re.sub(mindmap_div_pattern, '\n            <!-- Deep-Dive Study Guide (Dynamically Rendered) -->', html, flags=re.DOTALL)
    
    # Match and clean existing mindmap engine script
    script_pattern = r'\s*<!-- Interactive Mindmap -->.*?renderMindmap\(.*?\);\s*</script>'
    html = re.sub(script_pattern, '', html, flags=re.DOTALL)

    # Get topic title from content.json if it exists
    folder_path = os.path.dirname(html_path)
    content_json_path = os.path.join(folder_path, "content.json")
    folder_name = os.path.basename(folder_path)
    if folder_name == 'hi':
        parent_folder = os.path.dirname(folder_path)
        folder_name = os.path.basename(parent_folder)
        content_json_path = os.path.join(parent_folder, "hi", "content.json")
        if not os.path.exists(content_json_path):
            content_json_path = os.path.join(parent_folder, "content.json")

    clean_title = get_clean_title(folder_name)
    
    topic_name = clean_title
    if os.path.exists(content_json_path):
        try:
            with open(content_json_path, 'r', encoding='utf-8') as f:
                c_data = json.load(f)
                topic_name = c_data.get('hero', {}).get('title', topic_name)
        except Exception as e:
            print(f"  Error reading content.json: {e}")

    # Build unique mindmap data using refined keyword matching on the folder_name
    branches = get_custom_branches(folder_name, is_hindi)
    mindmap_data = {
        "label": clean_title,
        "type": "root",
        "children": branches
    }

    # Re-inject CSS link before closing </head>
    css_link = '    <link rel="stylesheet" href="/assets/css/mindmap.min.css?v=2">\n'
    if css_link not in html:
        html = html.replace('</head>', css_link + '</head>')

    # Re-inject Mindmap Div before deep-dive-section
    if is_hindi:
        instr = 'किसी <strong style="color:#a78bfa;">बैंगनी</strong> या <strong style="color:#2ecc71;">हरे</strong> <strong>+</strong> पर क्लिक करें — एक को खोलने पर दूसरे स्वतः बंद हो जाएंगे।'
        title_text = f"{topic_name} &mdash; इंटरैक्टिव माइंडमैप"
    else:
        instr = 'Tap a <strong style="color:#a78bfa;">purple</strong> or <strong style="color:#2ecc71;">green</strong> <strong>+</strong> to expand — opening one automatically closes its siblings.'
        title_text = f"{topic_name} &mdash; Interactive Mindmap"

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
    
    deep_dive_pattern = r'(<!-- Deep-Dive Study Guide \(Dynamically Rendered\) -->\s*<div class="card-premium" id="deep-dive-section">)'
    if re.search(deep_dive_pattern, html):
        html = re.sub(deep_dive_pattern, mindmap_card + r'\1', html)
    else:
        # Fallback to Tab 1 notes panel
        tab1_marker = '<div class="tab-panel active" id="notes-panel" role="tabpanel" aria-labelledby="notes-panel">'
        if tab1_marker in html:
            html = html.replace(tab1_marker, tab1_marker + '\n' + mindmap_card, 1)

    # Re-inject script before </body>
    tree_json = json.dumps(mindmap_data)
    lang_str = "'hi'" if is_hindi else "'en'"
    inline_script = f'''
    <!-- Interactive Mindmap -->
    <script src="/assets/js/mindmap-engine.min.js?v=2"></script>
    <script>
    renderMindmap({tree_json}, undefined, {lang_str});
    </script>
'''
    html = html.replace('</body>', inline_script + '\n</body>')

    # Write back
    with open(html_path, 'w', encoding='utf-8') as f:
        f.write(html)
        
    print(f"  Successfully patched {html_path}")

def main():
    total_processed = 0
    for root, dirs, files in os.walk(BASE):
        rel_path = os.path.relpath(root, BASE)
        parts = rel_path.split(os.sep)
        
        is_hindi = False
        if 'hi' in parts:
            is_hindi = True
        
        for file in files:
            if file == "index.html":
                html_path = os.path.join(root, file)
                process_file(html_path, is_hindi)
                total_processed += 1
                
    print(f"\nDone! Patched {total_processed} files successfully.")

if __name__ == '__main__':
    main()
