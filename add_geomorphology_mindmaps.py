#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import re
import json

BASE_DIR = r"upsc/geography/Geomorphology"

def get_clean_title(folder_name):
    # Split camelCase words like CharacteristicsCrystal to Characteristics Crystal
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
    
    # 1. Continental Drift & Pre-Plate Tectonics Theories
    if any(k in fl for k in ['drift', 'suess', 'post-drift', 'sea-floor', 'convectional-current', 'ocean-floor', 'theories-distribution', 'theories-suess']):
        if is_hindi:
            return [
                {
                    "label": "वेगनर का सिद्धांत (1912)",
                    "type": "branch",
                    "date": "अवधारणा",
                    "children": [
                        {"label": "पैंजिया (Pangea): विशाल महाद्वीप जो पैंथालसा (Panthalassa) महासागर से घिरा था", "type": "leaf"},
                        {"label": "विभाजन: लगभग 200 मिलियन वर्ष पहले (मेसोजोइक युग) अंगारालैंड और गोंडवानालैंड में विभाजन हुआ", "type": "leaf"}
                    ]
                },
                {
                    "label": "प्रमुख साक्ष्य (Evidences)",
                    "type": "branch",
                    "date": "साक्ष्य",
                    "children": [
                        {"label": "जिग-सॉ फिट (Jigsaw Fit): दक्षिण अमेरिका और अफ्रीका के तटों का सटीक जुड़ाव", "type": "leaf"},
                        {"label": "जीवाश्म वितरण: ग्लोसोप्टेरिस वनस्पति और मेसोसॉरस जीवाश्म दोनों महाद्वीपों पर", "type": "leaf"},
                        {"label": "प्लेसर निक्षेप: घाना के तट पर सोने के निक्षेप जबकि मूल चट्टानें ब्राजील में हैं", "type": "leaf"},
                        {"label": "टिलाइट चट्टानें: हिमानी निक्षेप जो प्राचीन हिमीकरण को दर्शाते हैं", "type": "leaf"}
                    ]
                },
                {
                    "label": "प्रवाह के बल (Forces)",
                    "type": "branch",
                    "date": "बल",
                    "children": [
                        {"label": "ध्रुवीय पलायन बल (Polar-fleeing force): पृथ्वी के घूर्णन और अपकेंद्री बल से संबंधित", "type": "leaf"},
                        {"label": "ज्वारीय बल (Tidal force): सूर्य और चंद्रमा का गुरुत्वाकर्षण खिंचाव (बाद में अपर्याप्त माना गया)", "type": "leaf"}
                    ]
                },
                {
                    "label": "यूपीएससी परीक्षा दृष्टिकोण (UPSC Focus)",
                    "type": "branch",
                    "date": "परीक्षा",
                    "children": [
                        {"label": "मुख्य परीक्षा आयाम: प्लेट टेक्टोनिक्स के अग्रदूत के रूप में वेगनर के सिद्धांत का महत्व", "type": "leaf"},
                        {"label": "आम गलतियाँ: वेगनर ने गलत मान लिया था कि महाद्वीप महासागर की तली को चीरते हुए तैरते हैं (जबकि पूरी प्लेटें तैरती हैं)", "type": "leaf"}
                    ]
                }
            ]
        else:
            return [
                {
                    "label": "Wegener's Concept (1912)",
                    "type": "branch",
                    "date": "Theory",
                    "children": [
                        {"label": "Pangea & Panthalassa: Supercontinent surrounded by a mega-ocean", "type": "leaf"},
                        {"label": "Mesozoic Breakup: Split began ~200M years ago into Laurasia (North) & Gondwanaland (South)", "type": "leaf"}
                    ]
                },
                {
                    "label": "Key Evidences",
                    "type": "branch",
                    "date": "Evidences",
                    "children": [
                        {"label": "Jigsaw Fit: Matching shorelines of South America and Africa", "type": "leaf"},
                        {"label": "Fossil Correlation: Glossopteris flora and Mesosaurus fossils across oceans", "type": "leaf"},
                        {"label": "Placer Deposits: Ghana gold source rocks located in Brazil", "type": "leaf"},
                        {"label": "Tillite: Glacial sedimentary rocks matching across Southern continents", "type": "leaf"}
                    ]
                },
                {
                    "label": "Forces of Drifting",
                    "type": "branch",
                    "date": "Forces",
                    "children": [
                        {"label": "Polar-Fleeing Force: Centrifugal force due to Earth's rotation", "type": "leaf"},
                        {"label": "Tidal Force: Gravitational pull of Sun and Moon (Wegener's proposed forces were later rejected as too weak)", "type": "leaf"}
                    ]
                },
                {
                    "label": "UPSC Exam Relevance",
                    "type": "branch",
                    "date": "UPSC Core",
                    "children": [
                        {"label": "Mains Dimension: Value of Wegener's hypothesis as the precursor to modern Plate Tectonics theory", "type": "leaf"},
                        {"label": "Concept Trap: Wegener incorrectly assumed continents plowed through static oceanic crust rather than lithospheric plates moving together", "type": "leaf"}
                    ]
                }
            ]

    # 2. Plate Tectonics & Dynamics
    elif any(k in fl for k in ['plate', 'tectonic', 'spreading', 'indian-plate', 'boundaries']):
        if is_hindi:
            return [
                {
                    "label": "सिद्धांत की रूपरेखा (1967)",
                    "type": "branch",
                    "date": "सिद्धांत",
                    "children": [
                        {"label": "स्थलमंडल (Lithosphere): क्रस्ट और ऊपरी मेंटल का भाग, जो एस्थेनोस्फीयर पर तैरता है", "type": "leaf"},
                        {"label": "प्लेटें: 7 मुख्य प्लेटें (जैसे प्रशांत, यूरेशियाई, भारतीय) और कई छोटी प्लेटें", "type": "leaf"}
                    ]
                },
                {
                    "label": "प्लेट सीमाएं (Boundaries)",
                    "type": "branch",
                    "date": "वर्गीकरण",
                    "children": [
                        {"label": "अपसारी (Divergent): प्लेटें दूर जाती हैं, मैग्मा ऊपर उठता है (जैसे मध्य-अटलांटिक कटक)", "type": "leaf"},
                        {"label": "अभिसारी (Convergent): प्लेटें टकराती हैं, गर्त और पर्वतों का निर्माण (जैसे हिमालय)", "type": "leaf"},
                        {"label": "रूपांतर (Transform): प्लेटें क्षैतिज रूप से खिसकती हैं (जैसे सैन एंड्रियास भ्रंश)", "type": "leaf"}
                    ]
                },
                {
                    "label": "चालक बल और भारतीय प्लेट",
                    "type": "branch",
                    "date": "गतिशीलता",
                    "children": [
                        {"label": "संवहन धाराएं (Convection Currents): मेंटल में आर्थर होम्स द्वारा प्रतिपादित थर्मल धाराएं", "type": "leaf"},
                        {"label": "भारतीय प्लेट: यूरेशियन प्लेट से टक्कर (~40-50M वर्ष पूर्व) जिससे हिमालय का उत्थान हुआ", "type": "leaf"}
                    ]
                },
                {
                    "label": "यूपीएससी परीक्षा दृष्टिकोण (UPSC Focus)",
                    "type": "branch",
                    "date": "परीक्षा",
                    "children": [
                        {"label": "मुख्य परीक्षा आयाम: वैश्विक वलित पर्वतों, भूकंपीय क्षेत्रों और ज्वालामुखियों के वितरण की व्याख्या (GS I)", "type": "leaf"},
                        {"label": "संबद्ध अवधारणा: विल्सन चक्र (Wilson Cycle) - सुपरकॉन्टिनेंट चक्र का चक्रीय विकास", "type": "leaf"}
                    ]
                }
            ]
        else:
            return [
                {
                    "label": "Core Theory (1967)",
                    "type": "branch",
                    "date": "Framework",
                    "children": [
                        {"label": "Lithospheric Plates: Rigid crustal blocks floating on ductile asthenosphere", "type": "leaf"},
                        {"label": "Major Plates: 7 major plates (Pacific, Eurasian, Indo-Australian, etc.) and minor plates", "type": "leaf"}
                    ]
                },
                {
                    "label": "Plate Boundaries",
                    "type": "branch",
                    "date": "Boundaries",
                    "children": [
                        {"label": "Divergent: Plates pull apart, magma rises to form new crust (e.g., Mid-Atlantic Ridge)", "type": "leaf"},
                        {"label": "Convergent: Plates collide, forming subduction zones or mountain belts (e.g., Himalayas)", "type": "leaf"},
                        {"label": "Transform: Plates slide horizontally past each other, creating fault zones (e.g., San Andreas Fault)", "type": "leaf"}
                    ]
                },
                {
                    "label": "Driving Forces & Indian Plate",
                    "type": "branch",
                    "date": "Forces",
                    "children": [
                        {"label": "Convection Currents: Thermal convective cells in mantle proposed by Arthur Holmes", "type": "leaf"},
                        {"label": "Slab Pull & Ridge Push: Gravitational forces driving plate motion", "type": "leaf"},
                        {"label": "Indian Plate: Rapid northward movement and collision with Eurasian plate uplifting Himalayas", "type": "leaf"}
                    ]
                },
                {
                    "label": "UPSC Exam Relevance",
                    "type": "branch",
                    "date": "UPSC Core",
                    "children": [
                        {"label": "Mains Application: Explains global distribution of fold mountains, earthquakes, trenches, and volcanism (GS Paper I)", "type": "leaf"},
                        {"label": "Wilson Cycle: Periodic aggregation and dispersal of Earth's continental crust", "type": "leaf"}
                    ]
                }
            ]

    # 3. Earthquakes & Seismic Activity
    elif any(k in fl for k in ['earthquake', 'seismic', 'frequency', 'intensity']):
        if is_hindi:
            return [
                {
                    "label": "भूकंपीय तरंगें (Waves)",
                    "type": "branch",
                    "date": "तरंगें",
                    "children": [
                        {"label": "प्राथमिक तरंगें (P-waves): अनुदैर्ध्य, तीव्रतम, ठोस/तरल/गैस तीनों में गमन", "type": "leaf"},
                        {"label": "द्वितीयक तरंगें (S-waves): अनुप्रस्थ, केवल ठोस माध्यम में गमन, बाह्य कोर में विलुप्त", "type": "leaf"},
                        {"label": "धरातलीय तरंगें (Surface Waves): सर्वाधिक विनाशकारी, भूकंपलेख पर अंत में दर्ज", "type": "leaf"}
                    ]
                },
                {
                    "label": "मापन पैमाने (Scales)",
                    "type": "branch",
                    "date": "मापन",
                    "children": [
                        {"label": "रिक्टर पैमाना (Richter Scale): परिमाण (ऊर्जा मुक्ति) मापता है, लॉगरिथमिक (0-10)", "type": "leaf"},
                        {"label": "मर्केली पैमाना (Mercalli Scale): तीव्रता (दृश्य क्षति) मापता है, गुणात्मक (I-XII)", "type": "leaf"}
                    ]
                },
                {
                    "label": "छाया क्षेत्र (Shadow Zone)",
                    "type": "branch",
                    "date": "भौतिकी",
                    "children": [
                        {"label": "P-तरंग छाया: 103° से 142° तक (तरल बाह्य कोर में अपवर्तन के कारण)", "type": "leaf"},
                        {"label": "S-तरंग छाया: 103° से आगे पूरा क्षेत्र (तरल बाय कोर को पार न कर पाने के कारण)", "type": "leaf"}
                    ]
                },
                {
                    "label": "भारत और शमन (India & Mitigation)",
                    "type": "branch",
                    "date": "शमन",
                    "children": [
                        {"label": "भारत के भूकंपीय क्षेत्र: ज़ोन II से V (ज़ोन I को समाप्त कर दिया गया है)", "type": "leaf"},
                        {"label": "शमन उपाय: भूकंप रोधी निर्माण तकनीक, NDMA दिशानिर्देश, और सुनामी प्रारंभिक चेतावनी प्रणालियां (DART बुआ)", "type": "leaf"}
                    ]
                }
            ]
        else:
            return [
                {
                    "label": "Seismic Waves",
                    "type": "branch",
                    "date": "Waves",
                    "children": [
                        {"label": "Primary (P) Waves: Longitudinal, fastest, travel through solid, liquid, and gas", "type": "leaf"},
                        {"label": "Secondary (S) Waves: Transverse, slower, travel through solids only (blocked by liquid outer core)", "type": "leaf"},
                        {"label": "Surface Waves: Slowest moving, travel along crust, cause maximum ground destruction", "type": "leaf"}
                    ]
                },
                {
                    "label": "Measurement Scales",
                    "type": "branch",
                    "date": "Measurement",
                    "children": [
                        {"label": "Richter Scale: Logarithmic scale (1-10) measuring magnitude (total energy released)", "type": "leaf"},
                        {"label": "Mercalli Scale: Linear scale (I-XII) measuring intensity based on observed damage", "type": "leaf"}
                    ]
                },
                {
                    "label": "Shadow Zones",
                    "type": "branch",
                    "date": "Dynamics",
                    "children": [
                        {"label": "P-Wave Shadow Zone: 103° to 142° from epicenter due to refraction at outer core boundary", "type": "leaf"},
                        {"label": "S-Wave Shadow Zone: Beyond 103° from epicenter because S-waves cannot penetrate liquid outer core", "type": "leaf"}
                    ]
                },
                {
                    "label": "UPSC India Focus & Mitigation",
                    "type": "branch",
                    "date": "India & NDMA",
                    "children": [
                        {"label": "India Seismic Zonation: Zone II (low) to Zone V (very high risk); Zone I no longer exists", "type": "leaf"},
                        {"label": "Disaster Management: NDMA guidelines, structural retrofitting, earthquake-resistant design, and DART buoys for undersea tsunami warnings", "type": "leaf"}
                    ]
                }
            ]

    # 4. Volcanism & Igneous Landforms
    elif any(k in fl for k in ['volcan', 'lava', 'magma', 'ring-of-fire']):
        if is_hindi:
            return [
                {
                    "label": "ज्वालामुखी प्रकार (Types)",
                    "type": "branch",
                    "date": "वर्गीकरण",
                    "children": [
                        {"label": "शील्ड ज्वालामुखी: क्षारीय बेसाल्ट लावा, कम ढाल, शांत प्रवाह (जैसे हवाई द्वीप)", "type": "leaf"},
                        {"label": "मिश्रित (Composite): अम्लीय चिपचिपा लावा, विस्फोटक विस्फोट (जैसे विसुवियस, फ़ूजी)", "type": "leaf"},
                        {"label": "काल्डेरा (Caldera): सर्वाधिक विस्फोटक, विस्फोट के बाद ढहकर गर्त बनाते हैं", "type": "leaf"}
                    ]
                },
                {
                    "label": "अंतर्वेधी स्थलाकृतियां (Intrusive)",
                    "type": "branch",
                    "date": "भू-आकृतियां",
                    "children": [
                        {"label": "बैथोलिथ (Batholith): बड़े मैग्मा चैंबर जो पाताल में ठंडे होते हैं (चट्टान की रीढ़)", "type": "leaf"},
                        {"label": "लैकोलिथ (Lacolith): गुंबदाकार अंतर्वेध जिसके नीचे एक नली होती है", "type": "leaf"},
                        {"label": "सिल और डाइक: सिल (Sill) क्षैतिज परत है; डाइक (Dyke) लंबवत दीवार है", "type": "leaf"}
                    ]
                },
                {
                    "label": "रिंग ऑफ फायर (Ring of Fire)",
                    "type": "branch",
                    "date": "वितरण",
                    "children": [
                        {"label": "प्रशांत महासागर की परिधि: विश्व के 75% से अधिक सक्रिय ज्वालामुखी यहीं स्थित हैं", "type": "leaf"},
                        {"label": "कारण: प्लेटों का अभिसरण और सबडक्शन ज़ोन का निर्माण", "type": "leaf"}
                    ]
                },
                {
                    "label": "यूपीएससी परीक्षा दृष्टिकोण (UPSC Focus)",
                    "type": "branch",
                    "date": "भारत",
                    "children": [
                        {"label": "दक्कन ट्रैप (Deccan Trap): ज्वालामुखी दरारी उद्भेदन से निर्मित बेसाल्ट लावा शीट, जो उपजाऊ काली मृदा (Regur) का निर्माण करती है", "type": "leaf"},
                        {"label": "भारतीय स्थान: बैरन द्वीप (Barren Island) - भारत का एकमात्र सक्रिय ज्वालामुखी; नारकोंडम (सुसुप्त)", "type": "leaf"}
                    ]
                }
            ]
        else:
            return [
                {
                    "label": "Volcanic Eruptions",
                    "type": "branch",
                    "date": "Eruptions",
                    "children": [
                        {"label": "Shield Volcanoes: Low viscosity basaltic lava, gentle slopes, quiet eruptions (e.g., Hawaii)", "type": "leaf"},
                        {"label": "Composite Volcanoes: Viscous andesitic lava, explosive eruptions, layered ash & lava (e.g., Mt. Fuji)", "type": "leaf"},
                        {"label": "Calderas: Highly explosive volcanoes that collapse inward forming a depression", "type": "leaf"}
                    ]
                },
                {
                    "label": "Intrusive Landforms",
                    "type": "branch",
                    "date": "Plutonic",
                    "children": [
                        {"label": "Batholiths: Large granitic magma chambers cooling deep in the crust", "type": "leaf"},
                        {"label": "Laccoliths: Dome-shaped intrusive bodies fed by a pipe-like conduit", "type": "leaf"},
                        {"label": "Sills vs Dykes: Sills are horizontal sheet intrusions; Dykes are vertical/transverse sheets", "type": "leaf"}
                    ]
                },
                {
                    "label": "Pacific Ring of Fire",
                    "type": "branch",
                    "date": "Distribution",
                    "children": [
                        {"label": "Circum-Pacific Belt: Home to over 75% of Earth's active and dormant volcanoes", "type": "leaf"},
                        {"label": "Tectonic Setting: Subduction of oceanic plates beneath continental plates creating magma arcs", "type": "leaf"}
                    ]
                },
                {
                    "label": "UPSC Indian Context",
                    "type": "branch",
                    "date": "India Geography",
                    "children": [
                        {"label": "Deccan Traps: Basaltic plateau created by fissure eruption, forming fertile black cotton soil (Regur)", "type": "leaf"},
                        {"label": "Indian Locations: Barren Island (active volcano in Andaman Sea) and Narcondam Island (extinct/dormant)", "type": "leaf"}
                    ]
                }
            ]

    # 5. Physical / Mechanical Weathering
    elif any(k in fl for k in ['physical-weathering', 'mechanical-weathering', 'gravitational', 'water-pressure']):
        if is_hindi:
            return [
                {
                    "label": "भौतिक अपक्षय (Physical)",
                    "type": "branch",
                    "date": "यांत्रिक",
                    "children": [
                        {"label": "तुषार अपक्षय (Frost Wedging): दरारों में पानी जमने और फैलने से चट्टान का टूटना", "type": "leaf"},
                        {"label": "अपशलकन (Exfoliation): तापीय प्रसार और दबाव मुक्ति से चट्टानों का परतों में उखड़ना", "type": "leaf"}
                    ]
                },
                {
                    "label": "दबाव मुक्ति (Unloading)",
                    "type": "branch",
                    "date": "दबाव",
                    "children": [
                        {"label": "दबाव मुक्ति: ऊपरी चट्टानों के अपरदन से दबाव हटने पर चट्टान फैलती है और समानांतर परतों में टूटती है", "type": "leaf"}
                    ]
                },
                {
                    "label": "लवण अपक्षय (Salt weathering)",
                    "type": "branch",
                    "date": "लवण",
                    "children": [
                        {"label": "लवण क्रिस्टलीकरण: शुष्क/तटीय क्षेत्रों में दरारों में नमक का जमाव चट्टान के कणों को तोड़ता है (Granular Disintegration)", "type": "leaf"}
                    ]
                },
                {
                    "label": "यूपीएससी परीक्षा दृष्टिकोण (UPSC Focus)",
                    "type": "branch",
                    "date": "परीक्षा",
                    "children": [
                        {"label": "महत्व: यांत्रिक टूटना चट्टान के सतह क्षेत्र को बढ़ाता है, जिससे रासायनिक अपक्षय तीव्र होता है; ठंडी/शुष्क जलवायु में प्रभावी", "type": "leaf"}
                    ]
                }
            ]
        else:
            return [
                {
                    "label": "Physical Weathering",
                    "type": "branch",
                    "date": "Mechanical",
                    "children": [
                        {"label": "Frost Wedging: Water freezing in fractures expands and forces rock sections apart", "type": "leaf"},
                        {"label": "Thermal Expansion & Exfoliation: Daily heating/cooling causes onion-like peeling of rock sheets", "type": "leaf"},
                        {"label": "Pressure Release: Expansion of rock due to unloading of overlying weight", "type": "leaf"}
                    ]
                },
                {
                    "label": "Pressure Release",
                    "type": "branch",
                    "date": "Unloading",
                    "children": [
                        {"label": "Unloading: Erosion of overlying rocks relieves confining pressure, causing rock to expand and split parallel to surface (sheeting)", "type": "leaf"}
                    ]
                },
                {
                    "label": "Salt weathering",
                    "type": "branch",
                    "date": "Salt wedges",
                    "children": [
                        {"label": "Crystallization: Salt solutions in rock cracks expand upon heating, causing granular disintegration in arid/coastal areas", "type": "leaf"}
                    ]
                },
                {
                    "label": "UPSC Core Relevance",
                    "type": "branch",
                    "date": "Syllabus Focus",
                    "children": [
                        {"label": "Mechanical Breakdown: Increases surface area, accelerating chemical weathering; dominates in cold/arid climates", "type": "leaf"}
                    ]
                }
            ]

    # 6. Chemical Weathering
    elif any(k in fl for k in ['chemical-weathering', 'chemical-action']):
        if is_hindi:
            return [
                {
                    "label": "हाइड्रेशन और समाधान",
                    "type": "branch",
                    "date": "समाधान",
                    "children": [
                        {"label": "हाइड्रेशन: खनिजों द्वारा जल का रासायनिक अवशोषण जिससे आयतन बढ़ता है (जैसे हेमाटाइट से लिमोनाईट)", "type": "leaf"},
                        {"label": "घोल/समाधान (Solution): पानी में घुलनशील खनिजों (जैसे सेंधा नमक) का सीधे विलीन हो जाना", "type": "leaf"}
                    ]
                },
                {
                    "label": "कार्बोनेशन और ऑक्सीकरण",
                    "type": "branch",
                    "date": "प्रतिक्रिया",
                    "children": [
                        {"label": "कार्बोनेशन: वर्षा जल + CO2 से कमजोर कार्बोनिक एसिड का निर्माण, जो चूना पत्थर को घोलता है", "type": "leaf"},
                        {"label": "ऑक्सीकरण: ऑक्सीजन और खनिजों (विशेष रूप से लोहे) की प्रतिक्रिया, जंग लगना (Rusting)", "type": "leaf"}
                    ]
                },
                {
                    "label": "हाइड्रोलेसिस (Hydrolysis)",
                    "type": "branch",
                    "date": "हाइड्रोलेसिस",
                    "children": [
                        {"label": "हाइड्रोलेसिस: खनिज और जल के आयनों ($H^+$ और $OH^-$) के बीच रासायनिक क्रिया जिससे फेल्डस्पार जैसी चट्टानें मिट्टी (Clay) में बदल जाती हैं", "type": "leaf"}
                    ]
                },
                {
                    "label": "यूपीएससी परीक्षा दृष्टिकोण (UPSC Focus)",
                    "type": "branch",
                    "date": "मृदा",
                    "children": [
                        {"label": "महत्व: उष्णकटिबंधीय मृदा निर्माण (Laterization) और कार्स्ट स्थलाकृतियों के लिए आवश्यक; गर्म, आर्द्र जलवायु में प्रभावी", "type": "leaf"}
                    ]
                }
            ]
        else:
            return [
                {
                    "label": "Hydration & Solution",
                    "type": "branch",
                    "date": "Solution",
                    "children": [
                        {"label": "Hydration: Chemical absorption of water expands mineral volume (e.g. hematite to limonite)", "type": "leaf"},
                        {"label": "Solution: Direct dissolution of soluble minerals in water (e.g., rock salt)", "type": "leaf"}
                    ]
                },
                {
                    "label": "Carbonation & Oxidation",
                    "type": "branch",
                    "date": "Reactions",
                    "children": [
                        {"label": "Carbonation: Rainwater + CO2 forms carbonic acid, dissolving limestone", "type": "leaf"},
                        {"label": "Oxidation: Reaction of iron-rich minerals with oxygen, producing iron oxides (rust)", "type": "leaf"}
                    ]
                },
                {
                    "label": "Hydrolysis",
                    "type": "branch",
                    "date": "Hydrolysis",
                    "children": [
                        {"label": "Clay formation: Chemical reaction between mineral and water ions, breaking down feldspar into clay minerals", "type": "leaf"}
                    ]
                },
                {
                    "label": "UPSC Exam Significance",
                    "type": "branch",
                    "date": "Pedogenesis",
                    "children": [
                        {"label": "Humid Tropics: Dominates in warm, humid climates; prerequisite for tropical soil formation (laterization) and karst landscapes", "type": "leaf"}
                    ]
                }
            ]

    # 7. Biological Weathering
    elif any(k in fl for k in ['biological', 'vegetative', 'plant']):
        if is_hindi:
            return [
                {
                    "label": "जीव-जंतु गतिविधि (Faunal)",
                    "type": "branch",
                    "date": "जीव-जंतु",
                    "children": [
                        {"label": "बिल बनाने वाले जीव: केंचुए, दीमक, चूहे चट्टानों को खोदते हैं और नई सतहों को हवा-पानी के संपर्क में लाते हैं", "type": "leaf"}
                    ]
                },
                {
                    "label": "वनस्पति बल (Floral)",
                    "type": "branch",
                    "date": "जड़ें",
                    "children": [
                        {"label": "जड़ों का दबाव: पौधों और पेड़ों की जड़ें दरारों में बढ़ती हैं और चट्टान के टुकड़ों को अलग कर देती हैं", "type": "leaf"}
                    ]
                },
                {
                    "label": "जैव-रासायनिक प्रभाव (Biochemical)",
                    "type": "branch",
                    "date": "एसिड",
                    "children": [
                        {"label": "कार्बनिक अम्ल: लाइकेन, काई और सड़ने वाले कार्बनिक पदार्थ से निकलने वाला ह्यूमिक एसिड चट्टानों को घोलता है", "type": "leaf"}
                    ]
                },
                {
                    "label": "यूपीएससी परीक्षा दृष्टिकोण (UPSC Focus)",
                    "type": "branch",
                    "date": "पर्यावरण",
                    "children": [
                        {"label": "मुख्य परीक्षा आयाम: भू-आकृति विज्ञान और पारिस्थितिकी का अंतर्संबंध; ढलानों की स्थिरता में वनस्पतियों की भूमिका", "type": "leaf"}
                    ]
                }
            ]
        else:
            return [
                {
                    "label": "Faunal Weathering",
                    "type": "branch",
                    "date": "Animals",
                    "children": [
                        {"label": "Faunal Action: Burrowing animals (rodents, earthworms, termites) expose fresh minerals to atmosphere", "type": "leaf"}
                    ]
                },
                {
                    "label": "Floral / Root Wedging",
                    "type": "branch",
                    "date": "Roots",
                    "children": [
                        {"label": "Root wedging: Plant/tree roots penetrate cracks, exerting lateral force that splits rocks", "type": "leaf"}
                    ]
                },
                {
                    "label": "Biochemical Action",
                    "type": "branch",
                    "date": "Acids",
                    "children": [
                        {"label": "Organic acids: Lichens & mosses produce acids that dissolve minerals; decaying matter releases humic acids", "type": "leaf"}
                    ]
                },
                {
                    "label": "UPSC Core Focus",
                    "type": "branch",
                    "date": "Eco-Geomorphology",
                    "children": [
                        {"label": "Slope Stabilization: Interlinkage between geomorphology and ecology; vegetation prevents erosion and mass wasting", "type": "leaf"}
                    ]
                }
            ]

    # 8. Climatic, Topographic, and Factors of Weathering
    elif any(k in fl for k in ['climatic-weathering', 'topographic-weathering', 'factors-weathering', 'geological-weathering', 'factors']):
        if is_hindi:
            return [
                {
                    "label": "जलवायु नियंत्रण (Climate)",
                    "type": "branch",
                    "date": "जलवायु",
                    "children": [
                        {"label": "तापमान और वर्षा: आर्द्र उष्णकटिबंधीय क्षेत्रों में रासायनिक अपक्षय तीव्र होता है; शुष्क और ध्रुवीय क्षेत्रों में भौतिक अपक्षय", "type": "leaf"}
                    ]
                },
                {
                    "label": "स्थलाकृतिक प्रभाव (Topography)",
                    "type": "branch",
                    "date": "ढाल",
                    "children": [
                        {"label": "ढाल की तीव्रता: तीव्र ढलानों पर पानी बह जाता है (भौतिक अपक्षय); मंद ढलानों पर नमी संचित होती है (रासायनिक अपक्षय)", "type": "leaf"}
                    ]
                },
                {
                    "label": "चट्टान संरचना (Structure)",
                    "type": "branch",
                    "date": "संरचना",
                    "children": [
                        {"label": "जोड़ों और दरारें: दरारें अपक्षय कारकों के प्रवेश का मार्ग प्रशस्त करती हैं; चट्टान की रासायनिक संरचना (गोल्डिच स्थिरता क्रम)", "type": "leaf"}
                    ]
                },
                {
                    "label": "यूपीएससी परीक्षा दृष्टिकोण (UPSC Focus)",
                    "type": "branch",
                    "date": "अनुप्रयोग",
                    "children": [
                        {"label": "महत्व: अपक्षय की दरें वैश्विक मृदा वितरण को निर्धारित करती हैं; पर्वतीय बुनियादी ढांचा विकास में ढाल स्थिरता का महत्व", "type": "leaf"}
                    ]
                }
            ]
        else:
            return [
                {
                    "label": "Climatic Control",
                    "type": "branch",
                    "date": "Climate",
                    "children": [
                        {"label": "Rainfall & Temperature: Humid tropics favor rapid chemical weathering; arid/polar zones dominate in physical weathering", "type": "leaf"}
                    ]
                },
                {
                    "label": "Topographic Influence",
                    "type": "branch",
                    "date": "Slope",
                    "children": [
                        {"label": "Slope Angle: Steep slopes favor gravity removal & physical weathering; gentle slopes retain water, promoting chemical weathering", "type": "leaf"}
                    ]
                },
                {
                    "label": "Rock Structure & Joints",
                    "type": "branch",
                    "date": "Rock Composition",
                    "children": [
                        {"label": "Joints & Fractures: Vulnerable pathways; Mineral stability (Goldich stability series where quartz is most resistant, olivine most vulnerable)", "type": "leaf"}
                    ]
                },
                {
                    "label": "UPSC Application",
                    "type": "branch",
                    "date": "Slope Stability",
                    "children": [
                        {"label": "Soil Mapping: Weathering rates determine global soil patterns; crucial for mountainous infrastructure slope safety analyses", "type": "leaf"}
                    ]
                }
            ]

    # 9. Geomorphic Processes (Endogenic vs. Exogenic)
    elif any(k in fl for k in ['process', 'surface', 'endogenic', 'exogenic', 'agent', 'evolution', 'causes']):
        if is_hindi:
            return [
                {
                    "label": "आंतरिक बल (Endogenic)",
                    "type": "branch",
                    "date": "आंतरिक",
                    "children": [
                        {"label": "पटल विरूपण (Diastrophism): महाद्वीप निर्माणकारी बल (Epeirogenic - लंबवत) और पर्वत निर्माणकारी बल (Orogenic - क्षैतिज, वलन/भ्रंशन)", "type": "leaf"},
                        {"label": "आकस्मिक बल: भूकंप और ज्वालामुखी क्रियाएं जो धरातल पर असमानता लाती हैं", "type": "leaf"}
                    ]
                },
                {
                    "label": "बाह्य बल (Exogenic)",
                    "type": "branch",
                    "date": "बाहरी",
                    "children": [
                        {"label": "अपक्षय (Weathering): चट्टानों का अपने ही स्थान पर टूटना (स्थानांतरण रहित)", "type": "leaf"},
                        {"label": "सामूहिक विनाश (Mass Wasting): गुरुत्वाकर्षण द्वारा मलबे का नीचे खिसकना", "type": "leaf"},
                        {"label": "अपरदन और परिवहन: जल, हवा, हिमनद द्वारा चट्टानों का घिसाव और परिवहन", "type": "leaf"}
                    ]
                },
                {
                    "label": "भू-आकृतिक कारक (Agents)",
                    "type": "branch",
                    "date": "कारक",
                    "children": [
                        {"label": "सक्रिय माध्यम: बहता जल (नदी), भूमिगत जल, पवन, हिमनद, समुद्री तरंगें जो धरातल का समतलीकरण (Gradation) करती हैं", "type": "leaf"}
                    ]
                },
                {
                    "label": "यूपीएससी परीक्षा दृष्टिकोण (UPSC Focus)",
                    "type": "branch",
                    "date": "अपरदन चक्र",
                    "children": [
                        {"label": "अपरदन चक्र सिद्धांत: डब्ल्यू. एम. डेविस (संरचना, प्रक्रम और अवस्था) बनाम डब्ल्यू. पेंक का समानांतर ढाल निवर्तन सिद्धांत", "type": "leaf"}
                    ]
                }
            ]
        else:
            return [
                {
                    "label": "Endogenic Forces",
                    "type": "branch",
                    "date": "Internal Forces",
                    "children": [
                        {"label": "Diastrophism: Epeirogenic (vertical continental uplift/subsidence) and Orogenic (horizontal mountain-building folding/faulting)", "type": "leaf"},
                        {"label": "Sudden forces: Volcanism and Earthquakes which rapidly create initial landforms", "type": "leaf"}
                    ]
                },
                {
                    "label": "Exogenic Forces",
                    "type": "branch",
                    "date": "External Forces",
                    "children": [
                        {"label": "Weathering: In-situ disintegration and decomposition of rocks", "type": "leaf"},
                        {"label": "Mass Wasting: Downslope movement of rock debris under direct influence of gravity", "type": "leaf"},
                        {"label": "Erosion & Transport: Acquisition and transportation of rock materials by mobile agents", "type": "leaf"}
                    ]
                },
                {
                    "label": "Geomorphic Agents",
                    "type": "branch",
                    "date": "Mobile Media",
                    "children": [
                        {"label": "Gradational Agents: Running water (fluvial), groundwater, wind (aeolian), glaciers, and waves which level down relief", "type": "leaf"}
                    ]
                },
                {
                    "label": "UPSC Geomorphology Core",
                    "type": "branch",
                    "date": "Landscape Evolution",
                    "children": [
                        {"label": "Erosion Theories: W.M. Davis 'Cycle of Erosion' (Structure, Process, Stage) vs Walther Penck's parallel slope decline theory", "type": "leaf"}
                    ]
                }
            ]

    # 10. Earth's Interior & Crust Elements
    elif any(k in fl for k in ['interior', 'crust', 'mantle', 'core', 'sources-of-information', 'elements-of-the-earths-crust']):
        if is_hindi:
            return [
                {
                    "label": "सूचना के स्रोत (Sources)",
                    "type": "branch",
                    "date": "अध्ययन",
                    "children": [
                        {"label": "प्रत्यक्ष स्रोत: खनन क्षेत्र, गहरे महासागरीय वेधन (Drilling), ज्वालामुखी लावा", "type": "leaf"},
                        {"label": "अप्रत्यक्ष स्रोत: भूकंपीय तरंगों का वेग परिवर्तन, उल्कापिंड, गुरुत्वाकर्षण विसंगति, चुंबकीय क्षेत्र", "type": "leaf"}
                    ]
                },
                {
                    "label": "रासायनिक और भौतिक परतें",
                    "type": "branch",
                    "date": "संरचना",
                    "children": [
                        {"label": "भूपर्पटी (Crust): ठोस बाहरी परत, महाद्वीपीय भाग ग्रेनाइट (Sial), महासागरीय भाग बेसाल्ट (Sima)", "type": "leaf"},
                        {"label": "मेंटल (Mantle): सीमा (Moho) से 2900 किमी गहराई तक; एस्थेनोस्फीयर (ऊपरी कमजोर भाग, मैग्मा स्रोत)", "type": "leaf"},
                        {"label": "क्रोड (Core): निकल और लोहा (Nife) से निर्मित; बाह्य क्रोड तरल अवस्था में, आंतरिक क्रोड ठोस", "type": "leaf"}
                    ]
                },
                {
                    "label": "भूकंपीय असंबद्धताएं (Discontinuities)",
                    "type": "branch",
                    "date": "सीमाएं",
                    "children": [
                        {"label": "कोनराड (Conrad): बाह्य और आंतरिक क्रस्ट; मोहा (Moho): क्रस्ट और मेंटल के बीच", "type": "leaf"},
                        {"label": "गुटेनबर्ग (Gutenberg): मेंटल और कोर; लेहमैन (Lehmann): बाह्य और आंतरिक कोर", "type": "leaf"}
                    ]
                },
                {
                    "label": "भूकंपीय तरंगों की भूमिका (UPSC Focus)",
                    "type": "branch",
                    "date": "अनुप्रयोग",
                    "children": [
                        {"label": "भूकंपीय टोमोग्राफी: विभिन्न गहराईयों पर तरंगों की गति के बदलाव से आंतरिक संरचना का मानचित्रण", "type": "leaf"},
                        {"label": "भू-डायनेमो (Geodynamo): बाह्य तरल कोर में संवहन धाराएं पृथ्वी के चुंबकीय क्षेत्र (Magnetosphere) को जन्म देती हैं", "type": "leaf"}
                    ]
                }
            ]
        else:
            return [
                {
                    "label": "Sources of Information",
                    "type": "branch",
                    "date": "Evidence",
                    "children": [
                        {"label": "Direct Sources: Deep gold mines, ocean drilling projects (e.g. Kola Superdeep), volcanic materials", "type": "leaf"},
                        {"label": "Indirect Sources: Seismic wave speeds, meteorites, gravity anomalies, geomagnetic fields", "type": "leaf"}
                    ]
                },
                {
                    "label": "Layered Chemical Structure",
                    "type": "branch",
                    "date": "Layers",
                    "children": [
                        {"label": "Crust: Granitic continental Sial (light) and basaltic oceanic Sima (denser)", "type": "leaf"},
                        {"label": "Mantle: Comprises 84% of Earth's volume; upper part has asthenosphere (magma source)", "type": "leaf"},
                        {"label": "Core: Rich in Nickel and Iron (Nife); outer core is liquid (geodynamo), inner core is solid", "type": "leaf"}
                    ]
                },
                {
                    "label": "Seismic Discontinuities",
                    "type": "branch",
                    "date": "Boundaries",
                    "children": [
                        {"label": "Mohorovicic (Moho): Boundary separating the crust from the mantle", "type": "leaf"},
                        {"label": "Gutenberg: Boundary separating the mantle from the core", "type": "leaf"},
                        {"label": "Conrad (crustal split), Repetti (mantle split), Lehmann (outer/inner core split)", "type": "leaf"}
                    ]
                },
                {
                    "label": "UPSC Core Geophysics",
                    "type": "branch",
                    "date": "Seismology Role",
                    "children": [
                        {"label": "Refraction/Reflection: How wave velocity changes (shadow zones) help map exact depth of internal interfaces", "type": "leaf"},
                        {"label": "Geodynamo: Convective flow of liquid iron in outer core generates Earth's protective magnetic field (Magnetosphere)", "type": "leaf"}
                    ]
                }
            ]

    # 11. Landforms, Rivers, Lakes, Karst & Coastal
    elif any(k in fl for k in ['landform', 'karst', 'wave', 'river', 'lake', 'depositional', 'erosional', 'mountain', 'plateau', 'peak']):
        if is_hindi:
            return [
                {
                    "label": "नदीकृत भू-आकृतियां (Fluvial)",
                    "type": "branch",
                    "date": "नदी",
                    "children": [
                        {"label": "अपरदनात्मक: V-आकार की घाटी, गार्ज, कैनियन, जलप्रपात, अवनमन कुंड", "type": "leaf"},
                        {"label": "निक्षेपात्मक: जलोढ़ पंख, प्राकृतिक तटबंध, विसर्प (Meanders), गोखुर झील, डेल्टा", "type": "leaf"}
                    ]
                },
                {
                    "label": "कार्स्ट और तटीय आकृतियां",
                    "type": "branch",
                    "date": "जल व लहरें",
                    "children": [
                        {"label": "कार्स्ट (भूजल): घोलरंध्र (Sinkholes), उवाला, लैपीज, स्टैलेक्टाइट, स्टैलेग्माइट, कंदराएं", "type": "leaf"},
                        {"label": "तटीय: क्लिफ, तरंग-घर्षित प्लेटफॉर्म, मेहराब (Arches), स्टैक (Erosional); पुलिन (Beaches), स्पिट, लैगून (Depositional)", "type": "leaf"}
                    ]
                },
                {
                    "label": "पवन और हिमनद भू-आकृतियां",
                    "type": "branch",
                    "date": "पवन व बर्फ",
                    "children": [
                        {"label": "पवन (शुष्क): छत्रक शिला (Mushroom Rocks), यारडंग, पेडीमेंट, प्लाया, बरखान (सैंड ड्यून्स)", "type": "leaf"},
                        {"label": "हिमनद: U-आकार की घाटी, सर्क (Cirque), हॉर्न, मोरेन (Moraines), एस्कर, ड्रमलिन", "type": "leaf"}
                    ]
                },
                {
                    "label": "अपरदन चक्र सिद्धांत (UPSC Core)",
                    "type": "branch",
                    "date": "भूगोलवेत्ता",
                    "children": [
                        {"label": "डेविस का अपरदन चक्र: भौगोलिक चक्र (Youth, Maturity, Old Age) जहाँ थलखंड का उत्थान तीव्र होता है", "type": "leaf"},
                        {"label": "पेंक का सिद्धांत: उत्थान और अपरदन साथ-साथ चलते हैं; ढाल प्रतिस्थापन (Slope Replacement) का नियम", "type": "leaf"}
                    ]
                }
            ]
        else:
            return [
                {
                    "label": "Fluvial Landforms",
                    "type": "branch",
                    "date": "Running Water",
                    "children": [
                        {"label": "Erosional: V-shaped valleys, gorges, canyons, potholes, waterfalls, plunge pools", "type": "leaf"},
                        {"label": "Depositional: Alluvial fans, natural levees, point bars, floodplains, oxbow lakes, deltas", "type": "leaf"}
                    ]
                },
                {
                    "label": "Karst & Coastal Systems",
                    "type": "branch",
                    "date": "Water & Waves",
                    "children": [
                        {"label": "Karst Topography: Sinkholes, uvalas, caves, stalactites, stalagmites, pillars (limestone solution)", "type": "leaf"},
                        {"label": "Coastal Erosional: Sea cliffs, wave-cut platforms, sea caves, sea arches, sea stacks", "type": "leaf"},
                        {"label": "Coastal Depositional: Sand beaches, spits, tombolos, barrier bars, coastal lagoons", "type": "leaf"}
                    ]
                },
                {
                    "label": "Aeolian & Glacial Systems",
                    "type": "branch",
                    "date": "Wind & Ice",
                    "children": [
                        {"label": "Aeolian (Desert): Pediments, playes, yardangs, mushroom rocks, barchans, seif dunes, loess", "type": "leaf"},
                        {"label": "Glacial: U-shaped valleys, hanging valleys, cirques, horns, lateral/terminal moraines, eskers, drumlins", "type": "leaf"}
                    ]
                },
                {
                    "label": "Geomorphic Erosion Cycles",
                    "type": "branch",
                    "date": "Geomorphology Theories",
                    "children": [
                        {"label": "W.M. Davis Cycle of Erosion: Triad of Structure, Process, and Stage (Youth, Maturity, Old age leading to Peneplain)", "type": "leaf"},
                        {"label": "Walther Penck Cycle: Landscape development governed by ratio of uplift rate to degradation rate (Slope decline & replacement)", "type": "leaf"}
                    ]
                }
            ]

    # 12. Rocks & Minerals
    elif any(k in fl for k in ['rock', 'mineral', 'physical-characteristics', 'transparency-structure', 'cleavage', 'hardness']):
        if is_hindi:
            return [
                {
                    "label": "आग्नेय चट्टानें (Igneous)",
                    "type": "branch",
                    "date": "चट्टान चक्र",
                    "children": [
                        {"label": "प्राथमिक चट्टानें: मैग्मा के ठंडे होकर जमने से निर्मित (अक्रिस्टलीय या क्रिस्टलीय)", "type": "leaf"},
                        {"label": "प्रकार: बेसाल्ट (बहिर्वेधी, महीन दानेदार), ग्रेनाइट (अंतर्वेधी, मोटे दानेदार)", "type": "leaf"}
                    ]
                },
                {
                    "label": "अवसादी और कायांतरित चट्टानें",
                    "type": "branch",
                    "date": "रूप परिवर्तन",
                    "children": [
                        {"label": "अवसादी (Sedimentary): परतदार चट्टानें, लिथिफिकेशन और सघनीकरण द्वारा निर्मित (जैसे बलुआ पत्थर)", "type": "leaf"},
                        {"label": "कायांतरित (Metamorphic): अत्यधिक तापमान और दबाव से पुनः क्रिस्टलीकरण (जैसे संगमरमर, नीस)", "type": "leaf"}
                    ]
                },
                {
                    "label": "खनिजों के भौतिक गुण",
                    "type": "branch",
                    "date": "गुणधर्म",
                    "children": [
                        {"label": "क्रिस्टल रूप, विदलन (Cleavage), फ्रैक्चर, चमक (Lustre), रंग, लकीर (Streak)", "type": "leaf"},
                        {"label": "कठोरता: मोह पैमाना (Mohs Scale) - टैल्क (1, सबसे कोमल) से हीरा (10, सबसे कठोर)", "type": "leaf"}
                    ]
                },
                {
                    "label": "भारतीय खनिज प्रणालियां (India Minerals)",
                    "type": "branch",
                    "date": "आर्थिक भूगोल",
                    "children": [
                        {"label": "धारवाड़ प्रणाली (Dharwar): धात्विक खनिजों (लोहा, मैंगनीज, सोना) से भरपूर भारत की सबसे महत्वपूर्ण चट्टान प्रणाली", "type": "leaf"},
                        {"label": "गोंडवाना प्रणाली (Gondwana): भारत का 98% कोयला भंडार इसी प्रणाली से प्राप्त होता है", "type": "leaf"}
                    ]
                }
            ]
        else:
            return [
                {
                    "label": "Igneous Rocks",
                    "type": "branch",
                    "date": "Primary Rocks",
                    "children": [
                        {"label": "Formation: Solidification and cooling of hot magma/lava either underground or on surface", "type": "leaf"},
                        {"label": "Subtypes: Extrusive basaltic (fine-grained, rapid cooling) and intrusive granitic (coarse-grained, slow cooling)", "type": "leaf"}
                    ]
                },
                {
                    "label": "Sedimentary & Metamorphic",
                    "type": "branch",
                    "date": "Rock Cycle",
                    "children": [
                        {"label": "Sedimentary: Stratified rocks formed via lithification of organic/mineral deposits (e.g., shale, sandstone)", "type": "leaf"},
                        {"label": "Metamorphic: Formed by recrystallization under high temperature & pressure conditions (e.g., marble, schist)", "type": "leaf"}
                    ]
                },
                {
                    "label": "Mineral Properties",
                    "type": "branch",
                    "date": "Properties",
                    "children": [
                        {"label": "Visuals: Crystal system, cleavage planes, fracture styles, luster, color, streak color", "type": "leaf"},
                        {"label": "Hardness: Mohs Scale ranging from 1 (Talc, softest) to 10 (Diamond, hardest)", "type": "leaf"}
                    ]
                },
                {
                    "label": "UPSC India Rock Systems",
                    "type": "branch",
                    "date": "Mineral Wealth",
                    "children": [
                        {"label": "Dharwar System: Structurally highly metamorphosed; primary source of India's metallic minerals (Iron, Manganese, Copper)", "type": "leaf"},
                        {"label": "Gondwana System: Late Paleozoic to Mesozoic formations; holds ~98% of India's commercial coal reserves", "type": "leaf"}
                    ]
                }
            ]

    # 13. Isostasy
    elif 'isostasy' in fl:
        if is_hindi:
            return [
                {
                    "label": "मूल अवधारणा",
                    "type": "branch",
                    "date": "संतुलन",
                    "children": [
                        {"label": "परिभाषा: हल्के पर्वतीय खंडों और भारी अधःस्तर (Substratum) के बीच गुरुत्वाकर्षण संतुलन", "type": "leaf"}
                    ]
                },
                {
                    "label": "एयरी का सिद्धांत (Airy)",
                    "type": "branch",
                    "date": "समान घनत्व",
                    "children": [
                        {"label": "धारणा: भूपर्पटी के खंडों का घनत्व समान होता है लेकिन उनकी गहराई अलग होती है (जैसे तैरता हुआ हिमखंड)", "type": "leaf"},
                        {"label": "नियम: ऊंचे पर्वतों की मेंटल में जड़ें गहरी होती हैं", "type": "leaf"}
                    ]
                },
                {
                    "label": "प्राट का सिद्धांत (Pratt)",
                    "type": "branch",
                    "date": "विविध घनत्व",
                    "children": [
                        {"label": "धारणा: भूपर्पटी के विभिन्न भागों का घनत्व भिन्न होता है लेकिन गहराई समान होती है", "type": "leaf"},
                        {"label": "नियम: मुआवजा स्तर (Level of Compensation) - ऊंचाई जितनी अधिक, घनत्व उतना ही कम", "type": "leaf"}
                    ]
                },
                {
                    "label": "यूपीएससी परीक्षा दृष्टिकोण (UPSC Focus)",
                    "type": "branch",
                    "date": "भू-संतुलन",
                    "children": [
                        {"label": "भू-संतुलन समायोजन (Isostatic Rebound): हिमनदों के पिघलने या अपरदन से भार हटने पर थलखंड का ऊपर उठना", "type": "leaf"},
                        {"label": "सिद्धांत तुलना: एयरी 'जड़ों' (Roots) की अवधारणा पर आधारित है; प्राट 'घनत्व में अंतर' पर आधारित है", "type": "leaf"}
                    ]
                }
            ]
        else:
            return [
                {
                    "label": "Core Concept",
                    "type": "branch",
                    "date": "Equilibrium",
                    "children": [
                        {"label": "Definition: State of gravitational equilibrium between the Earth's lithosphere and asthenosphere", "type": "leaf"}
                    ]
                },
                {
                    "label": "Airy's Hypothesis",
                    "type": "branch",
                    "date": "Uniform Density",
                    "children": [
                        {"label": "Mechanics: Crustal blocks have the same density but varying depths (roots)", "type": "leaf"},
                        {"label": "Rule: Taller topographic features (mountains) have deeper lithospheric roots floating in asthenosphere", "type": "leaf"}
                    ]
                },
                {
                    "label": "Pratt's Hypothesis",
                    "type": "branch",
                    "date": "Varying Density",
                    "children": [
                        {"label": "Mechanics: Crustal blocks have varying densities but subduct to a uniform depth (level of compensation)", "type": "leaf"},
                        {"label": "Rule: High features like mountains have lower density; low features like oceans have higher density", "type": "leaf"}
                    ]
                },
                {
                    "label": "UPSC Geodynamic Relevance",
                    "type": "branch",
                    "date": "Isostatic Adjustment",
                    "children": [
                        {"label": "Isostatic Rebound: Post-glacial crustal uplift (e.g. Scandinavia) or basin subsidence due to sediment loading", "type": "leaf"},
                        {"label": "Contrast: Airy relies on the concept of 'mountain roots' (floatation); Pratt relies on 'level of compensation' with no roots", "type": "leaf"}
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
