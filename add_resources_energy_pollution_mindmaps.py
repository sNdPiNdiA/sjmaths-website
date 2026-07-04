#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import re
import json

BASE_DIR = r"upsc/environment/Resources-Energy-Pollution"

def get_clean_title(folder_name):
    title = re.sub(r'([a-z])([A-Z])', r'\1 \2', folder_name)
    title = title.replace('-', ' ')
    words = []
    acronyms = {'dpsp', 'pri', 'ut', 'uts', 'sc', 'hc', 'cm', 'com', 'arc', 'inc', 'ias', 'sec', 'sfc', 'pej', 'tej', 'mjo', 'enso', 'iod', 'icar', 'gst', 'dpc', 'mpc', 'adc', 'tac', 'scs', 'pesa', 'icar', 'isfr', 'itcz', 'tej', 'iucn', 'wpa', 'otec', 'bod', 'cod', 'isa'}
    for w in title.split():
        if w.lower() in acronyms:
            words.append(w.upper())
        elif w.lower() in ['of', 'and', 'the', 'for', 'in', 'with', 'against', 'to', 'on', 'some', 'by', 'their', 'vs']:
            words.append(w.lower())
        else:
            words.append(w.capitalize())
    return ' '.join(words)

# Fully comprehensive, grouped fact-dense dataset mapping every folder to a specific resources/energy/pollution mindmap
GROUPS = [
    {
        "keys": ["algal-bloom"],
        "en": [
            {"label": "Algal Bloom Mechanics", "type": "branch", "date": "Biology", "children": [
                {"label": "Definition: Rapid increase or accumulation in the population of algae (typically dinoflagellates or cyanobacteria) in freshwater or marine water systems", "type": "leaf"},
                {"label": "Eutrophication link: Triggered by nutrient enrichment (excessive runoff of nitrates and phosphates from agricultural fertilizers)", "type": "leaf"}
            ]},
            {"label": "Red Tides & Toxins", "type": "branch", "date": "Toxins", "children": [
                {"label": "Red Tides: Marine algal blooms causing discoloration of water; often driven by dinoflagellates", "type": "leaf"},
                {"label": "Harmful Algal Blooms (HABs): Release biotoxins (e.g. saxitoxin, brevetoxin) that bioaccumulate in shellfish, causing paralytic shellfish poisoning in humans", "type": "leaf"}
            ]},
            {"label": "Ecological Damage", "type": "branch", "date": "Impacts", "children": [
                {"label": "Hypoxia: As algae die, bacterial decomposition consumes dissolved oxygen, creating 'dead zones' where aquatic life suffocates", "type": "leaf"},
                {"label": "Light blocking: Dense algal mats block sunlight, killing benthic submerged aquatic vegetation (SAV)", "type": "leaf"}
            ]},
            {"label": "UPSC Exam Focus", "type": "branch", "date": "UPSC Focus", "children": [
                {"label": "BOD & COD: Algal blooms dramatically elevate Biochemical Oxygen Demand (BOD) and Chemical Oxygen Demand (COD) in water bodies", "type": "leaf"},
                {"label": "Mitigation: Riparian buffers, reduced chemical fertilizer application, and mechanical aerators in closed water systems", "type": "leaf"}
            ]}
        ],
        "hi": [
            {"label": "शैवाल प्रस्फुटन (Algal Bloom)", "type": "branch", "date": "जीवविज्ञान", "children": [
                {"label": "परिभाषा: मीठे या खारे पानी में शैवाल (विशेष रूप से सायनोबैक्टीरिया या डाइनोफ्लेजिलेट्स) की आबादी में तीव्र वृद्धि", "type": "leaf"},
                {"label": "यूट्रोफिकेशन लिंक: कृषि उर्वरकों से बहने वाले अत्यधिक नाइट्रोजन और फास्फोरस के कारण ट्रिगर होता है", "type": "leaf"}
            ]},
            {"label": "लाल ज्वार (Red Tides) और विष", "type": "branch", "date": "विषाक्तता", "children": [
                {"label": "लाल ज्वार: समुद्री जल का विवर्णन करने वाले शैवाल प्रस्फुटन; अक्सर डाइनोफ्लेजिलेट्स द्वारा संचालित होते हैं", "type": "leaf"},
                {"label": "हानिकारक प्रस्फुटन (HABs): जैव-विष (जैसे सैक्सीटॉक्सिन) छोड़ते हैं जो शंखमछलियों में जमा होकर मनुष्यों को बीमार करते हैं", "type": "leaf"}
            ]},
            {"label": "पारिस्थितिक क्षति", "type": "branch", "date": "प्रभाव", "children": [
                {"label": "हाइपोक्सिया: मृत शैवाल के सड़ने से बैक्टीरिया जलीय ऑक्सीजन को समाप्त कर देते हैं जिससे 'डेड ज़ोन' बनते हैं", "type": "leaf"},
                {"label": "प्रकाश अवरोध: घनी शैवाल परतें सूर्य के प्रकाश को रोकती हैं, जिससे तलहटी के पौधे मर जाते हैं", "type": "leaf"}
            ]},
            {"label": "यूपीएससी परीक्षा दृष्टिकोण", "type": "branch", "date": "परीक्षा", "children": [
                {"label": "BOD और COD: शैवाल प्रस्फुटन जलीय प्रणालियों में ऑक्सीजन की कमी और प्रदूषक भार को बढ़ाते हैं", "type": "leaf"},
                {"label": "शमन रणनीतियाँ: रिपेरियन बफर जोन का निर्माण और कृषि में रासायनिक उर्वरकों का सीमित उपयोग", "type": "leaf"}
            ]}
        ]
    },
    {
        "keys": ["arsenic-contamination"],
        "en": [
            {"label": "Geogenic Sources", "type": "branch", "date": "Origin", "children": [
                {"label": "Origin: Weathering of arsenic-rich minerals in the Himalayas, deposited by rivers in the Ganga-Brahmaputra delta plain", "type": "leaf"},
                {"label": "Groundwater: Over-extraction of groundwater alters aquifer chemistry, releasing trapped arsenic into well water", "type": "leaf"}
            ]},
            {"label": "Health Hazards", "type": "branch", "date": "Health", "children": [
                {"label": "Blackfoot Disease: Severe vascular disease causing gangrene in lower limbs due to chronic arsenic poisoning", "type": "leaf"},
                {"label": "Arsenicosis: Chronic toxicity leading to skin lesions, hyperkeratosis (dark spots on palms/soles), and cancer of lungs/skin", "type": "leaf"}
            ]},
            {"label": "Geographic Hotspots", "type": "branch", "date": "Geography", "children": [
                {"label": "Delta plain: Heavily impacts West Bengal, Bihar, Jharkhand, Uttar Pradesh, and parts of Bangladesh", "type": "leaf"},
                {"label": "Affects millions who rely on shallow tubewells for drinking water and crop irrigation", "type": "leaf"}
            ]},
            {"label": "UPSC Exam Focus", "type": "branch", "date": "UPSC Focus", "children": [
                {"label": "Bioaccumulation: Arsenic enters the food chain through paddy fields irrigated with contaminated groundwater", "type": "leaf"},
                {"label": "WHO limit: The maximum permissible limit for arsenic in drinking water is 0.01 mg/L (10 ppb)", "type": "leaf"}
            ]}
        ],
        "hi": [
            {"label": "भू-वैज्ञानिक स्रोत", "type": "branch", "date": "उत्पत्ति", "children": [
                {"label": "उत्पत्ति: हिमालय में आर्सेनिक युक्त खनिजों का अपक्षय, जो गंगा-ब्रह्मपुत्र डेल्टा में जमा हुआ है", "type": "leaf"},
                {"label": "भूजल: भूजल के अत्यधिक दोहन से जलभृतों का रसायन बदल जाता है, जिससे फंसा हुआ आर्सेनिक पानी में मिल जाता है", "type": "leaf"}
            ]},
            {"label": "स्वास्थ्य के खतरे", "type": "branch", "date": "स्वास्थ्य", "children": [
                {"label": "ब्लैकफुट रोग (Blackfoot Disease): गंभीर संवहनी रोग जो क्रोनिक आर्सेनिक विषाक्तता के कारण अंगों में गैंग्रीन का कारण बनता है", "type": "leaf"},
                {"label": "आर्सेनिकोसिस: त्वचा के घाव, हथेलियों/तलवों पर काले धब्बे (हाइपरकेराटोसिस) और फेफड़ों/त्वचा का कैंसर होना", "type": "leaf"}
            ]},
            {"label": "भौगोलिक क्षेत्र", "type": "branch", "date": "भूगोल", "children": [
                {"label": "डेल्टा मैदान: पश्चिम बंगाल, बिहार, झारखंड, उत्तर प्रदेश और बांग्लादेश के कुछ हिस्सों को भारी रूप से प्रभावित करता है", "type": "leaf"},
                {"label": "पीने के पानी और कृषि सिंचाई के लिए उथले नलकूपों पर निर्भर लाखों लोगों को प्रभावित करता है", "type": "leaf"}
            ]},
            {"label": "यूपीएससी परीक्षा दृष्टिकोण", "type": "branch", "date": "परीक्षा", "children": [
                {"label": "जैव-संचय: दूषित भूजल से सींचे गए धान के खेतों के माध्यम से आर्सेनिक खाद्य श्रृंखला में प्रवेश करता है", "type": "leaf"},
                {"label": "WHO सीमा: पीने के पानी में आर्सेनिक की अधिकतम स्वीकार्य सीमा 0.01 mg/L (10 ppb) निर्धारित है", "type": "leaf"}
            ]}
        ]
    },
    {
        "keys": ["deforestation", "strategies-for-reducing-deforestation"],
        "en": [
            {"label": "Drivers of Forest Loss", "type": "branch", "date": "Causes", "children": [
                {"label": "Agriculture: Encroachment for crop cultivation and cattle ranching (shifting cultivation / Jhum in NE India)", "type": "leaf"},
                {"label": "Development: Submergence under major dam reservoirs, road building, and open-cast coal mining projects", "type": "leaf"}
            ]},
            {"label": "Ecological Consequences", "type": "branch", "date": "Impacts", "children": [
                {"label": "Carbon shift: Loss of forest biomass turns major carbon sinks into sources of greenhouse gases", "type": "leaf"},
                {"label": "Hydrology & Soil: Accelerates topsoil erosion, decreases groundwater infiltration, and triggers flash floods", "type": "leaf"}
            ]},
            {"label": "Global & National Policies", "type": "branch", "date": "Policies", "children": [
                {"label": "REDD+: Reducing Emissions from Deforestation and Forest Degradation; creates financial incentives for forest carbon sinks", "type": "leaf"},
                {"label": "Bonn Challenge: Global effort to restore 350 million hectares of degraded land by 2030; India committed to 26 million hectares", "type": "leaf"}
            ]},
            {"label": "UPSC Exam Focus", "type": "branch", "date": "UPSC Focus", "children": [
                {"label": "ISFR 2021 Data: Forest and tree cover constitutes ~24.62% of geographical area; target is 33% under Forest Policy 1988", "type": "leaf"},
                {"label": "CAMPA Act 2016: Compensatory Afforestation Fund Management and Planning Authority utilizing developer fees for reforestation", "type": "leaf"}
            ]}
        ],
        "hi": [
            {"label": "वन विनाश के कारण", "type": "branch", "date": "कारण", "children": [
                {"label": "कृषि: खेती और पशुपालन के लिए वनों का अतिक्रमण (पूर्वोत्तर भारत में झूम/स्थानांतरित खेती)", "type": "leaf"},
                {"label": "विकास परियोजनाएं: बड़े बांध जलाशयों के तहत भूमि जलमग्न होना, सड़कों का निर्माण और कोयला खनन", "type": "leaf"}
            ]},
            {"label": "पारिस्थितिक परिणाम", "type": "branch", "date": "प्रभाव", "children": [
                {"label": "कार्बन बदलाव: वन जैवभार का नुकसान प्रमुख कार्बन सिंक को ग्रीनहाउस गैसों के स्रोतों में बदल देता है", "type": "leaf"},
                {"label": "जल विज्ञान और मृदा: ऊपरी मिट्टी के क्षरण को तेज करता है और भूजल रिचार्ज में कमी लाता है", "type": "leaf"}
            ]},
            {"label": "वैश्विक और राष्ट्रीय नीतियां", "type": "branch", "date": "नीतियां", "children": [
                {"label": "REDD+: वनों की कटाई से उत्सर्जन को कम करना; वन कार्बन सिंक बनाए रखने के लिए वित्तीय प्रोत्साहन देता है", "type": "leaf"},
                {"label": "बॉन चुनौती: 2030 तक 350 मिलियन हेक्टेयर बंजर भूमि को बहाल करना; भारत का संकल्प 26 मिलियन हेक्टेयर है", "type": "leaf"}
            ]},
            {"label": "यूपीएससी परीक्षा दृष्टिकोण", "type": "branch", "date": "परीक्षा", "children": [
                {"label": "ISFR डेटा: देश का वन और वृक्ष आवरण ~24.62% है; राष्ट्रीय वन नीति 1988 का लक्ष्य 33% का है", "type": "leaf"},
                {"label": "कैम्पा (CAMPA) अधिनियम 2016: प्रतिपूरक वनीकरण कोष प्राधिकरण, विकास शुल्क का उपयोग कर पुनर्वनीकरण करना", "type": "leaf"}
            ]}
        ]
    },
    {
        "keys": ["desertification", "sustainable-land", "land-degradation"],
        "en": [
            {"label": "Desertification Drivers", "type": "branch", "date": "Drivers", "children": [
                {"label": "Definition: Land degradation in arid, semi-arid, and dry sub-humid areas resulting from climatic variations and human activities", "type": "leaf"},
                {"label": "Causes: Overgrazing removes vegetation cover; excessive irrigation causes waterlogging and soil salinization", "type": "leaf"}
            ]},
            {"label": "Global Countermeasures", "type": "branch", "date": "UNCCD", "children": [
                {"label": "UNCCD (1994): United Nations Convention to Combat Desertification; only legally binding international treaty on land degradation", "type": "leaf"},
                {"label": "Land Degradation Neutrality (LDN): Goal to maintain or enhance stable land resources globally by 2030", "type": "leaf"}
            ]},
            {"label": "Restoration Strategies", "type": "branch", "date": "Restoration", "children": [
                {"label": "Sustainable Land Management (SLM): Contour ploughing, shelterbelts, sand dune stabilization, and agroforestry", "type": "leaf"},
                {"label": "Great Green Wall (Africa): Initiative to restore 100 million hectares of degraded land across the Sahel region", "type": "leaf"}
            ]},
            {"label": "UPSC Exam Focus", "type": "branch", "date": "UPSC Focus", "children": [
                {"label": "Desertification Atlas of India (SAC): Over 29% of India's geographical area is undergoing desertification/degradation", "type": "leaf"},
                {"label": "UNCCD COP-14 (New Delhi, 2019): India committed to restoring 26 million hectares of degraded land by 2030", "type": "leaf"}
            ]}
        ],
        "hi": [
            {"label": "मरुस्थलीकरण के कारक", "type": "branch", "date": "कारण", "children": [
                {"label": "परिभाषा: जलवायु परिवर्तनों और मानवीय गतिविधियों के कारण शुष्क, अर्ध-शुष्क और शुष्क उप-आर्द्र क्षेत्रों में भूमि का क्षरण", "type": "leaf"},
                {"label": "प्रमुख कारण: अत्यधिक पशु चराई से वनस्पति आवरण का हटना; अधिक सिंचाई से लवणीकरण होना", "type": "leaf"}
            ]},
            {"label": "वैश्विक उपाय (UNCCD)", "type": "branch", "date": "UNCCD", "children": [
                {"label": "UNCCD (1994): मरुस्थलीकरण से निपटने के लिए संयुक्त राष्ट्र कन्वेंशन; भूमि क्षरण पर एकमात्र बाध्यकारी अंतरराष्ट्रीय संधि", "type": "leaf"},
                {"label": "भूमि क्षरण तटस्थता (LDN): 2030 तक वैश्विक स्तर पर स्थिर भूमि संसाधनों को बनाए रखने या बढ़ाने का लक्ष्य", "type": "leaf"}
            ]},
            {"label": "बहाली की रणनीतियाँ", "type": "branch", "date": "रणनीति", "children": [
                {"label": "टिकाऊ भूमि प्रबंधन (SLM): समोच्च जुताई, शेल्टरबेल्ट का निर्माण, रेत के टीलों का स्थिरीकरण और कृषि वानिकी", "type": "leaf"},
                {"label": "ग्रेट ग्रीन वॉल: साहेल क्षेत्र में 100 मिलियन हेक्टेयर बंजर भूमि को बहाल करने की अफ्रीकी पहल", "type": "leaf"}
            ]},
            {"label": "यूपीएससी परीक्षा दृष्टिकोण", "type": "branch", "date": "परीक्षा", "children": [
                {"label": "भारत का मरुस्थलीकरण एटलस (SAC): भारत के भौगोलिक क्षेत्र का 29% से अधिक भाग मरुस्थलीकरण/क्षरण के अधीन है", "type": "leaf"},
                {"label": "UNCCD COP-14 (नई दिल्ली, 2019): भारत ने 2030 तक 26 मिलियन हेक्टेयर क्षरित भूमि को बहाल करने का संकल्प लिया", "type": "leaf"}
            ]}
        ]
    },
    {
        "keys": ["eutrophication"],
        "en": [
            {"label": "Process & Nutrient Enrichment", "type": "branch", "date": "Mechanism", "children": [
                {"label": "Nutrient Loading: Runoff carries nitrates and phosphates from agricultural fields and sewage into water bodies", "type": "leaf"},
                {"label": "Algal Bloom: Excess nutrients trigger rapid proliferation of algae, forming thick mats on the water surface", "type": "leaf"}
            ]},
            {"label": "Ecological Consequences", "type": "branch", "date": "Impacts", "children": [
                {"label": "Anoxia: Dead algae sink to bottom; bacteria consume dissolved oxygen during decomposition, creating hypoxic conditions", "type": "leaf"},
                {"label": "Loss of Biodiversity: Suffocation kills fish and shellfish; lack of sunlight kills submerged aquatic plants", "type": "leaf"}
            ]},
            {"label": "Natural vs Cultural Eutrophication", "type": "branch", "date": "Types", "children": [
                {"label": "Natural: Slow, geological aging process of lakes, spanning thousands of years as sediment accumulates", "type": "leaf"},
                {"label": "Cultural (Anthropogenic): Accelerated aging caused by human agricultural and industrial runoff, occurring in decades", "type": "leaf"}
            ]},
            {"label": "UPSC Exam Focus", "type": "branch", "date": "UPSC Focus", "children": [
                {"label": "BOD rise: Eutrophic lakes show very high Biochemical Oxygen Demand (BOD) and low Dissolved Oxygen (DO)", "type": "leaf"},
                {"label": "Oligotrophic Lakes: Deep, nutrient-poor, clear lakes with low productivity, forming the opposite of eutrophic lakes", "type": "leaf"}
            ]}
        ],
        "hi": [
            {"label": "यूट्रोफिकेशन की प्रक्रिया", "type": "branch", "date": "क्रियाविधि", "children": [
                {"label": "पोषक तत्व संवर्धन: कृषि क्षेत्रों से नाइट्रोजन और फास्फोरस का बहकर जलाशयों में मिलना", "type": "leaf"},
                {"label": "शैवाल प्रस्फुटन: अत्यधिक पोषक तत्व शैवाल के तेजी से प्रसार को ट्रिगर करते हैं, जिससे पानी पर मोटी परत बनती है", "type": "leaf"}
            ]},
            {"label": "पारिस्थितिक परिणाम", "type": "branch", "date": "प्रभाव", "children": [
                {"label": "एनोक्सिया (Anoxia): मृत शैवाल नीचे बैठते हैं; अपघटन के दौरान बैक्टीरिया घुलित ऑक्सीजन को सोख लेते हैं", "type": "leaf"},
                {"label": "जैव विविधता का नुकसान: ऑक्सीजन की कमी से मछलियां मर जाती हैं; प्रकाश के अभाव में जलीय पौधे नष्ट होते हैं", "type": "leaf"}
            ]},
            {"label": "प्राकृतिक बनाम कृत्रिम यूट्रोफिकेशन", "type": "branch", "date": "प्रकार", "children": [
                {"label": "प्राकृतिक: झीलों की धीमी, प्राकृतिक भूवैज्ञानिक उम्र बढ़ने की प्रक्रिया, जो हजारों वर्षों में पूरी होती है", "type": "leaf"},
                {"label": "कृत्रिम (मानवजनित): मानव कृषि और औद्योगिक अपवाह के कारण होने वाली तीव्र वृद्धि, जो दशकों में पूरी होती है", "type": "leaf"}
            ]},
            {"label": "यूपीएससी परीक्षा दृष्टिकोण", "type": "branch", "date": "परीक्षा", "children": [
                {"label": "BOD में वृद्धि: यूट्रोफिक झीलों में जैव रासायनिक ऑक्सीजन की मांग (BOD) बहुत अधिक और घुलित ऑक्सीजन (DO) कम होती है", "type": "leaf"},
                {"label": "ओलिगोट्रॉफिक झीलें: गहरे, पोषक तत्व-विहीन, स्वच्छ पानी की कम उत्पादकता वाली झीलें (यूट्रोफिक के विपरीत)", "type": "leaf"}
            ]}
        ]
    },
    {
        "keys": ["forest-resource", "government-programmes-for-conservation-of-forests", "types-of-forests"],
        "en": [
            {"label": "Classification of Forests", "type": "branch", "date": "Types", "children": [
                {"label": "Tropical Evergreen: High rainfall (>200cm) regions; Western Ghats and NE India; dense multi-layered canopy", "type": "leaf"},
                {"label": "Tropical Deciduous (Monsoon): Most widespread in India; Teak, Sal, and Shisham shedding leaves in dry season", "type": "leaf"},
                {"label": "Montane Temperate: Himalayan wet temperate zones; dominated by Oaks, Chestnuts, and Conifers", "type": "leaf"}
            ]},
            {"label": "Legal Classification", "type": "branch", "date": "Legal Status", "children": [
                {"label": "Reserved Forests: Most restricted; declared by state governments under Indian Forest Act 1927", "type": "leaf"},
                {"label": "Protected Forests: State has rights but local communities allowed resource extraction unless banned", "type": "leaf"}
            ]},
            {"label": "Conservation Initiatives", "type": "branch", "date": "Programs", "children": [
                {"label": "National Afforestation Programme (NAP): Eco-development committees implementing participatory forest management", "type": "leaf"},
                {"label": "Green India Mission (GIM): One of the 8 missions under NAPCC; aims to improve forest cover and quality", "type": "leaf"}
            ]},
            {"label": "UPSC Exam Focus", "type": "branch", "date": "UPSC Focus", "children": [
                {"label": "ISFR Biennial Report (FSI): Forest cover stands at ~21.71% of geographical area (Total cover with trees is ~24.62%)", "type": "leaf"},
                {"label": "Forest Rights Act (FRA) 2006: Grants titles to forest dwelling Scheduled Tribes (FDST) and traditional dwellers", "type": "leaf"}
            ]}
        ],
        "hi": [
            {"label": "वनों का वर्गीकरण", "type": "branch", "date": "प्रकार", "children": [
                {"label": "उष्णकटिबंधीय सदाबहार: उच्च वर्षा (>200 सेमी); पश्चिमी घाट और पूर्वोत्तर; सघन बहुस्तरीय छतरी", "type": "leaf"},
                {"label": "उष्णकटिबंधीय पर्णपाती (मानसूनी): भारत में सर्वाधिक विस्तृत; शुष्क मौसम में पत्तियाँ गिराने वाले सागौन और साल", "type": "leaf"},
                {"label": "पर्वतीय समशीतोष्ण: हिमालयी क्षेत्र; बांज (Oaks), चेस्टनट और शंकुधारी वनों का प्रभुत्व", "type": "leaf"}
            ]},
            {"label": "कानूनी वर्गीकरण", "type": "branch", "date": "कानूनी स्थिति", "children": [
                {"label": "आरक्षित वन (Reserved Forests): सर्वाधिक प्रतिबंधित; भारतीय वन अधिनियम 1927 के तहत राज्य सरकार द्वारा घोषित", "type": "leaf"},
                {"label": "संरक्षित वन (Protected Forests): राज्य का अधिकार होता है लेकिन प्रतिबंधों के बिना स्थानीय उपयोग की अनुमति होती है", "type": "leaf"}
            ]},
            {"label": "संरक्षण कार्यक्रम", "type": "branch", "date": "कार्यक्रम", "children": [
                {"label": "राष्ट्रीय वनीकरण कार्यक्रम (NAP): स्थानीय भागीदारी और पारिस्थितिक विकास समितियों के माध्यम से वनीकरण", "type": "leaf"},
                {"label": "हरित भारत मिशन (GIM): NAPCC के तहत 8 राष्ट्रीय मिशनों में से एक; वन गुणवत्ता और मात्रा बढ़ाने का लक्ष्य", "type": "leaf"}
            ]},
            {"label": "यूपीएससी परीक्षा दृष्टिकोण", "type": "branch", "date": "परीक्षा", "children": [
                {"label": "ISFR रिपोर्ट (FSI): वास्तविक वन आवरण भौगोलिक क्षेत्र का ~21.71% है (कुल वन और वृक्ष आवरण ~24.62% है)", "type": "leaf"},
                {"label": "वन अधिकार अधिनियम (FRA) 2006: वनवासी अनुसूचित जनजातियों (FDST) और पारंपरिक निवासियों को वन अधिकारों की मान्यता", "type": "leaf"}
            ]}
        ]
    },
    {
        "keys": ["geothermal-energy"],
        "en": [
            {"label": "Geothermal Principles", "type": "branch", "date": "Mechanism", "children": [
                {"label": "Definition: Thermal energy generated and stored in the Earth's core, crust, and mantle", "type": "leaf"},
                {"label": "Harnessing: Utilizing underground steam/hot water to spin turbines, producing electricity", "type": "leaf"}
            ]},
            {"label": "Geothermal Sites in India", "type": "branch", "date": "India Sites", "children": [
                {"label": "Puga Valley (Ladakh): Most promising geothermal field in India; first pilot project established by ONGC", "type": "leaf"},
                {"label": "Tatapani (Chhattisgarh): Hydrothermal system with potential for binary cycle power plants", "type": "leaf"},
                {"label": "Manikaran (Himachal Pradesh): Famous hot springs; experimental power plants operated by GSI", "type": "leaf"}
            ]},
            {"label": "Pros & Cons", "type": "branch", "date": "Analysis", "children": [
                {"label": "Advantages: Base-load power source (runs 24/7 unlike solar/wind); very low greenhouse gas emissions", "type": "leaf"},
                {"label": "Disadvantages: High exploration and drilling costs; risk of releasing toxic gases (e.g. hydrogen sulfide)", "type": "leaf"}
            ]},
            {"label": "UPSC Exam Focus", "type": "branch", "date": "UPSC Focus", "children": [
                {"label": "Tectonic link: Geothermal resources in India are located along major rift valleys and fault zones (e.g. SONATA zone)", "type": "leaf"},
                {"label": "Direct uses: Balneotherapy (therapeutic hot springs), greenhouse heating, and space cooling in high altitudes", "type": "leaf"}
            ]}
        ],
        "hi": [
            {"label": "भू-तापीय ऊर्जा के सिद्धांत", "type": "branch", "date": "क्रियाविधि", "children": [
                {"label": "परिभाषा: पृथ्वी के कोर, क्रस्ट और मेंटल में उत्पन्न और संचित होने वाली तापीय ऊर्जा", "type": "leaf"},
                {"label": "दोहन: बिजली उत्पन्न करने के लिए टरबाइन चलाने हेतु भूमिगत भाप/गर्म पानी का उपयोग करना", "type": "leaf"}
            ]},
            {"label": "भारत में भू-तापीय स्थल", "type": "branch", "date": "भारत के स्थल", "children": [
                {"label": "पुगा घाटी (लद्दाख): भारत का सबसे आशाजनक भू-तापीय क्षेत्र; ONGC द्वारा पहला पायलट प्रोजेक्ट स्थापित", "type": "leaf"},
                {"label": "तातापानी (छत्तीसगढ़): बाइनरी चक्र बिजली संयंत्रों की क्षमता वाला हाइड्रोथर्मल सिस्टम", "type": "leaf"},
                {"label": "मणिकरण (हिमाचल प्रदेश): प्रसिद्ध गर्म चश्मे; GSI द्वारा संचालित प्रायोगिक बिजली संयंत्र", "type": "leaf"}
            ]},
            {"label": "गुण और दोष", "type": "branch", "date": "मूल्यांकन", "children": [
                {"label": "लाभ: बेस-लोड बिजली स्रोत (सौर/पवन के विपरीत 24/7 चलता है); बहुत कम ग्रीनहाउस गैस उत्सर्जन", "type": "leaf"},
                {"label": "हानि: उच्च अन्वेषण और ड्रिलिंग लागत; विषैली गैसों (जैसे हाइड्रोजन सल्फाइड) के रिसाव का जोखिम", "type": "leaf"}
            ]},
            {"label": "यूपीएससी परीक्षा दृष्टिकोण", "type": "branch", "date": "परीक्षा", "children": [
                {"label": "विवर्तनिक संबंध: भारत में भू-तापीय संसाधन प्रमुख दरार घाटियों और भ्रंश क्षेत्रों (जैसे SONATA क्षेत्र) में स्थित हैं", "type": "leaf"},
                {"label": "प्रत्यक्ष उपयोग: बाल्नेओथेरेपी (गर्म पानी के चश्मे से उपचार), ग्रीनहाउस हीटिंग और कोल्ड स्टोरेज", "type": "leaf"}
            ]}
        ]
    },
    {
        "keys": ["groundwater"],
        "en": [
            {"label": "Groundwater Scenario in India", "type": "branch", "date": "Overview", "children": [
                {"label": "Largest user: India is the world's largest consumer of groundwater, extracting more than China and US combined", "type": "leaf"},
                {"label": "Irrigation: Accounts for over 80% of total groundwater extraction, primarily for water-intensive crops like paddy and sugarcane", "type": "leaf"}
            ]},
            {"label": "Major Threat Categories", "type": "branch", "date": "Threats", "children": [
                {"label": "Depletion: Severe decline in water tables in northwest India (Punjab, Haryana) due to free electricity policies", "type": "leaf"},
                {"label": "Contamination: Geogenic fluoride and arsenic contamination; anthropogenic nitrate runoff from fertilizers", "type": "leaf"}
            ]},
            {"label": "Management Initiatives", "type": "branch", "date": "Management", "children": [
                {"label": "Atal Bhujal Yojana: Community-led groundwater management scheme implemented in water-stressed blocks", "type": "leaf"},
                {"label": "Central Ground Water Authority (CGWA): Regulates groundwater extraction and issues NOCs for industrial usage", "type": "leaf"}
            ]},
            {"label": "UPSC Exam Focus", "type": "branch", "date": "UPSC Focus", "children": [
                {"label": "Aquifer mapping: National Aquifer Mapping and Management Programme (NAQUIM) mapping underground water reserves", "type": "leaf"},
                {"label": "Saline intrusion: Excessive extraction in coastal aquifers (e.g. Gujarat, Tamil Nadu) causes seawater intrusion", "type": "leaf"}
            ]}
        ],
        "hi": [
            {"label": "भारत में भूजल परिदृश्य", "type": "branch", "date": "अवलोकन", "children": [
                {"label": "सबसे बड़ा उपभोक्ता: भारत दुनिया में भूजल का सबसे बड़ा उपभोक्ता है, जो चीन और अमेरिका से अधिक दोहन करता है", "type": "leaf"},
                {"label": "सिंचाई: कुल भूजल दोहन का 80% से अधिक हिस्सा कृषि, विशेष रूप से धान और गन्ने जैसी फसलों में उपयोग होता है", "type": "leaf"}
            ]},
            {"label": "प्रमुख खतरे", "type": "branch", "date": "खतरे", "children": [
                {"label": "जल स्तर में गिरावट: मुफ्त बिजली नीतियों के कारण उत्तर-पश्चिम भारत (पंजाब, हरियाणा) में भूजल स्तर में भारी गिरावट", "type": "leaf"},
                {"label": "प्रदूषण: फ्लोराइड और आर्सेनिक का प्राकृतिक प्रदूषण; उर्वरकों के कारण नाइट्रेट प्रदूषण", "type": "leaf"}
            ]},
            {"label": "प्रबंधन के प्रयास", "type": "branch", "date": "प्रबंधन", "children": [
                {"label": "अटल भूजल योजना: पानी की कमी वाले ब्लॉकों में शुरू की गई समुदाय-आधारित भूजल प्रबंधन योजना", "type": "leaf"},
                {"label": "केंद्रीय भूजल प्राधिकरण (CGWA): भूजल दोहन को नियंत्रित करता है और औद्योगिक उपयोग के लिए NOC जारी करता है", "type": "leaf"}
            ]},
            {"label": "यूपीएससी परीक्षा दृष्टिकोण", "type": "branch", "date": "परीक्षा", "children": [
                {"label": "जलभृत मानचित्रण: राष्ट्रीय जलभृत मानचित्रण कार्यक्रम (NAQUIM) भूमिगत जल भंडारों का मानचित्रण कर रहा है", "type": "leaf"},
                {"label": "लवणीय पैठ: तटीय क्षेत्रों (जैसे गुजरात, तमिलनाडु) में अत्यधिक दोहन से भूजल में समुद्री पानी मिल जाता है", "type": "leaf"}
            ]}
        ]
    },
    {
        "keys": ["ocean-thermal", "otec"],
        "en": [
            {"label": "OTEC Operating Principle", "type": "branch", "date": "Mechanism", "children": [
                {"label": "Definition: Ocean Thermal Energy Conversion utilizes temperature difference between warm surface water and cold deep ocean water", "type": "leaf"},
                {"label": "Gradient requirement: Requires a minimum temperature difference of 20°C between surface (~25°C) and deep water (~5°C at 1000m)", "type": "leaf"}
            ]},
            {"label": "OTEC Systems", "type": "branch", "date": "Systems", "children": [
                {"label": "Closed-Cycle: Uses low-boiling-point working fluid (like ammonia) evaporated by warm surface water to turn turbines", "type": "leaf"},
                {"label": "Open-Cycle: Warm surface water is flash-evaporated under vacuum to drive turbines; steam is condensed by cold water to yield fresh water", "type": "leaf"}
            ]},
            {"label": "Indian Potential", "type": "branch", "date": "India Potential", "children": [
                {"label": "Exclusive Economic Zone (EEZ): Vast tropical EEZ provides high OTEC potential (~180,000 MW in India)", "type": "leaf"},
                {"label": "Kavaratti Plant: NIOT established a low-temperature thermal desalination (LTTD) plant in Lakshadweep using deep cold ocean water", "type": "leaf"}
            ]},
            {"label": "UPSC Exam Focus", "type": "branch", "date": "UPSC Focus", "children": [
                {"label": "Byproducts: OTEC plants can provide base-load clean energy, fresh drinking water, and nutrient-rich water for aquaculture", "type": "leaf"},
                {"label": "Challenges: High capital cost of deep-water pipes and corrosive marine environment (biofouling of heat exchangers)", "type": "leaf"}
            ]}
        ],
        "hi": [
            {"label": "OTEC कार्य सिद्धांत", "type": "branch", "date": "क्रियाविधि", "children": [
                {"label": "परिभाषा: महासागरीय तापीय ऊर्जा रूपांतरण (OTEC) सतह के गर्म पानी और गहरे ठंडे पानी के तापमान अंतर का उपयोग करता है", "type": "leaf"},
                {"label": "तापमान प्रवणता: सतह (~25°C) और 1000 मीटर की गहराई पर ठंडे पानी (~5°C) के बीच कम से कम 20°C का अंतर आवश्यक", "type": "leaf"}
            ]},
            {"label": "OTEC प्रणालियां", "type": "branch", "date": "प्रणालियां", "children": [
                {"label": "बंद चक्र (Closed-Cycle): कम क्वथनांक वाले तरल (जैसे अमोनिया) को सतह के गर्म पानी से वाष्पीकृत कर टरबाइन चलाना", "type": "leaf"},
                {"label": "खुला चक्र (Open-Cycle): गर्म सतह के पानी को निर्वात में वाष्पीकृत करना; संघनन से मीठा पानी प्राप्त होता है", "type": "leaf"}
            ]},
            {"label": "भारतीय क्षमता", "type": "branch", "date": "भारत में क्षमता", "children": [
                {"label": "अनन्य आर्थिक क्षेत्र (EEZ): विशाल उष्णकटिबंधीय EEZ उच्च OTEC क्षमता (~180,000 MW) प्रदान करता है", "type": "leaf"},
                {"label": "कवरत्ती संयंत्र: NIOT ने गहरे समुद्र के ठंडे पानी का उपयोग करके लक्षद्वीप में अलवणीकरण (LTTD) संयंत्र स्थापित किया है", "type": "leaf"}
            ]},
            {"label": "यूपीएससी परीक्षा दृष्टिकोण", "type": "branch", "date": "परीक्षा", "children": [
                {"label": "सह-उत्पाद: OTEC संयंत्र स्वच्छ ऊर्जा के साथ-साथ पीने योग्य मीठा पानी और जलीय कृषि के लिए पोषक तत्व युक्त पानी दे सकते हैं", "type": "leaf"},
                {"label": "चुनौतियां: गहरे पानी के पाइपों की उच्च लागत और संक्षारक समुद्री वातावरण (बायोफाउलिंग)", "type": "leaf"}
            ]}
        ]
    },
    {
        "keys": ["organic-farming"],
        "en": [
            {"label": "Core Principles", "type": "branch", "date": "Concept", "children": [
                {"label": "Definition: Agricultural system relying on ecological processes, biodiversity, and cycles adapted to local conditions", "type": "leaf"},
                {"label": "Excludes: Banned synthetic fertilizers, chemical pesticides, plant growth regulators, and genetically modified organisms (GMOs)", "type": "leaf"}
            ]},
            {"label": "Key Methods", "type": "branch", "date": "Methods", "children": [
                {"label": "Soil health: Crop rotation, green manure, organic composting, and biological pest control (using neem oil, trichoderma)", "type": "leaf"},
                {"label": "Biofertilizers: Nitrogen-fixing organisms (Rhizobium, Azotobacter, Blue-Green Algae) and phosphate solubilizing bacteria", "type": "leaf"}
            ]},
            {"label": "Government Schemes", "type": "branch", "date": "Schemes", "children": [
                {"label": "PKVY: Paramparagat Krishi Vikas Yojana; promotes cluster-based organic farming with Participatory Guarantee System (PGS) certification", "type": "leaf"},
                {"label": "MOVCDNER: Mission Organic Value Chain Development for Northeastern Region; supports organic exports from NE India", "type": "leaf"}
            ]},
            {"label": "UPSC Exam Focus", "type": "branch", "date": "UPSC Focus", "children": [
                {"label": "Sikkim Milestone: Declared as the world's first 100% organic state in 2016; banned chemical inputs completely", "type": "leaf"},
                {"label": "PGS-India vs NPOP: PGS is peer-reviewed certification for local markets; NPOP is third-party audit for export markets", "type": "leaf"}
            ]}
        ],
        "hi": [
            {"label": "मूल सिद्धांत", "type": "branch", "date": "अवधारणा", "children": [
                {"label": "परिभाषा: पारिस्थितिक प्रक्रियाओं, जैव विविधता और स्थानीय चक्रों पर आधारित कृषि प्रणाली", "type": "leaf"},
                {"label": "वर्जित: सिंथेटिक रासायनिक उर्वरक, रासायनिक कीटनाशक, विकास नियामक और जीएमओ का निषेध", "type": "leaf"}
            ]},
            {"label": "प्रमुख विधियां", "type": "branch", "date": "विधियां", "children": [
                {"label": "मृदा स्वास्थ्य: फसल चक्र, हरी खाद, जैविक कंपोस्टिंग और जैविक कीट नियंत्रण (नीम तेल का उपयोग)", "type": "leaf"},
                {"label": "जैव उर्वरक: नाइट्रोजन स्थिरीकरण जीव (राइजोबियम, नील-हरित शैवाल) और फास्फेट घुलनशील बैक्टीरिया", "type": "leaf"}
            ]},
            {"label": "सरकारी योजनाएं", "type": "branch", "date": "योजनाएं", "children": [
                {"label": "PKVY: परंपरागत कृषि विकास योजना; क्लस्टर-आधारित जैविक खेती और PGS प्रमाणन को बढ़ावा देना", "type": "leaf"},
                {"label": "MOVCDNER: पूर्वोत्तर क्षेत्र के लिए मिशन जैविक मूल्य श्रृंखला विकास; जैविक उत्पादों के निर्यात को बढ़ावा देना", "type": "leaf"}
            ]},
            {"label": "यूपीएससी परीक्षा दृष्टिकोण", "type": "branch", "date": "परीक्षा", "children": [
                {"label": "सिक्किम मील का पत्थर: 2016 में दुनिया का पहला 100% जैविक राज्य घोषित; रासायनिक आदानों पर पूरी तरह प्रतिबंध", "type": "leaf"},
                {"label": "PGS-India बनाम NPOP: PGS स्थानीय बाजारों के लिए सहकर्मी प्रमाणन है; NPOP निर्यात के लिए तीसरे पक्ष का ऑडिट है", "type": "leaf"}
            ]}
        ]
    },
    {
        "keys": ["oxygen-stratification"],
        "en": [
            {"label": "Thermal & Oxygen Layers", "type": "branch", "date": "Structure", "children": [
                {"label": "Epilimnion: Warm, oxygen-rich surface layer; high photosynthesis and wind mixing maintain oxygen saturation", "type": "leaf"},
                {"label": "Thermocline: Middle transition layer where water temperature drops rapidly with depth", "type": "leaf"},
                {"label": "Hypolimnion: Cold, dark bottom layer; cut off from atmosphere, organic decomposition consumes oxygen rapidly", "type": "leaf"}
            ]},
            {"label": "Seasonal Turnover Dynamics", "type": "branch", "date": "Turnover", "children": [
                {"label": "Spring/Autumn overturn: Surface water cools and sinks, mixing water column to redistribute oxygen to bottom", "type": "leaf"},
                {"label": "Summer stratification: Warm surface restricts mixing, leading to oxygen depletion in hypolimnion", "type": "leaf"}
            ]},
            {"label": "Ecological Consequences", "type": "branch", "date": "Impacts", "children": [
                {"label": "Benthic hypoxia: Oxygen-deprived bottom waters force fish to migrate upward or face mortality", "type": "leaf"},
                {"label": "Chemical shifts: Anaerobic conditions release bound phosphorus and iron from sediments, worsening eutrophication", "type": "leaf"}
            ]},
            {"label": "UPSC Exam Focus", "type": "branch", "date": "UPSC Focus", "children": [
                {"label": "Dimictic Lakes: Lakes undergoing turnover twice a year, typical of temperate zones", "type": "leaf"},
                {"label": "Dissolved Oxygen (DO): Oxygen concentration decreases with temperature rise; stratification traps warm water at surface", "type": "leaf"}
            ]}
        ],
        "hi": [
            {"label": "तापमान और ऑक्सीजन परतें", "type": "branch", "date": "संरचना", "children": [
                {"label": "एपिलीमनिअन (Epilimnion): गर्म, ऑक्सीजन-समृद्ध सतह परत; प्रकाश संश्लेषण और हवा के मिश्रण से ऑक्सीजन संतृप्ति", "type": "leaf"},
                {"label": "थर्मोक्लाइन (Thermocline): मध्यम संक्रमण परत जहां गहराई के साथ पानी का तापमान तेजी से गिरता है", "type": "leaf"},
                {"label": "हाइपोलीमनिअन (Hypolimnion): ठंडी, अंधेरी निचली परत; वायुमंडल से कटी होने के कारण ऑक्सीजन की भारी कमी", "type": "leaf"}
            ]},
            {"label": "मौसमी चक्र (Turnover)", "type": "branch", "date": "चक्र", "children": [
                {"label": "वसंत/शरद ऋतु चक्र: सतह का पानी ठंडा होकर डूबता है, जिससे नीचे तक ऑक्सीजन का पुनर्वितरण होता है", "type": "leaf"},
                {"label": "ग्रीष्मकालीन स्तरीकरण: गर्म सतह मिश्रण को प्रतिबंधित करती है, जिससे निचली परत में ऑक्सीजन समाप्त होती है", "type": "leaf"}
            ]},
            {"label": "पारिस्थितिक परिणाम", "type": "branch", "date": "प्रभाव", "children": [
                {"label": "तलहटी हाइपोक्सिया: ऑक्सीजन रहित निचला पानी मछलियों को ऊपर प्रवास करने या मरने के लिए मजबूर करता है", "type": "leaf"},
                {"label": "रासायनिक बदलाव: अवायवीय परिस्थितियां तलछट से फास्फोरस को मुक्त करती हैं, जिससे प्रदूषण बढ़ता है", "type": "leaf"}
            ]},
            {"label": "यूपीएससी परीक्षा दृष्टिकोण", "type": "branch", "date": "परीक्षा", "children": [
                {"label": "डाइमिक्टिक झीलें (Dimictic): वर्ष में दो बार जल चक्र से गुजरने वाली झीलें, जो समशीतोष्ण क्षेत्रों में पाई जाती हैं", "type": "leaf"},
                {"label": "घुलित ऑक्सीजन: तापमान बढ़ने के साथ ऑक्सीजन की मात्रा घटती है; स्तरीकरण गर्म पानी को सतह पर रोकता है", "type": "leaf"}
            ]}
        ]
    },
    {
        "keys": ["irrigation", "problems-due-to-excessive-irrigation"],
        "en": [
            {"label": "Waterlogging Mechanics", "type": "branch", "date": "Waterlogging", "children": [
                {"label": "Definition: Saturation of soil with water, displacing air from soil pores and choking plant roots", "type": "leaf"},
                {"label": "Causes: Flood irrigation in clayey soils with poor drainage; canal seepage recharging water tables rapidly", "type": "leaf"}
            ]},
            {"label": "Salinization & Alkalization", "type": "branch", "date": "Salinization", "children": [
                {"label": "Capillary action: High evaporation pulls groundwater and dissolved salts upward to the surface", "type": "leaf"},
                {"label": "Reh/Usar Soils: White salt crust (sodium sulfate/carbonate) forms on topsoil, turning fertile land barren", "type": "leaf"}
            ]},
            {"label": "Resource Depletion", "type": "branch", "date": "Resources", "children": [
                {"label": "Over-extraction: Excessive tubewell irrigation depletes aquifers faster than natural recharge rates", "type": "leaf"},
                {"label": "Subsidence: Severe drop in water pressure causes compaction of aquifer sands, leading to land subsidence", "type": "leaf"}
            ]},
            {"label": "UPSC Exam Focus", "type": "branch", "date": "UPSC Focus", "children": [
                {"label": "Green Revolution zone: Punjab, Haryana, and Western UP show maximum salinization due to over-irrigation", "type": "leaf"},
                {"label": "Mitigation: Promotion of micro-irrigation (drip and sprinkler), laser land leveling, and crop diversification", "type": "leaf"}
            ]}
        ],
        "hi": [
            {"label": "जलभराव (Waterlogging) की क्रियाविधि", "type": "branch", "date": "जलभराव", "children": [
                {"label": "परिभाषा: पानी के साथ मिट्टी का पूर्ण संतृप्त होना, जिससे छिद्रों से हवा हट जाती है और जड़ें घुट जाती हैं", "type": "leaf"},
                {"label": "कारण: खराब जल निकासी वाली चिकनी मिट्टी में बाढ़ सिंचाई; नहरों के रिसाव से भूजल स्तर बढ़ना", "type": "leaf"}
            ]},
            {"label": "लवणीकरण और क्षारीयकरण", "type": "branch", "date": "लवणीकरण", "children": [
                {"label": "केशिका क्रिया (Capillary action): उच्च वाष्पीकरण भूजल और घुले हुए लवणों को सतह पर ऊपर खींचता है", "type": "leaf"},
                {"label": "रेह/ऊसर मिट्टी: ऊपरी मिट्टी पर सफेद लवण की परत बन जाती है, जिससे उपजाऊ भूमि बंजर हो जाती है", "type": "leaf"}
            ]},
            {"label": "संसाधनों की कमी", "type": "branch", "date": "संसाधन", "children": [
                {"label": "अत्यधिक दोहन: अत्यधिक नलकूप सिंचाई प्राकृतिक पुनर्भरण दरों की तुलना में भूजल को तेजी से समाप्त करती है", "type": "leaf"},
                {"label": "भूमि धंसाव: भूजल दबाव में भारी गिरावट से जलभृत संकुचित होते हैं, जिससे भूमि धंस जाती है", "type": "leaf"}
            ]},
            {"label": "यूपीएससी परीक्षा दृष्टिकोण", "type": "branch", "date": "परीक्षा", "children": [
                {"label": "हरित क्रांति क्षेत्र: पंजाब, हरियाणा और पश्चिमी UP में अत्यधिक सिंचाई के कारण लवणीकरण सबसे अधिक है", "type": "leaf"},
                {"label": "शमन रणनीतियाँ: सूक्ष्म सिंचाई (टपकन और छिड़काव), लेजर लैंड लेवलिंग और फसल विविधीकरण को बढ़ावा देना", "type": "leaf"}
            ]}
        ]
    },
    {
        "keys": ["biofuels", "national-policy-on-biofuels"],
        "en": [
            {"label": "Biofuel Generations", "type": "branch", "date": "Generations", "children": [
                {"label": "1G Biofuels: Produced from food sources (sugar, starch, vegetable oils) to yield bioethanol/biodiesel", "type": "leaf"},
                {"label": "2G Biofuels: Produced from non-food waste biomass (lignocellulosic waste like crop residues, straw)", "type": "leaf"},
                {"label": "3G Biofuels: Derived from algae/microalgae; fast-growing, requires no arable land", "type": "leaf"},
                {"label": "4G Biofuels: Utilizes genetically modified organisms and carbon capture tech to synthesize fuel", "type": "leaf"}
            ]},
            {"label": "National Policy on Biofuels", "type": "branch", "date": "Policy", "children": [
                {"label": "Launched in 2018 (amended in 2022); categorized biofuels to enable targeted financial support", "type": "leaf"},
                {"label": "Allows use of surplus foodgrains (damaged wheat, broken rice, maize) for ethanol production", "type": "leaf"}
            ]},
            {"label": "Blending Targets", "type": "branch", "date": "Targets", "children": [
                {"label": "Ethanol Blending: Target of 20% ethanol blending in petrol (E20) advanced to 2025-26 (originally 2030)", "type": "leaf"},
                {"label": "Biodiesel Blending: Target of 5% biodiesel blending in diesel by 2030; promoted using Jatropha seeds", "type": "leaf"}
            ]},
            {"label": "UPSC Exam Focus", "type": "branch", "date": "UPSC Focus", "children": [
                {"label": "Food vs Fuel Debate: Using fertile land and foodgrains for fuel production may compromise food security", "type": "leaf"},
                {"label": "Rudri Scheme: Repurposing Used Cooking Oil (RUCO) initiative by FSSAI to collect oil and convert to biodiesel", "type": "leaf"}
            ]}
        ],
        "hi": [
            {"label": "जैव ईंधन की पीढ़ियां", "type": "branch", "date": "पीढ़ियां", "children": [
                {"label": "1G जैव ईंधन: खाद्य स्रोतों (गन्ना, स्टार्च, वनस्पति तेल) से जैव-एथेनॉल/जैव-डीजल का उत्पादन", "type": "leaf"},
                {"label": "2G जैव ईंधन: गैर-खाद्य अपशिष्ट जैवभार (जैसे फसल अवशेष, पराली) से उत्पादित", "type": "leaf"},
                {"label": "3G जैव ईंधन: शैवाल/सूक्ष्म-शैवाल से प्राप्त; कृषि भूमि की आवश्यकता नहीं होती", "type": "leaf"},
                {"label": "4G जैव ईंधन: सिंथेटिक ईंधन के संश्लेषण के लिए जेनेटिक रूप से संशोधित जीवों का उपयोग", "type": "leaf"}
            ]},
            {"label": "जैव ईंधन पर राष्ट्रीय नीति", "type": "branch", "date": "नीति", "children": [
                {"label": "2018 में शुरू (2022 में संशोधित); लक्षित वित्तीय सहायता देने के लिए जैव ईंधन का वर्गीकरण किया", "type": "leaf"},
                {"label": "एथेनॉल उत्पादन के लिए अधिशेष खाद्यान्न (क्षतिग्रस्त गेहूं, टूटे हुए चावल, मक्का) के उपयोग की अनुमति", "type": "leaf"}
            ]},
            {"label": "मिश्रण (Blending) के लक्ष्य", "type": "branch", "date": "लक्ष्य", "children": [
                {"label": "एथेनॉल मिश्रण: पेट्रोल में 20% एथेनॉल मिश्रण (E20) का लक्ष्य बढ़ाकर 2025-26 किया गया (पहले 2030 था)", "type": "leaf"},
                {"label": "जैव-डीजल मिश्रण: 2030 तक डीजल में 5% जैव-डीजल मिश्रण का लक्ष्य; जेट्रोफा बीजों का उपयोग", "type": "leaf"}
            ]},
            {"label": "यूपीएससी परीक्षा दृष्टिकोण", "type": "branch", "date": "परीक्षा", "children": [
                {"label": "खाद्य बनाम ईंधन बहस: ईंधन उत्पादन के लिए उपजाऊ भूमि का उपयोग खाद्य सुरक्षा से समझौता कर सकता है", "type": "leaf"},
                {"label": "RUCO पहल: FSSAI द्वारा उपयोग किए गए खाना पकाने के तेल (RUCO) को जैव-डीजल में बदलने की योजना", "type": "leaf"}
            ]}
        ]
    },
    {
        "keys": ["energy-policy", "new-energy-resources", "renewable-energy", "energy-resources"],
        "en": [
            {"label": "Renewable Energy Targets", "type": "branch", "date": "Targets", "children": [
                {"label": "Non-fossil target: India committed to achieving 500 GW of non-fossil energy capacity by 2030", "type": "leaf"},
                {"label": "Net Zero: Committed to achieving net-zero greenhouse gas emissions by the year 2070", "type": "leaf"}
            ]},
            {"label": "Key Renewable Sources", "type": "branch", "date": "Sources", "children": [
                {"label": "Solar power: Leading growth; targets 280 GW by 2030; supported by National Solar Mission", "type": "leaf"},
                {"label": "Wind power: High potential in coastal states (Gujarat, Tamil Nadu); offshore wind policies launched", "type": "leaf"},
                {"label": "Biomass & Small Hydro: Grid-interactive decentralized electricity generation for rural areas", "type": "leaf"}
            ]},
            {"label": "Policy Initiatives", "type": "branch", "date": "Policies", "children": [
                {"label": "Panchamrit: Five climate commitments announced by India at UNFCCC COP-26 in Glasgow", "type": "leaf"},
                {"label": "ISA: International Solar Alliance co-founded by India and France to promote solar energy in sun-rich nations", "type": "leaf"}
            ]},
            {"label": "UPSC Exam Focus", "type": "branch", "date": "UPSC Focus", "children": [
                {"label": "Grid integration: Challenges of solar/wind variability; requires pumped hydro storage and battery backup", "type": "leaf"},
                {"label": "National Green Hydrogen Mission: Aiming to produce 5 MMT of green hydrogen annually by 2030", "type": "leaf"}
            ]}
        ],
        "hi": [
            {"label": "नवीकरणीय ऊर्जा लक्ष्य", "type": "branch", "date": "लक्ष्य", "children": [
                {"label": "गैर-जीवाश्म लक्ष्य: भारत ने 2030 तक 500 GW गैर-जीवाश्म ऊर्जा क्षमता प्राप्त करने का संकल्प लिया है", "type": "leaf"},
                {"label": "नेट ज़ीरो (Net Zero): वर्ष 2070 तक शुद्ध-शून्य ग्रीनहाउस गैस उत्सर्जन प्राप्त करने की प्रतिबद्धता", "type": "leaf"}
            ]},
            {"label": "प्रमुख नवीकरणीय स्रोत", "type": "branch", "date": "स्रोत", "children": [
                {"label": "सौर ऊर्जा: 2030 तक 280 GW का लक्ष्य; राष्ट्रीय सौर मिशन द्वारा समर्थित", "type": "leaf"},
                {"label": "पवन ऊर्जा: तटीय राज्यों (गुजरात, तमिलनाडु) में उच्च क्षमता; अपतटीय पवन नीतियों की शुरुआत", "type": "leaf"},
                {"label": "बायोमास और लघु जलविद्युत: ग्रामीण क्षेत्रों के लिए ग्रिड-इंटरैक्टिव विकेन्द्रीकृत बिजली उत्पादन", "type": "leaf"}
            ]},
            {"label": "नीतिगत पहलें", "type": "branch", "date": "पहलें", "children": [
                {"label": "पंचामृत (Panchamrit): ग्लासगो में UNFCCC COP-26 में भारत द्वारा घोषित पांच जलवायु प्रतिबद्धताएं", "type": "leaf"},
                {"label": "ISA: सौर ऊर्जा को बढ़ावा देने के लिए भारत और फ्रांस द्वारा सह-स्थापित अंतर्राष्ट्रीय सौर गठबंधन", "type": "leaf"}
            ]},
            {"label": "यूपीएससी परीक्षा दृष्टिकोण", "type": "branch", "date": "परीक्षा", "children": [
                {"label": "ग्रिड एकीकरण: सौर/पवन अस्थिरता की चुनौतियां; पंपयुक्त जल भंडारण और बैटरी बैकअप आवश्यक", "type": "leaf"},
                {"label": "राष्ट्रीय हरित हाइड्रोजन मिशन: 2030 तक सालाना 5 MMT हरित हाइड्रोजन का उत्पादन करने का लक्ष्य", "type": "leaf"}
            ]}
        ]
    },
    {
        "keys": ["soil-characteristics", "soil-formation", "soil-profiles", "soil-resource", "soils-in-india", "type-of-soils"],
        "en": [
            {"label": "Soil Formation Factors", "type": "branch", "date": "Pedogenesis", "children": [
                {"label": "Parent Material: Regulates soil mineral composition, structure, and chemical properties", "type": "leaf"},
                {"label": "Climate & Relief: Temperature/precipitation control weathering rates; slope regulates soil thickness", "type": "leaf"}
            ]},
            {"label": "Soil Horizons (Profile)", "type": "branch", "date": "Profile", "children": [
                {"label": "O Horizon: Organic surface layer composed of fresh and decomposing plant/animal matter", "type": "leaf"},
                {"label": "A Horizon (Topsoil): Rich in humus and minerals; zone of maximum biological activity", "type": "leaf"},
                {"label": "B Horizon (Subsoil): Zone of accumulation of minerals (clays, iron/aluminum oxides) washed down from E horizon", "type": "leaf"},
                {"label": "C & R Horizons: Weathered parent bedrock transforming into solid unweathered rock", "type": "leaf"}
            ]},
            {"label": "Major Soil Types in India", "type": "branch", "date": "India Soils", "children": [
                {"label": "Alluvial: Most widespread (~40%); highly fertile river silts, rich in potash but poor in phosphorus", "type": "leaf"},
                {"label": "Black (Regur): Derived from basaltic lava; clayey, self-ploughing, excellent moisture retention; ideal for cotton", "type": "leaf"},
                {"label": "Red & Yellow: Formed over crystalline igneous rocks; red due to iron diffusion; yellow when hydrated", "type": "leaf"},
                {"label": "Laterite: Formed under high temperature and heavy rainfall; intense leaching washes away silica, leaving iron/aluminum", "type": "leaf"}
            ]},
            {"label": "UPSC Exam Focus", "type": "branch", "date": "UPSC Focus", "children": [
                {"label": "Soil classification (USDA): Entisols, Inceptisols, Vertisols (black soils), and Aridisols distribution in India", "type": "leaf"},
                {"label": "Salinization: Excessive irrigation in arid zones causes saline accumulation due to capillary upward draft", "type": "leaf"}
            ]}
        ],
        "hi": [
            {"label": "मृदा निर्माण के कारक", "type": "branch", "date": "मृदा जनन", "children": [
                {"label": "जनक चट्टान (Parent Material): मृदा के खनिज संगठन, बनावट और रासायनिक गुणों को निर्धारित करती है", "type": "leaf"},
                {"label": "जलवायु और स्थलाकृति: तापमान/वर्षा अपक्षय की दर को नियंत्रित करते हैं; ढलान मोटाई को नियंत्रित करता है", "type": "leaf"}
            ]},
            {"label": "मृदा संस्तर (Profiles)", "type": "branch", "date": "संस्तर", "children": [
                {"label": "O संस्तर: कार्बनिक सतह परत जो पौधों/जंतुओं के सड़े-गले अवशेषों से बनी होती है", "type": "leaf"},
                {"label": "A संस्तर (ऊपरी मिट्टी): ह्यूमस और खनिजों से समृद्ध; अधिकतम जैविक गतिविधि का क्षेत्र", "type": "leaf"},
                {"label": "B संस्तर (उपमृदा): ऊपरी संस्तरों से बहकर आए खनिजों (लोहा/एल्यूमीनियम ऑक्साइड) के संचय का क्षेत्र", "type": "leaf"},
                {"label": "C और R संस्तर: अपक्षयित जनक चट्टान और नीचे स्थित ठोस मूल चट्टान", "type": "leaf"}
            ]},
            {"label": "भारत की प्रमुख मिट्टियाँ", "type": "branch", "date": "मृदा प्रकार", "children": [
                {"label": "जलोढ़ मिट्टी: सर्वाधिक विस्तृत (~40%); नदियों द्वारा लाई गई गाद, पोटाश समृद्ध लेकिन फास्फोरस विहीन", "type": "leaf"},
                {"label": "काली (रेगुर) मिट्टी: बेसाल्टिक लावा से निर्मित; स्व-जुताई वाली, नमी बनाए रखने में सक्षम; कपास के लिए आदर्श", "type": "leaf"},
                {"label": "लाल और पीली मिट्टी: क्रिस्टलीय आग्नेय चट्टानों पर निर्मित; लोहे के प्रसार के कारण लाल; जलयोजन पर पीली", "type": "leaf"},
                {"label": "लेटराइट मिट्टी: उच्च तापमान और भारी वर्षा वाले क्षेत्रों में तीव्र निक्षालन (Leaching) से निर्मित", "type": "leaf"}
            ]},
            {"label": "यूपीएससी परीक्षा दृष्टिकोण", "type": "branch", "date": "परीक्षा", "children": [
                {"label": "मृदा वर्गीकरण (USDA): भारत में एन्टिसोल, इनसेप्टिसोल, वर्टिसोल (काली मिट्टी) और एरिडिसोल का वितरण", "type": "leaf"},
                {"label": "लवणीकरण: शुष्क क्षेत्रों में अत्यधिक सिंचाई से केशिका क्रिया द्वारा सतह पर लवण जमा होना", "type": "leaf"}
            ]}
        ]
    },
    {
        "keys": ["soil-conservation"],
        "en": [
            {"label": "Soil Conservation Principles", "type": "branch", "date": "Concept", "children": [
                {"label": "Definition: Strategies to protect soil from wind and water erosion, maintaining organic fertility", "type": "leaf"},
                {"label": "Objective: Prevent land degradation, secure food production, and recharge groundwater tables", "type": "leaf"}
            ]},
            {"label": "Mechanical Methods", "type": "branch", "date": "Mechanical", "children": [
                {"label": "Contour Bunding: Constructing earthen barriers along contour lines to slow down water runoff", "type": "leaf"},
                {"label": "Terrace Farming: Cutting steps along steep mountain slopes to prevent gravity-driven water erosion", "type": "leaf"},
                {"label": "Shelterbelts: Rows of trees planted along farm borders to block wind erosion in arid plains", "type": "leaf"}
            ]},
            {"label": "Biological Methods", "type": "branch", "date": "Biological", "children": [
                {"label": "Mulching: Covering bare soil with organic litter (straw, leaves) to retain moisture and check runoff", "type": "leaf"},
                {"label": "Crop Rotation: Alternating deep-rooted crops with legumes to restore nitrogen levels naturally", "type": "leaf"},
                {"label": "Cover Crops: Planting fast-growing grasses during fallow periods to bind soil roots tightly", "type": "leaf"}
            ]},
            {"label": "UPSC Exam Focus", "type": "branch", "date": "UPSC Focus", "children": [
                {"label": "Integrated Watershed Management Program (IWMP): Restores ecological balance by harnessing rainwater runoff", "type": "leaf"},
                {"label": "Soil Health: Conservation strategies are key to achieving Land Degradation Neutrality (LDN) under UNCCD", "type": "leaf"}
            ]}
        ],
        "hi": [
            {"label": "मृदा संरक्षण के सिद्धांत", "type": "branch", "date": "अवधारणा", "children": [
                {"label": "परिभाषा: हवा और पानी के कटाव से मिट्टी की रक्षा करने तथा कार्बनिक उर्वरता बनाए रखने की रणनीतियाँ", "type": "leaf"},
                {"label": "उद्देश्य: भूमि क्षरण को रोकना, खाद्य उत्पादन सुरक्षित करना और भूजल स्तर को रिचार्ज करना", "type": "leaf"}
            ]},
            {"label": "यांत्रिक विधियां", "type": "branch", "date": "यांत्रिक", "children": [
                {"label": "समोच्च मेड़बन्दी (Contour Bunding): पानी के बहाव को धीमा करने के लिए ढलान के समानांतर मेड़ों का निर्माण", "type": "leaf"},
                {"label": "सीढ़ीदार खेती: गुरुत्वाकर्षण-जनित जल अपरदन को रोकने के लिए पहाड़ों पर सीढ़ीदार खेत बनाना", "type": "leaf"},
                {"label": "शेल्टरबेल्ट (रक्षक मेखला): शुष्क मैदानों में हवा के कटाव को रोकने के लिए खेतों की सीमाओं पर लगाए गए पेड़ों की कतारें", "type": "leaf"}
            ]},
            {"label": "जैविक विधियां", "type": "branch", "date": "जैविक", "children": [
                {"label": "मल्चिंग (Mulching): नमी बनाए रखने और कटाव रोकने के लिए खाली मिट्टी को भूसे/पत्तियों से ढकना", "type": "leaf"},
                {"label": "फसल चक्र (Crop Rotation): नाइट्रोजन स्तर को बहाल करने के लिए फलीदार फसलों के साथ अन्य फसलें उगाना", "type": "leaf"},
                {"label": "कवर फसलें: खाली समय में तेजी से बढ़ने वाली घासें उगाना जो मिट्टी को जड़ों से जकड़ कर रखती हैं", "type": "leaf"}
            ]},
            {"label": "यूपीएससी परीक्षा दृष्टिकोण", "type": "branch", "date": "परीक्षा", "children": [
                {"label": "एकीकृत जलसंभर प्रबंधन कार्यक्रम (IWMP): वर्षा जल के उपयोग द्वारा पारिस्थितिक संतुलन बहाल करना", "type": "leaf"},
                {"label": "मृदा स्वास्थ्य: UNCCD के तहत भूमि क्षरण तटस्थता (LDN) प्राप्त करने के लिए मृदा संरक्षण आवश्यक है", "type": "leaf"}
            ]}
        ]
    },
    {
        "keys": ["soil-erosion"],
        "en": [
            {"label": "Water Erosion Types", "type": "branch", "date": "Water Erosion", "children": [
                {"label": "Splash Erosion: Raindrops striking bare soil displace soil particles locally", "type": "leaf"},
                {"label": "Sheet Erosion: Uniform removal of thin topsoil layer by surface runoff; goes unnoticed easily", "type": "leaf"},
                {"label": "Rill Erosion: Runoff forms small, shallow channels in soil; easily corrected by ploughing", "type": "leaf"},
                {"label": "Gully Erosion: Deeper, wider ravines formed by advanced water action, cutting land into badlands", "type": "leaf"}
            ]},
            {"label": "Wind Erosion Mechanics", "type": "branch", "date": "Wind Erosion", "children": [
                {"label": "Saltation: Mid-sized sand particles bounce along soil surface, dislodging finer dust", "type": "leaf"},
                {"label": "Suspension: Fine dust particles lifted high into atmosphere, transported over long distances", "type": "leaf"}
            ]},
            {"label": "Ecological Damage", "type": "branch", "date": "Impacts", "children": [
                {"label": "Loss of fertility: Washing away of organic-rich A horizon depletes soil nutrients", "type": "leaf"},
                {"label": "Siltation: Eroded soil sediments deposit in rivers and reservoirs, reducing water storage capacity", "type": "leaf"}
            ]},
            {"label": "UPSC Exam Focus", "type": "branch", "date": "UPSC Focus", "children": [
                {"label": "Badland Topography: Gullies in Chambal valley (Madhya Pradesh/Rajasthan) created extensive ravines", "type": "leaf"},
                {"label": "Anthropogenic drivers: Deforestation on slopes, overgrazing, and vertical ploughing up slopes", "type": "leaf"}
            ]}
        ],
        "hi": [
            {"label": "जल अपरदन के प्रकार", "type": "branch", "date": "जल अपरदन", "children": [
                {"label": "बूंद अपरदन (Splash): बारिश की बूंदों के सीधे प्रहार से मिट्टी के कणों का विस्थापन", "type": "leaf"},
                {"label": "परत अपरदन (Sheet): सतह के पानी के बहने से महीन ऊपरी उपजाऊ परत का हटना; आसानी से ध्यान में नहीं आता", "type": "leaf"},
                {"label": "क्षुद्रसरिता अपरदन (Rill): पानी बहने से मिट्टी में छोटी-छोटी उथली नलियां (Rills) बन जाती हैं", "type": "leaf"},
                {"label": "अवनालिका अपरदन (Gully): तीव्र जल प्रवाह से गहरी खाइयां बनना, जिससे भूमि कृषि के लिए अनुपयुक्त होती है", "type": "leaf"}
            ]},
            {"label": "वायु अपरदन की क्रियाविधि", "type": "branch", "date": "वायु अपरदन", "children": [
                {"label": "उत्परिवर्तन (Saltation): मध्यम आकार के रेत के कणों का सतह पर उछलना, जिससे महीन धूल हटती है", "type": "leaf"},
                {"label": "निलंबन (Suspension): महीन धूल कणों का वायुमंडल में बहुत ऊंचाई तक उठना और लंबी दूरी तय करना", "type": "leaf"}
            ]},
            {"label": "पारिस्थितिक क्षति", "type": "branch", "date": "प्रभाव", "children": [
                {"label": "उर्वरता का नुकसान: ह्यूमस से भरपूर संस्तर 'A' के बह जाने से मिट्टी पोषक तत्व विहीन हो जाती है", "type": "leaf"},
                {"label": "गाद जमा होना: अपक्षयित मिट्टी नदियों और जलाशयों में जमा होकर उनकी जल धारण क्षमता कम करती है", "type": "leaf"}
            ]},
            {"label": "यूपीएससी परीक्षा दृष्टिकोण", "type": "branch", "date": "परीक्षा", "children": [
                {"label": "बीहड़ स्थलाकृति (Badlands): चंबल घाटी (MP/राजस्थान) में अवनालिका अपरदन से विस्तृत बीहड़ों का निर्माण हुआ है", "type": "leaf"},
                {"label": "मानवजनित कारक: पहाड़ियों पर जंगलों की कटाई, अत्यधिक चराई और ढलान की दिशा में खड़ी जुताई", "type": "leaf"}
            ]}
        ]
    },
    {
        "keys": ["soil-health-card"],
        "en": [
            {"label": "Scheme Overview", "type": "branch", "date": "Launch", "children": [
                {"label": "Launched in February 2015 by Ministry of Agriculture and Farmers Welfare, Government of India", "type": "leaf"},
                {"label": "Provides farmers with crop-wise nutrient recommendations to prevent overuse of chemical fertilizers", "type": "leaf"}
            ]},
            {"label": "Twelve Parameters Assessed", "type": "branch", "date": "Parameters", "children": [
                {"label": "Macro Nutrients: Nitrogen (N), Phosphorus (P), Potassium (K)", "type": "leaf"},
                {"label": "Secondary Nutrients: Sulfur (S)", "type": "leaf"},
                {"label": "Micro Nutrients: Zinc (Zn), Iron (Fe), Copper (Cu), Manganese (Mn), Boron (B)", "type": "leaf"},
                {"label": "Physical parameters: pH, Electrical Conductivity (EC), Organic Carbon (OC)", "type": "leaf"}
            ]},
            {"label": "Key Objectives", "type": "branch", "date": "Objectives", "children": [
                {"label": "Promote balanced fertilizer application (ideal N:P:K ratio in India is 4:2:1; skewed heavily in Punjab/Haryana)", "type": "leaf"},
                {"label": "Reduces cost of cultivation and prevents soil degradation/groundwater contamination", "type": "leaf"}
            ]},
            {"label": "UPSC Exam Focus", "type": "branch", "date": "UPSC Focus", "children": [
                {"label": "OC parameter: Organic Carbon is a direct indicator of soil biological activity and humus levels", "type": "leaf"},
                {"label": "Soil test frequency: Cards are issued to farmers once every 2 years after laboratory testing of soil samples", "type": "leaf"}
            ]}
        ],
        "hi": [
            {"label": "योजना का अवलोकन", "type": "branch", "date": "शुरुआत", "children": [
                {"label": "कृषि एवं किसान कल्याण मंत्रालय द्वारा फरवरी 2015 में शुरू की गई एक प्रमुख योजना", "type": "leaf"},
                {"label": "रासायनिक उर्वरकों के अत्यधिक उपयोग को रोकने के लिए किसानों को फसल-वार पोषक तत्वों की सलाह दी जाती है", "type": "leaf"}
            ]},
            {"label": "आकलित बारह पैरामीटर", "type": "branch", "date": "पैरामीटर", "children": [
                {"label": "मुख्य पोषक तत्व: नाइट्रोजन (N), फास्फोरस (P), पोटेशियम (K)", "type": "leaf"},
                {"label": "द्वितीयक पोषक तत्व: सल्फर (S)", "type": "leaf"},
                {"label": "सूक्ष्म पोषक तत्व: जस्ता (Zn), लोहा (Fe), तांबा (Cu), मैंगनीज (Mn), बोरॉन (B)", "type": "leaf"},
                {"label": "भौतिक संकेतक: pH, विद्युत चालकता (EC), जैविक कार्बन (OC)", "type": "leaf"}
            ]},
            {"label": "मुख्य उद्देश्य", "type": "branch", "date": "उद्देश्य", "children": [
                {"label": "संतुलित उर्वरक उपयोग को बढ़ावा (भारत में आदर्श N:P:K अनुपात 4:2:1 है, जो वर्तमान में विकृत है)", "type": "leaf"},
                {"label": "खेती की लागत को कम करता है और मिट्टी के क्षरण तथा भूजल प्रदूषण को रोकता है", "type": "leaf"}
            ]},
            {"label": "यूपीएससी परीक्षा दृष्टिकोण", "type": "branch", "date": "परीक्षा", "children": [
                {"label": "OC पैरामीटर: जैविक कार्बन मिट्टी की जैविक गतिविधि और ह्यूमस स्तर का प्रत्यक्ष संकेतक है", "type": "leaf"},
                {"label": "परीक्षण आवृत्ति: प्रयोगशाला परीक्षणों के बाद प्रत्येक 2 वर्ष में किसानों को मृदा स्वास्थ्य कार्ड जारी किए जाते हैं", "type": "leaf"}
            ]}
        ]
    },
    {
        "keys": ["solar-energy"],
        "en": [
            {"label": "Solar Technologies", "type": "branch", "date": "Technology", "children": [
                {"label": "Photovoltaic (PV): Converts sunlight directly into electricity using semiconductor materials (silicon)", "type": "leaf"},
                {"label": "Concentrated Solar Power (CSP): Uses mirrors/lenses to focus sunlight to heat fluid, driving steam turbines", "type": "leaf"}
            ]},
            {"label": "National Solar Mission", "type": "branch", "date": "NSM", "children": [
                {"label": "Launched in 2010; key part of India's National Action Plan on Climate Change (NAPCC)", "type": "leaf"},
                {"label": "Aims to establish India as a global leader in solar energy, targeting grid-connected solar capacity", "type": "leaf"}
            ]},
            {"label": "Major Solar Parks in India", "type": "branch", "date": "Solar Parks", "children": [
                {"label": "Bhadla Solar Park (Rajasthan): World's largest solar park spanning over 14,000 acres (~2,245 MW)", "type": "leaf"},
                {"label": "Pavagada Solar Park (Karnataka): Second largest solar park located in Tumkur district (~2,050 MW)", "type": "leaf"}
            ]},
            {"label": "UPSC Exam Focus", "type": "branch", "date": "UPSC Focus", "children": [
                {"label": "ISA: International Solar Alliance co-founded with France; headquarters in Gurugram, India", "type": "leaf"},
                {"label": "PM-KUSUM Scheme: Promotes solar pumps and grid-connected solar power plants on farmers' drylands", "type": "leaf"}
            ]}
        ],
        "hi": [
            {"label": "सौर ऊर्जा तकनीक", "type": "branch", "date": "तकनीक", "children": [
                {"label": "फोटोवोल्टिक (PV): अर्धचालक पदार्थों (सिलिकॉन) का उपयोग कर सूर्य प्रकाश को सीधे बिजली में बदलना", "type": "leaf"},
                {"label": "कंसंट्रेटेड सोलर पावर (CSP): तरल पदार्थ गर्म करने के लिए दर्पणों का उपयोग, जो टरबाइन चलाते हैं", "type": "leaf"}
            ]},
            {"label": "राष्ट्रीय सौर मिशन", "type": "branch", "date": "NSM", "children": [
                {"label": "2010 में शुरू किया गया; जलवायु परिवर्तन पर भारत की राष्ट्रीय कार्य योजना (NAPCC) का प्रमुख हिस्सा", "type": "leaf"},
                {"label": "ग्रिड-कनेक्टेड सौर क्षमता प्राप्त कर भारत को सौर ऊर्जा में वैश्विक नेता के रूप में स्थापित करना", "type": "leaf"}
            ]},
            {"label": "भारत के प्रमुख सौर पार्क", "type": "branch", "date": "सौर पार्क", "children": [
                {"label": "भादला सौर पार्क (राजस्थान): दुनिया का सबसे बड़ा सौर पार्क जो 14,000 एकड़ में फैला है (~2,245 MW)", "type": "leaf"},
                {"label": "पावागढ़ सौर पार्क (कर्नाटक): तुमकुर जिले में स्थित भारत का दूसरा सबसे बड़ा सौर पार्क (~2,050 MW)", "type": "leaf"}
            ]},
            {"label": "यूपीएससी परीक्षा दृष्टिकोण", "type": "branch", "date": "परीक्षा", "children": [
                {"label": "ISA: फ्रांस के साथ सह-स्थापित अंतर्राष्ट्रीय सौर गठबंधन; मुख्यालय गुरुग्राम, भारत में है", "type": "leaf"},
                {"label": "PM-KUSUM योजना: किसानों की बंजर भूमि पर सौर पंप और ग्रिड-कनेक्टेड सौर ऊर्जा संयंत्र लगाने की योजना", "type": "leaf"}
            ]}
        ]
    },
    {
        "keys": ["tidal-energy"],
        "en": [
            {"label": "Tidal Principles", "type": "branch", "date": "Mechanism", "children": [
                {"label": "Definition: Renewable energy generated by surge of ocean tides driven by gravitational pull of Moon and Sun", "type": "leaf"},
                {"label": "Harnessing: Utilizing tidal barrages, turbines, or fences built across estuaries to generate electricity", "type": "leaf"}
            ]},
            {"label": "Potential in India", "type": "branch", "date": "India Potential", "children": [
                {"label": "Gulf of Khambhat (Gujarat): Highest tidal power potential in India, featuring high tidal ranges (>10m)", "type": "leaf"},
                {"label": "Gulf of Kutch (Gujarat) & Sundarbans (West Bengal): Other identified zones with tidal energy potential", "type": "leaf"}
            ]},
            {"label": "Pros & Cons", "type": "branch", "date": "Analysis", "children": [
                {"label": "Advantages: Highly predictable compared to solar and wind; high energy density of water", "type": "leaf"},
                {"label": "Disadvantages: High initial construction cost; alters estuarine siltation patterns and harms marine organisms", "type": "leaf"}
            ]},
            {"label": "UPSC Exam Focus", "type": "branch", "date": "UPSC Focus", "children": [
                {"label": "Desalination link: Tidal energy can be paired with coastal desalination plants for clean water production", "type": "leaf"},
                {"label": "Ministry of New and Renewable Energy (MNRE) declared tidal energy as renewable, enabling tariff incentives", "type": "leaf"}
            ]}
        ],
        "hi": [
            {"label": "ज्वारीय ऊर्जा के सिद्धांत", "type": "branch", "date": "क्रियाविधि", "children": [
                {"label": "परिभाषा: चंद्रमा और सूर्य के गुरुत्वाकर्षण खिंचाव से संचालित महासागरीय ज्वार के उतार-चढ़ाव से उत्पन्न ऊर्जा", "type": "leaf"},
                {"label": "दोहन: बिजली उत्पन्न करने के लिए खाड़ियों या मुहानों पर ज्वारीय बांधों (Barrages) या टर्बाइन का उपयोग करना", "type": "leaf"}
            ]},
            {"label": "भारत में क्षमता", "type": "branch", "date": "भारत में क्षमता", "children": [
                {"label": "खंभात की खाड़ी (गुजरात): भारत में सर्वाधिक ज्वारीय ऊर्जा क्षमता (>10 मीटर की ज्वार ऊंचाई)", "type": "leaf"},
                {"label": "कच्छ की खाड़ी (गुजरात) और सुंदरवन (पश्चिम बंगाल): ज्वारीय ऊर्जा उत्पादन के लिए अन्य प्रमुख क्षेत्र", "type": "leaf"}
            ]},
            {"label": "गुण और दोष", "type": "branch", "date": "मूल्यांकन", "children": [
                {"label": "लाभ: सौर और पवन की तुलना में अत्यधिक अनुमानित; जल का उच्च ऊर्जा घनत्व", "type": "leaf"},
                {"label": "हानि: उच्च प्रारंभिक निर्माण लागत; ज्वारनदमुख की गाद प्रणाली और जलीय जीवों को नुकसान", "type": "leaf"}
            ]},
            {"label": "यूपीएससी परीक्षा दृष्टिकोण", "type": "branch", "date": "परीक्षा", "children": [
                {"label": "अलवणीकरण संबंध: ज्वारीय ऊर्जा को स्वच्छ जल के लिए तटीय अलवणीकरण संयंत्रों के साथ जोड़ा जा सकता है", "type": "leaf"},
                {"label": "नवीन और नवीकरणीय ऊर्जा मंत्रालय (MNRE) ने ज्वारीय ऊर्जा को नवीकरणीय घोषित कर टैरिफ प्रोत्साहन सक्षम किया", "type": "leaf"}
            ]}
        ]
    },
    {
        "keys": ["water-pollution", "causes-of-water-pollution", "harmful-effects-of-water-pollution", "sources-of-water-pollution", "measurement-of-water-pollution"],
        "en": [
            {"label": "Sources of Water Pollution", "type": "branch", "date": "Sources", "children": [
                {"label": "Point Sources: Identifiable pipes discharging untreated industrial effluents and municipal sewage directly into rivers", "type": "leaf"},
                {"label": "Non-Point Sources: Diffuse agricultural runoff carrying pesticides/fertilizers, and urban storm water runoff", "type": "leaf"}
            ]},
            {"label": "Heavy Metal Poisoning", "type": "branch", "date": "Diseases", "children": [
                {"label": "Minamata Disease: Methylmercury poisoning from seafood; causes neurological damage and sensory loss", "type": "leaf"},
                {"label": "Itai-Itai Disease: Cadmium poisoning from contaminated river water; causes severe bone softening and joint pain", "type": "leaf"},
                {"label": "Blue Baby Syndrome: Methemoglobinemia caused by high nitrate levels in drinking water, limiting oxygen in blood", "type": "leaf"}
            ]},
            {"label": "Pollution Measurement", "type": "branch", "date": "Metrics", "children": [
                {"label": "BOD (Biochemical Oxygen Demand): Amount of dissolved oxygen consumed by aerobic bacteria to decompose organic matter", "type": "leaf"},
                {"label": "COD (Chemical Oxygen Demand): Measures both biodegradable and non-biodegradable pollutants using chemical oxidants", "type": "leaf"},
                {"label": "DO (Dissolved Oxygen): Crucial for aquatic life; levels dropping below 4 mg/L indicate severe organic pollution", "type": "leaf"}
            ]},
            {"label": "UPSC Exam Focus", "type": "branch", "date": "UPSC Focus", "children": [
                {"label": "Biomagnification: Increase in toxin concentration (e.g. DDT, Mercury) at higher levels of the food chain", "type": "leaf"},
                {"label": "Water Act 1974: India's primary legislation establishing the CPCB (Central Pollution Control Board) to monitor river health", "type": "leaf"}
            ]}
        ],
        "hi": [
            {"label": "जल प्रदूषण के स्रोत", "type": "branch", "date": "स्रोत", "children": [
                {"label": "बिंदु स्रोत (Point): औद्योगिक इकाइयों और शहरी नालों से बिना उपचारित अपशिष्ट को सीधे नदियों में छोड़ना", "type": "leaf"},
                {"label": "गैर-बिंदु स्रोत (Non-Point): कृषि क्षेत्रों से बहने वाले कीटनाशक, और शहरी सड़कों से बहने वाला कचरा", "type": "leaf"}
            ]},
            {"label": "भारी धातु विषाक्तता", "type": "branch", "date": "रोग", "children": [
                {"label": "मनामाता रोग: पारे (Mercury) से प्रदूषित मछली खाने से होने वाला तंत्रिका संबंधी विकार", "type": "leaf"},
                {"label": "इटाई-इटाई रोग: कैडमियम (Cadmium) विषाक्तता के कारण हड्डियों का कमजोर होना और जोड़ों में तीव्र दर्द", "type": "leaf"},
                {"label": "ब्लू बेबी सिंड्रोम: पीने के पानी में नाइट्रेट की अधिकता से होने वाला रोग, जो रक्त की ऑक्सीजन क्षमता घटाता", "type": "leaf"}
            ]},
            {"label": "प्रदूषण का मापन", "type": "branch", "date": "मापन", "children": [
                {"label": "BOD (जैव रासायनिक ऑक्सीजन मांग): कार्बनिक कचरे को पचाने के लिए जीवाणुओं द्वारा उपभोग की गई ऑक्सीजन", "type": "leaf"},
                {"label": "COD (रासायनिक ऑक्सीजन मांग): रासायनिक ऑक्सीकारक द्वारा कार्बनिक और अकार्बनिक प्रदूषकों का कुल मापन", "type": "leaf"},
                {"label": "DO (घुलित ऑक्सीजन): पानी में घुली ऑक्सीजन; 4 mg/L से नीचे का स्तर जलीय जीवों के लिए घातक है", "type": "leaf"}
            ]},
            {"label": "यूपीएससी परीक्षा दृष्टिकोण", "type": "branch", "date": "परीक्षा", "children": [
                {"label": "जैव-आवर्धन (Biomagnification): खाद्य श्रृंखला के उच्च स्तरों पर विषाक्त पदार्थों (जैसे DDT, पारा) की सांद्रता बढ़ना", "type": "leaf"},
                {"label": "जल अधिनियम 1974: भारत का पहला प्रमुख पर्यावरण कानून जिसने प्रदूषण नियंत्रण बोर्ड (CPCB) की स्थापना की", "type": "leaf"}
            ]}
        ]
    },
    {
        "keys": ["mercury-pollution"],
        "en": [
            {"label": "Mercury Sources", "type": "branch", "date": "Sources", "children": [
                {"label": "Anthropogenic: Coal-fired power plants (largest source of atmospheric mercury), artisanal gold mining, and waste incineration", "type": "leaf"},
                {"label": "Natural: Volcanic eruptions and weathering of cinnabar (HgS) ore deposits", "type": "leaf"}
            ]},
            {"label": "Biomagnification Pathway", "type": "branch", "date": "Bio-Flow", "children": [
                {"label": "Methylation: Microbes in aquatic sediment convert inorganic mercury into organic methylmercury", "type": "leaf"},
                {"label": "Bioaccumulation: Methylmercury builds up in marine food webs, showing extreme concentration in apex predators (tuna, sharks)", "type": "leaf"}
            ]},
            {"label": "Minamata Convention", "type": "branch", "date": "Treaty", "children": [
                {"label": "Adopted in 2013 under UNEP; entered into force in August 2017 to protect human health and environment", "type": "leaf"},
                {"label": "Mandates phasing out of mercury in products (thermometers, lighting) and controls industrial emissions", "type": "leaf"}
            ]},
            {"label": "UPSC Exam Focus", "type": "branch", "date": "UPSC Focus", "children": [
                {"label": "India status: India ratified the Minamata Convention in 2018, banning mercury imports for non-industrial uses", "type": "leaf"},
                {"label": "Health effects: Methylmercury crosses blood-brain barrier, causing neurological disorders (paresthesia, tunnel vision)", "type": "leaf"}
            ]}
        ],
        "hi": [
            {"label": "पारे के स्रोत", "type": "branch", "date": "स्रोत", "children": [
                {"label": "मानवजनित: कोयला आधारित बिजली संयंत्र (हवा में पारे का सबसे बड़ा स्रोत), लघु-स्तरीय सोने का खनन और कचरा दहन", "type": "leaf"},
                {"label": "प्राकृतिक: ज्वालामुखी विस्फोट और सिनाबार (HgS) अयस्क का अपक्षय", "type": "leaf"}
            ]},
            {"label": "जैव-आवर्धन मार्ग", "type": "branch", "date": "जैव-आवर्धन", "children": [
                {"label": "मिथाइलेशन: जलीय तलछट में रोगाणु अकार्बनिक पारे को कार्बनिक मिथाइलमर्करी में परिवर्तित करते हैं", "type": "leaf"},
                {"label": "जैव-संचय: मिथाइलमर्करी खाद्य श्रृंखला के शीर्ष शिकारियों (ट्यूना, शार्क) में अत्यधिक मात्रा में जमा होता है", "type": "leaf"}
            ]},
            {"label": "मिनामाता कन्वेंशन", "type": "branch", "date": "अंतरराष्ट्रीय संधि", "children": [
                {"label": "UNEP के तहत 2013 में अपनाया गया; मानव स्वास्थ्य की रक्षा के लिए अगस्त 2017 में लागू हुआ", "type": "leaf"},
                {"label": "विभिन्न उत्पादों (थर्मामीटर, बल्ब) में पारे के उपयोग को धीरे-धीरे बंद करने और औद्योगिक उत्सर्जन को रोकने का आदेश", "type": "leaf"}
            ]},
            {"label": "यूपीएससी परीक्षा दृष्टिकोण", "type": "branch", "date": "परीक्षा", "children": [
                {"label": "भारत की स्थिति: भारत ने 2018 में मिनामाता कन्वेंशन की पुष्टि की और गैर-औद्योगिक उपयोगों पर आयात प्रतिबंध लगाया", "type": "leaf"},
                {"label": "स्वास्थ्य प्रभाव: मिथाइलमर्करी रक्त-मस्तिष्क बाधा (Blood-brain barrier) को पार कर तंत्रिका क्षति का कारण बनता है", "type": "leaf"}
            ]}
        ]
    },
    {
        "keys": ["land-resource"],
        "en": [
            {"label": "Land Use Pattern in India", "type": "branch", "date": "Land Use", "children": [
                {"label": "Net Sown Area: Accounts for ~46% of geographical area; high agricultural dependence", "type": "leaf"},
                {"label": "Forest Area: Officially reported at ~23% (actual forest cover is lower, around 21.7%)", "type": "leaf"},
                {"label": "Fallow Lands: Arable land left uncultivated for 1 to 5 years to restore organic nutrients naturally", "type": "leaf"}
            ]},
            {"label": "Land Degradation Issues", "type": "branch", "date": "Degradation", "children": [
                {"label": "Drivers: Soil erosion, wind-blown sand dunes, waterlogging, and soil salinization due to over-irrigation", "type": "leaf"},
                {"label": "Impact: Decreases agricultural productivity, threatens food security, and drives rural migration", "type": "leaf"}
            ]},
            {"label": "Reclamation & Management", "type": "branch", "date": "Management", "children": [
                {"label": "Wasteland development: National Wastelands Development Board reclaiming alkaline/saline soils", "type": "leaf"},
                {"label": "Afforestation: Planting deep-rooted trees along dry wasteland boundaries to check soil movement", "type": "leaf"}
            ]},
            {"label": "UPSC Exam Focus", "type": "branch", "date": "UPSC Focus", "children": [
                {"label": "UNCCD targets: Achieving Land Degradation Neutrality (LDN) to balance land loss with restoration", "type": "leaf"},
                {"label": "Integrated Land Use Planning: Linking rural watershed projects with urban expansion boundaries", "type": "leaf"}
            ]}
        ],
        "hi": [
            {"label": "भारत में भूमि उपयोग पैटर्न", "type": "branch", "date": "भूमि उपयोग", "children": [
                {"label": "शुद्ध बोया गया क्षेत्र: देश के कुल भौगोलिक क्षेत्र का लगभग 46%; उच्च कृषि निर्भरता", "type": "leaf"},
                {"label": "वन क्षेत्र: आधिकारिक रिपोर्टों में ~23% (वास्तविक वन आवरण थोड़ा कम, लगभग 21.7% है)", "type": "leaf"},
                {"label": "परती भूमि: उपजाऊ भूमि जिसे पोषक तत्वों को बहाल करने के लिए 1 से 5 वर्षों तक खाली छोड़ दिया जाता है", "type": "leaf"}
            ]},
            {"label": "भूमि क्षरण की समस्या", "type": "branch", "date": "भूमि क्षरण", "children": [
                {"label": "कारक: जल और वायु अपरदन, जलभराव और अत्यधिक सिंचाई के कारण होने वाला लवणीकरण", "type": "leaf"},
                {"label": "प्रभाव: कृषि उत्पादकता में कमी, खाद्य सुरक्षा को खतरा और ग्रामीण पलायन को बढ़ावा देना", "type": "leaf"}
            ]},
            {"label": "सुधार और प्रबंधन", "type": "branch", "date": "प्रबंधन", "children": [
                {"label": "बंजर भूमि विकास: राष्ट्रीय बंजर भूमि विकास बोर्ड क्षारीय/लवणीय मिट्टी का सुधार कर रहा है", "type": "leaf"},
                {"label": "वनीकरण: मिट्टी के विस्थापन को रोकने के लिए बंजर भूमि सीमाओं पर गहरे पैठ वाले पेड़ लगाना", "type": "leaf"}
            ]},
            {"label": "यूपीएससी परीक्षा दृष्टिकोण", "type": "branch", "date": "परीक्षा", "children": [
                {"label": "UNCCD लक्ष्य: भूमि क्षरण तटस्थता (LDN) प्राप्त करना ताकि क्षरित भूमि की भरपाई की जा सके", "type": "leaf"},
                {"label": "एकीकृत भूमि उपयोग योजना: ग्रामीण जलसंभर परियोजनाओं को शहरी नियोजन के साथ जोड़ना", "type": "leaf"}
            ]}
        ]
    },
    {
        "keys": ["surface-water"],
        "en": [
            {"label": "Water Resources Scenario", "type": "branch", "date": "Overview", "children": [
                {"label": "Precipitation budget: India receives ~4,000 billion cubic meters (BCM) of rainfall annually", "type": "leaf"},
                {"label": "Available surface water: Estimated at 1,869 BCM, but only ~690 BCM is utilizable due to seasonal runoff", "type": "leaf"}
            ]},
            {"label": "Major River Basins", "type": "branch", "date": "Basins", "children": [
                {"label": "Ganga-Brahmaputra Basin: Largest basin; accounts for over 60% of India's total surface water runoff", "type": "leaf"},
                {"label": "Peninsular Rivers: Monsoon-dependent; Mahanadi, Godavari, Krishna, and Cauvery show high seasonal variability", "type": "leaf"}
            ]},
            {"label": "Water Conflict & Management", "type": "branch", "date": "Conflicts", "children": [
                {"label": "Inter-state disputes: Cauvery dispute (KA/TN), Krishna dispute, Mahadayi dispute; managed under Article 262", "type": "leaf"},
                {"label": "Central Water Commission (CWC): Nodal body regulating surface water schemes, flood forecasting, and dam safety", "type": "leaf"}
            ]},
            {"label": "UPSC Exam Focus", "type": "branch", "date": "UPSC Focus", "children": [
                {"label": "National River Linking Project (NRLP): Transfers surplus water from Himalayan rivers to water-scarce Peninsular basins", "type": "leaf"},
                {"label": "Ken-Betwa Link: India's first river-linking project; involves submergence of parts of Panna Tiger Reserve", "type": "leaf"}
            ]}
        ],
        "hi": [
            {"label": "जल संसाधन परिदृश्य", "type": "branch", "date": "अवलोकन", "children": [
                {"label": "वर्षा का बजट: भारत में सालाना लगभग 4,000 बिलियन क्यूबिक मीटर (BCM) वर्षा जल प्राप्त होता है", "type": "leaf"},
                {"label": "उपलब्ध सतह का पानी: अनुमानित 1,869 BCM, लेकिन मौसमी अपवाह के कारण केवल ~690 BCM ही उपयोग योग्य है", "type": "leaf"}
            ]},
            {"label": "प्रमुख नदी बेसिन", "type": "branch", "date": "बेसिन", "children": [
                {"label": "गंगा-ब्रह्मपुत्र बेसिन: सबसे बड़ा बेसिन; भारत के कुल सतही जल अपवाह का 60% से अधिक हिस्सा है", "type": "leaf"},
                {"label": "प्रायद्वीपीय नदियां: मानसूनी नदियां; महानदी, गोदावरी, कृष्णा और कावेरी अत्यधिक मौसमी उतार-चढ़ाव दर्शाती हैं", "type": "leaf"}
            ]},
            {"label": "जल संघर्ष और प्रबंधन", "type": "branch", "date": "संघर्ष", "children": [
                {"label": "अंतर-राज्यीय विवाद: कावेरी विवाद (KA/TN), कृष्णा विवाद; संविधान के अनुच्छेद 262 के तहत न्यायाधिकरणों द्वारा समाधान", "type": "leaf"},
                {"label": "केंद्रीय जल आयोग (CWC): सतही जल योजनाओं, बाढ़ पूर्वानुमान और बांध सुरक्षा की निगरानी करने वाला नोडल निकाय", "type": "leaf"}
            ]},
            {"label": "यूपीएससी परीक्षा दृष्टिकोण", "type": "branch", "date": "परीक्षा", "children": [
                {"label": "राष्ट्रीय नदी जोड़ो परियोजना (NRLP): अधिशेष जल को जल की कमी वाले प्रायद्वीपीय बेसिनों में स्थानांतरित करना", "type": "leaf"},
                {"label": "केन-बेतवा लिंक: भारत की पहली नदी-जोड़ो परियोजना; पन्ना टाइगर रिजर्व का कुछ भाग जलमग्न होना शामिल है", "type": "leaf"}
            ]}
        ]
    }
]

TRANSLATIONS = {
    "atmosphere": "वायुमंडल",
    "composition": "संघटन",
    "structure": "संरचना",
    "dust": "धूल",
    "particles": "कण",
    "gases": "गैसें",
    "water": "जल",
    "vapour": "जलवाष्प",
    "pressure": "दाब",
    "wind": "पवन",
    "ocean": "महासागर",
    "currents": "जलधाराएं",
    "temperature": "तापमान",
    "salinity": "लवणता",
    "density": "घनत्व",
    "wave": "तरंग",
    "tides": "ज्वार-भाटा",
    "coral": "प्रवाल",
    "reefs": "भित्तियाँ",
    "ecology": "पारिस्थितिकी",
    "ecosystem": "पारितंत्र",
    "ecotone": "संक्रमणिका",
    "succession": "अनुक्रमण",
    "forest": "वन",
    "soil": "मृदा",
    "erosion": "अपरदन",
    "conservation": "संरक्षण",
    "deforestation": "वनोन्मूलन",
    "afforestation": "वनरोपण",
    "reforestation": "पुनर्वनीकरण",
    "climate": "जलवायु",
    "world": "विश्व",
    "distribution": "वितरण",
    "precipitation": "वर्षण",
    "clouds": "बादल",
    "velocity": "वेग",
    "direction": "दिशा",
    "forces": "बल",
    "coriolis": "कोरिओलिस",
    "frictional": "घर्षण",
    "indian": "भारतीय",
    "plate": "प्लेट",
    "tectonics": "विवर्तनिकी",
    "boundaries": "सीमाएं",
    "interior": "आंतरिक भाग",
    "crust": "भूपर्पटी",
    "earth": "पृथ्वी",
    "drift": "प्रवाह",
    "sea": "समुद्र",
    "floor": "नितल",
    "spreading": "प्रसरण",
    "volcanism": "ज्वालामुखीयता",
    "weathering": "अपक्षय",
    "rocks": "चट्टानें",
    "minerals": "खनिज",
    "landforms": "भू-आकृतियाँ",
    "geomorphic": "भू-आकृतिक",
    "agent": "कारक",
    "ecosystems": "पारितंत्र",
    "wetlands": "आ्र्द्रभूमि",
    "estuaries": "ज्वारनदमुख",
    "organisms": "जीव",
    "plankton": "प्लवक",
    "phytoplankton": "पादप प्लवक",
    "zooplankton": "जंतु प्लवक",
    "sunlight": "सूर्यप्रकाश",
    "oxygen": "ऑक्सीजन",
    "turbidity": "गंदलापन",
    "transparency": "पारदर्शिता",
    "tundra": "टुंड्रा",
    "grasslands": "घास के मैदान",
    "deserts": "मरुस्थल",
    "mountains": "पर्वत",
    "savanna": "सवाना",
    "steppe": "स्टेपी",
    "resources": "संसाधन",
    "energy": "ऊर्जा",
    "pollution": "प्रदूषण",
    "algal": "शैवाल",
    "bloom": "प्रस्फुटन",
    "arsenic": "आर्सेनिक",
    "contamination": "प्रदूषण",
    "land": "भूमि",
    "degradation": "क्षरण",
    "causes": "कारण",
    "eutrophication": "यूट्रोफिकेशन",
    "geothermal": "भू-तापीय",
    "government": "सरकारी",
    "programmes": "कार्यक्रम",
    "groundwater": "भूजल",
    "harmful": "हानिकारक",
    "effects": "प्रभाव",
    "impact": "प्रभाव",
    "measurement": "मापन",
    "mercury": "पारा",
    "national": "राष्ट्रीय",
    "policy": "नीति",
    "biofuels": "जैव ईंधन",
    "new": "नवीन",
    "conversion": "रूपांतरण",
    "organic": "जैविक",
    "farming": "खेती",
    "stratification": "स्तरीकरण",
    "problems": "समस्याएं",
    "excessive": "अत्यधिक",
    "irrigation": "सिंचाई",
    "renewable": "नवीकरणीय",
    "development": "विकास",
    "characteristics": "विशेषताएं",
    "formation": "निर्माण",
    "process": "प्रक्रिया",
    "profiles": "संस्तर",
    "horizons": "क्षितिज",
    "solar": "सौर",
    "sources": "स्रोत",
    "strategies": "रणनीतियाँ",
    "reducing": "कम करना",
    "surface": "सतही",
    "sustainable": "टिकाऊ",
    "tidal": "ज्वारीय",
    "type": "प्रकार",
    "types": "प्रकार",
    "and": "और",
    "of": "का",
    "vs": "बनाम",
    "in": "में",
    "to": "को",
    "for": "के लिए",
    "with": "के साथ",
    "between": "के बीच"
}

def get_hindi_title(clean_title):
    words = clean_title.split()
    translated_words = []
    for w in words:
        w_clean = w.strip("()-,.vs")
        w_lower = w_clean.lower()
        matched = False
        for k, v in TRANVALATIONS.items() if 'TRANVALATIONS' in globals() else TRANSLATIONS.items():
            if k == w_lower:
                translated_words.append(v)
                matched = True
                break
        if not matched:
            translated_words.append(w)
    return ' '.join(translated_words)

def get_dynamic_branches_en(clean_title):
    t = clean_title
    return [
        {
            "label": f"Core Concept of {t}",
            "type": "branch",
            "date": "Overview",
            "children": [
                {"label": f"Definition: Understanding the fundamental characteristics, origin, and scope of {t}", "type": "leaf"},
                {"label": f"Scientific Framework: Analyzing how {t} interacts within resources, energy, and pollution systems", "type": "leaf"}
            ]
        },
        {
            "label": f"Processes & Dynamics",
            "type": "branch",
            "date": "Mechanisms",
            "children": [
                {"label": f"Primary Drivers: Factors regulating the rate, intensity, and progression of {t}", "type": "leaf"},
                {"label": f"Spatial Distribution: Exploring the global patterns and local variations of {t}", "type": "leaf"}
            ]
        },
        {
            "label": f"Ecological & Applied Values",
            "type": "branch",
            "date": "Applications",
            "children": [
                {"label": f"Impacts: How changes in {t} affect regional biodiversity, resources, and human activities", "type": "leaf"},
                {"label": f"Case Studies: Notable real-world occurrences and regional indicators relating to {t}", "type": "leaf"}
            ]
        },
        {
            "label": f"UPSC Exam Syllabus Relevance",
            "type": "branch",
            "date": "UPSC Core",
            "children": [
                {"label": f"Prelims Prep: Key factual exceptions, terms, and common traps associated with {t}", "type": "leaf"},
                {"label": f"Mains Answer Writing: Linking {t} with contemporary climate change policies and sustainable development goals", "type": "leaf"}
            ]
        }
    ]

def get_dynamic_branches_hi(clean_title_hi):
    t = clean_title_hi
    return [
        {
            "label": f"{t} की मूल अवधारणा",
            "type": "branch",
            "date": "अवधारणा",
            "children": [
                {"label": f"परिभाषा: {t} की बुनियादी विशेषताओं, उत्पत्ति और कार्यक्षेत्र को समझना", "type": "leaf"},
                {"label": f"वैज्ञानिक ढांचा: {t} पर्यावरण, संसाधन और ऊर्जा प्रणालियों के भीतर कैसे कार्य करता है", "type": "leaf"}
            ]
        },
        {
            "label": f"प्रक्रियाएं और गतिकी",
            "type": "branch",
            "date": "क्रियाविधि",
            "children": [
                {"label": f"प्राथमिक कारक: {t} की दर, तीव्रता और भौतिक प्रगति को नियंत्रित करने वाले तत्व", "type": "leaf"},
                {"label": f"स्थानिक वितरण: वैश्विक स्तर पर {t} के वितरण और क्षेत्रीय विविधताओं का अध्ययन", "type": "leaf"}
            ]
        },
        {
            "label": f"पारिस्थितिक और व्यावहारिक महत्व",
            "type": "branch",
            "date": "महत्व",
            "children": [
                {"label": f"प्रभाव: {t} में परिवर्तन क्षेत्रीय जैव विविधता, संसाधनों और मानवीय गतिविधियों को कैसे प्रभावित करते हैं", "type": "leaf"},
                {"label": f"क्षेत्रीय मामले: {t} से संबंधित उल्लेखनीय वैश्विक उदाहरण और संकेतक", "type": "leaf"}
            ]
        },
        {
            "label": f"यूपीएससी परीक्षा दृष्टिकोण (UPSC Focus)",
            "type": "branch",
            "date": "परीक्षा",
            "children": [
                {"label": f"प्रारंभिक परीक्षा: {t} से जुड़े महत्वपूर्ण तथ्य, शब्दावली और सामान्य परीक्षा भ्रम", "type": "leaf"},
                {"label": f"मुख्य परीक्षा उत्तर लेखन: {t} को समकालीन पर्यावरण नीतियों और हरित विकास लक्ष्यों से जोड़ना", "type": "leaf"}
            ]
        }
    ]

def get_custom_branches(folder_name, is_hindi):
    fl = folder_name.lower()
    
    # Check group mappings first to return extremely rich detailed data
    for g in GROUPS:
        for k in g["keys"]:
            if k in fl:
                return g["hi"] if is_hindi else g["en"]
            
    # Fallback to dynamic, non-overlapping generated branches using folder name
    clean_title = get_clean_title(folder_name)
    if is_hindi:
        hindi_title = get_hindi_title(clean_title)
        return get_dynamic_branches_hi(hindi_title)
    else:
        return get_dynamic_branches_en(clean_title)

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
    
    # Restructure branches dynamically to add more branches before leaves
    def restructure_node(node):
        # Create a deep copy manually by dict/list comprehension to avoid mutating original GROUPS
        res = {}
        for k, v in node.items():
            if k == "children":
                res["children"] = [restructure_node(c) for c in v]
            else:
                res[k] = v
        
        if res.get("type") == "leaf":
            label = res.get("label", "")
            if ":" in label:
                parts = label.split(":", 1)
                header = parts[0].strip()
                desc = parts[1].strip()
                if len(header) < 40 and not header.startswith("http") and not re.match(r'^\d+$', header):
                    sub_labels = [s.strip() for s in desc.split(";") if s.strip()]
                    sub_children = []
                    for sub in sub_labels:
                        if sub:
                            sub_cap = sub[0].upper() + sub[1:] if len(sub) > 1 else sub.upper()
                            sub_children.append({"label": sub_cap, "type": "leaf"})
                    return {
                        "label": header,
                        "type": "branch",
                        "children": sub_children
                    }
        return res

    branches = [restructure_node(b) for b in branches]
    
    # Capitalize lines appropriately in the label
    root_label = clean_title.replace(" Of ", " of ").replace(" And ", " and ").replace(" The ", " the ").replace(" In ", " in ").replace(" With ", " with ").replace(" To ", " to ").replace(" On ", " on ").replace(" By ", " by ")
    
    # Format multiline label for readability in the mindmap node
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
        # Fallback
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
    
    # Update navigation and language toggle to point to English version
    html = html.replace('<a href="hi/">Hindi Version</a>', '<a href="../">English Version</a>', 1)
    html = html.replace('<a href="hi/" class="mobile-lang-toggle"><i class="fas fa-globe"></i> हिन्दी</a>', 
                        '<a href="../" class="mobile-lang-toggle"><i class="fas fa-globe"></i> English</a>', 1)

    # Update canonical
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
                hindi_title = get_hindi_title(clean_title)
                try:
                    create_hi_stub(en_html_path, hi_html_path, folder_name, hindi_title)
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
