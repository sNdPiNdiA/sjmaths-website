#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import re
import json

BASE_DIR = r"upsc/environment/Terrestrial-Aquatic-Ecosystems"

def get_clean_title(folder_name):
    title = re.sub(r'([a-z])([A-Z])', r'\1 \2', folder_name)
    title = title.replace('-', ' ')
    words = []
    acronyms = {'dpsp', 'pri', 'ut', 'uts', 'sc', 'hc', 'cm', 'com', 'arc', 'inc', 'ias', 'sec', 'sfc', 'pej', 'tej', 'mjo', 'enso', 'iod', 'icar', 'gst', 'dpc', 'mpc', 'adc', 'tac', 'scs', 'pesa', 'icar', 'isfr', 'itcz', 'tej'}
    for w in title.split():
        if w.lower() in acronyms:
            words.append(w.upper())
        elif w.lower() in ['of', 'and', 'the', 'for', 'in', 'with', 'against', 'to', 'on', 'some', 'by', 'their', 'vs']:
            words.append(w.lower())
        else:
            words.append(w.capitalize())
    return ' '.join(words)

# Unique mindmap data mapping for each of the 52 folders
DATA_MAP = {
    "about-asian-water-bird-census": {
        "en": [
            {"label": "AWC Overview", "type": "branch", "date": "Overview", "children": [
                {"label": "Citizen Science: Coordinated by Wetlands International since 1987", "type": "leaf"},
                {"label": "CAF Coverage: Part of International Waterbird Census covering Central Asian Flyway", "type": "leaf"}
            ]},
            {"label": "Objectives & Methodology", "type": "branch", "date": "Objectives", "children": [
                {"label": "Population Monitoring: Annual census in January to count wintering waterbirds", "type": "leaf"},
                {"label": "Wetland Status: Evaluates the ecological condition of monitored wetlands", "type": "leaf"}
            ]},
            {"label": "Migratory Flyways & India", "type": "branch", "date": "Flyways", "children": [
                {"label": "Central Asian Flyway: India is a key wintering destination; census tracks key nodes", "type": "leaf"},
                {"label": "Local Participation: Conducted with local NGOs, forest departments, and birdwatchers", "type": "leaf"}
            ]},
            {"label": "UPSC Relevance & Output", "type": "branch", "date": "UPSC Core", "children": [
                {"label": "Ramsar Criteria: Data helps designate new Ramsar sites based on waterbird populations", "type": "leaf"},
                {"label": "Threat Tracking: Highlights degradation of critical wetlands and loss of habitat", "type": "leaf"}
            ]}
        ],
        "hi": [
            {"label": "AWC सिंहावलोकन", "type": "branch", "date": "सिंहावलोकन", "children": [
                {"label": "नागरिक विज्ञान: 1987 से वेटलैंड्स इंटरनेशनल द्वारा समन्वित वार्षिक कार्यक्रम", "type": "leaf"},
                {"label": "CAF कवरेज: मध्य एशियाई फ्लाईवे को कवर करने वाली अंतर्राष्ट्रीय जलपक्षी गणना का हिस्सा", "type": "leaf"}
            ]},
            {"label": "उद्देश्य और कार्यप्रणाली", "type": "branch", "date": "उद्देश्य", "children": [
                {"label": "आबादी निगरानी: शीतकालीन जलपक्षियों की गिनती के लिए जनवरी में वार्षिक जनगणना", "type": "leaf"},
                {"label": "आर्द्रभूमि स्थिति: निगरानी की गई आर्द्रभूमियों की पारिस्थितिक स्थिति का मूल्यांकन", "type": "leaf"}
            ]},
            {"label": "प्रवासी मार्ग और भारत", "type": "branch", "date": "प्रवासी मार्ग", "children": [
                {"label": "मध्य एशियाई फ्लाईवे: भारत एक प्रमुख शीतकालीन गंतव्य है; जनगणना प्रमुख नोड्स को ट्रैक करती है", "type": "leaf"},
                {"label": "स्थानीय भागीदारी: स्थानीय गैर सरकारी संगठनों, वन विभागों और पक्षी प्रेमियों के साथ आयोजित", "type": "leaf"}
            ]},
            {"label": "यूपीएससी महत्व और आउटपुट", "type": "branch", "date": "यूपीएससी", "children": [
                {"label": "रामसर मानदंड: डेटा जलपक्षी आबादी के आधार पर नए रामसर स्थलों को नामित करने में मदद करता है", "type": "leaf"},
                {"label": "खतरे की ट्रैकिंग: महत्वपूर्ण आर्द्रभूमियों के क्षरण और आवास के नुकसान पर प्रकाश डालता है", "type": "leaf"}
            ]}
        ]
    },
    "about-ramsar-convention": {
        "en": [
            {"label": "Convention Foundations", "type": "branch", "date": "Foundations", "children": [
                {"label": "Establishment: Signed in Ramsar, Iran in 1971; oldest intergovernmental environmental treaty", "type": "leaf"},
                {"label": "Three Pillars: Wise use of wetlands, designating Ramsar sites, and international cooperation", "type": "leaf"}
            ]},
            {"label": "Montreux Record", "type": "branch", "date": "Montreux", "children": [
                {"label": "Definition: Register of Ramsar sites where ecological changes have occurred, are occurring, or likely to occur", "type": "leaf"},
                {"label": "India Sites: Keoladeo National Park (Rajasthan) and Loktak Lake (Manipur); Chilika Lake was removed", "type": "leaf"}
            ]},
            {"label": "India & Ramsar Network", "type": "branch", "date": "India Network", "children": [
                {"label": "Expansion: India has designated numerous sites under Mission Amrit Sarovar", "type": "leaf"},
                {"label": "Chilika Lake Success: Removed from Montreux Record due to successful ecological restoration", "type": "leaf"}
            ]},
            {"label": "UPSC Mains Core", "type": "branch", "date": "UPSC Core", "children": [
                {"label": "Wise Use Concept: Human use of wetlands on a sustainable basis compatible with conservation", "type": "leaf"},
                {"label": "Transboundary Wetlands: Guidelines for managing wetlands sharing international borders", "type": "leaf"}
            ]}
        ],
        "hi": [
            {"label": "अभिसमय की नींव", "type": "branch", "date": "नींव", "children": [
                {"label": "स्थापना: 1971 में ईरान के रामसर शहर में हस्ताक्षरित; सबसे पुराना अंतर-सरकारी पर्यावरण समझौता", "type": "leaf"},
                {"label": "तीन स्तंभ: आर्द्रभूमियों का बुद्धिमत्तापूर्ण उपयोग, रामसर स्थलों को नामित करना और अंतर्राष्ट्रीय सहयोग", "type": "leaf"}
            ]},
            {"label": "मॉन्ट्रो रिकॉर्ड (Montreux)", "type": "branch", "date": "मॉन्ट्रो", "children": [
                {"label": "परिभाषा: उन रामसर स्थलों का रजिस्टर जहां पारिस्थितिक परिवर्तन हुए हैं, हो रहे हैं या होने की संभावना है", "type": "leaf"},
                {"label": "भारतीय स्थल: केवलादेव राष्ट्रीय उद्यान (राजस्थान) और लोकतक झील (मणिपुर); चिल्का झील को हटा दिया गया था", "type": "leaf"}
            ]},
            {"label": "भारत और रामसर नेटवर्क", "type": "branch", "date": "भारतीय नेटवर्क", "children": [
                {"label": "विस्तार: मिशन अमृत सरोवर के तहत भारत ने कई नए रामसर स्थल नामित किए हैं", "type": "leaf"},
                {"label": "चिल्का झील की सफलता: सफल पारिस्थितिक बहाली के कारण मॉन्ट्रो रिकॉर्ड से हटा दिया गया", "type": "leaf"}
            ]},
            {"label": "यूपीएससी मुख्य परीक्षा फोकस", "type": "branch", "date": "यूपीएससी", "children": [
                {"label": "बुद्धिमत्तापूर्ण उपयोग: संरक्षण के अनुकूल सतत आधार पर आर्द्रभूमियों का मानव उपयोग", "type": "leaf"},
                {"label": "सीमा पार आर्द्रभूमियां: अंतर्राष्ट्रीय सीमाओं को साझा करने वाली आर्द्रभूमियों के प्रबंधन के लिए दिशानिर्देश", "type": "leaf"}
            ]}
        ]
    },
    "algal-bloom": {
        "en": [
            {"label": "Bloom Mechanics", "type": "branch", "date": "Mechanics", "children": [
                {"label": "Definition: Rapid increase or accumulation in the population of algae in freshwater or marine water systems", "type": "leaf"},
                {"label": "Indicators: Water discoloration (red, green, brown) often referred to as red tides", "type": "leaf"}
            ]},
            {"label": "Nutrient Enrichment", "type": "branch", "date": "Nutrients", "children": [
                {"label": "Runoff Sources: Agricultural fertilizers (nitrogen/phosphorus) and domestic sewage discharge", "type": "leaf"},
                {"label": "Limiting Factors: High temperature, sunny days, and stagnant water accelerate bloom density", "type": "leaf"}
            ]},
            {"label": "Ecological & Health Impacts", "type": "branch", "date": "Impacts", "children": [
                {"label": "HABs (Harmful Algal Blooms): Produce toxins (like microcystins) killing fish, mammals, and birds", "type": "leaf"},
                {"label": "Oxygen Depletion: Decaying algae consumes dissolved oxygen, creating hypoxic dead zones", "type": "leaf"}
            ]},
            {"label": "UPSC Mitigation Core", "type": "branch", "date": "UPSC Core", "children": [
                {"label": "Bioremediation: Riparian buffers to absorb nutrients before they reach water bodies", "type": "leaf"},
                {"label": "Conservation: Reducing fertilizer overuse; sewage treatment plant (STP) upgrades", "type": "leaf"}
            ]}
        ],
        "hi": [
            {"label": "अल्गल ब्लूम क्रियाविधि", "type": "branch", "date": "क्रियाविधि", "children": [
                {"label": "परिभाषा: मीठे पानी या समुद्री जल प्रणालियों में शैवाल की आबादी में तीव्र वृद्धि या संचय", "type": "leaf"},
                {"label": "संकेतक: पानी का विवर्ण होना (लाल, हरा, भूरा), जिसे अक्सर 'लाल ज्वार' कहा जाता है", "type": "leaf"}
            ]},
            {"label": "पोषक तत्व संवर्धन", "type": "branch", "date": "पोषक तत्व", "children": [
                {"label": "अपवाह स्रोत: कृषि उर्वरक (नाइट्रोजन/फास्फोरस) और घरेलू सीवेज का निर्वहन", "type": "leaf"},
                {"label": "सीमित कारक: उच्च तापमान, धूप वाले दिन और स्थिर पानी ब्लूम की गति बढ़ाते हैं", "type": "leaf"}
            ]},
            {"label": "पारिस्थितिक और स्वास्थ्य प्रभाव", "type": "branch", "date": "प्रभाव", "children": [
                {"label": "HABs (हानिकारक ब्लूम): विषाक्त पदार्थों (जैसे माइक्रोसिस्टिन) का उत्पादन करते हैं जो मछलियों और पक्षियों को मारते हैं", "type": "leaf"},
                {"label": "ऑक्सीजन की कमी: सड़ने वाले शैवाल घुली हुई ऑक्सीजन का उपभोग करते हैं, जिससे हाइपोक्सिक मृत क्षेत्र बनते हैं", "type": "leaf"}
            ]},
            {"label": "यूपीएससी शमन तकनीक", "type": "branch", "date": "शमन", "children": [
                {"label": "बायोरेमेडिएशन: जल निकायों तक पहुँचने से पहले पोषक तत्वों को अवशोषित करने के लिए रिपेरियन बफर लगाना", "type": "leaf"},
                {"label": "संरक्षण: उर्वरक के अत्यधिक उपयोग को कम करना; सीवेज ट्रीटमेंट प्लांट (STP) का आधुनिकीकरण", "type": "leaf"}
            ]}
        ]
    },
    "aphotic-zone": {
        "en": [
            {"label": "Aphotic Zonation", "type": "branch", "date": "Zonation", "children": [
                {"label": "Depth Profile: Begins below ~200m depth where less than 1% of sunlight penetrates", "type": "leaf"},
                {"label": "Light Absence: Complete darkness; photosynthesis is impossible", "type": "leaf"}
            ]},
            {"label": "Organism Adaptations", "type": "branch", "date": "Adaptations", "children": [
                {"label": "Bioluminescence: Chemical light production by fish (e.g. Anglerfish) to attract prey or mates", "type": "leaf"},
                {"label": "Gigantism: Extreme size adaptations in some deep-sea species (e.g. Giant Squid)", "type": "leaf"}
            ]},
            {"label": "Energy & Nutrient Sources", "type": "branch", "date": "Energy Sources", "children": [
                {"label": "Marine Snow: Continuous shower of organic detritus falling from the upper photic zone", "type": "leaf"},
                {"label": "Chemosynthesis: Hydrothermal vents supporting specialized bacteria deriving energy from hydrogen sulfide", "type": "leaf"}
            ]},
            {"label": "UPSC Oceanography Core", "type": "branch", "date": "UPSC Core", "children": [
                {"label": "Food Webs: Highly dependent on surface productivity; slow metabolism of bathypelagic organisms", "type": "leaf"},
                {"label": "Benthic Biology: High pressure, low temperature, and constant salinity define the environment", "type": "leaf"}
            ]}
        ],
        "hi": [
            {"label": "अप्रकाशीय क्षेत्र (Aphotic Zone)", "type": "branch", "date": "वर्गीकरण", "children": [
                {"label": "गहराई प्रोफ़ाइल: ~200 मीटर की गहराई के नीचे शुरू होता है जहाँ 1% से भी कम सूर्य का प्रकाश पहुँचता है", "type": "leaf"},
                {"label": "प्रकाश की अनुपस्थिति: पूर्ण अंधकार; प्रकाश संश्लेषण असंभव है", "type": "leaf"}
            ]},
            {"label": "जीव अनुकूलन", "type": "branch", "date": "अनुकूलन", "children": [
                {"label": "जैवदीप्ति (Bioluminescence): शिकार या साथी को आकर्षित करने के लिए मछलियों द्वारा रासायनिक प्रकाश उत्पादन", "type": "leaf"},
                {"label": "विशालता (Gigantism): कुछ गहरे समुद्री जीवों में अत्यधिक आकार का अनुकूलन (जैसे विशाल स्क्विड)", "type": "leaf"}
            ]},
            {"label": "ऊर्जा और पोषक तत्व स्रोत", "type": "branch", "date": "ऊर्जा स्रोत", "children": [
                {"label": "समुद्री हिमपात (Marine Snow): ऊपरी प्रकाशीय क्षेत्र से गिरने वाले कार्बनिक कचरे की निरंतर बौछार", "type": "leaf"},
                {"label": "रसायन-संश्लेषण: हाइड्रोथर्मल वेंट सल्फाइड से ऊर्जा प्राप्त करने वाले बैक्टीरिया का समर्थन करते हैं", "type": "leaf"}
            ]},
            {"label": "यूपीएससी समुद्र विज्ञान मुख्य", "type": "branch", "date": "यूपीएससी", "children": [
                {"label": "खाद्य जाल: सतह की उत्पादकता पर अत्यधिक निर्भर; गहरे जीवों की धीमी चयापचय दर", "type": "leaf"},
                {"label": "नितल जीव विज्ञान (Benthic): उच्च दाब, कम तापमान और निरंतर लवणता पर्यावरण को परिभाषित करती है", "type": "leaf"}
            ]}
        ]
    },
    "community-based-mangrove-regeneration": {
        "en": [
            {"label": "Community Involvement", "type": "branch", "date": "Involvement", "children": [
                {"label": "Local Ownership: Engaging coastal communities in nursery development and sapling planting", "type": "leaf"},
                {"label": "Traditional Knowledge: Utilizing local understanding of tidal channels and species suitability", "type": "leaf"}
            ]},
            {"label": "Regeneration Benefits", "type": "branch", "date": "Benefits", "children": [
                {"label": "Coastal Defense: Buffers storm surges, cyclonic winds, and controls coastal erosion", "type": "leaf"},
                {"label": "Livelihoods: Restores crab, fish nurseries, improving local artisanal fishery catches", "type": "leaf"}
            ]},
            {"label": "Successful Models", "type": "branch", "date": "Models", "children": [
                {"label": "Joint Forest Management (JFM): Forest departments partnering with Gram Panchayats in Sunderbans", "type": "leaf"},
                {"label": "Co-benefits: Ecotourism income, carbon credit shares, and non-timber forest products", "type": "leaf"}
            ]},
            {"label": "UPSC Policy Relevance", "type": "branch", "date": "UPSC Core", "children": [
                {"label": "MISHTI Alignment: Highlights importance of decentralized local action in national mangrove missions", "type": "leaf"},
                {"label": "Climate Adaptation: Local communities as primary actors in building climate-resilient coastlines", "type": "leaf"}
            ]}
        ],
        "hi": [
            {"label": "सामुदायिक भागीदारी", "type": "branch", "date": "सामुदायिक", "children": [
                {"label": "स्थानीय स्वामित्व: नर्सरी विकास और पौधों के रोपण में तटीय समुदायों को शामिल करना", "type": "leaf"},
                {"label": "पारंपरिक ज्ञान: ज्वारीय चैनलों और प्रजातियों की उपयुक्तता की स्थानीय समझ का उपयोग करना", "type": "leaf"}
            ]},
            {"label": "पुनर्जनन के लाभ", "type": "branch", "date": "लाभ", "children": [
                {"label": "तटीय सुरक्षा: तूफान के थपेड़ों, चक्रवाती हवाओं को रोकता है और तटीय क्षरण को नियंत्रित करता", "type": "leaf"},
                {"label": "आजीविका: केकड़ा और मछली नर्सरी को बहाल करता है, जिससे स्थानीय मछली पकड़ने में सुधार होता है", "type": "leaf"}
            ]},
            {"label": "सफल मॉडल", "type": "branch", "date": "मॉडल", "children": [
                {"label": "संयुक्त वन प्रबंधन (JFM): सुंदरबन में ग्राम पंचायतों के साथ वन विभागों की भागीदारी", "type": "leaf"},
                {"label": "सह-लाभ: पारिस्थितिक पर्यटन आय, कार्बन क्रेडिट शेयर और गैर-इमारती वन उत्पाद", "type": "leaf"}
            ]},
            {"label": "यूपीएससी नीति महत्व", "type": "branch", "date": "यूपीएससी", "children": [
                {"label": "मिष्टी योजना संरेखण: राष्ट्रीय मैंग्रोव मिशनों में विकेंद्रीकृत स्थानीय कार्रवाई के महत्व पर प्रकाश डालता है", "type": "leaf"},
                {"label": "जलवायु अनुकूलन: जलवायु-अनुकूल तटीय रेखाओं के निर्माण में प्राथमिक अभिनेताओं के रूप में स्थानीय समुदाय", "type": "leaf"}
            ]}
        ]
    },
    "conservation-of-estuaries": {
        "en": [
            {"label": "Estuarine Threats", "type": "branch", "date": "Threats", "children": [
                {"label": "Industrial Discharge: Effluents changing saline-freshwater chemical balance", "type": "leaf"},
                {"label": "Over-fishing: Disrupts food webs and decimates fingerling nurseries", "type": "leaf"}
            ]},
            {"label": "Conservation Strategies", "type": "branch", "date": "Strategies", "children": [
                {"label": "Silt Management: Controlling upstream river deforestation to prevent excessive siltation", "type": "leaf"},
                {"label": "Pollution Control: Establishing Common Effluent Treatment Plants (CETPs) for coastal industries", "type": "leaf"}
            ]},
            {"label": "Regulatory Protection", "type": "branch", "date": "Regulation", "children": [
                {"label": "CRZ Regulations: Categorizes estuaries under ecologically sensitive CRZ-I zones", "type": "leaf"},
                {"label": "EIA Mandates: Compulsory Environmental Impact Assessments for ports and dredging near estuaries", "type": "leaf"}
            ]},
            {"label": "UPSC Core Analysis", "type": "branch", "date": "UPSC Core", "children": [
                {"label": "Integrated Management: Connecting river basin management with coastal zone planning", "type": "leaf"},
                {"label": "Eco-services: Estuaries as carbon sinks and filters for nitrogen-phosphorus load", "type": "leaf"}
            ]}
        ],
        "hi": [
            {"label": "ज्वारनदमुख के खतरे", "type": "branch", "date": "खतरे", "children": [
                {"label": "औद्योगिक निर्वहन: खारे-मीठे पानी के रासायनिक संतुलन को बदलने वाले अपशिष्ट", "type": "leaf"},
                {"label": "अति-मत्स्यन: खाद्य जाल को बाधित करता है और नर्सरी को नष्ट करता है", "type": "leaf"}
            ]},
            {"label": "संरक्षण रणनीतियाँ", "type": "branch", "date": "रणनीतियाँ", "children": [
                {"label": "गाद प्रबंधन: अत्यधिक गाद को रोकने के लिए ऊपरी नदी क्षेत्र में वनों की कटाई को नियंत्रित करना", "type": "leaf"},
                {"label": "प्रदूषण नियंत्रण: तटीय उद्योगों के लिए सामान्य अपशिष्ट उपचार संयंत्र (CETP) स्थापित करना", "type": "leaf"}
            ]},
            {"label": "नियामक संरक्षण", "type": "branch", "date": "नियमन", "children": [
                {"label": "CRZ नियमन: ज्वारनदमुख को पारिस्थितिक रूप से संवेदनशील CRZ-I क्षेत्रों के तहत वर्गीकृत करता है", "type": "leaf"},
                {"label": "EIA जनादेश: बंदरगाहों और जलमार्ग परियोजनाओं के लिए अनिवार्य पर्यावरण प्रभाव आकलन", "type": "leaf"}
            ]},
            {"label": "यूपीएससी कोर विश्लेषण", "type": "branch", "date": "यूपीएससी", "children": [
                {"label": "एकीकृत प्रबंधन: तटीय क्षेत्र योजना के साथ नदी बेसिन प्रबंधन को जोड़ना", "type": "leaf"},
                {"label": "पारिस्थितिक सेवाएँ: कार्बन सिंक और नाइट्रोजन-फास्फोरस भार के लिए फिल्टर के रूप में कार्य", "type": "leaf"}
            ]}
        ]
    },
    "conservation-of-wetlands": {
        "en": [
            {"label": "Threat Mitigation", "type": "branch", "date": "Threats", "children": [
                {"label": "Urban Expansion: Encroachment of lakes for real estate (e.g. Bangalore lake encroachment)", "type": "leaf"},
                {"label": "Eutrophication: Excessive weed growth (Water Hyacinth) blocking sunlight and aeration", "type": "leaf"}
            ]},
            {"label": "Regulatory Framework", "type": "branch", "date": "Regulation", "children": [
                {"label": "Wetland Rules 2017: Focuses on decentralized conservation through State Wetland Authorities", "type": "leaf"},
                {"label": "Prohibitions: Bans reclamation, solid waste dumping, and discharge of untreated effluents", "type": "leaf"}
            ]},
            {"label": "Community Partnerships", "type": "branch", "date": "Partnerships", "children": [
                {"label": "Wise Use: Supporting sustainable fisheries and eco-agriculture in surrounding zones", "type": "leaf"},
                {"label": "Citizen Initiatives: Traditional desilting, local clean-ups, and bird monitoring", "type": "leaf"}
            ]},
            {"label": "UPSC Syllabus Core", "type": "branch", "date": "UPSC Core", "children": [
                {"label": "NPCA Scheme: National Plan for Conservation of Aquatic Eco-systems combining wetlands and lakes", "type": "leaf"},
                {"label": "SDG Target 6.6: Target to protect and restore water-related ecosystems, including wetlands", "type": "leaf"}
            ]}
        ],
        "hi": [
            {"label": "खतरे का शमन", "type": "branch", "date": "खतरे", "children": [
                {"label": "शहरी विस्तार: रियल एस्टेट के लिए झीलों का अतिक्रमण (जैसे बैंगलोर की झीलें)", "type": "leaf"},
                {"label": "यूट्रोफिकेशन: अत्यधिक खरपतवार (जलकुंभी) की वृद्धि जो धूप और वायु संचरण को रोकती है", "type": "leaf"}
            ]},
            {"label": "नियामक ढांचा", "type": "branch", "date": "नियमन", "children": [
                {"label": "आर्द्रभूमि नियम 2017: राज्य आर्द्रभूमि प्राधिकरणों के माध्यम से विकेंद्रीकृत संरक्षण पर ध्यान केंद्रित", "type": "leaf"},
                {"label": "प्रतिबंध: भूमि सुधार, ठोस कचरा डंपिंग और अनुपचारित अपशिष्टों के निर्वहन पर प्रतिबंध", "type": "leaf"}
            ]},
            {"label": "सामुदायिक भागीदारी", "type": "branch", "date": "भागीदारी", "children": [
                {"label": "बुद्धिमत्तापूर्ण उपयोग: आसपास के क्षेत्रों में स्थायी मत्स्य पालन और पर्यावरण-कृषि का समर्थन", "type": "leaf"},
                {"label": "नागरिक पहल: पारंपरिक गाद निकालना, स्थानीय सफाई और पक्षी निगरानी कार्यक्रम", "type": "leaf"}
            ]},
            {"label": "यूपीएससी पाठ्यक्रम कोर", "type": "branch", "date": "यूपीएससी", "children": [
                {"label": "NPCA योजना: आर्द्रभूमियों और झीलों को मिलाकर जलीय पारिस्थितिकी प्रणालियों के संरक्षण के लिए राष्ट्रीय योजना", "type": "leaf"},
                {"label": "SDG लक्ष्य 6.6: आर्द्रभूमि सहित पानी से संबंधित पारिस्थितिकी प्रणालियों की रक्षा और उन्हें बहाल करने का लक्ष्य", "type": "leaf"}
            ]}
        ]
    },
    "conservation-of-coral-reef": {
        "en": [
            {"label": "Restoration Techniques", "type": "branch", "date": "Restoration", "children": [
                {"label": "Biorock Technology: Passing low voltage electrical currents through steel structures to accelerate reef calcification", "type": "leaf"},
                {"label": "Coral Nurseries: Growing coral fragments in land/ocean nurseries and transplanting onto damaged reef beds", "type": "leaf"}
            ]},
            {"label": "Threat Mitigation", "type": "branch", "date": "Mitigation", "children": [
                {"label": "Marine Protected Areas (MPAs): Restricting bottom trawling and commercial diving in reef zones", "type": "leaf"},
                {"label": "Sediment Control: Restricting coastal construction runoff which smothers coral polyps", "type": "leaf"}
            ]},
            {"label": "Indian Conservation Hubs", "type": "branch", "date": "India Hubs", "children": [
                {"label": "Gulf of Mannar: Extensive biorock installation projects funded by government and NGOs", "type": "leaf"},
                {"label": "Lakshadweep & Andamans: Coral monitoring cells tracking sea surface temperature anomalies", "type": "leaf"}
            ]},
            {"label": "UPSC Syllabus Core", "type": "branch", "date": "UPSC Core", "children": [
                {"label": "Legal Status: Corals protected under Schedule I of Wildlife Protection Act 1972", "type": "leaf"},
                {"label": "ICRI Network: International Coral Reef Initiative promoting global conservation policies", "type": "leaf"}
            ]}
        ],
        "hi": [
            {"label": "बहाली तकनीकें", "type": "branch", "date": "बहाली", "children": [
                {"label": "बायोरॉक तकनीक: प्रवाल निर्माण में तेजी लाने के लिए इस्पात संरचनाओं के माध्यम से कम वोल्टेज विद्युत प्रवाह पारित करना", "type": "leaf"},
                {"label": "प्रवाल नर्सरी: नर्सरी में प्रवाल के टुकड़ों को उगाना और क्षतिग्रस्त बेडों पर उनका प्रत्यारोपण करना", "type": "leaf"}
            ]},
            {"label": "खतरे का शमन", "type": "branch", "date": "शमन", "children": [
                {"label": "समुद्री संरक्षित क्षेत्र (MPA): प्रवाल क्षेत्रों में वाणिज्यिक डाइविंग और नीचे जाल डालने (Trawling) को प्रतिबंधित करना", "type": "leaf"},
                {"label": "तलछट नियंत्रण: तटीय निर्माण के मलबे को प्रतिबंधित करना जो प्रवाल पॉलिप्स का दम घोटता है", "type": "leaf"}
            ]},
            {"label": "भारतीय संरक्षण केंद्र", "type": "branch", "date": "भारतीय केंद्र", "children": [
                {"label": "मन्नार की खाड़ी: सरकार और गैर सरकारी संगठनों द्वारा वित्त पोषित व्यापक बायोरॉक परियोजनाएं", "type": "leaf"},
                {"label": "लक्षद्वीप और अंडमान: समुद्र की सतह के तापमान की विसंगतियों पर नज़र रखने वाले प्रवाल निगरानी सेल", "type": "leaf"}
            ]},
            {"label": "यूपीएससी पाठ्यक्रम कोर", "type": "branch", "date": "यूपीएससी", "children": [
                {"label": "कानूनी स्थिति: वन्यजीव संरक्षण अधिनियम 1972 की अनुसूची I के तहत प्रवाल संरक्षित हैं", "type": "leaf"},
                {"label": "ICRI नेटवर्क: वैश्विक संरक्षण नीतियों को बढ़ावा देने वाली अंतर्राष्ट्रीय प्रवाल भित्ति पहल", "type": "leaf"}
            ]}
        ]
    },
    "coral-reef": {
        "en": [
            {"label": "Symbiotic Biology", "type": "branch", "date": "Biology", "children": [
                {"label": "Mutualism: Coral polyps (secrete CaCO3) and photosynthetic Zooxanthellae algae", "type": "leaf"},
                {"label": "Nutrient Exchange: Algae provides organic nutrients; polyps provide shelter and metabolic waste products", "type": "leaf"}
            ]},
            {"label": "Environmental Requirements", "type": "branch", "date": "Growth Requirements", "children": [
                {"label": "Temperature: Warm ocean waters ranging between 20°C to 28°C", "type": "leaf"},
                {"label": "Light & Salinity: High sunlight (shallow photic zone <50m) and stable saline waters (27-30 ppt)", "type": "leaf"}
            ]},
            {"label": "Biodiversity Hotspot", "type": "branch", "date": "Ecological Role", "children": [
                {"label": "Rainforests of Sea: Occupy less than 0.1% of ocean floor but host 25% of all marine species", "type": "leaf"},
                {"label": "Indian Locations: Gulf of Mannar, Lakshadweep (atolls), Gulf of Kutch, and Andaman & Nicobar", "type": "leaf"}
            ]},
            {"label": "UPSC Core Questions", "type": "branch", "date": "UPSC Core", "children": [
                {"label": "Darwin Subsidence Theory: Explains evolutionary progression from fringing -> barrier -> atoll reefs", "type": "leaf"},
                {"label": "Schedule I Status: Maximum legal protection in India due to high ecological vulnerability", "type": "leaf"}
            ]}
        ],
        "hi": [
            {"label": "सहजीवी जीव विज्ञान", "type": "branch", "date": "जीव विज्ञान", "children": [
                {"label": "सहोपकारिता: प्रवाल पॉलिप (CaCO3 स्रावित करते हैं) और प्रकाश संश्लेषक ज़ूक्सैंथेले शैवाल", "type": "leaf"},
                {"label": "पोषक तत्व विनिमय: शैवाल कार्बनिक पोषक तत्व प्रदान करता है; पॉलिप आश्रय और अपशिष्ट प्रदान करते हैं", "type": "leaf"}
            ]},
            {"label": "पर्यावरणीय आवश्यकताएं", "type": "branch", "date": "विकास दशाएं", "children": [
                {"label": "तापमान: 20°C से 28°C के बीच गर्म महासागरीय जल", "type": "leaf"},
                {"label": "प्रकाश और लवणता: उच्च सूर्यप्रकाश (उथला क्षेत्र <50m) और स्थिर खारा पानी (27-30 ppt)", "type": "leaf"}
            ]},
            {"label": "जैव विविधता हॉटस्पॉट", "type": "branch", "date": "पारिस्थितिक भूमिका", "children": [
                {"label": "समुद्र के वर्षावन: समुद्र तल के 0.1% से भी कम हिस्से पर हैं लेकिन 25% समुद्री प्रजातियों का घर हैं", "type": "leaf"},
                {"label": "भारतीय स्थान: मन्नार की खाड़ी, लक्षद्वीप (प्रवाल द्वीप), कच्छ की खाड़ी, और अंडमान व निकोबार", "type": "leaf"}
            ]},
            {"label": "यूपीएससी मुख्य प्रश्न", "type": "branch", "date": "यूपीएससी", "children": [
                {"label": "डार्विन का अवतलन सिद्धांत: तटीय भित्ति से अवरोधक भित्ति और फिर एटोल के विकास की व्याख्या करता है", "type": "leaf"},
                {"label": "अनुसूची I स्थिति: उच्च पारिस्थितिक संवेदनशीलता के कारण भारत में अधिकतम कानूनी सुरक्षा प्राप्त", "type": "leaf"}
            ]}
        ]
    },
    "deserts": {
        "en": [
            {"label": "Climatic Limits", "type": "branch", "date": "Climatic Limits", "children": [
                {"label": "Precipitation: Extremely arid; annual rainfall is less than 25 cm with high evaporation rates", "type": "leaf"},
                {"label": "Temperature: Hot deserts (e.g. Thar, Sahara) vs Cold deserts (e.g. Ladakh, Gobi)", "type": "leaf"}
            ]},
            {"label": "Xerophytic Adaptations", "type": "branch", "date": "Adaptations", "children": [
                {"label": "Leaves: Reduced to spines to minimize transpiration; thick waxy cuticles", "type": "leaf"},
                {"label": "Roots: Deep taproot systems reaching water table; succulent stems (water storage)", "type": "leaf"}
            ]},
            {"label": "Faunal Adaptations", "type": "branch", "date": "Fauna", "children": [
                {"label": "Nocturnal Habits: Animals active during cooler night hours; burrowing behavior", "type": "leaf"},
                {"label": "Physiology: Concentration of urine; fat storage in humps (e.g. Camel)", "type": "leaf"}
            ]},
            {"label": "UPSC Syllabus Core", "type": "branch", "date": "UPSC Core", "children": [
                {"label": "Desertification: Land degradation in drylands; monitored under UNCCD; India's restoration goals", "type": "leaf"},
                {"label": "Thar Desert: Most densely populated desert globally; unique pastoralism and solar potential", "type": "leaf"}
            ]}
        ],
        "hi": [
            {"label": "जलवायु सीमाएं", "type": "branch", "date": "जलवायु", "children": [
                {"label": "वर्षा: अत्यधिक शुष्क; वार्षिक वर्षा 25 सेमी से कम और वाष्पीकरण दर बहुत अधिक", "type": "leaf"},
                {"label": "तापमान: गर्म मरुस्थल (जैसे थार, सहारा) बनाम ठंडे मरुस्थल (जैसे लद्दाख, गोबी)", "type": "leaf"}
            ]},
            {"label": "मरुद्भिद (Xerophytic) अनुकूलन", "type": "branch", "date": "अनुकूलन", "children": [
                {"label": "पत्तियां: वाष्पोत्सर्जन को कम करने के लिए कांटों में रूपांतरित; मोटी मोमी परत (क्यूटिकल)", "type": "leaf"},
                {"label": "जड़ें: जल स्तर तक पहुँचने वाली गहरी जड़ें; मांसल तने (जल संचय)", "type": "leaf"}
            ]},
            {"label": "जीव अनुकूलन", "type": "branch", "date": "जीव अनुकूलन", "children": [
                {"label": "निशाचर आदतें: ठंडी रात के समय जीव सक्रिय होते हैं; बिलों में रहने का व्यवहार", "type": "leaf"},
                {"label": "शरीर क्रिया विज्ञान: मूत्र का सांद्रण; कूबड़ में वसा का संचय (जैसे ऊँट)", "type": "leaf"}
            ]},
            {"label": "यूपीएससी पाठ्यक्रम कोर", "type": "branch", "date": "यूपीएससी", "children": [
                {"label": "मरुस्थलीकरण: शुष्क भूमि में भूमि क्षरण; UNCCD के तहत निगरानी; भारत का बहाली लक्ष्य", "type": "leaf"},
                {"label": "थार मरुस्थल: विश्व स्तर पर सबसे सघन आबादी वाला मरुस्थल; अद्वितीय पशुपालन और सौर क्षमता", "type": "leaf"}
            ]}
        ]
    },
    "dry-deciduous-forest": {
        "en": [
            {"label": "Climatic Parameters", "type": "branch", "date": "Climate", "children": [
                {"label": "Rainfall Limits: Annual precipitation between 70 cm to 100 cm", "type": "leaf"},
                {"label": "Transition Zones: Sits between moist deciduous forests and tropical thorn forests", "type": "leaf"}
            ]},
            {"label": "Vegetative Traits", "type": "branch", "date": "Vegetation", "children": [
                {"label": "Leaf Shedding: Trees shed leaves completely for 6 to 8 weeks in dry spring/summer", "type": "leaf"},
                {"label": "Structure: Open canopy; low height; undergrowth of grasses and shrubs", "type": "leaf"}
            ]},
            {"label": "Dominant Flora Species", "type": "branch", "date": "Flora Species", "children": [
                {"label": "Key Trees: Teak, Tendu, Amaltas, Bel, Khair, and Palas (Flame of the Forest)", "type": "leaf"},
                {"label": "Ecology: High resilience to drought; bark adapts to fire resistance", "type": "leaf"}
            ]},
            {"label": "UPSC India Distribution", "type": "branch", "date": "UPSC Core", "children": [
                {"label": "Geographical Range: Large parts of peninsular India, Uttar Pradesh, Bihar, and Madhya Pradesh", "type": "leaf"},
                {"label": "Human Pressure: Highly cleared for agriculture and heavily grazed by livestock", "type": "leaf"}
            ]}
        ],
        "hi": [
            {"label": "जलवायु कारक", "type": "branch", "date": "जलवायु", "children": [
                {"label": "वर्षा सीमा: वार्षिक वर्षा 70 सेमी से 100 सेमी के बीच", "type": "leaf"},
                {"label": "संक्रमण क्षेत्र: नम पर्णपाती वनों और उष्णकटिबंधीय कांटेदार वनों के बीच की स्थिति", "type": "leaf"}
            ]},
            {"label": "वनस्पति विशेषताएं", "type": "branch", "date": "वनस्पति", "children": [
                {"label": "पर्णपात: शुष्क वसंत/गर्मियों में पेड़ 6 से 8 सप्ताह के लिए पत्तियां पूरी तरह से गिरा देते हैं", "type": "leaf"},
                {"label": "संरचना: खुला वितान; कम ऊंचाई; घास और झाड़ियों का घना निचला स्तर", "type": "leaf"}
            ]},
            {"label": "प्रमुख वनस्पति प्रजातियाँ", "type": "branch", "date": "प्रजातियां", "children": [
                {"label": "प्रमुख वृक्ष: सागौन, तेंदू, अमलतास, बेल, खैर, और पलाश (जंगल की आग)", "type": "leaf"},
                {"label": "पारिस्थितिकी: सूखे के प्रति उच्च लचीलापन; आग प्रतिरोधी छाल का अनुकूलन", "type": "leaf"}
            ]},
            {"label": "यूपीएससी भारत वितरण", "type": "branch", "date": "यूपीएससी", "children": [
                {"label": "भौगोलिक सीमा: प्रायद्वीपीय भारत के बड़े हिस्से, उत्तर प्रदेश, बिहार और मध्य प्रदेश", "type": "leaf"},
                {"label": "मानव दबाव: कृषि के लिए बड़े पैमाने पर सफ़ाई और पशुधन द्वारा अत्यधिक चराई", "type": "leaf"}
            ]}
        ]
    },
    "estuaries": {
        "en": [
            {"label": "Definition & Physics", "type": "branch", "date": "Physics", "children": [
                {"label": "Definition: Semi-enclosed coastal body of water where freshwater meets saline sea water", "type": "leaf"},
                {"label": "Dynamic Salinity: Fluctuates daily due to tidal actions; creates unique osmotic stress", "type": "leaf"}
            ]},
            {"label": "Primary Productivity", "type": "branch", "date": "Productivity", "children": [
                {"label": "Nutrient Trap: Estuarine circulation traps nutrients brought down by rivers", "type": "leaf"},
                {"label": "High Yield: Supported by phytoplankton, salt marshes, and seagrasses", "type": "leaf"}
            ]},
            {"label": "Types of Estuaries", "type": "branch", "date": "Types", "children": [
                {"label": "Coastal Plain: Formed by rising sea level flooding river valleys (e.g. Chesapeake Bay)", "type": "leaf"},
                {"label": "Tectonic & Fjord: Created by land subsidence or glacial carving (e.g. San Francisco Bay)", "type": "leaf"}
            ]},
            {"label": "UPSC Core Ecology", "type": "branch", "date": "UPSC Core", "children": [
                {"label": "Buffer Zone: Acts as a nursery for marine fish and shellfish; absorbs coastal storm energy", "type": "leaf"},
                {"label": "Conservation: Protected under Coastal Regulation Zone (CRZ) rules; highly sensitive to silting", "type": "leaf"}
            ]}
        ],
        "hi": [
            {"label": "परिभाषा और भौतिकी", "type": "branch", "date": "भौतिकी", "children": [
                {"label": "परिभाषा: अर्ध-बंद तटीय जल निकाय जहाँ नदियों का मीठा जल समुद्र के खारे पानी से मिलता है", "type": "leaf"},
                {"label": "गतिशील लवणता: ज्वारीय क्रियाओं के कारण प्रतिदिन उतार-चढ़ाव; अद्वितीय ऑस्मोटिक दबाव पैदा करता है", "type": "leaf"}
            ]},
            {"label": "प्राथमिक उत्पादकता", "type": "branch", "date": "उत्पादकता", "children": [
                {"label": "पोषक तत्व जाल: ज्वारनदमुख परिसंचरण नदियों द्वारा बहाकर लाए गए पोषक तत्वों को रोकता है", "type": "leaf"},
                {"label": "उच्च उपज: फाइटोप्लांकटन, नमक दलदल और समुद्री घास द्वारा समर्थित", "type": "leaf"}
            ]},
            {"label": "ज्वारनदमुख के प्रकार", "type": "branch", "date": "प्रकार", "children": [
                {"label": "तटीय मैदान: समुद्र के बढ़ते स्तर से नदी घाटियों में बाढ़ आने से निर्मित (जैसे चेसापीक खाड़ी)", "type": "leaf"},
                {"label": "विवर्तनिक और फियोर्ड: भूमि के धंसने या हिमनद के कटाव से निर्मित (जैसे सैन फ्रांसिस्को खाड़ी)", "type": "leaf"}
            ]},
            {"label": "यूपीएससी कोर पारिस्थितिकी", "type": "branch", "date": "यूपीएससी", "children": [
                {"label": "बफर जोन: समुद्री मछलियों और शंखधारियों के लिए नर्सरी का कार्य; तटीय तूफान ऊर्जा को सोखता है", "type": "leaf"},
                {"label": "संरक्षण: तटीय विनियमन क्षेत्र (CRZ) नियमों के तहत संरक्षित; गाद के प्रति अत्यधिक संवेदनशील", "type": "leaf"}
            ]}
        ]
    },
    "eutrophication": {
        "en": [
            {"label": "Causes & Sources", "type": "branch", "date": "Causes", "children": [
                {"label": "Nutrient Inflow: Runoff rich in Nitrates and Phosphates from agricultural fertilizers and municipal waste", "type": "leaf"},
                {"label": "Accelerators: Warm temperatures, stagnant waters, and low flow conditions", "type": "leaf"}
            ]},
            {"label": "Chemical Succession", "type": "branch", "date": "Succession", "children": [
                {"label": "Bloom Induction: Algal populations multiply rapidly, blocking sunlight penetration", "type": "leaf"},
                {"label": "Decomposition Cycle: Dead algae decompose via aerobic bacteria, consuming dissolved oxygen (DO)", "type": "leaf"}
            ]},
            {"label": "Ecological Consequences", "type": "branch", "date": "Consequences", "children": [
                {"label": "Hypoxia: DO drops below 2-3 mg/L, suffocating fish and shellfish", "type": "leaf"},
                {"label": "Loss of Species: Highly tolerant species (e.g. blue-green algae) dominate, wiping out endemic biodiversity", "type": "leaf"}
            ]},
            {"label": "UPSC Remediation Core", "type": "branch", "date": "UPSC Core", "children": [
                {"label": "Restoration: Bioremediation, aeration, weed harvesting, and establishing riparian buffer strips", "type": "leaf"},
                {"label": "Policy: Strict effluent discharge regulations and agricultural nutrient management", "type": "leaf"}
            ]}
        ],
        "hi": [
            {"label": "कारण और स्रोत", "type": "branch", "date": "कारण", "children": [
                {"label": "पोषक तत्व प्रवाह: कृषि उर्वरकों और अपशिष्ट से नाइट्रेट्स और फॉस्फेट्स से भरपूर अपवाह", "type": "leaf"},
                {"label": "त्वरक: गर्म तापमान, स्थिर पानी और कम प्रवाह की स्थिति ब्लूम को तेज करती है", "type": "leaf"}
            ]},
            {"label": "रासायनिक अनुक्रम", "type": "branch", "date": "अनुक्रम", "children": [
                {"label": "ब्लूम प्रेरण: शैवाल की आबादी तेजी से बढ़ती है, जिससे सूर्य के प्रकाश का प्रवेश रुक जाता है", "type": "leaf"},
                {"label": "अपघटन चक्र: मृत शैवाल वायवीय जीवाणुओं द्वारा अपघटित होते हैं, जिससे ऑक्सीजन (DO) का उपभोग होता है", "type": "leaf"}
            ]},
            {"label": "पारिस्थितिक परिणाम", "type": "branch", "date": "परिणाम", "children": [
                {"label": "हाइपोक्सिया: DO 2-3 mg/L से नीचे गिर जाता है, जिससे मछलियों का दम घुटने लगता है", "type": "leaf"},
                {"label": "प्रजाति हानि: अत्यधिक सहनशील प्रजातियां (जैसे नीले-हरे शैवाल) हावी हो जाती हैं, विविधता समाप्त होती है", "type": "leaf"}
            ]},
            {"label": "यूपीएससी शमन रणनीतियाँ", "type": "branch", "date": "यूपीएससी", "children": [
                {"label": "बहाली: बायोरेमेडिएशन, वातन (Aeration), खरपतवार निकालना और रिपेरियन बफर स्ट्रिप्स स्थापित करना", "type": "leaf"},
                {"label": "नीति: सख्त अपशिष्ट निर्वहन नियम और कृषि पोषक तत्व प्रबंधन नीतियां", "type": "leaf"}
            ]}
        ]
    },
    "forest-ecosystem-in-india": {
        "en": [
            {"label": "Forest Typology", "type": "branch", "date": "Typology", "children": [
                {"label": "Champion & Seth Classification: Categorizes Indian forests into 16 major groups", "type": "leaf"},
                {"label": "Dominant Type: Tropical Deciduous (both moist and dry) covers the largest share", "type": "leaf"}
            ]},
            {"label": "Ecological Functions", "type": "branch", "date": "Functions", "children": [
                {"label": "Carbon Sequestration: India's forests act as crucial sinks absorbing greenhouse gases", "type": "leaf"},
                {"label": "Soil & Water: Prevents soil erosion in Himalayas, regulates peninsular river flows", "type": "leaf"}
            ]},
            {"label": "Major Threat Pressures", "type": "branch", "date": "Threats", "children": [
                {"label": "Encroachment: Diversion of forest lands for mining, dams, and highways", "type": "leaf"},
                {"label": "Degradation: Fuelwood extraction, overgrazing, forest fires, and invasive weeds", "type": "leaf"}
            ]},
            {"label": "UPSC Regulatory Frame", "type": "branch", "date": "UPSC Core", "children": [
                {"label": "Biennial ISFR: Forest Survey of India publishes forest cover estimates; current target is 33% of area", "type": "leaf"},
                {"label": "Forest Conservation: Forest Conservation Act governs non-forest land diversions", "type": "leaf"}
            ]}
        ],
        "hi": [
            {"label": "वन प्रकार प्रणाली", "type": "branch", "date": "वर्गीकरण", "children": [
                {"label": "चैंपियन और सेठ वर्गीकरण: भारतीय वनों को 16 प्रमुख समूहों में वर्गीकृत करता है", "type": "leaf"},
                {"label": "प्रमुख प्रकार: उष्णकटिबंधीय पर्णपाती (नम और शुष्क दोनों) सबसे बड़े हिस्से को कवर करते हैं", "type": "leaf"}
            ]},
            {"label": "पारिस्थितिक कार्य", "type": "branch", "date": "कार्य", "children": [
                {"label": "कार्बन सिंक: भारत के वन ग्रीनहाउस गैसों को अवशोषित करने वाले महत्वपूर्ण सिंक के रूप में कार्य करते हैं", "type": "leaf"},
                {"label": "मृदा और जल: हिमालय में मृदा अपरदन को रोकता है, प्रायद्वीपीय नदियों के प्रवाह को नियंत्रित करता है", "type": "leaf"}
            ]},
            {"label": "प्रमुख खतरे", "type": "branch", "date": "खतरे", "children": [
                {"label": "अतिक्रमण: खनन, बांधों और राजमार्गों के लिए वन भूमि का गैर-वन उपयोग", "type": "leaf"},
                {"label": "क्षरण: ईंधन की लकड़ी निकालना, अतिचारण, जंगल की आग और आक्रामक खरपतवार", "type": "leaf"}
            ]},
            {"label": "यूपीएससी नियामक ढांचा", "type": "branch", "date": "यूपीएससी", "children": [
                {"label": "द्विवार्षिक ISFR: भारतीय वन सर्वेक्षण वन आवरण का अनुमान प्रकाशित करता है; वर्तमान लक्ष्य 33% है", "type": "leaf"},
                {"label": "वन संरक्षण: वन संरक्षण अधिनियम गैर-वन भूमि डायवर्जन को नियंत्रित करता है", "type": "leaf"}
            ]}
        ]
    },
    "freshwater-ecosystem": {
        "en": [
            {"label": "Classification Schemes", "type": "branch", "date": "Classifications", "children": [
                {"label": "Lentic Systems: Standing water environments including lakes, ponds, bogs, and swamps", "type": "leaf"},
                {"label": "Lotic Systems: Running water environments including rivers, streams, and brooks", "type": "leaf"}
            ]},
            {"label": "Thermal Stratification", "type": "branch", "date": "Stratification", "children": [
                {"label": "Vertical Layers: Epilimnion (warm surface), Thermocline (rapid change), and Hypolimnion (cold bottom)", "type": "leaf"},
                {"label": "Turnover: Seasonal mixing of nutrients and oxygen during spring and autumn", "type": "leaf"}
            ]},
            {"label": "Freshwater Biota", "type": "branch", "date": "Biota", "children": [
                {"label": "Producers: Phytoplankton, macrophytes (rooted and floating plants like water lilies)", "type": "leaf"},
                {"label": "Consumers: Benthic invertebrates, amphibians, and freshwater fish (e.g. Rohu, Catla)", "type": "leaf"}
            ]},
            {"label": "UPSC Conservation Focus", "type": "branch", "date": "UPSC Core", "children": [
                {"label": "NPCA Scheme: Unified program for conservation of lakes and wetlands in India", "type": "leaf"},
                {"label": "Water Quality Indices: Dissolved Oxygen (DO) and Biological Oxygen Demand (BOD) monitoring parameters", "type": "leaf"}
            ]}
        ],
        "hi": [
            {"label": "वर्गीकरण योजनाएं", "type": "branch", "date": "वर्गीकरण", "children": [
                {"label": "स्थिर जल (Lentic): शांत पानी का पर्यावरण जिसमें झीलें, तालाब और दलदल शामिल हैं", "type": "leaf"},
                {"label": "बहता जल (Lotic): बहते पानी का पर्यावरण जिसमें नदियाँ, जलधाराएँ शामिल हैं", "type": "leaf"}
            ]},
            {"label": "तापीय स्तरीकरण", "type": "branch", "date": "स्तरीकरण", "children": [
                {"label": "लंबवत परतें: एपिलिम्नियन (गर्म सतह), थर्मोक्लाइन (तीव्र परिवर्तन), और हाइपोलिम्नियन (ठंडा तल)", "type": "leaf"},
                {"label": "ओवरटर्न: वसंत और शरद ऋतु के दौरान पोषक तत्वों और ऑक्सीजन का मौसमी मिश्रण", "type": "leaf"}
            ]},
            {"label": "अलवणजलीय जीव", "type": "branch", "date": "जीव", "children": [
                {"label": "उत्पादक: फाइटोप्लांकटन, मैक्रोफाइट्स (जड़ वाले और तैरते हुए पौधे जैसे जलकुंभी)", "type": "leaf"},
                {"label": "उपभोक्ता: नितल अकशेरुकी (Benthic), उभयचर, और मीठे पानी की मछलियां (जैसे रोहू, कतला)", "type": "leaf"}
            ]},
            {"label": "यूपीएससी संरक्षण फोकस", "type": "branch", "date": "यूपीएससी", "children": [
                {"label": "NPCA योजना: भारत में झीलों और आर्द्रभूमियों के संरक्षण के लिए एकीकृत कार्यक्रम", "type": "leaf"},
                {"label": "जल गुणवत्ता संकेतक: घुलनशील ऑक्सीजन (DO) और जैविक ऑक्सीजन मांग (BOD) निगरानी मापदंड", "type": "leaf"}
            ]}
        ]
    },
    "grasslands": {
        "en": [
            {"label": "Global Classification", "type": "branch", "date": "Classification", "children": [
                {"label": "Tropical Grasslands: Warm climates; seasonal drought; tree-dotted (e.g. Savannas)", "type": "leaf"},
                {"label": "Temperate Grasslands: Continental interiors; cold winters; treeless (e.g. Steppes, Prairies)", "type": "leaf"}
            ]},
            {"label": "Ecological Adaptations", "type": "branch", "date": "Adaptations", "children": [
                {"label": "Grasses: Basal meristem growth (can regrow after grazing or fires); deep fibrous roots", "type": "leaf"},
                {"label": "Fauna: High speed running (cursorial) adaptations; burrowing habits", "type": "leaf"}
            ]},
            {"label": "Indian Grassland Ecosystems", "type": "branch", "date": "India Grasslands", "children": [
                {"label": "Semi-arid Plain: Shola grasslands in Western Ghats; Terai grasslands in Himalayan foothills", "type": "leaf"},
                {"label": "Faunal Indicators: Great Indian Bustard (critically endangered), Indian One-horned Rhino", "type": "leaf"}
            ]},
            {"label": "UPSC Degradation Focus", "type": "branch", "date": "UPSC Core", "children": [
                {"label": "Overgrazing: Leads to soil compaction, erosion, and weed invasion (e.g. Prosopis juliflora)", "type": "leaf"},
                {"label": "Conservation: Lack of a dedicated national grassland policy in India; highly neglected ecosystem", "type": "leaf"}
            ]}
        ],
        "hi": [
            {"label": "वैश्विक वर्गीकरण", "type": "branch", "date": "वर्गीकरण", "children": [
                {"label": "उष्णकटिबंधीय घास के मैदान: गर्म जलवायु; मौसमी सूखा; बिखरे पेड़ (जैसे सवाना)", "type": "leaf"},
                {"label": "शीतोष्ण घास के मैदान: महाद्वीपीय आंतरिक भाग; ठंडी सर्दियाँ; वृक्षविहीन (जैसे स्टेपी, प्रेयरी)", "type": "leaf"}
            ]},
            {"label": "पारिस्थितिक अनुकूलन", "type": "branch", "date": "अनुकूलन", "children": [
                {"label": "घास: बेसल मेरिस्टेम विकास (चराई या आग के बाद फिर से उग सकते हैं); गहरी रेशेदार जड़ें", "type": "leaf"},
                {"label": "जीव: तेज गति से दौड़ने (Cursorial) का अनुकूलन; बिल बनाने की आदतें", "type": "leaf"}
            ]},
            {"label": "भारतीय घास के मैदान", "type": "branch", "date": "भारतीय मैदान", "children": [
                {"label": "अर्ध-शुष्क मैदान: पश्चिमी घाट में शोला घास के मैदान; हिमालय की तलहटी में तराई घास के मैदान", "type": "leaf"},
                {"label": "जीव संकेतक: महान भारतीय सारंग (GIB - गंभीर रूप से लुप्तप्राय), भारतीय एक सींग वाला गेंडा", "type": "leaf"}
            ]},
            {"label": "यूपीएससी क्षरण फोकस", "type": "branch", "date": "यूपीएससी", "children": [
                {"label": "अतिचारण: मिट्टी के संघनन, क्षरण और खरपतवार के आक्रमण (जैसे प्रोसोपिस जूलिफ्लोरा) की ओर ले जाता है", "type": "leaf"},
                {"label": "संरक्षण: भारत में एक समर्पित राष्ट्रीय घास के मैदान नीति का अभाव; अत्यधिक उपेक्षित पारितंत्र", "type": "leaf"}
            ]}
        ]
    },
    "grasslands-savanna-and-steppe": {
        "en": [
            {"label": "Savanna Dynamics (Tropical)", "type": "branch", "date": "Savanna", "children": [
                {"label": "Climate: Aw type (Koppen); distinct wet and dry seasons; annual fire cycles", "type": "leaf"},
                {"label": "Flora Structure: Coarse grass (Elephant grass) with scattered fire-resistant trees (Acacia, Baobab)", "type": "leaf"}
            ]},
            {"label": "Steppe Dynamics (Temperate)", "type": "branch", "date": "Steppe", "children": [
                {"label": "Climate: Semi-arid BS type; cold dry winters and warm summers; treeless landscape", "type": "leaf"},
                {"label": "Soil Fertility: Dominated by Chernozem/Mollisol soils; highly fertile wheat belts", "type": "leaf"}
            ]},
            {"label": "Faunal Contrast", "type": "branch", "date": "Fauna Comparison", "children": [
                {"label": "Savanna: Large herds of migratory ungulates (wildebeest, zebras) and top carnivores (lions, cheetahs)", "type": "leaf"},
                {"label": "Steppe: Burrowing rodents (prairie dogs), pronghorn, and bison", "type": "leaf"}
            ]},
            {"label": "UPSC Comparative Core", "type": "branch", "date": "UPSC Core", "children": [
                {"label": "Human Impact: Steppes extensively converted to agriculture ('granaries'); Savannas threatened by pastoral overgrazing", "type": "leaf"},
                {"label": "Fire Adaptation: Pyrophytic traits of plants essential for ecosystem nutrient recycling in Savannas", "type": "leaf"}
            ]}
        ],
        "hi": [
            {"label": "सवाना गतिशीलता (उष्णकटिबंधीय)", "type": "branch", "date": "सवाना", "children": [
                {"label": "जलवायु: Aw प्रकार (कोपेन); स्पष्ट गीला और सूखा मौसम; वार्षिक आग चक्र", "type": "leaf"},
                {"label": "वनस्पति संरचना: बिखरे हुए आग-प्रतिरोधी पेड़ों (बबूल, बाओबाब) के साथ खुरदरी घास (हाथी घास)", "type": "leaf"}
            ]},
            {"label": "स्टेपी गतिशीलता (शीतोष्ण)", "type": "branch", "date": "स्टेपी", "children": [
                {"label": "जलवायु: अर्ध-शुष्क BS प्रकार; ठंडी शुष्क सर्दियाँ और गर्मियाँ; वृक्षविहीन परिदृश्य", "type": "leaf"},
                {"label": "मृदा उर्वरता: चेरनोज़ेम/मॉलिसोल मिट्टी का प्रभुत्व; अत्यधिक उपजाऊ गेहूं बेल्ट (विश्व की टोकरी)", "type": "leaf"}
            ]},
            {"label": "जीवों में अंतर", "type": "branch", "date": "जीव अंतर", "children": [
                {"label": "सवाना: प्रवासी शाकाहारियों (ज़ेबरा, विल्डेबीस्ट) के बड़े झुंड और शीर्ष मांसाहारी (शेर, चीता)", "type": "leaf"},
                {"label": "स्टेपी: बिल बनाने वाले कृंतक (प्रेयरी कुत्ते), प्रोंगहॉर्न और बाइसन", "type": "leaf"}
            ]},
            {"label": "यूपीएससी तुलनात्मक कोर", "type": "branch", "date": "यूपीएससी", "children": [
                {"label": "मानव प्रभाव: स्टेपीज को बड़े पैमाने पर कृषि में बदला गया; सवाना अतिचारण से संकट में है", "type": "leaf"},
                {"label": "अग्नि अनुकूलन: सवाना में पारितंत्र पोषक तत्व पुनर्चक्रण के लिए पौधों के पाइरोफाइटिक लक्षण आवश्यक हैं", "type": "leaf"}
            ]}
        ]
    },
    "human-modified-ecosystems": {
        "en": [
            {"label": "Characteristics", "type": "branch", "date": "Characteristics", "children": [
                {"label": "Low Biodiversity: Highly simplified food webs dominated by selected crops or urban weeds", "type": "leaf"},
                {"label": "External Energy: High dependence on fossil fuels, synthetic fertilizers, and water infrastructure", "type": "leaf"}
            ]},
            {"label": "Major Types", "type": "branch", "date": "Types", "children": [
                {"label": "Croplands: Agroecosystems managed for monoculture grain/cash crop production", "type": "leaf"},
                {"label": "Aquaculture: Artificial fish ponds and marine pens replacing coastal wetlands", "type": "leaf"},
                {"label": "Urban Zones: Concrete structures with altered microclimates (Urban Heat Islands)", "type": "leaf"}
            ]},
            {"label": "Ecological Side-effects", "type": "branch", "date": "Consequences", "children": [
                {"label": "Soil Degradation: Salinization from canal irrigation, erosion of bare soil", "type": "leaf"},
                {"label": "Pollution: Chemical runoffs inducing downstream eutrophication and pesticide toxicity", "type": "leaf"}
            ]},
            {"label": "UPSC Sustainability Core", "type": "branch", "date": "UPSC Core", "children": [
                {"label": "Sustainable Agroecology: Promoting organic farming, permaculture, and urban green spaces", "type": "leaf"},
                {"label": "Circular Economy: Waste-to-energy and sewage recycling in urban ecosystem management", "type": "leaf"}
            ]}
        ],
        "hi": [
            {"label": "लक्षण और विशेषताएं", "type": "branch", "date": "लक्षण", "children": [
                {"label": "कम जैव विविधता: अत्यधिक सरलीकृत खाद्य जाल जिसमें चुनिंदा फसलें या खरपतवार हावी होते हैं", "type": "leaf"},
                {"label": "बाहरी ऊर्जा: जीवाश्म ईंधन, सिंथेटिक उर्वरकों और जल बुनियादी ढांचे पर अत्यधिक निर्भरता", "type": "leaf"}
            ]},
            {"label": "प्रमुख प्रकार", "type": "branch", "date": "प्रमुख प्रकार", "children": [
                {"label": "कृषि भूमि: एकल-फसल अनाज/नकदी फसल उत्पादन के लिए प्रबंधित कृषि पारितंत्र", "type": "leaf"},
                {"label": "जलीय कृषि (Aquaculture): तटीय आर्द्रभूमियों की जगह लेने वाले कृत्रिम मछली तालाब", "type": "leaf"},
                {"label": "शहरी क्षेत्र: परिवर्तित सूक्ष्म जलवायु (शहरी ऊष्मा द्वीप) वाली कंक्रीट संरचनाएं", "type": "leaf"}
            ]},
            {"label": "पारिस्थितिक दुष्प्रभाव", "type": "branch", "date": "दुष्प्रभाव", "children": [
                {"label": "मृदा क्षरण: नहर सिंचाई से लवणीकरण, नग्न मिट्टी का अपरदन", "type": "leaf"},
                {"label": "प्रदूषण: रासायनिक अपवाह जो डाउनस्ट्रीम यूट्रोफिकेशन और कीटनाशक विषाक्तता को प्रेरित करते हैं", "type": "leaf"}
            ]},
            {"label": "यूपीएससी स्थिरता कोर", "type": "branch", "date": "यूपीएससी", "children": [
                {"label": "सतत कृषि पारिस्थितिकी: जैविक खेती, परमाकल्चर और शहरी हरित क्षेत्रों को बढ़ावा देना", "type": "leaf"},
                {"label": "सर्कुलर इकोनॉमी: शहरी पारितंत्र प्रबंधन में कचरे से ऊर्जा और सीवेज का पुनर्चक्रण", "type": "leaf"}
            ]}
        ]
    },
    "importance-of-mangroves": {
        "en": [
            {"label": "Coastal Shield Protection", "type": "branch", "date": "Shield", "children": [
                {"label": "Wave Energy Dissipation: Densely tangled stilt roots reduce wave impact by up to 66%", "type": "leaf"},
                {"label": "Storm Protection: Crucial barriers during supercyclones preventing shoreline breach", "type": "leaf"}
            ]},
            {"label": "Ecological Nursery", "type": "branch", "date": "Nursery", "children": [
                {"label": "Fish Incubators: Acts as spawning grounds for 80% of commercial fish and shellfish species", "type": "leaf"},
                {"label": "Food Webs: Leaf litter detritus fuels extremely rich coastal detrital food chains", "type": "leaf"}
            ]},
            {"label": "Blue Carbon Sequestration", "type": "branch", "date": "Blue Carbon", "children": [
                {"label": "High Sink Capacity: Sequesters up to 10x more carbon per hectare than terrestrial tropical forests", "type": "leaf"},
                {"label": "Soil Storage: Stores carbon in anaerobic soils where decomposition is extremely slow", "type": "leaf"}
            ]},
            {"label": "UPSC Mains Application", "type": "branch", "date": "UPSC Core", "children": [
                {"label": "Tsunami Mitigation: Sunderbans and Pichavaram communities suffered less damage in 2004 Indian Ocean Tsunami", "type": "leaf"},
                {"label": "Economic Valuation: Combines coastal fisheries, timber, honey collection, and ecotourism values", "type": "leaf"}
            ]}
        ],
        "hi": [
            {"label": "तटीय ढाल संरक्षण", "type": "branch", "date": "संरक्षण ढाल", "children": [
                {"label": "लहर ऊर्जा अवशोषण: घनी स्टिल्ट जड़ें लहरों के प्रभाव को 66% तक कम कर देती हैं", "type": "leaf"},
                {"label": "तूफान सुरक्षा: सुपरचक्रवातों के दौरान तटीय रेखा के टूटने को रोकने वाले महत्वपूर्ण अवरोध", "type": "leaf"}
            ]},
            {"label": "पारिस्थितिक नर्सरी", "type": "branch", "date": "नर्सरी", "children": [
                {"label": "मछली इनक्यूबेटर: 80% वाणिज्यिक मछलियों और शंखधारियों के लिए अंडे देने के मैदान के रूप में कार्य", "type": "leaf"},
                {"label": "खाद्य जाल: गिरे हुए पत्ते तटीय खाद्य श्रृंखलाओं को ऊर्जा प्रदान करते हैं", "type": "leaf"}
            ]},
            {"label": "ब्लू कार्बन पृथक्करण", "type": "branch", "date": "ब्लू कार्बन", "children": [
                {"label": "उच्च सिंक क्षमता: स्थलीय उष्णकटिबंधीय वनों की तुलना में प्रति हेक्टेयर 10 गुना अधिक कार्बन सोखते हैं", "type": "leaf"},
                {"label": "मिट्टी में भंडारण: ऑक्सीजन-रहित मिट्टी में कार्बन जमा करते हैं जहां क्षय बहुत धीमा होता है", "type": "leaf"}
            ]},
            {"label": "यूपीएससी मुख्य परीक्षा अनुप्रयोग", "type": "branch", "date": "यूपीएससी", "children": [
                {"label": "सुनामी शमन: सुंदरबन और पिचावरम समुदायों को 2004 की हिंद महासागर सुनामी में बहुत कम नुकसान हुआ था", "type": "leaf"},
                {"label": "आर्थिक मूल्यांकन: तटीय मत्स्य पालन, लकड़ी, शहद संग्रह और पर्यावरण-पर्यटन मूल्यों को जोड़ता है", "type": "leaf"}
            ]}
        ]
    },
    "importance-of-estuaries": {
        "en": [
            {"label": "High Productivity", "type": "branch", "date": "Productivity", "children": [
                {"label": "Ecosystem Services: Nutrient accumulation makes them hotspots for marine and bird life", "type": "leaf"},
                {"label": "Food Source: Supplies massive biomass supporting coastal fisheries", "type": "leaf"}
            ]},
            {"label": "Hydrological Filter", "type": "branch", "date": "Filter", "children": [
                {"label": "Water Purification: Traps sediment and absorbs pollutants before they reach open ocean", "type": "leaf"},
                {"label": "Silt Retention: Natural settling basin reducing coastal water turbidity", "type": "leaf"}
            ]},
            {"label": "Livelihood & Navigation", "type": "branch", "date": "Livelihood", "children": [
                {"label": "Natural Harbors: Safe anchorage zones due to sheltered configurations (e.g., Mumbai Harbor)", "type": "leaf"},
                {"label": "Fisheries Support: Breeding ground for crabs, oysters, prawns, and migratory fish", "type": "leaf"}
            ]},
            {"label": "UPSC Core Significance", "type": "branch", "date": "UPSC Core", "children": [
                {"label": "Carbon Capture: Coastal marshes in estuaries serve as key blue carbon repositories", "type": "leaf"},
                {"label": "Disaster Shield: Wetland vegetation along estuaries dampens storm wave velocities", "type": "leaf"}
            ]}
        ],
        "hi": [
            {"label": "उच्च उत्पादकता", "type": "branch", "date": "उत्पादकता", "children": [
                {"label": "पारितंत्र सेवाएँ: पोषक तत्वों का संचय इन्हें समुद्री और पक्षी जीवन के लिए हॉटस्पॉट बनाता है", "type": "leaf"},
                {"label": "भोजन स्रोत: तटीय मत्स्य पालन का समर्थन करने वाले विशाल जैवभार की आपूर्ति करता है", "type": "leaf"}
            ]},
            {"label": "जल विज्ञान फिल्टर", "type": "branch", "date": "फिल्टर", "children": [
                {"label": "जल शुद्धिकरण: खुले महासागर तक पहुँचने से पहले तलछट को रोकता है और प्रदूषकों को अवशोषित करता है", "type": "leaf"},
                {"label": "गाद प्रतिधारण: तटीय पानी के गंदलेपन को कम करने वाला प्राकृतिक बेसिन", "type": "leaf"}
            ]},
            {"label": "आजीविका और नौवहन", "type": "branch", "date": "आजीविका", "children": [
                {"label": "प्राकृतिक बंदरगाह: सुरक्षित स्थान प्रदान करते हैं (जैसे, मुंबई हार्बर)", "type": "leaf"},
                {"label": "मत्स्य पालन सहायता: केकड़ों, सीपों, झींगों और प्रवासी मछलियों के लिए प्रजनन मैदान", "type": "leaf"}
            ]},
            {"label": "यूपीएससी महत्व", "type": "branch", "date": "यूपीएससी", "children": [
                {"label": "कार्बन कैप्चर: ज्वारनदमुख में तटीय दलदल प्रमुख ब्लू कार्बन रिपॉजिटरी के रूप में कार्य करते हैं", "type": "leaf"},
                {"label": "आपदा ढाल: ज्वारनदमुख के किनारे की वनस्पति तूफान की लहरों की गति को कम करती है", "type": "leaf"}
            ]}
        ]
    },
    "importance-of-wetlands": {
        "en": [
            {"label": "Ecological Kidneys", "type": "branch", "date": "Kidneys", "children": [
                {"label": "Waste Filtration: Absorbs nitrogen, phosphorus, and heavy metals from runoff", "type": "leaf"},
                {"label": "Groundwater Recharge: Acts as sponge holding monsoon water and slowly recharging aquifers", "type": "leaf"}
            ]},
            {"label": "Flood Regulation", "type": "branch", "date": "Flood Regulation", "children": [
                {"label": "Natural Buffers: Stores excess storm runoff, slowing down peak flood waves", "type": "leaf"},
                {"label": "Coastal Defense: Salt marshes and mangroves absorb wave energy", "type": "leaf"}
            ]},
            {"label": "Biodiversity Support", "type": "branch", "date": "Biodiversity", "children": [
                {"label": "Migratory Birds: Key stops on global flyways for wintering waterbirds", "type": "leaf"},
                {"label": "Unique Biota: Supports specialized hydrophytes, molluscs, and amphibians", "type": "leaf"}
            ]},
            {"label": "UPSC Core Application", "type": "branch", "date": "UPSC Core", "children": [
                {"label": "Climate Mitigation: Peatlands cover 3% of land but store 30% of soil carbon", "type": "leaf"},
                {"label": "Livelihood Security: Essential for local agriculture, fishing, and reed harvesting", "type": "leaf"}
            ]}
        ],
        "hi": [
            {"label": "पारिस्थितिक गुर्दे (Ecological Kidneys)", "type": "branch", "date": "पारिस्थितिक गुर्दे", "children": [
                {"label": "अपशिष्ट निस्पंदन: अपवाह से नाइट्रोजन, फास्फोरस और भारी धातुओं को अवशोषित करना", "type": "leaf"},
                {"label": "भूजल पुनर्भरण: मानसून के पानी को सोखने वाले स्पंज की तरह काम करते हैं और भूजल स्तर को बढ़ाते हैं", "type": "leaf"}
            ]},
            {"label": "बाढ़ नियंत्रण", "type": "branch", "date": "बाढ़ नियंत्रण", "children": [
                {"label": "प्राकृतिक बफर: अतिरिक्त तूफानी पानी को जमा करते हैं, जिससे बाढ़ की गति धीमी हो जाती है", "type": "leaf"},
                {"label": "तटीय रक्षा: नमक दलदल और मैंग्रोव तटीय क्षेत्रों में लहरों की गति को मंद करते हैं", "type": "leaf"}
            ]},
            {"label": "जैव विविधता समर्थन", "type": "branch", "date": "जैव विविधता", "children": [
                {"label": "प्रवासी पक्षी: शीतकालीन जलपक्षियों के लिए वैश्विक प्रवासी मार्गों पर प्रमुख पड़ाव", "type": "leaf"},
                {"label": "अद्वितीय जीव: विशेष हाइड्रोफाइट्स, मोलस्क और उभयचरों का समर्थन करते हैं", "type": "leaf"}
            ]},
            {"label": "यूपीएससी अनुप्रयोग", "type": "branch", "date": "यूपीएससी", "children": [
                {"label": "जलवायु शमन: पीटलैंड्स केवल 3% भूमि को कवर करते हैं लेकिन मिट्टी के 30% कार्बन को संचित करते हैं", "type": "leaf"},
                {"label": "आजीविका सुरक्षा: स्थानीय कृषि, मत्स्य पालन और ईख की कटाई के लिए आवश्यक हैं", "type": "leaf"}
            ]}
        ]
    },
    "legal-and-regulatory-approaches-for-mangrove-protection": {
        "en": [
            {"label": "CRZ Guidelines (India)", "type": "branch", "date": "CRZ Rules", "children": [
                {"label": "CRZ-I Classification: Mangroves designated in CRZ-I (Ecologically Sensitive Area) with maximum restrictions", "type": "leaf"},
                {"label": "CRZ Buffer Zone: Mandatory 50m buffer zone around mangrove patches larger than 1000 sq m", "type": "leaf"}
            ]},
            {"label": "Wildlife Protection Act", "type": "branch", "date": "Wildlife Act", "children": [
                {"label": "Protected Status: Specific mangrove areas declared as National Parks/Sanctuaries (e.g. Bhitarkanika)", "type": "leaf"},
                {"label": "Destruction Ban: Clearing or felling mangroves in protected coastal tracts is a cognizable offense", "type": "leaf"}
            ]},
            {"label": "Forest Conservation Act", "type": "branch", "date": "Forest Act", "children": [
                {"label": "Diversion Restraints: Diversion of mangrove forests for non-forest activities requires central clearance", "type": "leaf"},
                {"label": "Compensatory Afforestation: Mandates compensatory planting if any mangrove tract is diverted", "type": "leaf"}
            ]},
            {"label": "UPSC Regulatory Analysis", "type": "branch", "date": "UPSC Core", "children": [
                {"label": "Enforcement Challenges: Monitoring remote coastal tracts, illegal aquaculture conversions", "type": "leaf"},
                {"label": "Judicial Activism: NGT (National Green Tribunal) rulings ordering restoration of destroyed mangroves", "type": "leaf"}
            ]}
        ],
        "hi": [
            {"label": "CRZ दिशानिर्देश (भारत)", "type": "branch", "date": "CRZ दिशानिर्देश", "children": [
                {"label": "CRZ-I वर्गीकरण: मैंग्रोव को अधिकतम प्रतिबंधों के साथ संवेदनशील CRZ-I श्रेणी में रखा गया है", "type": "leaf"},
                {"label": "CRZ बफर ज़ोन: 1000 वर्ग मीटर से बड़े मैंग्रोव पैच के चारों ओर अनिवार्य 50 मीटर बफर ज़ोन", "type": "leaf"}
            ]},
            {"label": "वन्यजीव संरक्षण अधिनियम", "type": "branch", "date": "वन्यजीव अधिनियम", "children": [
                {"label": "संरक्षित स्थिति: विशिष्ट मैंग्रोव क्षेत्रों को राष्ट्रीय उद्यान/अभयारण्य घोषित करना (जैसे भीतरकनिका)", "type": "leaf"},
                {"label": "कटाई पर प्रतिबंध: संरक्षित तटीय क्षेत्रों में मैंग्रोव को काटना या नष्ट करना एक संज्ञेय अपराध है", "type": "leaf"}
            ]},
            {"label": "वन संरक्षण अधिनियम", "type": "branch", "date": "वन संरक्षण", "children": [
                {"label": "डायवर्जन प्रतिबंध: गैर-वन गतिविधियों के लिए मैंग्रोव वनों के डायवर्जन के लिए केंद्रीय मंजूरी आवश्यक", "type": "leaf"},
                {"label": "प्रतिपूरक वनीकरण: यदि किसी मैंग्रोव क्षेत्र को डायवर्ट किया जाता है तो अनिवार्य प्रतिपूरक रोपण का नियम", "type": "leaf"}
            ]},
            {"label": "यूपीएससी नियामक विश्लेषण", "type": "branch", "date": "यूपीएससी", "children": [
                {"label": "प्रवर्तन चुनौतियाँ: दूरदराज के तटीय क्षेत्रों की निगरानी, अवैध झींगा मछली पालन में परिवर्तन", "type": "leaf"},
                {"label": "न्यायिक सक्रियता: एनजीटी (NGT) के आदेश जिसमें नष्ट किए गए मैंग्रोव की बहाली का निर्देश दिया गया है", "type": "leaf"}
            ]}
        ]
    },
    "littoral-and-swamp-forests": {
        "en": [
            {"label": "Ecological Profile", "type": "branch", "date": "Profile", "children": [
                {"label": "Definition: Wetlands and swampy delta forests subject to tidal inundation and saline/freshwater mix", "type": "leaf"},
                {"label": "Soils: Heavy, clayey soils rich in organic matter but deficient in oxygen due to waterlogging", "type": "leaf"}
            ]},
            {"label": "Major Subtypes", "type": "branch", "date": "Subtypes", "children": [
                {"label": "Littoral (Coastal): Beach forests dominated by Casuarina and Manilkara along sandy shores", "type": "leaf"},
                {"label": "Swamp (Freshwater): Inundated by freshwater rivers; dominated by Myristica and Syzygium", "type": "leaf"}
            ]},
            {"label": "Adaptations", "type": "branch", "date": "Adaptations", "children": [
                {"label": "Pneumatophores: Blind roots growing upwards to capture oxygen from the air", "type": "leaf"},
                {"label": "Stilt Roots: Prop roots providing stability in shifting coastal mud", "type": "leaf"}
            ]},
            {"label": "UPSC India Distribution", "type": "branch", "date": "UPSC Core", "children": [
                {"label": "Key Locations: Ganga-Brahmaputra Delta (Sunderbans), Mahanadi, Godavari, and Krishna deltas", "type": "leaf"},
                {"label": "Threats: Land reclamation for agriculture, salinity changes due to upstream dams", "type": "leaf"}
            ]}
        ],
        "hi": [
            {"label": "पारिस्थितिक प्रोफ़ाइल", "type": "branch", "date": "प्रोफ़ाइल", "children": [
                {"label": "परिभाषा: दलदली डेल्टा वन जो ज्वारीय जलभराव और खारे/मीठे पानी के मिश्रण के अधीन हैं", "type": "leaf"},
                {"label": "मिट्टी: जैविक पदार्थों से भरपूर भारी, चिकनी मिट्टी लेकिन जलभराव के कारण ऑक्सीजन की कमी", "type": "leaf"}
            ]},
            {"label": "प्रमुख उपप्रकार", "type": "branch", "date": "उपप्रकार", "children": [
                {"label": "तटीय (Littoral): रेतीले तटों के साथ कैसुरीना और मणिलकारा के प्रभुत्व वाले समुद्र तटीय वन", "type": "leaf"},
                {"label": "दलदली (Swamp): मीठे पानी की नदियों से जलमग्न; मायिस्टिका और सिज़ीजियम का प्रभुत्व", "type": "leaf"}
            ]},
            {"label": "पारिस्थितिक अनुकूलन", "type": "branch", "date": "अनुकूलन", "children": [
                {"label": "श्वसन जड़ें: हवा से ऑक्सीजन लेने के लिए ऊपर की ओर बढ़ने वाली अंधी जड़ें", "type": "leaf"},
                {"label": "स्टिल्ट जड़ें: दलदली मिट्टी में पेड़ को स्थिरता प्रदान करने वाली सहारा जड़ें", "type": "leaf"}
            ]},
            {"label": "यूपीएससी भारत वितरण", "type": "branch", "date": "यूपीएससी", "children": [
                {"label": "प्रमुख स्थान: गंगा-भ्रमपुत्र डेल्टा (सुंदरवन), महानदी, गोदावरी और कृष्णा डेल्टा क्षेत्र", "type": "leaf"},
                {"label": "खतरे: कृषि के लिए भूमि सुधार, बांधों के कारण खारेपन में बदलाव", "type": "leaf"}
            ]}
        ]
    },
    "mangroves": {
        "en": [
            {"label": "Biological Adaptations", "type": "branch", "date": "Adaptations", "children": [
                {"label": "Halophytic Nature: Salt-tolerant trees growing in intertidal zones of tropical/subtropical coasts", "type": "leaf"},
                {"label": "Viviparity: Seeds germinate while still on parent tree, dropping as propagules to anchor in mud", "type": "leaf"}
            ]},
            {"label": "Pneumatophores & Roots", "type": "branch", "date": "Roots", "children": [
                {"label": "Breathing Roots: Upward-growing roots with lenticels for oxygen exchange in anaerobic soils", "type": "leaf"},
                {"label": "Stilt Roots: Arching roots branching from stems to resist wave action and stabilize muddy substrate", "type": "leaf"}
            ]},
            {"label": "Eco-System Services", "type": "branch", "date": "Services", "children": [
                {"label": "Coastal Defense: Buffers storms, controls erosion, traps river silt to protect coral reefs", "type": "leaf"},
                {"label": "Nurseries: Key habitat for juvenile crabs, prawns, and commercial fish species", "type": "leaf"}
            ]},
            {"label": "UPSC Core Questions", "type": "branch", "date": "UPSC Core", "children": [
                {"label": "Blue Carbon: Extremely high carbon capture efficiency compared to terrestrial forests", "type": "leaf"},
                {"label": "Threats: Aquaculture conversion, wood exploitation, and sea level rise", "type": "leaf"}
            ]}
        ],
        "hi": [
            {"label": "जैविक अनुकूलन", "type": "branch", "date": "अनुकूलन", "children": [
                {"label": "लवणमृदोद्भिद (Halophyte): उष्णकटिबंधीय/उपोष्णकटिबंधीय तटों के ज्वारीय क्षेत्रों में उगने वाले लवण-सहनशील पेड़", "type": "leaf"},
                {"label": "जरायुजता (Viviparity): बीज मूल वृक्ष पर रहते हुए ही अंकुरित होते हैं, दलदल में जमने के लिए प्रोपेग्यूल के रूप में गिरते हैं", "type": "leaf"}
            ]},
            {"label": "न्यूमेटोफोर्स और जड़ें", "type": "branch", "date": "जड़ें", "children": [
                {"label": "श्वसन जड़ें: ऑक्सीजन विनिमय के लिए लेंटीसेल्स के साथ ऊपर की ओर बढ़ने वाली जड़ें", "type": "leaf"},
                {"label": "स्टिल्ट जड़ें: लहरों के प्रभाव का विरोध करने और दलदली आधार को स्थिर करने के लिए तनों से निकलने वाली मेहराबदार जड़ें", "type": "leaf"}
            ]},
            {"label": "पारितंत्र सेवाएँ", "type": "branch", "date": "पारितंत्र सेवाएँ", "children": [
                {"label": "तटीय सुरक्षा: तूफान को रोकता है, कटाव को नियंत्रित करता है, प्रवाल भित्तियों की रक्षा के लिए गाद रोकता है", "type": "leaf"},
                {"label": "नर्सरी: केकड़ों, झींगों और मछलियों की प्रजातियों के लिए प्रमुख आवास", "type": "leaf"}
            ]},
            {"label": "यूपीएससी मुख्य प्रश्न", "type": "branch", "date": "यूपीएससी", "children": [
                {"label": "ब्लू कार्बन: स्थलीय वनों की तुलना में अत्यधिक उच्च कार्बन कैप्चर दक्षता", "type": "leaf"},
                {"label": "खतरे: झींगा पालन (Aquaculture) में परिवर्तन, लकड़ी का दोहन और समुद्र के स्तर में वृद्धि", "type": "leaf"}
            ]}
        ]
    },
    "mangroves-in-india": {
        "en": [
            {"label": "Geographical Range", "type": "branch", "date": "Range", "children": [
                {"label": "Sundarbans: Largest contiguous mangrove forest globally; shared with Bangladesh; Tiger habitat", "type": "leaf"},
                {"label": "Bhitarkanika: Odisha coast; high biodiversity; home to Saltwater Crocodile", "type": "leaf"}
            ]},
            {"label": "Other Key Sites", "type": "branch", "date": "Other Sites", "children": [
                {"label": "Pichavaram: Tamil Nadu; complex boating channels; protected by stilt root systems", "type": "leaf"},
                {"label": "Western Coast: Smaller patches in Goa, Maharashtra, and extensive dwarf mangroves in Gujarat (Kutch)", "type": "leaf"}
            ]},
            {"label": "National Policies", "type": "branch", "date": "Policies", "children": [
                {"label": "CRZ Regulations: Places all mangrove tracts under CRZ-I (Ecologically Sensitive Area)", "type": "leaf"},
                {"label": "MISHTI Scheme: Launched in Budget 2023 for mangrove plantation along India's coastline", "type": "leaf"}
            ]},
            {"label": "UPSC Core Analysis", "type": "branch", "date": "UPSC Core", "children": [
                {"label": "Cyclone Buffer: Sunderbans buffers Kolkata from severe Bay of Bengal cyclones", "type": "leaf"},
                {"label": "Livelihood: Honey collectors (Mouli) and fishermen dependent on mangrove eco-services", "type": "leaf"}
            ]}
        ],
        "hi": [
            {"label": "भौगोलिक सीमा", "type": "branch", "date": "भौगोलिक सीमा", "children": [
                {"label": "सुंदरबन: वैश्विक स्तर पर सबसे बड़ा मैंग्रोव वन; बांग्लादेश के साथ साझा; बाघों का पर्यावास", "type": "leaf"},
                {"label": "भीतरकनिका: ओडिशा तट; उच्च जैव विविधता; लवणीय मगरमच्छों का घर", "type": "leaf"}
            ]},
            {"label": "अन्य प्रमुख स्थल", "type": "branch", "date": "अन्य स्थल", "children": [
                {"label": "पिचावरम: तमिलनाडु; जटिल नौका विहार चैनल; स्टिल्ट रूट सिस्टम द्वारा संरक्षित", "type": "leaf"},
                {"label": "पश्चिमी तट: गोवा, महाराष्ट्र में छोटे पैच और गुजरात (कच्छ) में व्यापक बौने मैंग्रोव", "type": "leaf"}
            ]},
            {"label": "राष्ट्रीय नीतियां", "type": "branch", "date": "नीतियां", "children": [
                {"label": "CRZ नियमन: सभी मैंग्रोव क्षेत्रों को संवेदनशील CRZ-I श्रेणी में रखता है", "type": "leaf"},
                {"label": "मिष्टी योजना: भारत की तटीय रेखा के किनारे मैंग्रोव रोपण के लिए बजट 2023 में शुरू की गई", "type": "leaf"}
            ]},
            {"label": "यूपीएससी कोर विश्लेषण", "type": "branch", "date": "यूपीएससी", "children": [
                {"label": "चक्रवात बफर: सुंदरबन कोलकाता को बंगाल की खाड़ी के चक्रवातों से बचाता है", "type": "leaf"},
                {"label": "आजीविका: शहद संग्रहकर्ता (मौली) और मछुआरे मैंग्रोव पारितंत्र सेवाओं पर निर्भर हैं", "type": "leaf"}
            ]}
        ]
    },
    "mangroves-under-threats": {
        "en": [
            {"label": "Anthropogenic Pressures", "type": "branch", "date": "Human Threats", "children": [
                {"label": "Shrimp Farming: Conversion of mangrove swamps into commercial aquaculture ponds", "type": "leaf"},
                {"label": "Timber Felling: Illegal clearing for firewood, charcoal, and local timber construction", "type": "leaf"}
            ]},
            {"label": "Hydrological Alterations", "type": "branch", "date": "Water Threats", "children": [
                {"label": "Upstream Dams: Reduced freshwater inflow increases salinity, killing sensitive mangrove species", "type": "leaf"},
                {"label": "Siltation Block: Heavy silt deposition blocking the respiratory lenticels of pneumatophores", "type": "leaf"}
            ]},
            {"label": "Climate Change Effects", "type": "branch", "date": "Climate Threats", "children": [
                {"label": "Sea Level Rise: Submergence of seaward fringes beyond the capacity of species to migrate inland", "type": "leaf"},
                {"label": "Severe Weather: Cyclone frequency destroying forest canopy and disrupting soil stability", "type": "leaf"}
            ]},
            {"label": "UPSC Mitigation Core", "type": "branch", "date": "UPSC Core", "children": [
                {"label": "Protection: Strengthening CRZ-I regulations, banning untreated aquaculture effluents", "type": "leaf"},
                {"label": "Restoration: Restoring tidal hydrology through channel desilting and community patrols", "type": "leaf"}
            ]}
        ],
        "hi": [
            {"label": "मानवजनित दबाव", "type": "branch", "date": "मानव जनित", "children": [
                {"label": "झींगा पालन: मैंग्रोव दलदलों को वाणिज्यिक जलीय कृषि तालाबों में बदलना", "type": "leaf"},
                {"label": "लकड़ी की कटाई: जलाऊ लकड़ी, कोयला और स्थानीय निर्माण के लिए अवैध कटाई", "type": "leaf"}
            ]},
            {"label": "जल विज्ञान संबंधी बदलाव", "type": "branch", "date": "जल विज्ञान", "children": [
                {"label": "ऊपरी बांध: मीठे पानी के प्रवाह में कमी से लवणता बढ़ती है, जिससे संवेदनशील प्रजातियां मर जाती हैं", "type": "leaf"},
                {"label": "गाद जमाव: भारी गाद का जमाव न्यूमेटोफोर्स के श्वसन द्वारों (Lenticels) को बंद कर देता है", "type": "leaf"}
            ]},
            {"label": "जलवायु परिवर्तन के प्रभाव", "type": "branch", "date": "जलवायु परिवर्तन", "children": [
                {"label": "समुद्र के स्तर में वृद्धि: प्रजातियों की अंतर्देशीय प्रवास क्षमता से अधिक समुद्र का बढ़ना", "type": "leaf"},
                {"label": "चक्रवात आवृत्ति: तीव्र चक्रवातों द्वारा वनों के वितान को नष्ट करना और मिट्टी की स्थिरता को बिगाड़ना", "type": "leaf"}
            ]},
            {"label": "यूपीएससी शमन रणनीतियाँ", "type": "branch", "date": "यूपीएससी", "children": [
                {"label": "संरक्षण: CRZ-I नियमों को सुदृढ़ करना, अनुपचारित जलीय कृषि अपशिष्टों पर प्रतिबंध लगाना", "type": "leaf"},
                {"label": "बहाली: ज्वारीय चैनलों से गाद हटाकर प्राकृतिक जल विज्ञान को बहाल करना और सामुदायिक गश्त बढ़ाना", "type": "leaf"}
            ]}
        ]
    },
    "marine-ecosystem": {
        "en": [
            {"label": "Physical Characteristics", "type": "branch", "date": "Physics", "children": [
                {"label": "Salinity Profile: Average salinity is ~35 ppt, governed by evaporation and freshwater input", "type": "leaf"},
                {"label": "Depth Profile: Epipelagic (surface), Mesopelagic, Bathypelagic, Abyssopelagic, Hadalpelagic (trenches)", "type": "leaf"}
            ]},
            {"label": "Marine Food Web", "type": "branch", "date": "Food Web", "children": [
                {"label": "Primary Producers: Phytoplankton (diatoms, dinoflagellates) driving global oxygen production", "type": "leaf"},
                {"label": "Trophic Levels: Zooplankton -> Small forage fish -> Apex predators (sharks, killer whales)", "type": "leaf"}
            ]},
            {"label": "Major Subdivisions", "type": "branch", "date": "Subdivisions", "children": [
                {"label": "Coastal/Neritic: Highly productive shallow shelves supporting kelp forests and coral reefs", "type": "leaf"},
                {"label": "Open Ocean/Pelagic: Lower nutrient density ('biological deserts') but huge surface area", "type": "leaf"}
            ]},
            {"label": "UPSC Environmental Focus", "type": "branch", "date": "UPSC Core", "children": [
                {"label": "Threats: Ocean acidification, plastic pollution (microplastics), and commercial over-fishing", "type": "leaf"},
                {"label": "Blue Economy: Sustainable use of ocean resources for economic growth (e.g. Deep Ocean Mission)", "type": "leaf"}
            ]}
        ],
        "hi": [
            {"label": "भौतिक विशेषताएँ", "type": "branch", "date": "भौतिक", "children": [
                {"label": "लवणता प्रोफ़ाइल: औसत लवणता ~35 ppt है, जो वाष्पीकरण और मीठे पानी के प्रवाह से नियंत्रित होती है", "type": "leaf"},
                {"label": "गहराई प्रोफ़ाइल: एपिपेलाजिक (सतह), मेसोपेलाजिक, बाथीपेलाजिक, एबिसोपेलाजिक, हाडालपेलाजिक (गर्त)", "type": "leaf"}
            ]},
            {"label": "समुद्री खाद्य जाल", "type": "branch", "date": "खाद्य जाल", "children": [
                {"label": "प्राथमिक उत्पादक: फाइटोप्लांकटन (डायटम) जो वैश्विक ऑक्सीजन उत्पादन को संचालित करते हैं", "type": "leaf"},
                {"label": "पोषण स्तर: जंतु प्लवक -> छोटी मछलियां -> शीर्ष शिकारी (शार्क, व्हेल)", "type": "leaf"}
            ]},
            {"label": "प्रमुख उपखंड", "type": "branch", "date": "उपखंड", "children": [
                {"label": "तटीय (Neritic): अत्यधिक उत्पादक मग्नतट जो केल्प वनों और प्रवाल भित्तियों का समर्थन करते हैं", "type": "leaf"},
                {"label": "खुला महासागर: कम पोषक तत्व घनत्व ('जैविक मरुस्थल') लेकिन विशाल सतह क्षेत्र", "type": "leaf"}
            ]},
            {"label": "यूपीएससी पर्यावरण फोकस", "type": "branch", "date": "यूपीएससी", "children": [
                {"label": "खतरे: महासागरीय अम्लीकरण, प्लास्टिक प्रदूषण (माइक्रोप्लास्टिक), और वाणिज्यिक अति-मत्स्यन", "type": "leaf"},
                {"label": "ब्लू इकोनॉमी: आर्थिक विकास के लिए महासागरीय संसाधनों का सतत उपयोग (जैसे डीप ओशन मिशन)", "type": "leaf"}
            ]}
        ]
    },
    "marine-organisms": {
        "en": [
            {"label": "Ecological Groups", "type": "branch", "date": "Groups", "children": [
                {"label": "Plankton: Drifting organisms incapable of swimming against currents (Phyto- & Zooplankton)", "type": "leaf"},
                {"label": "Nekton: Active swimmers residing in water column (fish, squid, marine mammals)", "type": "leaf"},
                {"label": "Benthos: Bottom dwellers residing on or within ocean floor (crabs, sea cucumbers)", "type": "leaf"}
            ]},
            {"label": "Survival Adaptations", "type": "branch", "date": "Adaptations", "children": [
                {"label": "Osmoregulation: Specialized kidneys and gills to excrete excess salts and conserve water", "type": "leaf"},
                {"label": "Buoyancy: Swim bladders in bony fish; oil-filled livers in sharks", "type": "leaf"}
            ]},
            {"label": "Deep Ocean Specialists", "type": "branch", "date": "Deep Sea", "children": [
                {"label": "Chemoautotrophs: Hydrothermal vent bacteria processing sulfur for energy", "type": "leaf"},
                {"label": "Barophiles: Organisms adapted to withstand extreme hydrostatic pressures", "type": "leaf"}
            ]},
            {"label": "UPSC Environmental Relevance", "type": "branch", "date": "UPSC Core", "children": [
                {"label": "Key Indicators: Phytoplankton blooms indicate nutrient levels; corals indicate water clarity/temp", "type": "leaf"},
                {"label": "Bio-prospecting: Extracting unique chemical compounds from marine organisms for pharmaceuticals", "type": "leaf"}
            ]}
        ],
        "hi": [
            {"label": "पारिस्थितिक समूह", "type": "branch", "date": "समूह", "children": [
                {"label": "प्लवक (Plankton): लहरों के विरुद्ध तैरने में असमर्थ निष्क्रिय जीव (पादप व जंतु प्लवक)", "type": "leaf"},
                {"label": "नेक्टन (Nekton): जल स्तंभ में रहने वाले सक्रिय तैराक (मछली, स्क्विड, समुद्री स्तनधारी)", "type": "leaf"},
                {"label": "नितल जीव (Benthos): समुद्र तल पर या उसके भीतर रहने वाले जीव (केकड़े, समुद्री खीरे)", "type": "leaf"}
            ]},
            {"label": "उत्तरजीविता अनुकूलन", "type": "branch", "date": "अनुकूलन", "children": [
                {"label": "ऑस्मोरिगुलेशन: अतिरिक्त लवणों को बाहर निकालने और पानी के संरक्षण के लिए विशेष गुर्दे और गलफड़े", "type": "leaf"},
                {"label": "उत्प्लावकता (Buoyancy): अस्थि मछलियों में वायु मूत्राशय; शार्क में तेल से भरे यकृत", "type": "leaf"}
            ]},
            {"label": "गहरे सागर के विशेषज्ञ", "type": "branch", "date": "गहरा सागर", "children": [
                {"label": "रसायन-स्वपोषी: ऊर्जा के लिए सल्फर का प्रसंस्करण करने वाले हाइड्रोथर्मल वेंट बैक्टीरिया", "type": "leaf"},
                {"label": "बैरोफिल्स: अत्यधिक हाइड्रोस्टेटिक दबावों का सामना करने के लिए अनुकूलित जीव", "type": "leaf"}
            ]},
            {"label": "यूपीएससी पर्यावरण महत्व", "type": "branch", "date": "यूपीएससी", "children": [
                {"label": "प्रमुख संकेतक: पादप प्लवक पोषण स्तर को दर्शाते हैं; प्रवाल स्पष्टता/तापमान को दर्शाते हैं", "type": "leaf"},
                {"label": "बायो-प्रोस्पेक्टिंग: फार्मास्यूटिकल्स के लिए समुद्री जीवों से अद्वितीय रासायनिक यौगिक निकालना", "type": "leaf"}
            ]}
        ]
    },
    "montane-forests": {
        "en": [
            {"label": "Himalayan Altitudinal Zonation", "type": "branch", "date": "Zonation", "children": [
                {"label": "Wet Hill Forests (1000-2000m): Evergreen oak and chestnut dominate", "type": "leaf"},
                {"label": "Pine & Coniferous (1500-3000m): Chir Pine, Deodar, Blue Pine, Spruce, and Silver Fir", "type": "leaf"},
                {"label": "Alpine & Meadows (3000m+): Juniper, Birch (Bhojpatra), transitioning to alpine pastures", "type": "leaf"}
            ]},
            {"label": "Western Ghats Montane (Sholas)", "type": "branch", "date": "Sholas", "children": [
                {"label": "Stunted Forests: Patches of stunted evergreen trees separated by rolling grasslands", "type": "leaf"},
                {"label": "Endemism: High rate of endemic plant species; threatened by exotic plantations (wattle, eucalyptus)", "type": "leaf"}
            ]},
            {"label": "Ecological Functions", "type": "branch", "date": "Functions", "children": [
                {"label": "Water Towers: Acts as watersheds feeding major Indian rivers (Ganga, Cauvery)", "type": "leaf"},
                {"label": "Slope Stability: Deep roots bind soil, preventing mountain landslides and avalanches", "type": "leaf"}
            ]},
            {"label": "UPSC Core Analysis", "type": "branch", "date": "UPSC Core", "children": [
                {"label": "Climate Vulnerability: Altitudinal ranges are shifting upwards due to temperature rises", "type": "leaf"},
                {"label": "Threats: Hydroelectric projects, unsustainable mountain tourism, and slope clearing", "type": "leaf"}
            ]}
        ],
        "hi": [
            {"label": "हिमालयी लंबवत स्तरीकरण", "type": "branch", "date": "स्तरीकरण", "children": [
                {"label": "नम पर्वतीय वन (1000-2000m): सदाबहार ओक और चेस्टनट का प्रभुत्व", "type": "leaf"},
                {"label": "चीड़ और कोणधारी वन (1500-3000m): चीड़, देवदार, ब्लू पाइन, स्प्रूस और सिल्वर फर", "type": "leaf"},
                {"label": "अल्पाइन और घास के मैदान (3000m+): जुनिपर, बर्च (भोजपत्र), अल्पाइन चरागाहों में संक्रमण", "type": "leaf"}
            ]},
            {"label": "पश्चिमी घाट मोंटेन वन (शोला)", "type": "branch", "date": "शोला वन", "children": [
                {"label": "बौने वन: लुढ़कते घास के मैदानों द्वारा अलग किए गए बौने सदाबहार पेड़ों के पैच", "type": "leaf"},
                {"label": "स्थानिकता: स्थानिक पौधों की प्रजातियों की उच्च दर; विदेशी वृक्षारोपण (नीलगिरी) से खतरा", "type": "leaf"}
            ]},
            {"label": "पारिस्थितिक कार्य", "type": "branch", "date": "कार्य", "children": [
                {"label": "जल मीनारें: भारत की प्रमुख नदियों (गंगा, कावेरी) को जल प्रदान करने वाले जलसंभर", "type": "leaf"},
                {"label": "ढाल स्थिरता: गहरी जड़ें मिट्टी को बांधती हैं, जिससे भूस्खलन और हिमस्खलन रुकता है", "type": "leaf"}
            ]},
            {"label": "यूपीएससी कोर विश्लेषण", "type": "branch", "date": "यूपीएससी", "children": [
                {"label": "जलवायु संवेदनशीलता: तापमान वृद्धि के कारण वनस्पतियों की ऊंचाई सीमा ऊपर की ओर बढ़ रही है", "type": "leaf"},
                {"label": "खतरे: जलविद्युत परियोजनाएं, गैर-सतत पर्वतीय पर्यटन और पर्वतीय ढलानों की सफाई", "type": "leaf"}
            ]}
        ]
    },
    "mountains": {
        "en": [
            {"label": "Fragile Topography", "type": "branch", "date": "Topography", "children": [
                {"label": "Steep Gradients: High gravity-driven processes (landslides, mass wasting, soil creep)", "type": "leaf"},
                {"label": "Climatic Variation: Rapid lapse rate changes (average 6.5°C drop per 1000m elevation)", "type": "leaf"}
            ]},
            {"label": "Ecological Zonation", "type": "branch", "date": "Zonation", "children": [
                {"label": "Vegetation Shifts: Tropical -> Temperate -> Taiga -> Alpine -> Snowline in a compact range", "type": "leaf"},
                {"label": "Slope Contrast: Windward slopes get heavy orographic rainfall; leeward is dry shadow", "type": "leaf"}
            ]},
            {"label": "Key Threats", "type": "branch", "date": "Threats", "children": [
                {"label": "Glacial Retreat: Melting Himalayan glaciers threatening long-term river water security", "type": "leaf"},
                {"label": "Infrastructure: Road expansion (e.g. Char Dham project) destabilizing fragile mountain slopes", "type": "leaf"}
            ]},
            {"label": "UPSC Disaster Focus", "type": "branch", "date": "UPSC Core", "children": [
                {"label": "GLOFs (Glacial Lake Outburst Floods): Triggered by moraine collapse; devastating downstream impacts", "type": "leaf"},
                {"label": "NDMA Guidelines: Guidelines for managing landslides and glacial hazards in mountain states", "type": "leaf"}
            ]}
        ],
        "hi": [
            {"label": "संवेदनशील स्थलाकृति", "type": "branch", "date": "स्थलाकृति", "children": [
                {"label": "तीव्र ढाल: गुरुत्वाकर्षण-संचालित प्रक्रियाएं (भूस्खलन, मलबे का खिसकना) अधिक सक्रिय", "type": "leaf"},
                {"label": "जलवायु परिवर्तनशीलता: तीव्र सामान्य ह्रास दर (प्रति 1000 मीटर पर औसतन 6.5°C तापमान में गिरावट)", "type": "leaf"}
            ]},
            {"label": "पारिस्थितिक क्षेत्रीकरण", "type": "branch", "date": "क्षेत्रीकरण", "children": [
                {"label": "वनस्पति बदलाव: एक ही पर्वत पर उष्णकटिबंधीय से शीतोष्ण, टैगा, अल्पाइन और हिमरेखा तक का बदलाव", "type": "leaf"},
                {"label": "ढलान अंतर: पवनमुखी ढलानों पर भारी पर्वतीय वर्षा; पवनविमुख ढलान वृष्टि छाया क्षेत्र बनता है", "type": "leaf"}
            ]},
            {"label": "प्रमुख खतरे", "type": "branch", "date": "खतरे", "children": [
                {"label": "हिमनद पीछे हटना: हिमालय के ग्लेशियरों का पिघलना लंबी अवधि के जल सुरक्षा के लिए खतरा", "type": "leaf"},
                {"label": "बुनियादी ढांचा: सड़क विस्तार (जैसे चार धाम परियोजना) नाजुक ढलानों को अस्थिर कर रहा है", "type": "leaf"}
            ]},
            {"label": "यूपीएससी आपदा फोकस", "type": "branch", "date": "यूपीएससी", "children": [
                {"label": "GLOFs (हिमनद झील विस्फोट बाढ़): मोराइन के ढहने से शुरू; विनाशकारी परिणाम", "type": "leaf"},
                {"label": "NDMA दिशानिर्देश: पर्वतीय राज्यों में भूस्खलन और हिमनद आपदाओं के प्रबंधन के लिए दिशानिर्देश", "type": "leaf"}
            ]}
        ]
    },
    "photic-zone": {
        "en": [
            {"label": "Sunlight Penetration", "type": "branch", "date": "Sunlight", "children": [
                {"label": "Depth Limit: Extends from surface down to ~200m depth where light intensity supports photosynthesis", "type": "leaf"},
                {"label": "Limiting Factors: High water turbidity, sediment loading, and algal blooms reduce zone thickness", "type": "leaf"}
            ]},
            {"label": "Ecological Engine", "type": "branch", "date": "Ecological Engine", "children": [
                {"label": "Photosynthesis: Base of the marine trophic pyramid; phytoplanktons harness solar energy", "type": "leaf"},
                {"label": "Productivity: Accounts for over 90% of all primary carbon fixation in oceans", "type": "leaf"}
            ]},
            {"label": "Biota Concentration", "type": "branch", "date": "Biota", "children": [
                {"label": "Habitat: Anchors coral reefs, seagrass meadows, and pelagic schooling fish", "type": "leaf"},
                {"label": "Plankton Abundance: Dense concentrations of zooplankton feeding on primary producers", "type": "leaf"}
            ]},
            {"label": "UPSC Oceanography Core", "type": "branch", "date": "UPSC Core", "children": [
                {"label": "Ocean Carbon Sink: Biological pump transports atmospheric carbon from photic zone to deep sea", "type": "leaf"},
                {"label": "Acidification Threat: Warming and acidification alter phytoplankton cell calcification in the photic zone", "type": "leaf"}
            ]}
        ],
        "hi": [
            {"label": "सूर्य प्रकाश प्रवेश", "type": "branch", "date": "प्रकाश प्रवेश", "children": [
                {"label": "गहराई सीमा: सतह से ~200 मीटर की गहराई तक विस्तृत जहाँ प्रकाश संश्लेषण के लिए पर्याप्त धूप होती है", "type": "leaf"},
                {"label": "सीमित कारक: पानी की उच्च टर्बिडिटी, तलछट का भार और अल्गल ब्लूम प्रकाशीय परत को कम करते हैं", "type": "leaf"}
            ]},
            {"label": "पारिस्थितिक इंजन", "type": "branch", "date": "पारिस्थितिक इंजन", "children": [
                {"label": "प्रकाश संश्लेषण: समुद्री पोषण पिरामिड का आधार; पादप प्लवक सौर ऊर्जा का उपयोग करते हैं", "type": "leaf"},
                {"label": "उत्पादक क्षमता: महासागरों में सभी प्राथमिक कार्बन स्थिरीकरण के 90% से अधिक के लिए जिम्मेदार", "type": "leaf"}
            ]},
            {"label": "जीवों का संकेंद्रण", "type": "branch", "date": "जीव संकेंद्रण", "children": [
                {"label": "आवास: प्रवाल भित्तियों, समुद्री घास के मैदानों और तैरती मछलियों के झुंड का समर्थन करता है", "type": "leaf"},
                {"label": "प्लवक प्रचुरता: प्राथमिक उत्पादकों को खाने वाले जंतु प्लवक की घनी आबादी यहाँ पाई जाती है", "type": "leaf"}
            ]},
            {"label": "यूपीएससी समुद्र विज्ञान कोर", "type": "branch", "date": "यूपीएससी", "children": [
                {"label": "महासागरीय कार्बन सिंक: जैविक पंप कार्बन को प्रकाशीय क्षेत्र से गहरे समुद्र में ले जाता है", "type": "leaf"},
                {"label": "अम्लीकरण का खतरा: तापमान वृद्धि और अम्लीकरण पादप प्लवक के कैल्सीकरण को प्रभावित करते हैं", "type": "leaf"}
            ]}
        ]
    },
    "phytoplankton": {
        "en": [
            {"label": "Taxonomic Groups", "type": "branch", "date": "Groups", "children": [
                {"label": "Diatoms: Siliceous shell walls; dominate temperate and polar nutrient-rich waters", "type": "leaf"},
                {"label": "Dinoflagellates: Flagellated shells; major group inducing bioluminescence and red tides", "type": "leaf"},
                {"label": "Cyanobacteria: Microscopic blue-green algae conducting nitrogen fixation in warm seas", "type": "leaf"}
            ]},
            {"label": "Global Carbon Sink", "type": "branch", "date": "Carbon Sink", "children": [
                {"label": "Oxygen Output: Generates ~50% of atmospheric oxygen through marine photosynthesis", "type": "leaf"},
                {"label": "Biological Pump: Fixes atmospheric carbon which sinks as detritus to ocean floors", "type": "leaf"}
            ]},
            {"label": "Factors of Growth", "type": "branch", "date": "Growth Factors", "children": [
                {"label": "Nutrient Upwelling: Wind-driven upwelling bringing nitrates and phosphates to surface", "type": "leaf"},
                {"label": "Iron Limitation: High-nutrient, low-chlorophyll (HNLC) zones where iron dust limits growth", "type": "leaf"}
            ]},
            {"label": "UPSC Environmental Core", "type": "branch", "date": "UPSC Core", "children": [
                {"label": "Ocean Warming: Layer stratification prevents nutrient upwelling, reducing plankton counts", "type": "leaf"},
                {"label": "Acidification Impact: Calcifying coccolithophores struggle to build shells under lower pH", "type": "leaf"}
            ]}
        ],
        "hi": [
            {"label": "वर्गीकरण समूह", "type": "branch", "date": "समूह", "children": [
                {"label": "डायटम (Diatoms): सिलिका युक्त खोल; ठंडे पोषक तत्वों से भरपूर जल में हावी", "type": "leaf"},
                {"label": "डिनोफ्लैगलेट्स: कोड़े जैसी संरचना; जैवदीप्ति और 'लाल ज्वार' उत्पन्न करने वाला प्रमुख समूह", "type": "leaf"},
                {"label": "सायनोबैक्टीरिया: सूक्ष्म नीले-हरे शैवाल जो गर्म समुद्रों में नाइट्रोजन स्थिरीकरण करते हैं", "type": "leaf"}
            ]},
            {"label": "वैश्विक कार्बन सिंक", "type": "branch", "date": "कार्बन सिंक", "children": [
                {"label": "ऑक्सीजन उत्पादन: समुद्री प्रकाश संश्लेषण के माध्यम से वायुमंडलीय ऑक्सीजन का ~50% उत्पन्न करते हैं", "type": "leaf"},
                {"label": "जैविक पंप: वायुमंडलीय कार्बन को स्थिर करते हैं जो कचरे के रूप में गहरे समुद्र तल में डूब जाता है", "type": "leaf"}
            ]},
            {"label": "विकास के कारक", "type": "branch", "date": "कारक", "children": [
                {"label": "पोषक तत्व अपवेलिंग: हवा से चलने वाली अपवेलिंग जो नाइट्रेट और फास्फेट को सतह पर लाती है", "type": "leaf"},
                {"label": "आयरन की कमी: उच्च-पोषक तत्व, कम-क्लोरोफिल (HNLC) क्षेत्र जहां लोहे की धूल विकास को सीमित करती है", "type": "leaf"}
            ]},
            {"label": "यूपीएससी पर्यावरण कोर", "type": "branch", "date": "यूपीएससी", "children": [
                {"label": "महासागर तापन: तापीय परत अपवेलिंग को रोकती है, जिससे प्लवक की संख्या कम होती है", "type": "leaf"},
                {"label": "अम्लीकरण प्रभाव: कैल्सीफाइंग कोकोलिथोफोर्स कम pH के तहत कवच बनाने में असमर्थ होते हैं", "type": "leaf"}
            ]}
        ]
    },
    "plankton": {
        "en": [
            {"label": "Primary Divisions", "type": "branch", "date": "Divisions", "children": [
                {"label": "Phytoplankton: Photoautotrophic microscopic algae (Diatoms, Coccolithophores)", "type": "leaf"},
                {"label": "Zooplankton: Heterotrophic plankton feeding on phytoplankton or smaller detritus", "type": "leaf"}
            ]},
            {"label": "Lifecycle Classification", "type": "branch", "date": "Lifecycle", "children": [
                {"label": "Holoplankton: Organisms spending their entire life cycle as plankton (e.g. Copepods)", "type": "leaf"},
                {"label": "Meroplankton: Organisms that are planktonic only during larval stages (e.g. crab larvae, fish larvae)", "type": "leaf"}
            ]},
            {"label": "Trophic Level Role", "type": "branch", "date": "Trophic Role", "children": [
                {"label": "Base Food: Crucial link transferring energy from primary producers to secondary nekton", "type": "leaf"},
                {"label": "Diurnal Migration: Deep scattering layer where zooplankton migrate to surface at night to feed", "type": "leaf"}
            ]},
            {"label": "UPSC Core Questions", "type": "branch", "date": "UPSC Core", "children": [
                {"label": "Ocean Productivity: Primary productivity estimates are mapped using chlorophyll-a plankton indexes", "type": "leaf"},
                {"label": "Eutrophication Indicator: Sudden plankton blooms reflect agricultural nutrient pollution", "type": "leaf"}
            ]}
        ],
        "hi": [
            {"label": "प्राथमिक विभाजन", "type": "branch", "date": "विभाजन", "children": [
                {"label": "पादप प्लवक (Phytoplankton): प्रकाश-स्वपोषी सूक्ष्म शैवाल (डायटम, कोकोलिथोफोर्स)", "type": "leaf"},
                {"label": "जंतु प्लवक (Zooplankton): परपोषी प्लवक जो पादप प्लवक या कार्बनिक मलबे को खाते हैं", "type": "leaf"}
            ]},
            {"label": "जीवन चक्र वर्गीकरण", "type": "branch", "date": "जीवन चक्र", "children": [
                {"label": "होलोप्लांकटन: ऐसे जीव जो अपना पूरा जीवन चक्र प्लवक के रूप में बिताते हैं (जैसे कोपेपोड्स)", "type": "leaf"},
                {"label": "मेरोप्लांकटन: ऐसे जीव जो केवल लार्वा चरणों के दौरान प्लवक होते हैं (जैसे केकड़े/मछली के लार्वा)", "type": "leaf"}
            ]},
            {"label": "पोषण स्तर की भूमिका", "type": "branch", "date": "पोषण भूमिका", "children": [
                {"label": "आधार भोजन: ऊर्जा को प्राथमिक उत्पादकों से द्वितीयक तैराक जीवों (Nekton) में स्थानांतरित करने वाली कड़ी", "type": "leaf"},
                {"label": "दैनिक प्रवास: जंतु प्लवक रात में भोजन करने के लिए सतह पर प्रवास करते हैं (Vertical Migration)", "type": "leaf"}
            ]},
            {"label": "यूपीएससी मुख्य प्रश्न", "type": "branch", "date": "यूपीएससी", "children": [
                {"label": "महासागरीय उत्पादकता: प्राथमिक उत्पादकता का मानचित्रण क्लोरोफिल-ए प्लवक सूचकांकों का उपयोग करके किया जाता है", "type": "leaf"},
                {"label": "यूट्रोफिकेशन संकेतक: अचानक प्लवक के खिलने से कृषि पोषक तत्व प्रदूषण झलकता है", "type": "leaf"}
            ]}
        ]
    },
    "sea-grass": {
        "en": [
            {"label": "Biological Identity", "type": "branch", "date": "Identity", "children": [
                {"label": "Flowering Plants: Only marine angiosperms completing entire life cycles fully submerged in seawater", "type": "leaf"},
                {"label": "Anatomy: Possesses true roots, rhizomes, stems, leaves, flowers, and seeds", "type": "leaf"}
            ]},
            {"label": "Blue Carbon Sink", "type": "branch", "date": "Carbon Sink", "children": [
                {"label": "Soil Trapping: Dense canopy traps organic particles; roots anchor carbon in anaerobic sediment", "type": "leaf"},
                {"label": "Efficiency: Stores carbon up to 40x faster than land forests, mitigating atmospheric greenhouse buildup", "type": "leaf"}
            ]},
            {"label": "Ecological Services", "type": "branch", "date": "Services", "children": [
                {"label": "Shelter & Food: Core foraging habitat for Dugongs (Sea Cows) and Green Sea Turtles", "type": "leaf"},
                {"label": "Stabilization: Binds ocean floor sediment, reducing wave energy and protecting coastal beaches", "type": "leaf"}
            ]},
            {"label": "UPSC Conservation Focus", "type": "branch", "date": "UPSC Core", "children": [
                {"label": "India Locations: Abundant in Gulf of Mannar, Palk Bay, Lakshadweep, and Andaman Islands", "type": "leaf"},
                {"label": "Threats: Bottom trawling, dredging, and eutrophication blocking light penetration", "type": "leaf"}
            ]}
        ],
        "hi": [
            {"label": "जैविक पहचान", "type": "branch", "date": "पहचान", "children": [
                {"label": "सपुष्पक पौधे (Angiosperms): एकमात्र समुद्री आवृतबीजी जो समुद्र के पानी में पूरी तरह जलमग्न रहकर जीवन चक्र पूरा करते हैं", "type": "leaf"},
                {"label": "शारीरिक रचना: सच्ची जड़ें, प्रकंद (Rhizomes), तने, पत्तियाँ, फूल और बीज होते हैं", "type": "leaf"}
            ]},
            {"label": "ब्लू कार्बन सिंक", "type": "branch", "date": "कार्बन सिंक", "children": [
                {"label": "मृदा ट्रैपिंग: घना वितान कार्बनिक कणों को रोकता है; जड़ें कार्बन को अवायवीय तलछट में बांधती हैं", "type": "leaf"},
                {"label": "क्षमता: स्थलीय वनों की तुलना में 40 गुना तेजी से कार्बन का संचय करते हैं, जलवायु परिवर्तन को कम करते हैं", "type": "leaf"}
            ]},
            {"label": "पारिस्थितिक सेवाएँ", "type": "branch", "date": "सेवाएँ", "children": [
                {"label": "आश्रय और भोजन: डुगोंग (समुद्री गाय) और कछुओं के लिए मुख्य भोजन क्षेत्र", "type": "leaf"},
                {"label": "स्थिरीकरण: समुद्र तल की तलछट को बांधता है, लहरों के प्रभाव को कम करता है और तटों की रक्षा करता है", "type": "leaf"}
            ]},
            {"label": "यूपीएससी संरक्षण फोकस", "type": "branch", "date": "यूपीएससी", "children": [
                {"label": "भारतीय स्थान: मन्नार की खाड़ी, पाल्क खाड़ी, लक्षद्वीप और अंडमान द्वीप समूह में प्रचुरता", "type": "leaf"},
                {"label": "खतरे: नीचे जाल डालना (Bottom trawling), ड्रेजिंग और यूट्रोफिकेशन जो धूप को अवरुद्ध करता है", "type": "leaf"}
            ]}
        ]
    },
    "seaweeds": {
        "en": [
            {"label": "Taxonomic Identity", "type": "branch", "date": "Identity", "children": [
                {"label": "Algae Classification: Macroscopic marine algae lacking roots, stems, or leaves (divided into Red, Brown, and Green)", "type": "leaf"},
                {"label": "Structure: Simple thallus body; attaches to rocks via holdfast anchors", "type": "leaf"}
            ]},
            {"label": "Commercial Exploitation", "type": "branch", "date": "Usage", "children": [
                {"label": "Hydrocolloids: Source of Agar, Alginate, and Carrageenan used in food stabilizers and cosmetics", "type": "leaf"},
                {"label": "Nutrient Rich: Used as biofertilizers, animal fodder, and directly as food (rich in Iodine)", "type": "leaf"}
            ]},
            {"label": "Ecological Value", "type": "branch", "date": "Value", "children": [
                {"label": "Habitat: Kelp forests (giant brown seaweed) supporting highly biodiverse ecosystems", "type": "leaf"},
                {"label": "Bioremediation: Absorbs dissolved heavy metals and nutrients, combating coastal pollution", "type": "leaf"}
            ]},
            {"label": "UPSC Policy Relevance", "type": "branch", "date": "UPSC Core", "children": [
                {"label": "Seaweed Farming: Low-carbon aquaculture; alternative livelihood for coastal communities (SHGs)", "type": "leaf"},
                {"label": "Indian Projects: CSMCRI initiatives promoting Kappaphycus cultivation along Tamil Nadu coast", "type": "leaf"}
            ]}
        ],
        "hi": [
            {"label": "वर्गीकरण पहचान", "type": "branch", "date": "पहचान", "children": [
                {"label": "शैवाल वर्गीकरण: स्थूल समुद्री शैवाल जिनमें जड़ों, तनों या पत्तियों का अभाव होता है (लाल, भूरे और हरे रंग में विभाजित)", "type": "leaf"},
                {"label": "संरचना: सरल थैलस शरीर; होल्डफास्ट एंकर के माध्यम से चट्टानों से जुड़ता है", "type": "leaf"}
            ]},
            {"label": "वाणिज्यिक दोहन", "type": "branch", "date": "उपयोग", "children": [
                {"label": "हाइड्रोकोलॉइड्स: अगर (Agar), एल्जिनेट और कैरागीनन का स्रोत जो खाद्य स्टेबलाइजर्स में उपयोग किया जाता है", "type": "leaf"},
                {"label": "पोषक तत्व प्रचुरता: जैव उर्वरक, पशु चारा और प्रत्यक्ष भोजन (आयोडीन से भरपूर) के रूप में उपयोग", "type": "leaf"}
            ]},
            {"label": "पारिस्थितिक मूल्य", "type": "branch", "date": "मूल्य", "children": [
                {"label": "आवास: केल्प वन (विशाल भूरे समुद्री शैवाल) जो अत्यधिक समृद्ध पारितंत्र का समर्थन करते हैं", "type": "leaf"},
                {"label": "बायोरेमेडिएशन: घुलित भारी धातुओं और अतिरिक्त पोषक तत्वों को अवशोषित कर प्रदूषण से लड़ता है", "type": "leaf"}
            ]},
            {"label": "यूपीएससी नीति महत्व", "type": "branch", "date": "यूपीएससी", "children": [
                {"label": "सीवीड फार्मिंग: कम कार्बन वाली जलीय कृषि; तटीय समुदायों (SHGs) के लिए वैकल्पिक आजीविका", "type": "leaf"},
                {"label": "भारतीय परियोजनाएं: तमिलनाडु तट पर कप्पाफाइकस खेती को बढ़ावा देने वाली CSMCRI की पहल", "type": "leaf"}
            ]}
        ]
    },
    "sunlight": {
        "en": [
            {"label": "Ocean Penetration", "type": "branch", "date": "Penetration", "children": [
                {"label": "Spectrum Absorption: Red light absorbed first (top 10m); blue/green light penetrates deepest", "type": "leaf"},
                {"label": "Secchi Depth: Measure of water transparency and light penetration efficiency", "type": "leaf"}
            ]},
            {"label": "Biological Driver", "type": "branch", "date": "Biological Driver", "children": [
                {"label": "Photosynthesis Limit: Restricts primary production to the shallow photic zone", "type": "leaf"},
                {"label": "Diurnal Rhythms: Controls marine organism migration patterns and spawning cycles", "type": "leaf"}
            ]},
            {"label": "Climatic Balance", "type": "branch", "date": "Climate", "children": [
                {"label": "Surface Heating: Drives thermal stratification and wind-driven ocean currents", "type": "leaf"},
                {"label": "Albedo Feedback: Polar ice reflects sunlight; melting ice absorbs heat, accelerating warming", "type": "leaf"}
            ]},
            {"label": "UPSC Syllabus Core", "type": "branch", "date": "UPSC Core", "children": [
                {"label": "Turbidity Threats: Heavy coastal sediment pollution blocks sunlight, killing coral reefs and seagrasses", "type": "leaf"},
                {"label": "Solar Energy Link: Offshore floating solar panels and their impact on marine light budgets", "type": "leaf"}
            ]}
        ],
        "hi": [
            {"label": "महासागरीय प्रवेश", "type": "branch", "date": "प्रवेश", "children": [
                {"label": "स्पेक्ट्रम अवशोषण: लाल प्रकाश सबसे पहले अवशोषित (ऊपरी 10m); नीला/हरा प्रकाश सबसे गहराई तक जाता है", "type": "leaf"},
                {"label": "सेची गहराई (Secchi): पानी की पारदर्शिता और प्रकाश प्रवेश दक्षता का माप", "type": "leaf"}
            ]},
            {"label": "जैविक चालक बल", "type": "branch", "date": "जैविक चालक", "children": [
                {"label": "प्रकाश संश्लेषण सीमा: प्राथमिक उत्पादकता को उथले प्रकाशीय क्षेत्र तक सीमित करता है", "type": "leaf"},
                {"label": "दैनिक लय: समुद्री जीवों के प्रवास पैटर्न और अंडे देने के चक्र को नियंत्रित करता है", "type": "leaf"}
            ]},
            {"label": "जलवायु संतुलन", "type": "branch", "date": "जलवायु", "children": [
                {"label": "सतह तापन: तापीय स्तरीकरण और हवा से संचालित महासागरीय धाराओं को नियंत्रित करता है", "type": "leaf"},
                {"label": "एल्बीडो फीडबैक: ध्रुवीय बर्फ सूर्य के प्रकाश को परावर्तित करती है; पिघलती बर्फ गर्मी सोखती है", "type": "leaf"}
            ]},
            {"label": "यूपीएससी पाठ्यक्रम कोर", "type": "branch", "date": "यूपीएससी", "children": [
                {"label": "गंदलापन का खतरा: भारी तटीय तलछट प्रदूषण धूप को रोकता है, जिससे प्रवाल और समुद्री घास नष्ट होते हैं", "type": "leaf"},
                {"label": "सौर ऊर्जा लिंक: फ्लोटिंग सोलर पैनल और उनका जलीय प्रकाश बजट पर प्रभाव", "type": "leaf"}
            ]}
        ]
    },
    "temperature-and-oxygen-concentration": {
        "en": [
            {"label": "Solubility Dynamics", "type": "branch", "date": "Solubility", "children": [
                {"label": "Inverse Relation: Oxygen solubility decreases as water temperature increases", "type": "leaf"},
                {"label": "Oxygen Content: Average aquatic dissolved oxygen is ~10 ppm (vs ~200,000 ppm in air)", "type": "leaf"}
            ]},
            {"label": "Oxygen Minimum Zone (OMZ)", "type": "branch", "date": "OMZ", "children": [
                {"label": "Location: Typically occurs between 200m to 1000m depth where respiration exceeds replenishment", "type": "leaf"},
                {"label": "Mechanisms: Sinking organic matter decomposition consumes dissolved oxygen rapidly", "type": "leaf"}
            ]},
            {"label": "Warming Consequences", "type": "branch", "date": "Warming", "children": [
                {"label": "Ocean Deoxygenation: Climate warming lowers deep-sea ventilation, expanding hypoxic dead zones", "type": "leaf"},
                {"label": "Metabolic Stress: Marine organisms require more oxygen as warming accelerates metabolic rates", "type": "leaf"}
            ]},
            {"label": "UPSC Environmental Core", "type": "branch", "date": "UPSC Core", "children": [
                {"label": "BOD Indices: Biological Oxygen Demand tracks organic pollution load in river systems", "type": "leaf"},
                {"label": "Hypoxia Triggers: Eutrophication runoffs accelerating algal decomposition in coastal lagoons", "type": "leaf"}
            ]}
        ],
        "hi": [
            {"label": "विलेयता गतिकी", "type": "branch", "date": "विलेयता", "children": [
                {"label": "विपरीत संबंध: पानी का तापमान बढ़ने पर ऑक्सीजन की घुलनशीलता कम हो जाती है", "type": "leaf"},
                {"label": "ऑक्सीजन की मात्रा: जलीय घुलित ऑक्सीजन औसतन ~10 ppm होती है (हवा में ~200,000 ppm के मुकाबले)", "type": "leaf"}
            ]},
            {"label": "न्यूनतम ऑक्सीजन क्षेत्र (OMZ)", "type": "branch", "date": "OMZ", "children": [
                {"label": "स्थिति: आमतौर पर 200 मीटर से 1000 मीटर की गहराई के बीच जहां श्वसन पुनः पूर्ति से अधिक होता है", "type": "leaf"},
                {"label": "क्रियाविधि: डूबने वाले कार्बनिक पदार्थों का अपघटन तेजी से घुलित ऑक्सीजन का उपभोग करता है", "type": "leaf"}
            ]},
            {"label": "ताप वृद्धि के परिणाम", "type": "branch", "date": "परिणाम", "children": [
                {"label": "महासागरीय डीऑक्सीजनेशन: जलवायु तापन गहरे समुद्र के वेंटिलेशन को कम करता है, जिससे मृत क्षेत्र बढ़ते हैं", "type": "leaf"},
                {"label": "चयापचय तनाव: गर्म होने से चयापचय दर बढ़ने पर समुद्री जीवों को अधिक ऑक्सीजन की आवश्यकता होती है", "type": "leaf"}
            ]},
            {"label": "यूपीएससी पर्यावरण कोर", "type": "branch", "date": "यूपीएससी", "children": [
                {"label": "BOD संकेतक: जैविक ऑक्सीजन मांग नदी प्रणालियों में कार्बनिक प्रदूषण भार को ट्रैक करती है", "type": "leaf"},
                {"label": "हाइपोक्सिया ट्रिगर: तटीय लैगून में शैवाल के अपघटन को तेज करने वाले उर्वरक अपवाह", "type": "leaf"}
            ]}
        ]
    },
    "threats-to-coral-reefs": {
        "en": [
            {"label": "Anthropogenic Pressures", "type": "branch", "date": "Human Threats", "children": [
                {"label": "Destructive Fishing: Bottom trawling, blast fishing, and cyanide poisoning", "type": "leaf"},
                {"label": "Coastal Runoff: Heavy sediments from construction choking coral polyps and blocking light", "type": "leaf"}
            ]},
            {"label": "Climate Anomalies", "type": "branch", "date": "Climate", "children": [
                {"label": "Mass Bleaching: Sea surface temperature anomalies expelling zooxanthellae algae", "type": "leaf"},
                {"label": "Acidification: Ocean absorption of CO2 decreases carbonate ions, weakening reef skeletons", "type": "leaf"}
            ]},
            {"label": "Biotic Threats", "type": "branch", "date": "Biotic", "children": [
                {"label": "Crown-of-Thorns: Outbreaks of coral-eating starfish destroying vast reef tracts", "type": "leaf"},
                {"label": "Coral Diseases: Black band and white band bacterial infections spreading in warm waters", "type": "leaf"}
            ]},
            {"label": "UPSC Mitigation Core", "type": "branch", "date": "UPSC Core", "children": [
                {"label": "Policy: Protection under Schedule I of WPA 1972; strict regulations on coastal tourism", "type": "leaf"},
                {"label": "Restoration: Biorock mineral accretion technology to rebuild calcification capacity", "type": "leaf"}
            ]}
        ],
        "hi": [
            {"label": "मानवजनित दबाव", "type": "branch", "date": "मानव जनित", "children": [
                {"label": "विनाशकारी मत्स्यन: तली का जाल (Bottom trawling), डायनामाइट विस्फोट और साइनाइड का जहर देना", "type": "leaf"},
                {"label": "तटीय अपवाह: निर्माण गतिविधियों से निकलने वाली गाद जो पॉलिप्स का दम घोटती है", "type": "leaf"}
            ]},
            {"label": "जलवायु विसंगतियां", "type": "branch", "date": "जलवायु", "children": [
                {"label": "सामूहिक विरंजन: समुद्र की सतह के तापमान में वृद्धि से ज़ूक्सैंथेले शैवाल का निष्कासन", "type": "leaf"},
                {"label": "अम्लीकरण: महासागर द्वारा CO2 का अवशोषण कार्बोनेट आयनों को कम करता है, जिससे ढांचा कमजोर होता है", "type": "leaf"}
            ]},
            {"label": "जैविक खतरे", "type": "branch", "date": "जैविक", "children": [
                {"label": "कांटों का ताज (Crown-of-Thorns): प्रवाल खाने वाले स्टारफिश का प्रकोप जो भित्तियों को नष्ट करता है", "type": "leaf"},
                {"label": "प्रवाल रोग: गर्म पानी में फैलने वाले ब्लैक बैंड और व्हाइट बैंड बैक्टीरिया के संक्रमण", "type": "leaf"}
            ]},
            {"label": "यूपीएससी शमन रणनीतियाँ", "type": "branch", "date": "यूपीएससी", "children": [
                {"label": "नीति: WPA 1972 की अनुसूची I के तहत संरक्षण; तटीय पर्यटन पर कड़े नियम", "type": "leaf"},
                {"label": "बहाली: प्रवाल कंकालों के पुनर्निर्माण के लिए बायोरॉक खनिज संवर्धन तकनीक का उपयोग", "type": "leaf"}
            ]}
        ]
    },
    "threats-to-estuaries": {
        "en": [
            {"label": "Urban & Industrial Pollution", "type": "branch", "date": "Pollution", "children": [
                {"label": "Heavy Metals: Effluents from coastal factories causing bioaccumulation in shellfish", "type": "leaf"},
                {"label": "Eutrophication: Agricultural runoff causing algal blooms and hypoxic dead zones", "type": "leaf"}
            ]},
            {"label": "Physical Modifications", "type": "branch", "date": "Modifications", "children": [
                {"label": "Port Dredging: Destroys benthic habitats, increases turbidity, blocking light", "type": "leaf"},
                {"label": "Land Reclamation: Converting estuarine mudflats into urban real estate or ports", "type": "leaf"}
            ]},
            {"label": "Hydrological Disruptions", "type": "branch", "date": "Hydrology", "children": [
                {"label": "Upstream Dams: Traps freshwater and river nutrients, allowing marine salt water intrusion", "type": "leaf"},
                {"label": "Barrages: Blocks migratory pathway of fish (e.g. Hilsa) spawning in rivers", "type": "leaf"}
            ]},
            {"label": "UPSC Mitigation Focus", "type": "branch", "date": "UPSC Core", "children": [
                {"label": "Policy: Enforcing CRZ-I regulations to ban development in mudflats and salt marshes", "type": "leaf"},
                {"label": "EIA: Restricting major engineering projects without Environmental Impact Assessments", "type": "leaf"}
            ]}
        ],
        "hi": [
            {"label": "शहरी और औद्योगिक प्रदूषण", "type": "branch", "date": "प्रदूषण", "children": [
                {"label": "भारी धातुएँ: तटीय कारखानों से निकलने वाले अपशिष्ट जो शंखधारी जीवों में संचित होते हैं", "type": "leaf"},
                {"label": "यूट्रोफिकेशन: कृषि अपवाह से अल्गल ब्लूम और हाइपोक्सिक मृत क्षेत्रों का निर्माण", "type": "leaf"}
            ]},
            {"label": "भौतिक संशोधन", "type": "branch", "date": "भौतिक संशोधन", "children": [
                {"label": "बंदरगाह ड्रेजिंग: नितल आवासों को नष्ट करता है, गंदलापन बढ़ाता है, जिससे प्रकाश रुकता है", "type": "leaf"},
                {"label": "भूमि सुधार: दलदली मैदानों (Mudflats) को शहरी रियल एस्टेट या बंदरगाहों में बदलना", "type": "leaf"}
            ]},
            {"label": "जल विज्ञान संबंधी व्यवधान", "type": "branch", "date": "जल विज्ञान", "children": [
                {"label": "ऊपरी बांध: मीठे पानी और पोषक तत्वों को रोकते हैं, जिससे समुद्री नमक के पानी का आक्रमण बढ़ता है", "type": "leaf"},
                {"label": "बैराज: नदियों में अंडे देने वाली प्रवासी मछलियों (जैसे हिल्सा) के मार्ग को अवरुद्ध करना", "type": "leaf"}
            ]},
            {"label": "यूपीएससी शमन फोकस", "type": "branch", "date": "यूपीएससी", "children": [
                {"label": "नीति: कीचड़ के मैदानों और नमक के दलदलों में विकास को प्रतिबंधित करने के लिए CRZ-I नियमों को लागू करना", "type": "leaf"},
                {"label": "EIA: बिना पर्यावरण प्रभाव आकलन के प्रमुख इंजीनियरिंग परियोजनाओं को प्रतिबंधित करना", "type": "leaf"}
            ]}
        ]
    },
    "threats-to-wetland-ecosystems": {
        "en": [
            {"label": "Urbanization Encroachment", "type": "branch", "date": "Encroachment", "children": [
                {"label": "Drainage: Wetlands filled up for infrastructure development (e.g. East Kolkata wetlands threat)", "type": "leaf"},
                {"label": "Siltation: Silt from deforestation filling up lakes, reducing depth and storage", "type": "leaf"}
            ]},
            {"label": "Pollution Pressure", "type": "branch", "date": "Pollution", "children": [
                {"label": "Agricultural Runoff: Excess nitrogen and phosphorus inducing eutrophication", "type": "leaf"},
                {"label": "Industrial Effluents: Untreated discharge depositing toxic heavy metals in sediment", "type": "leaf"}
            ]},
            {"label": "Weed Invasion", "type": "branch", "date": "Weeds", "children": [
                {"label": "Water Hyacinth: Rapidly covers lake surfaces, depleting dissolved oxygen", "type": "leaf"},
                {"label": "Prosopis Juliflora: Invasive shrub drying up wetland shorelines", "type": "leaf"}
            ]},
            {"label": "UPSC Mitigation Core", "type": "branch", "date": "UPSC Core", "children": [
                {"label": "Policies: Implementation of Wetlands Rules 2017 to empower state enforcement", "type": "leaf"},
                {"label": "Montreux Record: Monitoring heavily degraded Ramsar sites for priority restoration funding", "type": "leaf"}
            ]}
        ],
        "hi": [
            {"label": "शहरीकरण का अतिक्रमण", "type": "branch", "date": "अतिक्रमण", "children": [
                {"label": "जल निकासी: बुनियादी ढांचे के विकास के लिए आर्द्रभूमियों को भरना (जैसे पूर्व कोलकाता आर्द्रभूमि खतरा)", "type": "leaf"},
                {"label": "गाद जमाव: वनों की कटाई से निकलने वाली गाद झीलों को भरती है, जिससे गहराई और जल संचय क्षमता कम होती है", "type": "leaf"}
            ]},
            {"label": "प्रदूषण का दबाव", "type": "branch", "date": "प्रदूषण", "children": [
                {"label": "कृषि अपवाह: अत्यधिक नाइट्रोजन और फास्फोरस यूट्रोफिकेशन को बढ़ावा देते हैं", "type": "leaf"},
                {"label": "औद्योगिक अपशिष्ट: अनुपचारित निर्वहन तलछट में जहरीली भारी धातुओं को जमा करता है", "type": "leaf"}
            ]},
            {"label": "खरपतवार का आक्रमण", "type": "branch", "date": "खरपतवार", "children": [
                {"label": "जलकुंभी: झीलों की सतह को तेजी से ढकती है, जिससे घुलित ऑक्सीजन समाप्त हो जाती है", "type": "leaf"},
                {"label": "प्रोसोपिस जूलिफ्लोरा: आक्रामक झाड़ी जो आर्द्रभूमि के किनारे सुखा देती है", "type": "leaf"}
            ]},
            {"label": "यूपीएससी शमन रणनीतियाँ", "type": "branch", "date": "यूपीएससी", "children": [
                {"label": "नीतियां: राज्य प्रवर्तन को सशक्त बनाने के लिए आर्द्रभूमि नियम 2017 का कार्यान्वयन", "type": "leaf"},
                {"label": "मॉन्ट्रो रिकॉर्ड: प्राथमिकता बहाली वित्त पोषण के लिए अत्यधिक निम्नीकृत रामसर स्थलों की निगरानी", "type": "leaf"}
            ]}
        ]
    },
    "tropical-deciduous-forests": {
        "en": [
            {"label": "Dry vs Moist Types", "type": "branch", "date": "Subtypes", "children": [
                {"label": "Moist Deciduous: Rainfall 100-200 cm; transitional to evergreen; teak, sal, rosewood dominate", "type": "leaf"},
                {"label": "Dry Deciduous: Rainfall 70-100 cm; transitional to thorn forest; tendu, amaltas, khair dominate", "type": "leaf"}
            ]},
            {"label": "Adaptations", "type": "branch", "date": "Adaptations", "children": [
                {"label": "Leaf Shedding: Shed leaves for 6-8 weeks during dry spring to conserve water via transpiration", "type": "leaf"},
                {"label": "Thick Bark: Fire-resistant trunks adapting to dry season brush fires", "type": "leaf"}
            ]},
            {"label": "Indian Distribution", "type": "branch", "date": "India Distribution", "children": [
                {"label": "Moist Deciduous: Western Ghats slopes, Shivalik foothills, North-East states, Odisha", "type": "leaf"},
                {"label": "Dry Deciduous: Plains of Uttar Pradesh, Bihar, and interior parts of Deccan plateau", "type": "leaf"}
            ]},
            {"label": "UPSC Forestry Focus", "type": "branch", "date": "UPSC Core", "children": [
                {"label": "Economic Value: Source of valuable timber (teak, sal), sandalwood, and minor forest produce (tendu leaves)", "type": "leaf"},
                {"label": "Deforestation: Extensively cleared for agricultural expansion and commercial plantations", "type": "leaf"}
            ]}
        ],
        "hi": [
            {"label": "शुष्क बनाम नम प्रकार", "type": "branch", "date": "उपप्रकार", "children": [
                {"label": "नम पर्णपाती: वर्षा 100-200 सेमी; सदाबहार में परिवर्तित; सागौन, साल, शीशम का प्रभुत्व", "type": "leaf"},
                {"label": "शुष्क पर्णपाती: वर्षा 70-100 सेमी; कांटेदार वनों में परिवर्तित; तेंदू, अमलतास, खैर का प्रभुत्व", "type": "leaf"}
            ]},
            {"label": "पारिस्थितिक अनुकूलन", "type": "branch", "date": "अनुकूलन", "children": [
                {"label": "पर्णपात: वाष्पोत्सर्जन को कम करने के लिए शुष्क वसंत में 6-8 सप्ताह के लिए पत्तियां गिराते हैं", "type": "leaf"},
                {"label": "मोटी छाल: शुष्क मौसम की आग के अनुकूल अग्निरोधी तने का विकास", "type": "leaf"}
            ]},
            {"label": "भारतीय वितरण", "type": "branch", "date": "भारतीय वितरण", "children": [
                {"label": "नम पर्णपाती: पश्चिमी घाट के पूर्वी ढलान, शिवालिक तलहटी, पूर्वोत्तर राज्य, ओडिशा", "type": "leaf"},
                {"label": "शुष्क पर्णपाती: उत्तर प्रदेश, बिहार के मैदान और दक्कन के पठार के आंतरिक भाग", "type": "leaf"}
            ]},
            {"label": "यूपीएससी वानिकी फोकस", "type": "branch", "date": "यूपीएससी", "children": [
                {"label": "आर्थिक मूल्य: मूल्यवान लकड़ी (सागौन, साल), चंदन और लघु वन उपज (तेंदू पत्ता) का स्रोत", "type": "leaf"},
                {"label": "वनोन्मूलन: कृषि विस्तार और वाणिज्यिक वृक्षारोपण के लिए बड़े पैमाने पर सफ़ाई की गई है", "type": "leaf"}
            ]}
        ]
    },
    "tropical-evergreen-and-semi-evergreen-forests": {
        "en": [
            {"label": "Climatic Parameters", "type": "branch", "date": "Climate", "children": [
                {"label": "Rainfall & Temp: Annual precipitation exceeding 250 cm; mean annual temperature > 22°C", "type": "leaf"},
                {"label": "Evergreen Nature: No uniform leaf-shedding season; forests appear green year-round", "type": "leaf"}
            ]},
            {"label": "Structural Complexity", "type": "branch", "date": "Structure", "children": [
                {"label": "Layered Canopy: Multi-layered vertical structure; tall trees (>60m), shrubs, and ground ferns", "type": "leaf"},
                {"label": "Epiphytes: Abundant orchids, lianas climbing trees to access sunlight", "type": "leaf"}
            ]},
            {"label": "Flora & Fauna Indicators", "type": "branch", "date": "Biodiversity", "children": [
                {"label": "Key Trees: Rosewood, Mahogany, Ebony, Semul, Gurjan, and bamboo brakes", "type": "leaf"},
                {"label": "Fauna: Lion-tailed Macaque (Western Ghats), Hoolock Gibbon (North-East India)", "type": "leaf"}
            ]},
            {"label": "UPSC India Distribution", "type": "branch", "date": "UPSC Core", "children": [
                {"label": "Geographical Range: Western slopes of Western Ghats, Lakshadweep, Andaman Islands, and North-East hills", "type": "leaf"},
                {"label": "Semi-evergreen: Found in transitional areas with lower rainfall; mixture of evergreen and deciduous species", "type": "leaf"}
            ]}
        ],
        "hi": [
            {"label": "जलवायु कारक", "type": "branch", "date": "जलवायु", "children": [
                {"label": "वर्षा और तापमान: 250 सेमी से अधिक वार्षिक वर्षा; औसत वार्षिक तापमान > 22°C", "type": "leaf"},
                {"label": "सदाबहार प्रकृति: पत्तियों को गिराने का कोई निश्चित मौसम नहीं; वन साल भर हरे दिखाई देते हैं", "type": "leaf"}
            ]},
            {"label": "संरचनात्मक जटिलता", "type": "branch", "date": "संरचना", "children": [
                {"label": "स्तरित वितान: बहुस्तरीय लंबवत संरचना; ऊंचे पेड़ (>60m), झाड़ियां और जमीनी फर्न", "type": "leaf"},
                {"label": "अधिपादप (Epiphytes): धूप तक पहुँचने के लिए पेड़ों पर चढ़ने वाले प्रचुर ऑर्किड और लताएँ (Lianas)", "type": "leaf"}
            ]},
            {"label": "वनस्पति और जीव संकेतक", "type": "branch", "date": "जैव विविधता", "children": [
                {"label": "प्रमुख वृक्ष: शीशम, महोगनी, आबनूस, सेमल, गुर्जन और बांस के झुरमुट", "type": "leaf"},
                {"label": "जीव: शेर जैसी पूंछ वाला बंदर (पश्चिमी घाट), हूलॉक गिब्बन (पूर्वोत्तर भारत)", "type": "leaf"}
            ]},
            {"label": "यूपीएससी भारत वितरण", "type": "branch", "date": "यूपीएससी", "children": [
                {"label": "भौगोलिक सीमा: पश्चिमी घाट के पश्चिमी ढलान, लक्षद्वीप, अंडमान द्वीप समूह और पूर्वोत्तर पहाड़ियाँ", "type": "leaf"},
                {"label": "अर्ध-सदाबहार: कम वर्षा वाले संक्रमण क्षेत्रों में पाए जाते हैं; सदाबहार और पर्णपाती प्रजातियों का मिश्रण", "type": "leaf"}
            ]}
        ]
    },
    "tropical-thorn-forests": {
        "en": [
            {"label": "Climatic Limits", "type": "branch", "date": "Climate", "children": [
                {"label": "Rainfall Limits: Annual precipitation is less than 50 cm", "type": "leaf"},
                {"label": "Arid Transition: Transitions into desert scrubs in hot dry plains", "type": "leaf"}
            ]},
            {"label": "Xerophytic Adaptations", "type": "branch", "date": "Adaptations", "children": [
                {"label": "Thorns: Leaves reduced to thorns to prevent water loss and protect from herbivores", "type": "leaf"},
                {"label": "Stems & Bark: Succulent green stems performing photosynthesis; thick bark to resist fires", "type": "leaf"}
            ]},
            {"label": "Flora & Fauna", "type": "branch", "date": "Flora & Fauna", "children": [
                {"label": "Key Trees: Babool, Kikar, Neem, Khejri, Date Palms, and Euphorbia species", "type": "leaf"},
                {"label": "Fauna: Blackbuck, Chinkara, Wild Ass (Rann of Kutch), Desert Fox", "type": "leaf"}
            ]},
            {"label": "UPSC India Geography", "type": "branch", "date": "UPSC Core", "children": [
                {"label": "Geographical Range: Semi-arid areas of South-West Punjab, Haryana, Rajasthan, Gujarat, and dry rain-shadow parts of Deccan", "type": "leaf"},
                {"label": "Khejri Significance: National tree of Rajasthan; key agroforestry tree worshipped by Bishnoi community", "type": "leaf"}
            ]}
        ],
        "hi": [
            {"label": "जलवायु सीमाएं", "type": "branch", "date": "शुष्क जलवायु", "children": [
                {"label": "वर्षा सीमा: वार्षिक वर्षा 50 सेमी से कम होती है", "type": "leaf"},
                {"label": "शुष्क संक्रमण: गर्म शुष्क मैदानों में मरुस्थलीय झाड़ियों में संक्रमण", "type": "leaf"}
            ]},
            {"label": "मरुद्भिद (Xerophytic) अनुकूलन", "type": "branch", "date": "अनुकूलन", "children": [
                {"label": "कांटे: पानी के नुकसान को रोकने और शाकाहारियों से बचाने के लिए पत्तियां कांटों में रूपांतरित", "type": "leaf"},
                {"label": "तने और छाल: मांसल हरे तने जो प्रकाश संश्लेषण करते हैं; आग से बचाव के लिए मोटी छाल", "type": "leaf"}
            ]},
            {"label": "वनस्पति और जीव", "type": "branch", "date": "जीव व वनस्पति", "children": [
                {"label": "प्रमुख वृक्ष: बबूल, कीकर, नीम, खेजड़ी, खजूर और यूफोरबिया की प्रजातियां", "type": "leaf"},
                {"label": "जीव: काला हिरण, चिंकारा, जंगली गधा (कच्छ का रन), मरुस्थलीय लोमड़ी", "type": "leaf"}
            ]},
            {"label": "यूपीएससी भारत भूगोल", "type": "branch", "date": "यूपीएससी", "children": [
                {"label": "भौगोलिक सीमा: दक्षिण-पश्चिम पंजाब, हरियाणा, राजस्थान, गुजरात के अर्ध-शुष्क क्षेत्र और दक्कन के शुष्क वृष्टि-छाया क्षेत्र", "type": "leaf"},
                {"label": "खेजड़ी का महत्व: राजस्थान का राज्य वृक्ष; बिश्नोई समुदाय द्वारा पूजनीय प्रमुख कृषि-वानिकी वृक्ष", "type": "leaf"}
            ]}
        ]
    },
    "tundra": {
        "en": [
            {"label": "Permafrost Soils", "type": "branch", "date": "Soil", "children": [
                {"label": "Active Layer: Thin upper soil layer melting briefly in summer supporting vegetation", "type": "leaf"},
                {"label": "Frozen Subsoil: Underneath soil is permanently frozen year-round, blocking deep root growth", "type": "leaf"}
            ]},
            {"label": "Vegetative Adaptations", "type": "branch", "date": "Vegetation", "children": [
                {"label": "Low Profile: Cushion-like dwarf shrubs, mosses, and lichens close to ground to avoid wind", "type": "leaf"},
                {"label": "Short Lifecycle: Rapid growth and seed production during brief 50-60 day summer", "type": "leaf"}
            ]},
            {"label": "Faunal Adaptations", "type": "branch", "date": "Fauna", "children": [
                {"label": "Insulation: Thick fur coats and fat layers (blubber) in mammals (e.g. Musk Ox, Caribou)", "type": "leaf"},
                {"label": "Migration: Birds and larger mammals migrate south before polar winter onset", "type": "leaf"}
            ]},
            {"label": "UPSC Global Climate", "type": "branch", "date": "UPSC Core", "children": [
                {"label": "Arctic Amplification: Polar regions warming faster than global average, melting permafrost", "type": "leaf"},
                {"label": "Methane Threat: Melting permafrost releases trapped methane gas, accelerating climate feedback", "type": "leaf"}
            ]}
        ],
        "hi": [
            {"label": "पर्माफ्रॉस्ट मिट्टी", "type": "branch", "date": "मिट्टी", "children": [
                {"label": "सक्रिय परत: पतली ऊपरी परत जो गर्मियों में कुछ समय के लिए पिघलती है और वनस्पति का समर्थन करती है", "type": "leaf"},
                {"label": "जमी हुई उपमृदा: नीचे की मिट्टी साल भर जमी रहती है, जिससे गहरी जड़ों का विकास रुक जाता है", "type": "leaf"}
            ]},
            {"label": "वनस्पति अनुकूलन", "type": "branch", "date": "वनस्पति", "children": [
                {"label": "बौना कद: हवा से बचने के लिए जमीन के करीब कुशन जैसी बौनी झाड़ियाँ, काई और लाइकेन का विकास", "type": "leaf"},
                {"label": "लघु जीवन चक्र: संक्षिप्त 50-60 दिनों की गर्मियों के दौरान तेजी से विकास और बीज उत्पादन", "type": "leaf"}
            ]},
            {"label": "जीव अनुकूलन", "type": "branch", "date": "जीव अनुकूलन", "children": [
                {"label": "इन्सुलेशन: स्तनधारियों में घने फर और वसा की परतें (जैसे कस्तूरी बैल, कैरीबौ)", "type": "leaf"},
                {"label": "प्रवास: ध्रुवीय सर्दियों की शुरुआत से पहले पक्षी और बड़े स्तनधारी दक्षिण की ओर चले जाते हैं", "type": "leaf"}
            ]},
            {"label": "यूपीएससी वैश्विक जलवायु", "type": "branch", "date": "यूपीएससी", "children": [
                {"label": "आर्कटिक प्रवर्धन: वैश्विक औसत की तुलना में ध्रुवीय क्षेत्रों का तेजी से गर्म होना, पर्माफ्रॉस्ट पिघलना", "type": "leaf"},
                {"label": "मीथेन का खतरा: पर्माफ्रॉस्ट पिघलने से फंसी हुई मीथेन गैस निकलती है, जो जलवायु फीडबैक को तेज करती है", "type": "leaf"}
            ]}
        ]
    },
    "turbidity-and-transparency": {
        "en": [
            {"label": "Physics of Turbidity", "type": "branch", "date": "Physics", "children": [
                {"label": "Definition: Measure of relative clarity of liquid; suspended solids scatter light", "type": "leaf"},
                {"label": "Measurement: Measured in Nephelometric Turbidity Units (NTU) or using Secchi discs", "type": "leaf"}
            ]},
            {"label": "Light Limitation", "type": "branch", "date": "Light Limit", "children": [
                {"label": "Photic Depth Reduction: High turbidity absorbs/scatters sunlight, reducing photic layer depth", "type": "leaf"},
                {"label": "Photosynthesis Stop: Decreased primary production by phytoplankton and benthic seagrasses", "type": "leaf"}
            ]},
            {"label": "Causes of Turbidity", "type": "branch", "date": "Causes", "children": [
                {"label": "Natural: River sediment runoff, tidal churning of mudflats, and organic detritus", "type": "leaf"},
                {"label": "Human: Coastal dredging, mining discharge, urban stormwater, and sewage runoffs", "type": "leaf"}
            ]},
            {"label": "UPSC Environmental Core", "type": "branch", "date": "UPSC Core", "children": [
                {"label": "Coral Reef Smothering: Siltation blocks zooxanthellae photosynthesis and physically chokes polyps", "type": "leaf"},
                {"label": "Riparian Restoration: Forest buffers along rivers trap sediments, restoring downstream transparency", "type": "leaf"}
            ]}
        ],
        "hi": [
            {"label": "गंदलापन की भौतिकी", "type": "branch", "date": "भौतिकी", "children": [
                {"label": "परिभाषा: तरल की सापेक्ष स्पष्टता का माप; निलंबित कण प्रकाश को बिखेरते हैं", "type": "leaf"},
                {"label": "मापन: नेफेलोमेट्रिक टर्बिडिटी यूनिट्स (NTU) या सेची डिस्क का उपयोग करके मापा जाता है", "type": "leaf"}
            ]},
            {"label": "प्रकाश की सीमा", "type": "branch", "date": "प्रकाश सीमा", "children": [
                {"label": "प्रकाशीय गहराई में कमी: उच्च गंदलापन धूप को अवशोषित करता है, जिससे प्रकाशीय परत पतली हो जाती है", "type": "leaf"},
                {"label": "प्रकाश संश्लेषण अवरोध: पादप प्लवक और समुद्री घास द्वारा प्राथमिक उत्पादन में गिरावट", "type": "leaf"}
            ]},
            {"label": "गंदलापन के कारण", "type": "branch", "date": "कारण", "children": [
                {"label": "प्राकृतिक: नदी तलछट अपवाह, कीचड़ के मैदानों का ज्वारीय मंथन और कार्बनिक कचरा", "type": "leaf"},
                {"label": "मानव जनित: तटीय ड्रेजिंग, खनन अपशिष्ट, शहरी तूफान जल और अनुपचारित सीवेज अपवाह", "type": "leaf"}
            ]},
            {"label": "यूपीएससी पर्यावरण कोर", "type": "branch", "date": "यूपीएससी", "children": [
                {"label": "प्रवाल भित्ति दमघुटन: तलछट ज़ूक्सैंथेले प्रकाश संश्लेषण को अवरुद्ध करता है और पॉलिप्स का दम घोटता है", "type": "leaf"},
                {"label": "तटीय वनरोपण: नदियों के किनारे वन बफर तलछट को रोकते हैं, जिससे पारदर्शिता बहाल होती है", "type": "leaf"}
            ]}
        ]
    },
    "types-of-coral-reefs": {
        "en": [
            {"label": "Fringing Reefs (Shore)", "type": "branch", "date": "Fringing", "children": [
                {"label": "Location: Grows directly from shorelines of continents or volcanic islands", "type": "leaf"},
                {"label": "Structure: Lacks a deep lagoon; vulnerable to coastal agricultural runoff and siltation", "type": "leaf"}
            ]},
            {"label": "Barrier Reefs (Offshore)", "type": "branch", "date": "Barrier", "children": [
                {"label": "Lagoon Divider: Separated from coast by a wide, deep channel or lagoon", "type": "leaf"},
                {"label": "Great Barrier Reef: World's largest system; runs parallel to Queensland (Australia) coast", "type": "leaf"}
            ]},
            {"label": "Atolls (Circular)", "type": "branch", "date": "Atolls", "children": [
                {"label": "Form: Ring-shaped reef enclosing a central deep lagoon with no central volcanic peak", "type": "leaf"},
                {"label": "Darwin Model: Formed as volcanic island subsides slowly while coral reef grows upwards", "type": "leaf"}
            ]},
            {"label": "UPSC Geomorphology Core", "type": "branch", "date": "UPSC Core", "children": [
                {"label": "Subsidence Theory: Darwin's evolutionary progression model from fringing -> barrier -> atoll", "type": "leaf"},
                {"label": "India Examples: Lakshadweep (atolls); Gulf of Mannar and Andamans (fringing reefs)", "type": "leaf"}
            ]}
        ],
        "hi": [
            {"label": "तटीय प्रवाल भित्ति (Fringing)", "type": "branch", "date": "तटीय भित्ति", "children": [
                {"label": "स्थिति: महाद्वीपों या ज्वालामुखी द्वीपों की तटरेखाओं से सीधे विकसित होती है", "type": "leaf"},
                {"label": "संरचना: गहरे लैगून का अभाव; तटीय कृषि अपवाह और गाद जमाव के प्रति अत्यधिक संवेदनशील", "type": "leaf"}
            ]},
            {"label": "अवरोधक प्रवाल भित्ति (Barrier)", "type": "branch", "date": "अवरोधक", "children": [
                {"label": "लैगून विभाजक: एक विस्तृत, गहरे चैनल या लैगून द्वारा तट से अलग होती है", "type": "leaf"},
                {"label": "ग्रेट बैरियर रीफ: विश्व की सबसे बड़ी प्रणाली; क्वींसलैंड (ऑस्ट्रेलिया) तट के समानांतर विस्तृत", "type": "leaf"}
            ]},
            {"label": "वलयाकार प्रवाल द्वीप (Atoll)", "type": "branch", "date": "एटोल", "children": [
                {"label": "आकृति: मध्य गहरे लैगून को घेरने वाली अंगूठी के आकार की भित्ति; कोई ज्वालामुखी शिखर शेष नहीं रहता", "type": "leaf"},
                {"label": "डार्विन मॉडल: ज्वालामुखी द्वीप के धीरे-धीरे डूबने से निर्मित जब प्रवाल ऊपर की ओर बढ़ता है", "type": "leaf"}
            ]},
            {"label": "यूपीएससी भू-आकृति विज्ञान कोर", "type": "branch", "date": "यूपीएससी", "children": [
                {"label": "अवतलन सिद्धांत: डार्विन का विकासवादी मॉडल (तटीय -> अवरोधक -> एटोल)", "type": "leaf"},
                {"label": "भारतीय उदाहरण: लक्षद्वीप (एटोल); मन्नार की खाड़ी और अंडमान (तटीय प्रवाल भित्तियाँ)", "type": "leaf"}
            ]}
        ]
    },
    "types-of-estuaries": {
        "en": [
            {"label": "Geomorphological Types", "type": "branch", "date": "Geomorphology", "children": [
                {"label": "Drowned River Valleys: Formed by rising post-glacial sea level flooding valleys (e.g. Hudson River)", "type": "leaf"},
                {"label": "Bar-built Estuaries: Sandbars build parallel to coast, creating shallow lagoons (e.g. Outer Banks)", "type": "leaf"}
            ]},
            {"label": "Tectonic & Fjords", "type": "branch", "date": "Tectonic & Fjord", "children": [
                {"label": "Tectonic Estuaries: Formed by land subsidence along fault zones (e.g. San Francisco Bay)", "type": "leaf"},
                {"label": "Fjords: Glacial-carved deep valleys flooded by sea water with sill structures (e.g. Norway fjords)", "type": "leaf"}
            ]},
            {"label": "Water Mixing Types", "type": "branch", "date": "Mixing", "children": [
                {"label": "Salt-wedge: High river flow pushes fresh water over denser saltwater layer, forming wedge", "type": "leaf"},
                {"label": "Well-mixed: Strong tidal mixing creates uniform salinity from surface to bottom", "type": "leaf"}
            ]},
            {"label": "UPSC Syllabus Core", "type": "branch", "date": "UPSC Core", "children": [
                {"label": "Classification Value: Helps identify sediment dispersal patterns and benthic species zones", "type": "leaf"},
                {"label": "Indian Examples: Hooghly estuary (well-mixed deltaic); Zuari and Mandovi (tides dominate)", "type": "leaf"}
            ]}
        ],
        "hi": [
            {"label": "भू-आकृतिक प्रकार", "type": "branch", "date": "भू-आकृतिक", "children": [
                {"label": "डूब चुकी नदी घाटियाँ: हिमनद-पश्चात समुद्र के स्तर में वृद्धि से घाटियों के जलमग्न होने से निर्मित", "type": "leaf"},
                {"label": "बार-बिल्ट ज्वारनदमुख: रेत की पट्टियाँ तट के समानांतर बनती हैं, जिससे उथले लैगून बनते हैं", "type": "leaf"}
            ]},
            {"label": "विवर्तनिक और फियोर्ड", "type": "branch", "date": "विवर्तनिक", "children": [
                {"label": "विवर्तनिक ज्वारनदमुख: फॉल्ट जोन के साथ भूमि के धंसने से निर्मित (जैसे सैन फ्रांसिस्को खाड़ी)", "type": "leaf"},
                {"label": "फियोर्ड (Fjords): समुद्र के पानी से भरी गहरी हिमनद-कटौती घाटियाँ (जैसे नॉर्वे के फियोर्ड)", "type": "leaf"}
            ]},
            {"label": "जल मिश्रण प्रकार", "type": "branch", "date": "जल मिश्रण", "children": [
                {"label": "सॉल्ट-वेज (Salt-wedge): तीव्र नदी प्रवाह मीठे पानी को सघन खारे पानी की परत के ऊपर धकेलता है", "type": "leaf"},
                {"label": "वेल-मिक्स्ड (Well-mixed): तीव्र ज्वारीय मिश्रण सतह से नीचे तक समान लवणता बनाता है", "type": "leaf"}
            ]},
            {"label": "यूपीएससी पाठ्यक्रम कोर", "type": "branch", "date": "यूपीएससी", "children": [
                {"label": "वर्गीकरण का महत्व: तलछट प्रसार पैटर्न और नितल प्रजातियों के क्षेत्रों की पहचान करने में मदद करता है", "type": "leaf"},
                {"label": "भारतीय उदाहरण: हुगली ज्वारनदमुख (अच्छी तरह से मिश्रित); जुआरी और मांडवी (ज्वार का प्रभुत्व)", "type": "leaf"}
            ]}
        ]
    },
    "types-of-wetlands": {
        "en": [
            {"label": "Inland Wetlands", "type": "branch", "date": "Inland", "children": [
                {"label": "Marshes: Frequently flooded wetlands dominated by herbaceous plants (cattails, reeds)", "type": "leaf"},
                {"label": "Swamps: Forested wetlands dominated by water-tolerant woody trees (e.g. Cypress, Mangrove)", "type": "leaf"},
                {"label": "Bogs & Fens: Peat-accumulating wetlands; bogs are acidic and rainwater-fed; fens are alkaline and groundwater-fed", "type": "leaf"}
            ]},
            {"label": "Coastal/Marine Wetlands", "type": "branch", "date": "Coastal", "children": [
                {"label": "Estuaries: Salt marshes and brackish lagoons at river mouth boundaries", "type": "leaf"},
                {"label": "Mangrove Swamps: Intertidal coastal tracts dominated by halophytic tree species", "type": "leaf"}
            ]},
            {"label": "Man-Made Wetlands", "type": "branch", "date": "Man-made", "children": [
                {"label": "Reservoirs & Tanks: Constructed for agricultural irrigation and drinking storage", "type": "leaf"},
                {"label": "Paddy Fields: Seasonally flooded agricultural lands serving as secondary waterfowl habitats", "type": "leaf"}
            ]},
            {"label": "UPSC Wetland Policy", "type": "branch", "date": "UPSC Core", "children": [
                {"label": "Ramsar Scheme: Groups wetlands into Marine/Coastal, Inland, and Human-made categories", "type": "leaf"},
                {"label": "Conservation Priority: Inland marshes and high-altitude lakes in Himalayas (e.g. Tso Moriri)", "type": "leaf"}
            ]}
        ],
        "hi": [
            {"label": "अंतर्देशीय आर्द्रभूमियां", "type": "branch", "date": "अंतर्देशीय", "children": [
                {"label": "दलदल (Marshes): शाकीय पौधों (जैसे ईख) के प्रभुत्व वाली अक्सर जलमग्न रहने वाली आर्द्रभूमियां", "type": "leaf"},
                {"label": "दलदली वन (Swamps): जल-सहनशील काष्ठीय पेड़ों (जैसे सरू, मैंग्रोव) के प्रभुत्व वाले वन", "type": "leaf"},
                {"label": "बॉग्स और फेन्स: पीट जमा करने वाली आर्द्रभूमियां; बॉग्स अम्लीय और वर्षा आधारित होते हैं; फेन्स क्षारीय होते हैं", "type": "leaf"}
            ]},
            {"label": "तटीय/समुद्री आर्द्रभूमियां", "type": "branch", "date": "तटीय", "children": [
                {"label": "ज्वारनदमुख: नदी मुहाने की सीमाओं पर खारे दलदल और खारी झीलें", "type": "leaf"},
                {"label": "मैंग्रोव दलदल: लवणमृदोद्भिद वृक्ष प्रजातियों के प्रभुत्व वाले तटीय क्षेत्र", "type": "leaf"}
            ]},
            {"label": "मानव निर्मित आर्द्रभूमियां", "type": "branch", "date": "मानव निर्मित", "children": [
                {"label": "जलाशय और टैंक: कृषि सिंचाई और पेयजल भंडारण के लिए निर्मित संरचनाएं", "type": "leaf"},
                {"label": "धान के खेत: मौसमी रूप से जलमग्न कृषि भूमि जो जलीय पक्षियों के आवास का कार्य करती है", "type": "leaf"}
            ]},
            {"label": "यूपीएससी आर्द्रभूमि नीति", "type": "branch", "date": "यूपीएससी", "children": [
                {"label": "रामसर योजना: आर्द्रभूमियों को तटीय, अंतर्देशीय और मानव निर्मित श्रेणियों में विभाजित करती है", "type": "leaf"},
                {"label": "संरक्षण प्राथमिकता: हिमालय में अंतर्देशीय दलदल और उच्च ऊंचाई वाली झीलें (जैसे त्सो मोरीरी)", "type": "leaf"}
            ]}
        ]
    },
    "uses-of-coral-reefs": {
        "en": [
            {"label": "Coastal Defense Shield", "type": "branch", "date": "Defense Shield", "children": [
                {"label": "Wave Energy Absorption: Buffer zones reducing storm wave height by up to 97%", "type": "leaf"},
                {"label": "Erosion Control: Protects shoreline beaches and property from severe cyclonic damage", "type": "leaf"}
            ]},
            {"label": "Economic Valuation", "type": "branch", "date": "Economic Value", "children": [
                {"label": "Fisheries Support: Hosts 25% of marine fish species, providing critical food resources for millions", "type": "leaf"},
                {"label": "Tourism Industry: Major source of international diving tourism revenues", "type": "leaf"}
            ]},
            {"label": "Medicinal Discoveries", "type": "branch", "date": "Medicine", "children": [
                {"label": "Coral Skeletons: Used as bone graft materials due to structural similarity to human bone", "type": "leaf"},
                {"label": "Chemical Compounds: Source of active compounds used in cancer, AIDS, and cardiovascular drugs", "type": "leaf"}
            ]},
            {"label": "UPSC Core Analysis", "type": "branch", "date": "UPSC Core", "children": [
                {"label": "Global Heritage: Provides ecosystem services valued at trillions of dollars annually", "type": "leaf"},
                {"label": "Livelihood Security: Essential for artisanal fishermen in tropical developing countries", "type": "leaf"}
            ]}
        ],
        "hi": [
            {"label": "तटीय सुरक्षा ढाल", "type": "branch", "date": "सुरक्षा ढाल", "children": [
                {"label": "लहर ऊर्जा अवशोषण: बफर जोन जो तूफान की लहरों की ऊंचाई को 97% तक कम करते हैं", "type": "leaf"},
                {"label": "कटाव नियंत्रण: तटरेखा के समुद्र तटों और संपत्तियों को गंभीर चक्रवाती क्षति से बचाता है", "type": "leaf"}
            ]},
            {"label": "आर्थिक मूल्यांकन", "type": "branch", "date": "आर्थिक", "children": [
                {"label": "मत्स्य पालन सहायता: 25% समुद्री मछलियों की प्रजातियों का घर, लाखों लोगों को भोजन प्रदान करता है", "type": "leaf"},
                {"label": "पर्यटन उद्योग: अंतर्राष्ट्रीय डाइविंग पर्यटन राजस्व का प्रमुख स्रोत", "type": "leaf"}
            ]},
            {"label": "चिकित्सा क्षेत्र में खोजें", "type": "branch", "date": "चिकित्सा", "children": [
                {"label": "प्रवाल कंकाल: मानव हड्डी से संरचनात्मक समानता के कारण बोन ग्राफ्ट सामग्री के रूप में उपयोग", "type": "leaf"},
                {"label": "रासायनिक यौगिक: कैंसर, एड्स और हृदय रोग की दवाओं में उपयोग होने वाले सक्रिय यौगिकों का स्रोत", "type": "leaf"}
            ]},
            {"label": "यूपीएससी कोर विश्लेषण", "type": "branch", "date": "यूपीएससी", "children": [
                {"label": "वैश्विक विरासत: सालाना खरबों डॉलर मूल्य की पारितंत्र सेवाएं प्रदान करता है", "type": "leaf"},
                {"label": "आजीविका सुरक्षा: उष्णकटिबंधीय विकासशील देशों में छोटे मछुआरों के लिए आवश्यक", "type": "leaf"}
            ]}
        ]
    },
    "wetlands": {
        "en": [
            {"label": "Wetland Ecology Basics", "type": "branch", "date": "Basics", "children": [
                {"label": "Definition: Land areas saturated or inundated with water seasonally or permanently", "type": "leaf"},
                {"label": "Hydrophytes: Supports vegetation adapted to waterlogged anaerobic soil conditions", "type": "leaf"}
            ]},
            {"label": "Ecological Kidneys", "type": "branch", "date": "Kidneys", "children": [
                {"label": "Filtration: Absorbs excess nutrients, heavy metals, and suspended sediment", "type": "leaf"},
                {"label": "Recharge: Sponge action absorbing monsoon flows and recharging groundwater tables", "type": "leaf"}
            ]},
            {"label": "Ramsar Site Network", "type": "branch", "date": "Ramsar", "children": [
                {"label": "Treaty (1971): Intergovernmental treaty Signed in Ramsar, Iran promoting 'wise use'", "type": "leaf"},
                {"label": "Montreux Record: Register of Ramsar sites facing ecological degradation", "type": "leaf"}
            ]},
            {"label": "UPSC Core Questions", "type": "branch", "date": "UPSC Core", "children": [
                {"label": "India Wetland Rules 2017: Mandates State Wetland Authorities; bans waste dumping", "type": "leaf"},
                {"label": "Climate Role: Peatlands act as high-efficiency long-term terrestrial carbon sinks", "type": "leaf"}
            ]}
        ],
        "hi": [
            {"label": "आर्द्रभूमि पारिस्थितिकी मूल बातें", "type": "branch", "date": "मूल बातें", "children": [
                {"label": "परिभाषा: मौसमी या स्थायी रूप से पानी से संतृप्त या जलमग्न भूमि क्षेत्र", "type": "leaf"},
                {"label": "जलप्रिय पौधे (Hydrophytes): जलभराव वाली अवायवीय मिट्टी की स्थिति के अनुकूल वनस्पति का समर्थन", "type": "leaf"}
            ]},
            {"label": "पारिस्थितिक गुर्दे", "type": "branch", "date": "पारिस्थितिक गुर्दे", "children": [
                {"label": "अपशिष्ट निस्पंदन: अपवाह से अत्यधिक पोषक तत्वों, भारी धातुओं और निलंबित तलछट को अवशोषित करना", "type": "leaf"},
                {"label": "पुनर्भरण: मानसून के प्रवाह को अवशोषित करने और भूजल स्तर को रिचार्ज करने की स्पंज क्रिया", "type": "leaf"}
            ]},
            {"label": "रामसर साइट नेटवर्क", "type": "branch", "date": "रामसर", "children": [
                {"label": "अभिसमय (1971): आर्द्रभूमियों के 'बुद्धिमत्तापूर्ण उपयोग' को बढ़ावा देने के लिए ईरान में हस्ताक्षरित समझौता", "type": "leaf"},
                {"label": "मॉन्ट्रो रिकॉर्ड: पारिस्थितिक क्षरण का सामना कर रहे रामसर स्थलों का रजिस्टर", "type": "leaf"}
            ]},
            {"label": "यूपीएससी मुख्य प्रश्न", "type": "branch", "date": "यूपीएससी", "children": [
                {"label": "भारत आर्द्रभूमि नियम 2017: राज्य आर्द्रभूमि प्राधिकरणों को अधिकार; अपशिष्ट डंपिंग पर प्रतिबंध", "type": "leaf"},
                {"label": "जलवायु भूमिका: पीटलैंड्स उच्च दक्षता वाले दीर्घकालिक स्थलीय कार्बन सिंक के रूप में कार्य करते हैं", "type": "leaf"}
            ]}
        ]
    },
    "wetlands-in-india": {
        "en": [
            {"label": "Geographical Extent", "type": "branch", "date": "Extent", "children": [
                {"label": "Total Area: Gujarat leads in wetland area; Sundarbans is the largest Ramsar site in India", "type": "leaf"},
                {"label": "Ramsar Sites: Large network of designated wetlands under the Ramsar Convention", "type": "leaf"}
            ]},
            {"label": "Key Ramsar Sites", "type": "branch", "date": "Key Sites", "children": [
                {"label": "Chilika Lake: Odisha coast; Asia's largest brackish water lagoon; removed from Montreux Record", "type": "leaf"},
                {"label": "Loktak Lake: Manipur; famous for floating islands (phumdis) and Keibul Lamjao National Park", "type": "leaf"},
                {"label": "Keoladeo Ghana: Rajasthan; man-made wetland; crucial stop for migratory waterfowl", "type": "leaf"}
            ]},
            {"label": "Conservation Rules", "type": "branch", "date": "Rules", "children": [
                {"label": "Wetlands Rules 2017: Decentralized structure; State Wetland Authorities monitor sites", "type": "leaf"},
                {"label": "Banned Activities: Reclaiming land, setting up industries, and dumping untreated wastes", "type": "leaf"}
            ]},
            {"label": "UPSC Core Analysis", "type": "branch", "date": "UPSC Core", "children": [
                {"label": "Montreux Record: Loktak Lake and Keoladeo National Park are currently registered", "type": "leaf"},
                {"label": "Mission Amrit Sarovar: Government scheme to rejuvenate wetlands and build water security", "type": "leaf"}
            ]}
        ],
        "hi": [
            {"label": "भौगोलिक विस्तार", "type": "branch", "date": "विस्तार", "children": [
                {"label": "कुल क्षेत्रफल: गुजरात आर्द्रभूमि क्षेत्र में अग्रणी है; सुंदरवन भारत का सबसे बड़ा रामसर स्थल है", "type": "leaf"},
                {"label": "रामसर स्थल: रामसर अभिसमय के तहत नामित आर्द्रभूमियों का एक बड़ा नेटवर्क", "type": "leaf"}
            ]},
            {"label": "प्रमुख रामसर स्थल", "type": "branch", "date": "प्रमुख स्थल", "children": [
                {"label": "चिल्का झील: ओडिशा तट; एशिया की सबसे बड़ी खारे पानी की झील; मॉन्ट्रो रिकॉर्ड से हटाई गई", "type": "leaf"},
                {"label": "लोकतक झील: मणिपुर; तैरते द्वीपों (फुमदी) और केबुल लामजाओ राष्ट्रीय उद्यान के लिए प्रसिद्ध", "type": "leaf"},
                {"label": "केवलादेव घाना: राजस्थान; मानव निर्मित आर्द्रभूमि; प्रवासी पक्षियों के लिए महत्वपूर्ण पड़ाव", "type": "leaf"}
            ]},
            {"label": "संरक्षण नियम", "type": "branch", "date": "नियम", "children": [
                {"label": "आर्द्रभूमि नियम 2017: विकेंद्रीकृत संरचना; राज्य आर्द्रभूमि प्राधिकरण साइटों की निगरानी करते हैं", "type": "leaf"},
                {"label": "प्रतिबंधित गतिविधियां: भूमि सुधार, उद्योग स्थापित करना और अनुपचारित कचरा डंप करना", "type": "leaf"}
            ]},
            {"label": "यूपीएससी कोर विश्लेषण", "type": "branch", "date": "यूपीएससी", "children": [
                {"label": "मॉन्ट्रो रिकॉर्ड: लोकतक झील और केवलादेव राष्ट्रीय उद्यान वर्तमान में दर्ज हैं", "type": "leaf"},
                {"label": "मिशन अमृत सरोवर: आर्द्रभूमियों के पुनरुद्धार और जल सुरक्षा के निर्माण के लिए सरकारी योजना", "type": "leaf"}
            ]}
        ]
    },
    "zooplankton": {
        "en": [
            {"label": "Zooplankton Classification", "type": "branch", "date": "Classification", "children": [
                {"label": "Protozoans: Unicellular heterotrophs feeding on bacteria and nanoplankton", "type": "leaf"},
                {"label": "Copepods: Multicellular crustaceans; the most abundant group of zooplankton globally", "type": "leaf"}
            ]},
            {"label": "Vertical Migration", "type": "branch", "date": "Migration", "children": [
                {"label": "DVM (Diel Vertical Migration): Migrating to the surface photic zone at night to feed and returning to dark deep zone during day to avoid predators", "type": "leaf"},
                {"label": "Biological Significance: Triggers massive daily biomass transfers in the ocean water column", "type": "leaf"}
            ]},
            {"label": "Marine Food Web Role", "type": "branch", "date": "Trophic Role", "children": [
                {"label": "Trophic Link: Secondary producers converting phytoplankton biomass into food for fish and baleen whales", "type": "leaf"},
                {"label": "Fecal Pellet Fall: Excrement sinks rapidly, transporting carbon to deep-sea benthic sediments", "type": "leaf"}
            ]},
            {"label": "UPSC Oceanography Focus", "type": "branch", "date": "UPSC Core", "children": [
                {"label": "Deep Scattering Layer (DSL): Sonic-reflecting layer formed by dense migrating zooplankton and fish", "type": "leaf"},
                {"label": "Warming Stress: Ocean acidification weakens shells of calcifying zooplanktons (e.g. pteropods)", "type": "leaf"}
            ]}
        ],
        "hi": [
            {"label": "जंतु प्लवक वर्गीकरण", "type": "branch", "date": "वर्गीकरण", "children": [
                {"label": "प्रोटोजोअन: एककोशिकीय परपोषी जो बैक्टीरिया और नैनोप्लांकटन को खाते हैं", "type": "leaf"},
                {"label": "कोपेपोड्स (Copepods): बहुकोशिकीय क्रस्टेशियंस; वैश्विक स्तर पर जंतु प्लवक का सबसे प्रचुर समूह", "type": "leaf"}
            ]},
            {"label": "ऊर्ध्वाधर प्रवास (Vertical Migration)", "type": "branch", "date": "प्रवास", "children": [
                {"label": "DVM (दैनिक प्रवास): शिकारियों से बचने के लिए रात में भोजन के लिए सतह पर आना और दिन में गहरे क्षेत्र में लौटना", "type": "leaf"},
                {"label": "जैविक महत्व: महासागरीय जल स्तंभ में बड़े पैमाने पर दैनिक जैवभार स्थानांतरण को ट्रिगर करता है", "type": "leaf"}
            ]},
            {"label": "समुद्री खाद्य जाल में भूमिका", "type": "branch", "date": "पोषण भूमिका", "children": [
                {"label": "पोषण कड़ी: पादप प्लवक के जैवभार को मछलियों और बलीन व्हेल के लिए भोजन में परिवर्तित करते हैं", "type": "leaf"},
                {"label": "कार्बन सिंक: इनके मल के कण (Pellets) तेजी से नीचे डूबते हैं, जिससे कार्बन गहरे समुद्र में जमा होता है", "type": "leaf"}
            ]},
            {"label": "यूपीएससी समुद्र विज्ञान फोकस", "type": "branch", "date": "यूपीएससी", "children": [
                {"label": "डीप स्कैटरिंग लेयर (DSL): घने प्रवासी जंतु प्लवक और मछलियों द्वारा निर्मित ध्वनि-परावर्तक परत", "type": "leaf"},
                {"label": "अम्लीकरण का प्रभाव: महासागरीय अम्लीकरण कैल्सीफाइंग जंतु प्लवक (जैसे टेरोपोड) के कवच को कमजोर करता है", "type": "leaf"}
            ]}
        ]
    }
}

# Add default patterns for other folders in Terrestrial-Aquatic-Ecosystems to prevent overlaps
# Group by common types if not explicitly in DATA_MAP

def get_default_branches(fl, is_hindi):
    # Forest Types
    if any(k in fl for k in ['forest-ecosystem', 'deciduous', 'evergreen', 'thorn-forest', 'montane-forest', 'littoral-and-swamp', 'shola', 'swamp']):
        if is_hindi:
            return [
                {"label": "भारतीय वन प्रणाली", "type": "branch", "date": "वन", "children": [
                    {"label": "सदाबहार वन: भारी वर्षा (>250cm), बहुस्तरीय वितान, आबनूस और शीशम", "type": "leaf"},
                    {"label": "पर्णपाती वन: भारत में सबसे बड़े भाग पर विस्तृत; सागौन और साल प्रमुख", "type": "leaf"}
                ]},
                {"label": "पारिस्थितिक विशेषताएँ", "type": "branch", "date": "विशेषताएँ", "children": [
                    {"label": "अनुकूलन: शुष्क वसंत ऋतु में वाष्पोत्सर्जन को कम करने के लिए पत्तियों को गिराना", "type": "leaf"},
                    {"label": "सदाबहार वितान: ऊंचे पेड़ों, अधिपादपों और घने झाड़ियों की बहुस्तरीय संरचना", "type": "leaf"}
                ]},
                {"label": "वन संरक्षण नीतियां", "type": "branch", "date": "नीतियां", "children": [
                    {"label": "लक्ष्य: राष्ट्रीय वन नीति 1988 के तहत कुल क्षेत्रफल का 33% वन आवरण प्राप्त करना", "type": "leaf"},
                    {"label": "संवैधानिक प्रावधान: वन संरक्षण अधिनियम 1980 के तहत गैर-वन उपयोग पर रोक", "type": "leaf"}
                ]},
                {"label": "यूपीएससी परीक्षा दृष्टिकोण (UPSC Focus)", "type": "branch", "date": "परीक्षा", "children": [
                    {"label": "ISFR रिपोर्ट: भारतीय वन सर्वेक्षण द्वारा प्रत्येक 2 वर्ष में जारी वन आवरण के आंकड़े", "type": "leaf"},
                    {"label": "FRA 2006: वनवासियों और जनजातियों को पारंपरिक वन भूमि पर अधिकार देना", "type": "leaf"}
                ]}
            ]
        else:
            return [
                {"label": "Indian Forest System", "type": "branch", "date": "Forests", "children": [
                    {"label": "Evergreen Forests: Rainfall >250cm; multi-layered canopy; Ebony, Rosewood dominant", "type": "leaf"},
                    {"label": "Deciduous Forests: Most widespread; shed leaves for 6-8 weeks in dry season; Teak, Sal dominant", "type": "leaf"}
                ]},
                {"label": "Ecological Traits", "type": "branch", "date": "Traits", "children": [
                    {"label": "Adaptations: Broad leaves, thick bark in fire-prone zones, xerophytic needles in montane tracts", "type": "leaf"},
                    {"label": "Layered Canopy: Vertical layering maximizing light capture (canopy, sub-canopy, forest floor)", "type": "leaf"}
                ]},
                {"label": "Forest Conservation Laws", "type": "branch", "date": "Laws", "children": [
                    {"label": "National Goal: Minimum 33% of geographical area under forest cover (NFP 1988)", "type": "leaf"},
                    {"label": "Act 1980: Strict regulation of forest land diversion for industrial or mining purposes", "type": "leaf"}
                ]},
                {"label": "UPSC Exam Focus Dimensions", "type": "branch", "date": "UPSC Core", "children": [
                    {"label": "Biennial ISFR: State of Forest Report statistics compiled by FSI using remote sensing", "type": "leaf"},
                    {"label": "Forest Rights Act: Empowering forest-dwelling communities with title deeds and resource rights", "type": "leaf"}
                ]}
            ]
            
    # Wet lands
    elif any(k in fl for k in ['wetland', 'ramsar', 'water-bird-census']):
        if is_hindi:
            return [
                {"label": "आर्द्रभूमि पारितंत्र", "type": "branch", "date": "आर्द्रभूमि", "children": [
                    {"label": "परिभाषा: थल और जल के बीच का दलदली क्षेत्र जो साल भर या मौसमी रूप से जलमग्न रहता है", "type": "leaf"},
                    {"label": "पारिस्थितिक सेवाएँ: बाढ़ नियंत्रण, भूजल पुनर्भरण और जल का प्राकृतिक शुद्धिकरण", "type": "leaf"}
                ]},
                {"label": "रामसर अभिसमय", "type": "branch", "date": "रामसर", "children": [
                    {"label": "रामसर संधि (1971): ईरान में हस्ताक्षरित; आर्द्रभूमियों के बुद्धिमत्तापूर्ण उपयोग का संकल्प", "type": "leaf"},
                    {"label": "मॉन्ट्रो रिकॉर्ड: अत्यधिक संकटग्रस्त भारतीय रामसर स्थल (केवलादेव, लोकतक झील)", "type": "leaf"}
                ]},
                {"label": "खतरे और संरक्षण", "type": "branch", "date": "संरक्षण", "children": [
                    {"label": "संकट: शहरीकरण का अतिक्रमण, यूट्रोफिकेशन और आक्रामक जलकुंभी खरपतवार", "type": "leaf"},
                    {"label": "संरक्षण: आर्द्रभूमि नियम 2017 के तहत राज्य स्तर पर डिजिटल डेटाबेस और निगरानी", "type": "leaf"}
                ]},
                {"label": "यूपीएससी परीक्षा दृष्टिकोण (UPSC Focus)", "type": "branch", "date": "परीक्षा", "children": [
                    {"label": "मिशन अमृत सरोवर: स्थानीय स्तर पर जलाशयों और आर्द्रभूमियों के संरक्षण की राष्ट्रीय पहल", "type": "leaf"},
                    {"label": "प्रवासी पक्षी: आर्द्रभूमियों में प्रवासी पक्षियों की निगरानी हेतु एशियाई जलपक्षी गणना (AWC)", "type": "leaf"}
                ]}
            ]
        else:
            return [
                {"label": "Wetland Ecosystems", "type": "branch", "date": "Wetlands", "children": [
                    {"label": "Definition: Transitional zones between terrestrial and aquatic systems saturated with water", "type": "leaf"},
                    {"label": "Eco-Services: Ground water recharge, flood control, and water filtration ('ecological kidneys')", "type": "leaf"}
                ]},
                {"label": "Ramsar Treaty Frame", "type": "branch", "date": "Ramsar", "children": [
                    {"label": "Ramsar (1971): International treaty for wise use and protection of wetlands", "type": "leaf"},
                    {"label": "Montreux Record: Register of heavily degraded wetlands; Keoladeo and Loktak are listed", "type": "leaf"}
                ]},
                {"label": "Threats & Mitigation", "type": "branch", "date": "Threats", "children": [
                    {"label": "Threats: Siltation from rivers, real estate reclamation, domestic sewage runoffs", "type": "leaf"},
                    {"label": "Conservation Rules: Wetlands Rules 2017 decentralize management to State Wetland Authorities", "type": "leaf"}
                ]},
                {"label": "UPSC Exam Focus Dimensions", "type": "branch", "date": "UPSC Core", "children": [
                    {"label": "Amrit Sarovar: Government scheme to restore 75 water bodies in each district of India", "type": "leaf"},
                    {"label": "AWC Census: Annual bird counts evaluating flyways and wetland health indices", "type": "leaf"}
                ]}
            ]

    # Mangroves & Estuaries
    elif any(k in fl for k in ['estuar', 'mangrove']):
        if is_hindi:
            return [
                {"label": "तटीय पारितंत्र", "type": "branch", "date": "तटीय", "children": [
                    {"label": "ज्वारनदमुख: नदी मुहाने पर मीठे और खारे पानी का मिश्रण; पोषक जाल के कारण उच्च उत्पादकता", "type": "leaf"},
                    {"label": "मैंग्रोव: उष्णकटिबंधीय तटों पर उगने वाले लवण-सहनशील (Halophytic) झाड़ियाँ और वृक्ष", "type": "leaf"}
                ]},
                {"label": "पारिस्थितिक अनुकूलन", "type": "branch", "date": "अनुकूलन", "children": [
                    {"label": "न्यूमेटोफोर्स: अवायवीय मिट्टी में सांस लेने के लिए ऊपर की ओर बढ़ने वाली श्वसन जड़ें", "type": "leaf"},
                    {"label": "जरायुजता (Viviparity): बीजों का मूल पेड़ पर रहते हुए ही अंकुरित होना", "type": "leaf"}
                ]},
                {"label": "तटीय सुरक्षा", "type": "branch", "date": "सुरक्षा", "children": [
                    {"label": "लहर अवशोषण: घनी स्टिल्ट जड़ें तूफान और सुनामी की लहरों की ऊर्जा को सोखती हैं", "type": "leaf"},
                    {"label": "नर्सरी: वाणिज्यिक मछलियों और केकड़ों के प्रजनन के लिए सुरक्षित क्षेत्र", "type": "leaf"}
                ]},
                {"label": "यूपीएससी परीक्षा दृष्टिकोण (UPSC Focus)", "type": "branch", "date": "परीक्षा", "children": [
                    {"label": "मिष्टी (MISHTI) योजना: बजट 2023 के तहत तटीय रेखा के किनारे मैंग्रोव रोपण कार्यक्रम", "type": "leaf"},
                    {"label": "CRZ नियम 2019: तटीय विकास को नियंत्रित करने के लिए मैंग्रोव को CRZ-I संवेदनशील क्षेत्र घोषित करना", "type": "leaf"}
                ]}
            ]
        else:
            return [
                {"label": "Coastal Ecosystems", "type": "branch", "date": "Coastal", "children": [
                    {"label": "Estuaries: Highly productive brackish water zones forming nutrient traps at river mouths", "type": "leaf"},
                    {"label": "Mangroves: Halophytic vegetation adapted to saline intertidal tropical coastlines", "type": "leaf"}
                ]},
                {"label": "Ecological Adaptations", "type": "branch", "date": "Adaptations", "children": [
                    {"label": "Pneumatophores: Blind respiratory roots with lenticels for oxygen absorption", "type": "leaf"},
                    {"label": "Viviparity: Seed germination on parent tree before dropping into soft tidal mud", "type": "leaf"}
                ]},
                {"label": "Coastal Protection Role", "type": "branch", "date": "Protection", "children": [
                    {"label": "Wave Barrier: Stilt root systems absorbing 66% of wave energy during cyclones", "type": "leaf"},
                    {"label": "Marine Nurseries: Spawning habitats supporting coastal estuarine fisheries", "type": "leaf"}
                ]},
                {"label": "UPSC Exam Focus Dimensions", "type": "branch", "date": "UPSC Core", "children": [
                    {"label": "MISHTI Initiative: Budget 2023 scheme targeting coastal mangrove plantation and carbon sinks", "type": "leaf"},
                    {"label": "CRZ Zoning: Classification of mangrove areas under CRZ-I protecting them from ports/industrial effluents", "type": "leaf"}
                ]}
            ]

    # Coral reefs
    elif any(k in fl for k in ['coral', 'eutrophication', 'algal-bloom', 'human-modified']):
        if is_hindi:
            return [
                {"label": "प्रवाल भित्तियाँ (Corals)", "type": "branch", "date": "प्रवाल", "children": [
                    {"label": "सहजीवन: प्रवाल पॉलिप और ज़ूक्सैंथेले (Zooxanthellae) शैवाल की परस्पर सहोपकारिता", "type": "leaf"},
                    {"label": "प्रकार: तटीय भित्ति (Fringing), अवरोधक भित्ति (Barrier) और प्रवाल द्वीप (Atoll)", "type": "leaf"}
                ]},
                {"label": "खतरे और विरंजन (Bleaching)", "type": "branch", "date": "विरंजन", "children": [
                    {"label": "विरंजन: समुद्र के तापमान बढ़ने से शैवाल का निष्कासन जिससे प्रवाल सफेद हो जाते हैं", "type": "leaf"},
                    {"label": "अम्लीकरण: अतिरिक्त CO2 अवशोषण से समुद्री pH गिरना और कैल्शियम कार्बोनेट कवच कमजोर पड़ना", "type": "leaf"}
                ]},
                {"label": "यूट्रोफिकेशन और अल्गल ब्लूम", "type": "branch", "date": "प्रदूषण", "children": [
                    {"label": "सुपोषणीकरण: रासायनिक उर्वरकों के बहाव से जल निकायों में पोषक तत्वों की तीव्र वृद्धि", "type": "leaf"},
                    {"label": "अल्गल ब्लूम: शैवाल की तीव्र वृद्धि से धूप का रुकना और सड़ने पर ऑक्सीजन की कमी (हाइपोक्सिया) होना", "type": "leaf"}
                ]},
                {"label": "यूपीएससी परीक्षा दृष्टिकोण (UPSC Focus)", "type": "branch", "date": "परीक्षा", "children": [
                    {"label": "कानूनी संरक्षण: प्रवाल वन्यजीव संरक्षण अधिनियम 1972 की अनुसूची I के तहत संरक्षित हैं", "type": "leaf"},
                    {"label": "बायोरॉक बहाली: कंक्रीट ब्लॉकों में हल्की बिजली प्रवाहित कर मन्नार की खाड़ी में प्रवाल पुनर्जनन", "type": "leaf"}
                ]}
            ]
        else:
            return [
                {"label": "Coral Reef Ecosystems", "type": "branch", "date": "Corals", "children": [
                    {"label": "Symbiosis: Mutualism between calcium-secreting polyps and photosynthetic zooxanthellae algae", "type": "leaf"},
                    {"label": "Geomorphology: Classified into Fringing (shoreline), Barrier (separated by lagoon), and Atoll reefs", "type": "leaf"}
                ]},
                {"label": "Threats & Bleaching", "type": "branch", "date": "Threats", "children": [
                    {"label": "Bleaching: Elevated sea surface temperature drives out algae, starving the coral polyps", "type": "leaf"},
                    {"label": "Ocean Acidification: Rising atmospheric carbon decreases seawater pH, dissolving skeletons", "type": "leaf"}
                ]},
                {"label": "Eutrophication Hazards", "type": "branch", "date": "Pollution", "children": [
                    {"label": "Eutrophication: Fertilizer (NPK) runoff causing organic nutrient enrichment in waterbodies", "type": "leaf"},
                    {"label": "Algal Bloom: Rapid bloom covers surface, reducing light; decomposition causes hypoxic dead zones", "type": "leaf"}
                ]},
                {"label": "UPSC Exam Focus Dimensions", "type": "branch", "date": "UPSC Core", "children": [
                    {"label": "Schedule I WPA: Indian law grants corals maximum protection equivalent to tigers", "type": "leaf"},
                    {"label": "Biorock Restorations: Mineral accretion technology deployed in Gulf of Mannar for reef rebuilding", "type": "leaf"}
                ]}
            ]

    # Default
    else:
        if is_hindi:
            return [
                {"label": "पर्यावरण और जैव भूगोल", "type": "branch", "date": "अवधारणा", "children": [
                    {"label": "परिभाषा: स्थलीय और जलीय पारितंत्रों के संतुलन और संरक्षण का अध्ययन", "type": "leaf"}
                ]},
                {"label": "प्रमुख आयाम", "type": "branch", "date": "पाठ्यक्रम", "children": [
                    {"label": "वन, मरुस्थल, आर्द्रभूमियां, मैंग्रोव और महासागरीय उच्चावच आकृतियां", "type": "leaf"}
                ]},
                {"label": "यूपीएससी परीक्षा दृष्टिकोण (UPSC Focus)", "type": "branch", "date": "परीक्षा", "children": [
                    {"label": "मुख्य विषय: रामसर अभिसमय, राष्ट्रीय वन नीतियां और जलवायु परिवर्तन संरक्षण परियोजनाएं", "type": "leaf"}
                ]}
            ]
        else:
            return [
                {"label": "Environment & Biogeography Core", "type": "branch", "date": "Overview", "children": [
                    {"label": "Definition: Study of the dynamics, structure, and conservation of terrestrial/aquatic systems", "type": "leaf"}
                ]},
                {"label": "Core Dimensions", "type": "branch", "date": "Syllabus Areas", "children": [
                    {"label": "Key Systems: Forests, grasslands, tundra, wetlands, estuaries, mangroves, and marine benthos", "type": "leaf"}
                ]},
                {"label": "UPSC Exam Focus Dimensions", "type": "branch", "date": "UPSC Core", "children": [
                    {"label": "GS Paper III: Conservation, environmental degradation, environmental impact assessments (EIA)", "type": "leaf"}
                ]}
            ]

def get_custom_branches(folder_name, is_hindi):
    fl = folder_name.lower()
    
    # 1. Exact match from DATA_MAP
    if fl in DATA_MAP:
        return DATA_MAP[fl]["hi" if is_hindi else "en"]
        
    # 2. Fallback matching grouped logic
    return get_default_branches(fl, is_hindi)

def process_file(html_path, is_hindi):
    print(f"Processing: {html_path} (is_hindi={is_hindi})")
    with open(html_path, 'r', encoding='utf-8') as f:
        html = f.read()
    
    html = html.replace('\r\n', '\n')
    
    # Clean previous mindmap elements to prevent duplicate inserts
    for old in ['    <link rel="stylesheet" href="/assets/css/mindmap.min.css?v=3">\n',
                '    <link rel="stylesheet" href="/assets/css/mindmap.min.css?v=2">\n',
                '    <link rel="stylesheet" href="/assets/css/mindmap.min.css?v=1">\n',
                '    <link rel="stylesheet" href="/assets/css/mindmap.min.css">\n']:
        html = html.replace(old, '')
    
    html = re.sub(r'\s*<!-- Interactive Mindmap -->.*?<!-- Deep-Dive Study Guide \(Dynamically Rendered\) -->', '\n            <!-- Deep-Dive Study Guide (Dynamically Rendered) -->', html, flags=re.DOTALL)
    html = re.sub(r'\s*<!-- Interactive Mindmap -->.*?renderMindmap\(.*?\);\s*</script>', '', html, flags=re.DOTALL)

    folder_path = os.path.dirname(html_path)
    folder_name = os.path.basename(folder_path)
    if folder_name == 'hi':
        folder_name = os.path.basename(os.path.dirname(folder_path))

    clean_title = get_clean_title(folder_name)
    topic_name = clean_title
    cj = os.path.join(os.path.dirname(html_path), "content.json")
    if os.path.exists(cj):
        try:
            topic_name = json.load(open(cj, encoding='utf-8')).get('hero', {}).get('title', topic_name)
        except Exception:
            pass

    branches = get_custom_branches(folder_name, is_hindi)
    
    root_label = clean_title.replace(" Of ", " of ").replace(" And ", " and ").replace(" The ", " the ").replace(" In ", " in ").replace(" With ", " with ").replace(" To ", " to ").replace(" On ", " on ").replace(" By ", " by ")
    
    words = root_label.split()
    formatted_label = ""
    for idx, word in enumerate(words):
        formatted_label += word
        if (idx + 1) % 3 == 0 and (idx + 1) < len(words):
            formatted_label += "\n"
        else:
            formatted_label += " "
    formatted_label = formatted_label.strip()

    mindmap_data = {"label": formatted_label, "type": "root", "children": branches}

    css_link = '    <link rel="stylesheet" href="/assets/css/mindmap.min.css?v=2">\n'
    if css_link not in html:
        html = html.replace('</head>', css_link + '</head>')

    if is_hindi:
        instr = 'किसी <strong style="color:#a78bfa;">बैंगनी</strong> या <strong style="color:#2ecc71;">हरे</strong> <strong>+</strong> पर क्लिक करें।'
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
        tab1_marker = '<div class="tab-panel active" id="notes-panel" role="tabpanel" aria-labelledby="notes-panel">'
        if tab1_marker in html:
            html = html.replace(tab1_marker, tab1_marker + '\n' + mindmap_card, 1)

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
    with open(html_path, 'w', encoding='utf-8') as f:
        f.write(html)
    print(f"  Patched: {html_path}")
    return True

def create_hi_stub(en_html_path, hi_html_path, folder_name, hindi_title):
    with open(en_html_path, 'r', encoding='utf-8') as f:
        html = f.read()
    html = html.replace('\r\n', '\n')
    html = html.replace('<html lang="en">', '<html lang="hi">', 1)
    
    html = html.replace('<a href="hi/">Hindi Version</a>', '<a href="../">English Version</a>', 1)
    html = html.replace('<a href="hi/" class="mobile-lang-toggle"><i class="fas fa-globe"></i> हिन्दी</a>', 
                        '<a href="../" class="mobile-lang-toggle"><i class="fas fa-globe"></i> English</a>', 1)

    html = re.sub(
        r'<link rel="canonical" href="([^"]+)"',
        lambda m: f'<link rel="canonical" href="{m.group(1).rstrip("/")}/hi/"',
        html, count=1
    )
    html = re.sub(r'<title>[^<]+</title>',
                  f'<title>{hindi_title} - UPSC सिविल सेवा अध्ययन गाइड | SJMaths</title>',
                  html, count=1)
    html = re.sub(r'<meta name="description" content="[^"]*"',
                  f'<meta name="description" content="{hindi_title} पर विस्तृत UPSC अध्ययन गाइड। माइंडमैप, नोट्स, मनेमोनिक्स और प्रश्नोत्तर।"',
                  html, count=1)
    os.makedirs(os.path.dirname(hi_html_path), exist_ok=True)
    with open(hi_html_path, 'w', encoding='utf-8') as f:
        f.write(html)

def main():
    total = 0
    # First pass: find all English index.html files and generate Hindi stubs if missing
    for root, dirs, files in os.walk(BASE_DIR):
        parts = os.path.relpath(root, BASE_DIR).split(os.sep)
        is_hindi = 'hi' in parts
        if not is_hindi and 'index.html' in files:
            en_html_path = os.path.join(root, 'index.html')
            hi_dir = os.path.join(root, 'hi')
            hi_html_path = os.path.join(hi_dir, 'index.html')
            if not os.path.exists(hi_html_path):
                folder_name = os.path.basename(root)
                clean_title = get_clean_title(folder_name)
                try:
                    create_hi_stub(en_html_path, hi_html_path, folder_name, clean_title)
                    print(f"Created Hindi stub: {hi_html_path}")
                except Exception as e:
                    print(f"Error creating Hindi stub for {folder_name}: {e}")

    # Second pass: process and patch all index.html files (both English and newly created Hindi ones)
    for root, dirs, files in os.walk(BASE_DIR):
        parts = os.path.relpath(root, BASE_DIR).split(os.sep)
        is_hindi = 'hi' in parts
        for file in files:
            if file == "index.html":
                try:
                    process_file(os.path.join(root, file), is_hindi)
                    total += 1
                except Exception as e:
                    print(f"Error processing {os.path.join(root, file)}: {e}")
    print(f"\nDone! Patched {total} files.")

if __name__ == '__main__':
    main()
