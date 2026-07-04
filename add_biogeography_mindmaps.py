#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import re
import json

BASE_DIR = r"upsc/geography/Biogeography"

def get_clean_title(folder_name):
    # Split camelCase words like SoilClassification to Soil Classification
    title = re.sub(r'([a-z])([A-Z])', r'\1 \2', folder_name)
    title = title.replace('-', ' ')
    words = []
    acronyms = {'dpsp', 'pri', 'ut', 'uts', 'sc', 'hc', 'cm', 'com', 'arc', 'inc', 'ias', 'sec', 'sfc', 'pej', 'tej', 'mjo', 'enso', 'iod', 'icar', 'gst', 'dpc', 'mpc', 'adc', 'tac', 'scs', 'pesa', 'icar', 'isfr', 'itcz', 'tej'}
    for w in title.split():
        if w.lower() in acronyms:
            words.append(w.upper())
        elif w.lower() in ['of', 'and', 'the', 'for', 'in', 'with', 'against', 'to', 'on', 'some', 'by', 'their']:
            words.append(w.lower())
        else:
            words.append(w.capitalize())
    return ' '.join(words)

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
    "wetlands": "आर्द्रभूमि",
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
        for k, v in TRANSLATIONS.items():
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
                {"label": f"Scientific Framework: Analyzing how {t} interacts within the earth and environmental systems", "type": "leaf"}
            ]
        },
        {
            "label": f"Processes & Dynamics",
            "type": "branch",
            "date": "Mechanisms",
            "children": [
                {"label": f"Primary Drivers: Factors regulating the rate, intensity, and physical progression of {t}", "type": "leaf"},
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
                {"label": f"वैज्ञानिक ढांचा: {t} पृथ्वी और पर्यावरण प्रणालियों के भीतर कैसे कार्य करता है", "type": "leaf"}
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
                {"label": f"मुख्य परीक्षा उत्तर लेखन: {t} को समकालीन जलवायु नीतियों और सतत विकास लक्ष्यों (SDGs) से जोड़ना", "type": "leaf"}
            ]
        }
    ]

def get_custom_branches(folder_name, is_hindi):
    fl = folder_name.lower()
    
    # 1. Afforestation, Reforestation, Deforestation & Monoculture
    if any(k in fl for k in ['forestation', 'deforestation', 'monoculture']):
        if is_hindi:
            return [
                {
                    "label": "वनोन्मूलन के कारण और प्रभाव (Deforestation)",
                    "type": "branch",
                    "date": "वनोन्मूलन",
                    "children": [
                        {"label": "कारण: कृषि विस्तार, व्यावसायिक लॉगिंग, बुनियादी ढांचा विकास और झूम खेती", "type": "leaf"},
                        {"label": "प्रभाव: जैव विविधता की हानि, जल चक्र में व्यवधान और मृदा अपरदन में वृद्धि", "type": "leaf"}
                    ]
                },
                {
                    "label": "वनरोपण और पुनर्वनीकरण",
                    "type": "branch",
                    "date": "वनरोपण",
                    "children": [
                        {"label": "वनरोपण (Afforestation): ऐसे क्षेत्र में नए वन लगाना जहाँ पहले वन नहीं थे", "type": "leaf"},
                        {"label": "पुनर्वनीकरण (Reforestation): काटे गए या नष्ट हुए वनों के स्थान पर पुनः वृक्षारोपण", "type": "leaf"}
                    ]
                },
                {
                    "label": "एकल-कृषि वृक्षारोपण के मुद्दे",
                    "type": "branch",
                    "date": "एकल-कृषि",
                    "children": [
                        {"label": "अवधारणा: केवल एक ही प्रजाति (जैसे नीलगिरी/यूकेलिप्टस, चीड़) का बड़े पैमाने पर रोपण", "type": "leaf"},
                        {"label": "नकारात्मक पक्ष: कम जैव विविधता, कीटों के प्रति उच्च संवेदनशीलता और भूजल स्तर में गिरावट", "type": "leaf"}
                    ]
                },
                {
                    "label": "यूपीएससी सरकारी योजनाएं (UPSC Focus)",
                    "type": "branch",
                    "date": "योजनाएं",
                    "children": [
                        {"label": "राष्ट्रीय हरित भारत मिशन (GIM): जलवायु परिवर्तन पर राष्ट्रीय कार्य योजना (NAPCC) का हिस्सा", "type": "leaf"},
                        {"label": "CAMPA अधिनियम (2016): प्रतिपूरक वनीकरण कोष; वन भूमि के गैर-वन उपयोग पर अनिवार्य भुगतान", "type": "leaf"}
                    ]
                }
            ]
        else:
            return [
                {
                    "label": "Deforestation Drivers & Impacts",
                    "type": "branch",
                    "date": "Deforestation",
                    "children": [
                        {"label": "Drivers: Agricultural expansion, logging, infrastructure projects, and forest fires", "type": "leaf"},
                        {"label": "Impacts: Biodiversity loss, carbon sink reduction, soil erosion, and disrupted micro-climates", "type": "leaf"}
                    ]
                },
                {
                    "label": "Afforestation & Reforestation",
                    "type": "branch",
                    "date": "Forestry",
                    "children": [
                        {"label": "Afforestation: Creating forests on land that has historically not been forested", "type": "leaf"},
                        {"label": "Reforestation: Re-establishing forest cover on denuded or degraded forest land", "type": "leaf"}
                    ]
                },
                {
                    "label": "Monoculture Plantation Issues",
                    "type": "branch",
                    "date": "Monoculture",
                    "children": [
                        {"label": "Concept: Planting a single crop/tree species (e.g. Eucalyptus, Teak, Pine) over a large area", "type": "leaf"},
                        {"label": "Drawbacks: High vulnerability to pests, low ecological biodiversity, and depletion of specific soil nutrients", "type": "leaf"}
                    ]
                },
                {
                    "label": "UPSC Core & India Schemes",
                    "type": "branch",
                    "date": "India Forestry",
                    "children": [
                        {"label": "Green India Mission: One of the 8 missions under NAPCC aiming to increase forest/tree cover", "type": "leaf"},
                        {"label": "CAMPA Act (2016): Compensatory Afforestation Fund Management and Planning Authority; utilizes funds collected for diverting forest lands", "type": "leaf"}
                    ]
                }
            ]

    # 2. Soil Formation, Profiles & Classification
    elif any(k in fl for k in ['formation', 'profile', 'classification', 'processes', 'stages', 'horizons']):
        if is_hindi:
            return [
                {
                    "label": "मृदा निर्माण के कारक (Jenny's Factors)",
                    "type": "branch",
                    "date": "कारक",
                    "children": [
                        {"label": "सक्रिय कारक: जलवायु (तापमान, वर्षा) और जैविक कारक (सूक्ष्मजीव, वनस्पति)", "type": "leaf"},
                        {"label": "निष्क्रिय कारक: पैतृक चट्टान (Parent rock), स्थलाकृति (ढाल), और समय (Time)", "type": "leaf"}
                    ]
                },
                {
                    "label": "मृदा निर्माण प्रक्रियाएं (Processes)",
                    "type": "branch",
                    "date": "प्रक्रियाएं",
                    "children": [
                        {"label": "निक्षालन (Eluviation): ऊपरी संस्तर (A) से पोषक तत्वों का नीचे जाना; संचय (Illuviation): संस्तर (B) में जमाव", "type": "leaf"},
                        {"label": "विशिष्ट प्रक्रियाएं: पोडज़ोलिसेशन (शीतोष्ण), लैटेराइटिकरण (उष्णकटिबंधीय), कैल्सीकरण (अर्ध-शुष्क)", "type": "leaf"}
                    ]
                },
                {
                    "label": "मृदा परिच्छेदिका (Profiles & Horizons)",
                    "type": "branch",
                    "date": "परिच्छेदिका",
                    "children": [
                        {"label": "O संस्तर: कार्बनिक पदार्थ परत; A संस्तर: ऊपरी उपजाऊ मिट्टी (ह्यूमस से भरपूर)", "type": "leaf"},
                        {"label": "E संस्तर (निक्षालित परत); B संस्तर (उपमृदा - संचित खनिज); C संस्तर: आंशिक रूप से अपक्षयित चट्टान; R: मूल ठोस चट्टान", "type": "leaf"}
                    ]
                },
                {
                    "label": "भारत की मृदा वर्गीकरण (UPSC Focus)",
                    "type": "branch",
                    "date": "भारत की मृदा",
                    "children": [
                        {"label": "ICAR वर्गीकरण (8 प्रमुख प्रकार): जलोढ़ (सबसे उपजाऊ), काली/रेगुर (कपास), लाल-पीली, लैटेराइट (लीचिंग), शुष्क/मरुस्थलीय", "type": "leaf"},
                        {"label": "USDA सॉइल टैक्सोनॉमी: इनसेप्टिसॉल्स (Inceptisols), एंटिसॉल्स (Entisols) भारत में सर्वाधिक विस्तृत हैं", "type": "leaf"}
                    ]
                }
            ]
        else:
            return [
                {
                    "label": "Jenny's Soil Forming Factors",
                    "type": "branch",
                    "date": "Factors",
                    "children": [
                        {"label": "Active Factors: Climate (moisture and temperature governing reactions) and Biosphere (organisms, humification)", "type": "leaf"},
                        {"label": "Passive Factors: Parent Material (determines texture/chemistry), Topography (slope and drainage), and Time", "type": "leaf"}
                    ]
                },
                {
                    "label": "Soil Genesis Processes",
                    "type": "branch",
                    "date": "Pedogenesis",
                    "children": [
                        {"label": "Translocation: Eluviation (leaching/downward movement from A horizon) and Illuviation (accumulation in B horizon)", "type": "leaf"},
                        {"label": "Specific Regimes: Laterization (silica leaching in hot humid tropics), Podzolization (acidic leaching in cool climates), Calcification", "type": "leaf"}
                    ]
                },
                {
                    "label": "Soil Profile & Horizons",
                    "type": "branch",
                    "date": "Profile",
                    "children": [
                        {"label": "O Horizon: Organic surface litter; A Horizon: Mineral topsoil rich in dark organic humus", "type": "leaf"},
                        {"label": "E Horizon: Zone of maximum eluviation; B Horizon: Subsoil zone of illuviation; C Horizon: Parent bedrock fragments; R: Bedrock", "type": "leaf"}
                    ]
                },
                {
                    "label": "ICAR Soil Classification (UPSC)",
                    "type": "branch",
                    "date": "India Soils",
                    "children": [
                        {"label": "Major Types: Alluvial (covers ~40% of India; Indo-Gangetic plains), Black/Regur (basaltic traps, cotton), Red & Yellow, Laterite (leached, cashew)", "type": "leaf"},
                        {"label": "USDA Soil Taxonomy in India: Inceptisols (largest share), followed by Entisols and Alfisols", "type": "leaf"}
                    ]
                }
            ]

    # 3. Soil Erosion & Conservation
    elif 'erosion' in fl:
        if is_hindi:
            return [
                {
                    "label": "मृदा अपरदन के प्रकार (Erosion)",
                    "type": "branch",
                    "date": "अपरदन",
                    "children": [
                        {"label": "जल अपरदन: बूंद अपरदन (Splash), परत अपरदन (Sheet - अदृश्य क्षति), क्षुद्रसरिता (Rill), और अवनालिका अपरदन (Gully)", "type": "leaf"},
                        {"label": "चंबल बीहड़ (Badlands): तीव्र अवनालिका अपरदन का उदाहरण; कृषि के लिए अनुपयुक्त खड्ड", "type": "leaf"}
                    ]
                },
                {
                    "label": "मृदा संरक्षण तकनीकें (Conservation)",
                    "type": "branch",
                    "date": "संरक्षण",
                    "children": [
                        {"label": "कृषि सम्बन्धी उपाय: समोच्च जुताई (Contour Ploughing), पट्टीदार खेती (Strip cropping), शस्यावर्तन (Crop rotation)", "type": "leaf"},
                        {"label": "यांत्रिक उपाय: सीढ़ीदार खेती (Terracing), समोच्च मेड़बन्दी (Bunding), और रक्षक मेखला (Shelterbelts - पवन रोधी)", "type": "leaf"}
                    ]
                },
                {
                    "label": "मृदा क्षरण के कारण",
                    "type": "branch",
                    "date": "क्षरण",
                    "children": [
                        {"label": "लवणीकरण (Salinization): अत्यधिक सिंचाई और खराब जल निकासी से नमक का ऊपर आना (जैसे पंजाब, हरियाणा)", "type": "leaf"},
                        {"label": "मरुस्थलीकरण: रासायनिक खादों का अत्यधिक उपयोग, अतिचारण और वनोन्मूलन", "type": "leaf"}
                    ]
                },
                {
                    "label": "यूपीएससी परीक्षा दृष्टिकोण (UPSC Focus)",
                    "type": "branch",
                    "date": "योजनाएं",
                    "children": [
                        {"label": "मृदा स्वास्थ्य कार्ड योजना (2015): सूक्ष्म पोषक तत्वों की जांच; संतुलित उर्वरक उपयोग को बढ़ावा", "type": "leaf"},
                        {"label": "संयुक्त राष्ट्र मरुस्थलीकरण रोकथाम अभिसमय (UNCCD): भारत का 2030 तक भूमि क्षरण तटस्थता (LDN) का लक्ष्य", "type": "leaf"}
                    ]
                }
            ]
        else:
            return [
                {
                    "label": "Water & Wind Erosion Styles",
                    "type": "branch",
                    "date": "Erosion Types",
                    "children": [
                        {"label": "Water Erosion Stages: Splash (impact) -> Sheet (uniform removal, most dangerous) -> Rill (small channels) -> Gully (deep ravines)", "type": "leaf"},
                        {"label": "Badland Topography: Deep gullies and ravines formed in semi-arid zones (e.g. Chambal valley, India)", "type": "leaf"}
                    ]
                },
                {
                    "label": "Soil Conservation Measures",
                    "type": "branch",
                    "date": "Conservation",
                    "children": [
                        {"label": "Agronomic Practices: Contour plowing, strip cropping, mulching (organic layer), and crop rotation with legumes", "type": "leaf"},
                        {"label": "Mechanical Methods: Terracing (steep slopes), contour bunding (water retention), and shelterbelts (windbreaks in dry areas)", "type": "leaf"}
                    ]
                },
                {
                    "label": "Soil Degradation Pressures",
                    "type": "branch",
                    "date": "Degradation",
                    "children": [
                        {"label": "Salinization: Capillary action brings salts to surface due to canal over-irrigation (e.g., Kallar/Usar soils of Punjab/UP)", "type": "leaf"},
                        {"label": "Desertification: Overgrazing, deforestation, and excessive chemical fertilizer application leading to barren soils", "type": "leaf"}
                    ]
                },
                {
                    "label": "UPSC & Policy Frameworks",
                    "type": "branch",
                    "date": "Soil Policies",
                    "children": [
                        {"label": "Soil Health Card Scheme (2015): Analyzes NPK and micronutrients to optimize fertilizer dosage and soil health", "type": "leaf"},
                        {"label": "UNCCD Target: India committed to achieving Land Degradation Neutrality (LDN) by restoring 26 million hectares by 2030", "type": "leaf"}
                    ]
                }
            ]

    # 4. Forests & Natural Vegetation
    elif any(k in fl for k in ['forest', 'vegetation', 'monoculture']):
        if is_hindi:
            return [
                {
                    "label": "प्राकृतिक वनस्पति के प्रकार",
                    "type": "branch",
                    "date": "प्रकार",
                    "children": [
                        {"label": "सदाबहार वन (Evergreen): भारी वर्षा (>250cm); बहुस्तरीय वितान; महोगनी, आबनूस", "type": "leaf"},
                        {"label": "पर्णपाती वन (Deciduous): मानसूनी वन; भारत में सर्वाधिक विस्तृत; साल, सागौन (Teak)", "type": "leaf"},
                        {"label": "कांटेदार वन (Thorn): शुष्क क्षेत्र (<75cm वर्षा); बबूल, खजूर, कैक्टस", "type": "leaf"},
                        {"label": "पर्वतीय और मैंग्रोव वन: पर्वतों पर ऊंचाई के साथ बदलाव; मैंग्रोव तटों पर (सुंदरबन - सुंदरी वृक्ष)", "type": "leaf"}
                    ]
                },
                {
                    "label": "वन पारिस्थितिकी और प्रबंधन",
                    "type": "branch",
                    "date": "पारिस्थितिकी",
                    "children": [
                        {"label": "कार्बन पृथक्करण (Carbon Sink): जलवायु परिवर्तन नियंत्रण; ऑक्सीजन उत्पादन; जलभृत पुनर्भरण", "type": "leaf"},
                        {"label": "खतरे: दावानल (Forest fires), झूम खेती, आक्रामक विदेशी प्रजातियाँ (जैसे लैंटाना कैमरा)", "type": "leaf"}
                    ]
                },
                {
                    "label": "वन संरक्षण नीतियां",
                    "type": "branch",
                    "date": "नीतियां",
                    "children": [
                        {"label": "राष्ट्रीय वन नीति (1988): भारत के कुल भौगोलिक क्षेत्र के 33% हिस्से पर वन आवरण का लक्ष्य", "type": "leaf"},
                        {"label": "वन संरक्षण संशोधन अधिनियम (2023): गैर-वन उपयोग नियंत्रण; सीमावर्ती क्षेत्रों में बुनियादी ढांचे को छूट", "type": "leaf"}
                    ]
                },
                {
                    "label": "यूपीएससी वन रिपोर्ट (UPSC Focus)",
                    "type": "branch",
                    "date": "ISFR रिपोर्ट",
                    "children": [
                        {"label": "ISFR (द्विवार्षिक रिपोर्ट): भारतीय वन सर्वेक्षण (FSI) द्वारा; भारत में वन और वृक्ष आवरण ~24.62% है", "type": "leaf"},
                        {"label": "वन अधिकार अधिनियम (FRA 2006): अनुसूचित जनजातियों और पारंपरिक वन निवासियों को भूमि अधिकार", "type": "leaf"}
                    ]
                }
            ]
        else:
            return [
                {
                    "label": "Natural Vegetation Types",
                    "type": "branch",
                    "date": "Forest Types",
                    "children": [
                        {"label": "Tropical Wet Evergreen: Rainfall > 250cm; multi-layered canopy; Mahogany, Ebony, Rosewood", "type": "leaf"},
                        {"label": "Tropical Deciduous (Monsoon): Most widespread in India; Teak, Sal, Sandalwood; shed leaves in dry season", "type": "leaf"},
                        {"label": "Montane & Mangroves: Altitudinal zonation (Himalayas); halophytic swamp forests (Sundarbans - pneumatophores)", "type": "leaf"}
                    ]
                },
                {
                    "label": "Ecological Functions & Threats",
                    "type": "branch",
                    "date": "Forest Ecology",
                    "children": [
                        {"label": "Climate Regulation: Carbon sequestration; moisture feedback; prevention of surface soil wash", "type": "leaf"},
                        {"label": "Forest Fires & Invasive Species: Major hazards; Shifting Cultivation (Jhum) causes canopy loss; Lantana infestation", "type": "leaf"}
                    ]
                },
                {
                    "label": "Conservation Laws",
                    "type": "branch",
                    "date": "Forest Laws",
                    "children": [
                        {"label": "Forest Conservation Act 1980 (Amended 2023): Restricts diversion of forest land for non-forest purposes", "type": "leaf"},
                        {"label": "National Forest Policy 1988: Set national goal of maintaining minimum 33% of land area under forest cover", "type": "leaf"}
                    ]
                },
                {
                    "label": "UPSC India Forestry Focus",
                    "type": "branch",
                    "date": "FSI & FRA",
                    "children": [
                        {"label": "ISFR Report: Biennial forest survey by FSI; current India forest/tree cover stands at ~24.62% of geographic area", "type": "leaf"},
                        {"label": "Forest Rights Act (FRA 2006): Empowers forest-dwelling Scheduled Tribes and other traditional forest dwellers (OTFD)", "type": "leaf"}
                    ]
                }
            ]

    # Fallback / Default
    else:
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
