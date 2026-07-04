#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import re
import json

BASE_DIR = r"upsc/geography/Climatology"

def get_clean_title(folder_name):
    # Split camelCase words like KoppensClassification to Koppens Classification
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
    
    # 1. Atmosphere Composition & Structure
    if any(k in fl for k in ['composition', 'structure', 'dust', 'gases', 'water-vapour', 'troposphere', 'stratosphere', 'mesosphere', 'thermosphere', 'exosphere']):
        if is_hindi:
            return [
                {
                    "label": "वायुमंडल की परतें (Structure)",
                    "type": "branch",
                    "date": "संरचना",
                    "children": [
                        {"label": "क्षोभमंडल (Troposphere): सबसे निचली परत, मौसम की सभी घटनाएं यहीं; ऊंचाई के साथ तापमान गिरता है (Lapse Rate)", "type": "leaf"},
                        {"label": "समतापमंडल (Stratosphere): ओजोन परत; हवाई जहाजों के लिए आदर्श; ऊंचाई के साथ तापमान बढ़ता है", "type": "leaf"},
                        {"label": "मध्यमंडल (Mesosphere): सबसे ठंडी परत; उल्कापिंड इसी परत में जलते हैं", "type": "leaf"},
                        {"label": "तापमंडल/आयनमंडल (Thermosphere): रेडियो तरंग परावर्तन; ध्रुवीय ज्योति (Auroras) का निर्माण", "type": "leaf"}
                    ]
                },
                {
                    "label": "वायुमंडल का संघटन (Composition)",
                    "type": "branch",
                    "date": "संघटन",
                    "children": [
                        {"label": "स्थायी गैसें: नाइट्रोजन (78%), ऑक्सीजन (21%), आर्गन (0.93%), कार्बन डाइऑक्साइड (0.04%)", "type": "leaf"},
                        {"label": "परिवर्तनशील तत्व: जलवाष्प (ध्रुवों पर 1% से विषुवत रेखा पर 4%), धूल कण (संघनन केंद्र)", "type": "leaf"}
                    ]
                },
                {
                    "label": "भौतिक लक्षण (Physical)",
                    "type": "branch",
                    "date": "लक्षण",
                    "children": [
                        {"label": "गुरुत्वाकर्षण प्रभाव: वायुमंडल के कुल द्रव्यमान का 99% केवल 32 किमी की ऊंचाई तक सीमित है", "type": "leaf"},
                        {"label": "दाब में गिरावट: ऊंचाई बढ़ने पर वायुदाब तेजी से घटता है", "type": "leaf"}
                    ]
                },
                {
                    "label": "यूपीएससी परीक्षा दृष्टिकोण (UPSC Focus)",
                    "type": "branch",
                    "date": "परीक्षा",
                    "children": [
                        {"label": "ओजोन रिक्तीकरण: समताप मंडल में क्लोरोफ्लोरोकार्बन (CFC) के प्रभाव और मॉन्ट्रियल प्रोटोकॉल नीतियां", "type": "leaf"},
                        {"label": "हरितगृह प्रभाव (Greenhouse Effect): जलवाष्प सबसे बड़ा योगदानकर्ता है, इसके बाद CO2 और मीथेन का स्थान है", "type": "leaf"}
                    ]
                }
            ]
        else:
            return [
                {
                    "label": "Atmospheric Stratification",
                    "type": "branch",
                    "date": "Structure",
                    "children": [
                        {"label": "Troposphere: Lowest layer; contains 75% of mass; all weather events occur here; temperature drops with height (normal lapse rate)", "type": "leaf"},
                        {"label": "Stratosphere: Holds Ozone Layer ($O_3$); free from clouds and dust; ideal for jet aircraft; temp rises with height", "type": "leaf"},
                        {"label": "Mesosphere: Coldest layer of atmosphere (down to $-90^\\circ\\text{C}$); where meteors burn up upon entry", "type": "leaf"},
                        {"label": "Ionosphere & Exosphere: Ionized molecules reflect radio waves back to Earth; site of Auroras", "type": "leaf"}
                    ]
                },
                {
                    "label": "Atmospheric Composition",
                    "type": "branch",
                    "date": "Composition",
                    "children": [
                        {"label": "Permanent Gases: Nitrogen (78.08%), Oxygen (20.95%), Argon (0.93%), and Carbon Dioxide (currently ~0.04%)", "type": "leaf"},
                        {"label": "Variable Components: Water vapor (0-4% depending on humidity); dust particles (act as hygroscopic condensation nuclei)", "type": "leaf"}
                    ]
                },
                {
                    "label": "Mass & Pressure Dynamics",
                    "type": "branch",
                    "date": "Physics",
                    "children": [
                        {"label": "Gravity Boundary: 99% of total atmospheric mass is concentrated within 32 km from Earth's surface", "type": "leaf"},
                        {"label": "Vertical Profile: Atmospheric pressure and density decrease exponentially with increasing altitude", "type": "leaf"}
                    ]
                },
                {
                    "label": "UPSC Core Relevance",
                    "type": "branch",
                    "date": "Global Issues",
                    "children": [
                        {"label": "Stratospheric Ozone: Montreal Protocol updates; role of Polar Stratospheric Clouds (PSCs) in ozone hole formation", "type": "leaf"},
                        {"label": "Greenhouse Effect: Major contributors (water vapor is primary absorber, followed by carbon dioxide, methane, and ozone)", "type": "leaf"}
                    ]
                }
            ]

    # 2. Insolation, Heat Budget & Temperature
    elif any(k in fl for k in ['insolation', 'radiation', 'heat-budget', 'heating', 'conduction', 'altitude-vs-temperature', 'inversion']):
        if is_hindi:
            return [
                {
                    "label": "सूर्यातप और हीटिंग तंत्र",
                    "type": "branch",
                    "date": "सूर्यातप",
                    "children": [
                        {"label": "सूर्यातप (Insolation): पृथ्वी को प्राप्त होने वाली सौर ऊर्जा; कोण, दिन की अवधि और वायुमंडल से प्रभावित", "type": "leaf"},
                        {"label": "गर्म होने की प्रक्रियाएं: चालन (Conduction - संपर्क), संवहन (Convection - लंबवत), अभिवहन (Advection - क्षैतिज)", "type": "leaf"}
                    ]
                },
                {
                    "label": "पृथ्वी का ऊष्मा बजट (Heat Budget)",
                    "type": "branch",
                    "date": "ऊष्मा बजट",
                    "children": [
                        {"label": "एल्बीडो (Albedo): सौर विकिरण का 35% भाग पृथ्वी पर बिना अवशोषित हुए अंतरिक्ष में परावर्तित हो जाता है", "type": "leaf"},
                        {"label": "संतुलन: पृथ्वी और वायुमंडल पार्थिव विकिरण (Terrestrial Radiation) द्वारा 65 इकाइयों को वापस भेजते हैं", "type": "leaf"}
                    ]
                },
                {
                    "label": "तापमान का व्युत्क्रमण (Inversion)",
                    "type": "branch",
                    "date": "व्युत्क्रमण",
                    "children": [
                        {"label": "अवधारणा: ऊंचाई के साथ सामान्य ह्रास दर (Lapse Rate) के विपरीत तापमान का बढ़ना", "type": "leaf"},
                        {"label": "आवश्यक दशाएं: लंबी ठंडी रातें, साफ आकाश, शांत हवा; घाटी में ठंडी हवा का नीचे बैठना", "type": "leaf"}
                    ]
                },
                {
                    "label": "यूपीएससी अनुप्रयोग (UPSC Focus)",
                    "type": "branch",
                    "date": "परीक्षा",
                    "children": [
                        {"label": "एल्बीडो मान: ताजे बर्फ का एल्बीडो सर्वाधिक (80-90%) होता है, वनों और महासागरों का सबसे कम", "type": "leaf"},
                        {"label": "व्युत्क्रमण प्रभाव: शहरों में प्रदूषकों का फंसना (Smog), और कृषि में पाले (Frost) से फसलों की क्षति", "type": "leaf"}
                    ]
                }
            ]
        else:
            return [
                {
                    "label": "Insolation & Heat Transfer",
                    "type": "branch",
                    "date": "Insolation",
                    "children": [
                        {"label": "Factors: Solar elevation angle, day length, distance from sun (Aphelion/Perihelion), and atmospheric transparency", "type": "leaf"},
                        {"label": "Mechanisms: Conduction (molecular contact), Convection (vertical mass flow), Advection (horizontal wind flow)", "type": "leaf"}
                    ]
                },
                {
                    "label": "Planetary Heat Budget",
                    "type": "branch",
                    "date": "Heat Budget",
                    "children": [
                        {"label": "Albedo of Earth: ~35% of incoming solar radiation is reflected back without heating (highest for fresh snow, lowest for oceans)", "type": "leaf"},
                        {"label": "Radiation Balance: Net gain of 65 units is balanced by outgoing longwave Terrestrial Radiation from Earth & atmosphere", "type": "leaf"}
                    ]
                },
                {
                    "label": "Temperature Inversion",
                    "type": "branch",
                    "date": "Inversion",
                    "children": [
                        {"label": "Concept: Reversal of normal lapse rate; temperature increases with altitude in a stable air column", "type": "leaf"},
                        {"label": "Ideal Conditions: Long winter nights, clear cloudless skies, dry calm air, and valley basins (cold air drainage)", "type": "leaf"}
                    ]
                },
                {
                    "label": "UPSC Core & Application",
                    "type": "branch",
                    "date": "Environmental",
                    "children": [
                        {"label": "Urban Heat Islands: Higher heat retention in concrete cities vs rural surroundings due to low albedo", "type": "leaf"},
                        {"label": "Pollution Trap: Inversion layer acts as lid, trapping particulate matter and gases (causing heavy winter Smog in Delhi)", "type": "leaf"}
                    ]
                }
            ]

    # 3. Pressure Belts & Winds
    elif any(k in fl for k in ['pressure', 'wind', 'circulation', 'coriolis', 'frictional', 'planetary-winds', 'gradient-force']):
        if is_hindi:
            return [
                {
                    "label": "वायुदाब पेटियां (Pressure Belts)",
                    "type": "branch",
                    "date": "पेटियां",
                    "children": [
                        {"label": "तापजन्य पेटियां: भूमध्यरेखीय निम्न दाब (Doldrums), ध्रुवीय उच्च दाब", "type": "leaf"},
                        {"label": "गतिकजन्य पेटियां: उपोष्णकटिबंधीय उच्च दाब (Horse Latitudes - हवा का बैठना), उपध्रुवीय निम्न दाब", "type": "leaf"}
                    ]
                },
                {
                    "label": "पवन को प्रभावित करने वाले बल",
                    "type": "branch",
                    "date": "बल",
                    "children": [
                        {"label": "दाब प्रवणता बल (PGF): उच्च से निम्न दाब की ओर; हवा की गति निर्धारित करता है", "type": "leaf"},
                        {"label": "कोरिओलिस बल: पृथ्वी के घूर्णन के कारण विक्षेपण बल; उत्तरी गोलार्ध में दाईं ओर, दक्षिणी गोलार्ध में बाईं ओर", "type": "leaf"},
                        {"label": "घर्षण बल: धरातल के पास हवा की गति को धीमा करता है और कोरिओलिस विक्षेपण को कम करता है", "type": "leaf"}
                    ]
                },
                {
                    "label": "भूमंडलीय और स्थानीय पवनें",
                    "type": "branch",
                    "date": "पवन प्रकार",
                    "children": [
                        {"label": "भूमंडलीय पवनें (Planetary): व्यापारिक पवनें (Trade), पछुआ पवनें (Westerlies), ध्रुवीय पूर्वी पवनें", "type": "leaf"},
                        {"label": "स्थानीय पवनें: चिनूक और फाह्न (गर्म शुष्क ढाल ढलान), लू (उत्तर भारत की ग्रीष्मकालीन)", "type": "leaf"}
                    ]
                },
                {
                    "label": "यूपीएससी परीक्षा दृष्टिकोण (UPSC Focus)",
                    "type": "branch",
                    "date": "परिसंचरण",
                    "children": [
                        {"label": "त्रिकोशीय देशांतरीय परिसंचरण: हैडली (Hadley), फेरेल (Ferrel) और ध्रुवीय (Polar) कोशिकाएं", "type": "leaf"},
                        {"label": "भू-विक्षेपी पवन (Geostrophic Wind): जब कोरिओलिस बल दाब प्रवणता बल को संतुलित करता है, हवा समदाब रेखाओं के समानांतर बहती है", "type": "leaf"}
                    ]
                }
            ]
        else:
            return [
                {
                    "label": "Global Pressure Belts",
                    "type": "branch",
                    "date": "Belts",
                    "children": [
                        {"label": "Thermal Belts: Equatorial Low (Doldrums - rising warm air) and Polar Highs (subsiding cold air)", "type": "leaf"},
                        {"label": "Dynamic Belts: Subtropical Highs (Horse Latitudes - air sinking) and Subpolar Lows (frontogenesis zones)", "type": "leaf"}
                    ]
                },
                {
                    "label": "Forces Affecting Winds",
                    "type": "branch",
                    "date": "Wind Forces",
                    "children": [
                        {"label": "Pressure Gradient Force: Drives wind from high to low pressure; perpendicular to isobars", "type": "leaf"},
                        {"label": "Coriolis Force: Apparent deflection due to Earth's rotation (deflects right in NH, left in SH; zero at equator, max at poles)", "type": "leaf"},
                        {"label": "Frictional Force: Surface drag that reduces wind speed up to 1-2 km altitude, altering Coriolis deflection angle", "type": "leaf"}
                    ]
                },
                {
                    "label": "Wind Classifications",
                    "type": "branch",
                    "date": "Winds",
                    "children": [
                        {"label": "Planetary: Trade Winds (Hadley cell), Westerlies (Ferrel cell), Polar Easterlies (Polar cell)", "type": "leaf"},
                        {"label": "Seasonal & Local: Monsoons (reversing winds); Chinook/Fohn (snow-eater, dry mountain downslope), Mistral (cold), Loo", "type": "leaf"}
                    ]
                },
                {
                    "label": "UPSC Core Concepts",
                    "type": "branch",
                    "date": "Geostrophic",
                    "children": [
                        {"label": "Geostrophic Wind: Blows parallel to straight isobars when PGF and Coriolis Force are equal and opposite (above friction layer)", "type": "leaf"},
                        {"label": "Walker Circulation: Zonal atmospheric cell across equatorial Pacific; links to ENSO sea-surface anomalies", "type": "leaf"}
                    ]
                }
            ]

    # 4. Air Masses, Fronts, Cyclones & Jet Streams
    elif any(k in fl for k in ['mass', 'front', 'cyclone', 'jet-stream', 'thunderstorm', 'tornado']):
        if is_hindi:
            return [
                {
                    "label": "वायु राशियां और वाताग्र (Fronts)",
                    "type": "branch",
                    "date": "वाताग्र",
                    "children": [
                        {"label": "वायु राशि: तापमान और आर्द्रता के समान लक्षणों वाला विशाल हवा का पिंड (ध्रुवीय/उष्णकटिबंधीय)", "type": "leaf"},
                        {"label": "वाताग्र: दो विपरीत वायु राशियों की सीमा; उष्ण वाताग्र, शीत वाताग्र, अचर (Stationary) वाताग्र", "type": "leaf"}
                    ]
                },
                {
                    "label": "शीतोष्ण चक्रवात (Temperate)",
                    "type": "branch",
                    "date": "शीतोष्ण चक्रवात",
                    "children": [
                        {"label": "उत्पत्ति: वाताग्र जनन (Frontogenesis) द्वारा; मध्य और उच्च अक्षांशों (35°-65°) पर", "type": "leaf"},
                        {"label": "लक्षण: विस्तृत क्षेत्र, मंद वर्षा, पश्चिम से पूर्व की ओर गति (पछुआ पवन द्वारा निर्देशित)", "type": "leaf"}
                    ]
                },
                {
                    "label": "उष्णकटिबंधीय चक्रवात (Tropical)",
                    "type": "branch",
                    "date": "उष्णकटिबंधीय",
                    "children": [
                        {"label": "आवश्यक दशाएं: गर्म महासागरीय सतह (>27°C), कोरिओलिस बल की उपस्थिति (भूमध्य रेखा पर नहीं), ऊर्ध्वाधर पवन गति में कम बदलाव", "type": "leaf"},
                        {"label": "संरचना: चक्रवात की आंख (Eye - शांत और साफ आकाश), फेनिल (Explosive wall)", "type": "leaf"}
                    ]
                },
                {
                    "label": "जेट स्ट्रीम और आपदा प्रबंधन",
                    "type": "branch",
                    "date": "जेट स्ट्रीम",
                    "children": [
                        {"label": "जेट स्ट्रीम: ऊपरी क्षोभमंडल में तीव्र गति वाली संकीर्ण हवा की पट्टी (Rossby Waves)", "type": "leaf"},
                        {"label": "भारतीय मानसून: उपोष्णकटिबंधीय पश्चिमी जेट का पीछे हटना और पूर्वी जेट का आना मानसून की शुरुआत का कारण", "type": "leaf"}
                    ]
                }
            ]
        else:
            return [
                {
                    "label": "Air Masses & Fronts",
                    "type": "branch",
                    "date": "Frontogenesis",
                    "children": [
                        {"label": "Air Mass: Extensive body of air with uniform temperature & humidity; classified by source region (mT, mP, cT, cP)", "type": "leaf"},
                        {"label": "Fronts: Boundaries separating contrasting air masses; Warm front (gentle slope), Cold front (steep slope, convective rain), Occluded front", "type": "leaf"}
                    ]
                },
                {
                    "label": "Temperate (Extra-Tropical) Cyclones",
                    "type": "branch",
                    "date": "Mid-Latitude",
                    "children": [
                        {"label": "Origin: Frontal origin; dynamic collision of polar and tropical air masses; lifecycle has wave, mature, and occluded stages", "type": "leaf"},
                        {"label": "Movement: Travel from West to East guided by Westerlies; covers large area; brings gradual, long-lasting rainfall", "type": "leaf"}
                    ]
                },
                {
                    "label": "Tropical Cyclones",
                    "type": "branch",
                    "date": "Tropical Storms",
                    "children": [
                        {"label": "Pre-requisites: Sea surface temp > $27^\\circ\\text{C}$, presence of Coriolis Force (absent $0-5^\\circ$ latitude), high moisture, low vertical wind shear", "type": "leaf"},
                        {"label": "Structure: Eye (low pressure center, sinking air, cloudless), Eyewall (maximum winds and torrential cumulonimbus rains)", "type": "leaf"}
                    ]
                },
                {
                    "label": "Jet Streams & Disaster Focus",
                    "type": "branch",
                    "date": "Jet Streams",
                    "children": [
                        {"label": "Jet Streams: High-altitude ($9-12$ km) fast geostrophic winds; Rossby waves; Polar front jet and Subtropical westerly jet", "type": "leaf"},
                        {"label": "Indian Monsoon Link: Subtropical Westerly Jet must retreat north of Himalayas to allow Tropical Easterly Jet (TEJ) to burst the monsoon", "type": "leaf"},
                        {"label": "Disaster Management: NDMA cyclone guidelines; early warning systems, coastal shelterbelts, and storm surge zonation", "type": "leaf"}
                    ]
                }
            ]

    # 5. Clouds & Precipitation
    elif any(k in fl for k in ['clouds', 'precipitation', 'rainfall', 'water-v-pre', 'water-in-the-atmosphere']):
        if is_hindi:
            return [
                {
                    "label": "आर्द्रता और संघनन",
                    "type": "branch",
                    "date": "आर्द्रता",
                    "children": [
                        {"label": "सापेक्ष आर्द्रता (RH): वायु में उपस्थित जलवाष्प और उसकी क्षमता का अनुपात; ओस बिंदु (Dew Point) पर RH = 100%", "type": "leaf"},
                        {"label": "संघनन रूप: ओस, पाला, कोहरा, कुहासा (Mist) और बादल", "type": "leaf"}
                    ]
                },
                {
                    "label": "बादलों का वर्गीकरण",
                    "type": "branch",
                    "date": "बादल",
                    "children": [
                        {"label": "उच्च बादल (6-12 किमी): पक्षाभ (Cirrus - रेशमी), पक्षाभ स्तरी (ओजोन प्रभामंडल)", "type": "leaf"},
                        {"label": "मध्य व निम्न बादल: कपासी (Cumulus - रुई जैसे), कपासी वर्षी (Cumulonimbus - अत्यधिक ऊर्ध्वाधर विकास, मूसलाधार वर्षा)", "type": "leaf"}
                    ]
                },
                {
                    "label": "वर्षा के प्रकार (Precipitation)",
                    "type": "branch",
                    "date": "वर्षा",
                    "children": [
                        {"label": "संवहनीय वर्षा: गर्म धरातल के कारण हवा का उठना; विषुवत रेखा पर दोपहर 4 बजे की वर्षा", "type": "leaf"},
                        {"label": "पर्वतीय वर्षा: नमीयुक्त हवा का पर्वत ढाल से टकराकर उठना; पवनविमुख ढाल वृष्टि-छाया (Rain-shadow) क्षेत्र बनता है", "type": "leaf"}
                    ]
                },
                {
                    "label": "यूपीएससी आधुनिक आयाम (UPSC Focus)",
                    "type": "branch",
                    "date": "प्रौद्योगिकी",
                    "children": [
                        {"label": "कृत्रिम वर्षा: बादलों में सिल्वर आयोडाइड या शुष्क बर्फ (ठोस CO2) का छिड़काव (Cloud Seeding) करना", "type": "leaf"},
                        {"label": "बादल फटना (Cloudburst): सीमित क्षेत्र में लघु अवधि (जैसे 100mm/घंटा) में होने वाली भीषण वर्षा; पहाड़ी क्षेत्रों में फ्लैश फ्लड का कारण", "type": "leaf"}
                    ]
                }
            ]
        else:
            return [
                {
                    "label": "Humidity Concepts",
                    "type": "branch",
                    "date": "Humidity",
                    "children": [
                        {"label": "Relative Humidity (RH): Ratio of actual water vapor to maximum holding capacity; reaches 100% at Dew Point (saturation)", "type": "leaf"},
                        {"label": "Condensation Forms: Dew, frost, fog (surface air suspension), mist, and clouds (high altitude)", "type": "leaf"}
                    ]
                },
                {
                    "label": "Cloud Classification",
                    "type": "branch",
                    "date": "Clouds",
                    "children": [
                        {"label": "High Clouds ($6-12$ km): Cirrus (feathery ice crystals), Cirrostratus (creates halo around Sun)", "type": "leaf"},
                        {"label": "Low & Vertical Clouds: Stratus (layered, gray), Cumulus (flat base, cauliflower shape), Cumulonimbus (towering vertical storm clouds)", "type": "leaf"}
                    ]
                },
                {
                    "label": "Precipitation Mechanisms",
                    "type": "branch",
                    "date": "Rain Types",
                    "children": [
                        {"label": "Convective: Heated air expands and rises; typical equatorial afternoon showers with thunder", "type": "leaf"},
                        {"label": "Orographic: Warm moist air forced up mountain slopes; windward side gets heavy rain; leeward becomes dry Rain-shadow", "type": "leaf"},
                        {"label": "Cyclonic/Frontal: Warm air lifted over cold dense air mass at frontal boundary", "type": "leaf"}
                    ]
                },
                {
                    "label": "UPSC Tech & Environment",
                    "type": "branch",
                    "date": "Cloud Seeding",
                    "children": [
                        {"label": "Cloud Seeding: Dispersal of Silver Iodide ($AgI$), Potassium Iodide, or Dry Ice to induce precipitation in dry areas", "type": "leaf"},
                        {"label": "Cloudburst: Sudden intense rainfall exceeding 100mm/hour in a small area; common in Himalayas, causing devastating flash floods", "type": "leaf"}
                    ]
                }
            ]

    # 6. Climates & Koppen's Classification
    elif any(k in fl for k in ['koppen', 'monsoon', 'climate', 'steppe', 'mediterranean', 'savanna', 'equatorial', 'siberian', 'laurentian', 'western-margin', 'eastern-margin', 'desert', 'arctic', 'steppe', 'china-type', 'british-type']):
        if is_hindi:
            return [
                {
                    "label": "कोपेन का जलवायु वर्गीकरण",
                    "type": "branch",
                    "date": "वर्गीकरण",
                    "children": [
                        {"label": "आधार: औसत तापमान, वर्षा और वनस्पति सीमाएं; A (उष्णकटिबंधीय), B (शुष्क), C (मध्य-अक्षांश), D (शीतोष्ण), E (ध्रुवीय)", "type": "leaf"},
                        {"label": "भारत में कोपेन योजना: Cwg (गंगा का मैदान), Amw (पश्चिमी तट मानसून), As (कोरोमंडल तट - शीतकालीन वर्षा)", "type": "leaf"}
                    ]
                },
                {
                    "label": "उष्णकटिबंधीय जलवायु प्रकार",
                    "type": "branch",
                    "date": "उष्णकटिबंधीय",
                    "children": [
                        {"label": "भूमध्यरेखीय (Af): साल भर गर्मी और वर्षा; घने सदाबहार वन (सेल्वास); महोगनी, आबनूस", "type": "leaf"},
                        {"label": "सवाना/सूडान (Aw): स्पष्ट शुष्क और गीला मौसम; लंबी हाथी घास; 'विश्व का चिड़ियाघर'", "type": "leaf"},
                        {"label": "उष्णकटिबंधीय मानसून (Am): मौसमी हवाओं का उलटना; पर्णपाती वन (टीक, साल)", "type": "leaf"}
                    ]
                },
                {
                    "label": "शीतोष्ण और शुष्क जलवायु प्रकार",
                    "type": "branch",
                    "date": "शीतोष्ण",
                    "children": [
                        {"label": "भूमध्यसागरीय (Cs): ग्रीष्मकाल शुष्क, शीतकाल वर्षा (पछुआ पवन द्वारा); खट्टे फलों (Citrus) की कृषि", "type": "leaf"},
                        {"label": "स्टेपी (Bs): अर्ध-शुष्क घास के मैदान; अनाज उत्पादन (गेहूं की टोकरी); चरवाहे", "type": "leaf"},
                        {"label": "साइबेरियन (Df): कोणधारी वन (Taiga); चीड़, देवदार; अत्यंत ठंडी सर्दियाँ", "type": "leaf"}
                    ]
                },
                {
                    "label": "यूपीएससी मानसून सिद्धांत (UPSC Focus)",
                    "type": "branch",
                    "date": "मानसून सिद्धांत",
                    "children": [
                        {"label": "मानसून गतिक सिद्धांत (Flohn): आईटीसीजेड (ITCZ) के ग्रीष्मकालीन विस्थापन के कारण व्यापारिक पवनों का विक्षेपण", "type": "leaf"},
                        {"label": "तिब्बती पठार का प्रभाव: ग्रीष्मकालीन तीव्र तापीय तापन जो उप-ध्रुवीय जेट को उत्तर में धकेलता है और पूर्वी जेट को जन्म देता है", "type": "leaf"}
                    ]
                }
            ]
        else:
            return [
                {
                    "label": "Koppen's Classification",
                    "type": "branch",
                    "date": "Koppen System",
                    "children": [
                        {"label": "Methodology: Based on monthly temperature, precipitation, and vegetation limits; uses letter codes (A, B, C, D, E)", "type": "leaf"},
                        {"label": "India Application: Cwg (Indo-Gangetic plains), Amw (Western Ghats monsoon), As (Coromandel coast winter rain)", "type": "leaf"}
                    ]
                },
                {
                    "label": "Tropical Climatic Zones",
                    "type": "branch",
                    "date": "Tropical",
                    "children": [
                        {"label": "Equatorial (Af): No seasonality; daily convectional rainfall; dense evergreen rainforests (Selvas)", "type": "leaf"},
                        {"label": "Monsoon (Am): Seasonal reversal of winds; deciduous forests (Sal, Teak) shedding leaves in dry season", "type": "leaf"},
                        {"label": "Savanna (Aw): Alternating wet and dry seasons; coarse elephant grass; 'Big Game Country'", "type": "leaf"}
                    ]
                },
                {
                    "label": "Temperate & Arid Zones",
                    "type": "branch",
                    "date": "Temperate",
                    "children": [
                        {"label": "Mediterranean (Cs): Mild wet winters (Westerlies) and hot dry summers (trade winds offshore); citrus fruit viticulture", "type": "leaf"},
                        {"label": "Steppe (Bs): Semi-arid grasslands; wheat granaries of the world; pastoral nomadism", "type": "leaf"},
                        {"label": "Siberian (Df) & Laurentian: Coniferous needleleaf Taiga forests (Pine, Spruce, Fir); logging industries", "type": "leaf"}
                    ]
                },
                {
                    "label": "UPSC Monsoon Dynamics",
                    "type": "branch",
                    "date": "Monsoon Theory",
                    "children": [
                        {"label": "Dynamic Theory: Flohn's concept of ITCZ migration shifting Southeast Trades across equator to deflect as SW Monsoon", "type": "leaf"},
                        {"label": "Tibetan Plateau Heating: High-level anticyclone over Tibet strengthens Tropical Easterly Jet (TEJ), pulling SW Monsoon wind", "type": "leaf"}
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
