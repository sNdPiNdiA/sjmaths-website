#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import re
import json

BASE_DIR = r"upsc/geography/Oceanography"

def get_clean_title(folder_name):
    # Split camelCase words like GreatBarrierReef to Great Barrier Reef
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
    
    # 1. Ocean Floor Relief & Features
    if any(k in fl for k in ['shelf', 'slope', 'plain', 'minor-relief', 'trenches', 'relief-of-the-ocean', 'deep-sea-plain', 'abyssal', 'oceanic-deep']):
        if is_hindi:
            return [
                {
                    "label": "प्रमुख महासागरीय उच्चावच",
                    "type": "branch",
                    "date": "मुख्य आकृतियाँ",
                    "children": [
                        {"label": "महाद्वीपीय मग्नतट (Shelf): अत्यंत उथला ढाल, चौड़ाई अलग-अलग (0-200m गहराई)", "type": "leaf"},
                        {"label": "महाद्वीपीय ढाल (Slope): 200-3000 मीटर गहराई; तीव्र ढाल (2-5°); पनडुब्बी कैनियन", "type": "leaf"},
                        {"label": "गहरे समुद्र के मैदान (Abyssal Plain): अत्यंत सपाट, सागर तल का 75-80% भाग", "type": "leaf"}
                    ]
                },
                {
                    "label": "लघु उच्चावच आकृतियाँ",
                    "type": "branch",
                    "date": "लघु आकृतियाँ",
                    "children": [
                        {"label": "मध्य-महासागरीय कटक (Ridges): विवर्तनिक प्लेटों के अपसरण पर मैग्मा जमने से बने पठार/पर्वत", "type": "leaf"},
                        {"label": "सीमाउंट और गुयोट (Seamounts/Guyots): समुद्री ज्वालामुखी पर्वत; गुयोट का शीर्ष समतल होता है", "type": "leaf"},
                        {"label": "महासागरीय गर्त (Trenches): अभिसरण सीमाओं पर सबडक्शन द्वारा निर्मित सबसे गहरे गर्त", "type": "leaf"}
                    ]
                },
                {
                    "label": "आर्थिक और भू-वैज्ञानिक मूल्य",
                    "type": "branch",
                    "date": "संसाधन",
                    "children": [
                        {"label": "मत्स्य पालन: मग्नतटों पर प्रचुर सूर्यप्रकाश और पोषक तत्व; 90% समुद्री मछली यहीं मिलती है", "type": "leaf"},
                        {"label": "ऊर्जा भंडार: मुंबई हाई और के-जी बेसिन जैसे मग्नतटों पर विश्व के 30% तेल-गैस भंडार", "type": "leaf"}
                    ]
                },
                {
                    "label": "यूपीएससी परीक्षा दृष्टिकोण (UPSC Focus)",
                    "type": "branch",
                    "date": "परीक्षा",
                    "children": [
                        {"label": "UNCLOS नियम: प्रादेशिक जल (12 NM), विशेष आर्थिक क्षेत्र (EEZ - 200 NM) सीमाएं", "type": "leaf"},
                        {"label": "संबंधित विषय: इंटरनेशनल सीबेड अथॉरिटी (ISA) द्वारा गहरे समुद्र में खनन नियमन", "type": "leaf"}
                    ]
                }
            ]
        else:
            return [
                {
                    "label": "Major Relief Features",
                    "type": "branch",
                    "date": "Features",
                    "children": [
                        {"label": "Continental Shelf: Submerged margin; gentle gradient; 0-200m depth; wide in Arctic, narrow in Pacific", "type": "leaf"},
                        {"label": "Continental Slope: Boundary from shelf break; steep 2-5° gradient; cut by deep Submarine Canyons", "type": "leaf"},
                        {"label": "Abyssal Plains: Flat deep ocean floor; 3000-6000m depth; covers ~40% of ocean floor area", "type": "leaf"}
                    ]
                },
                {
                    "label": "Minor Relief Features",
                    "type": "branch",
                    "date": "Minor Features",
                    "children": [
                        {"label": "Mid-Oceanic Ridges: Spreading plate boundaries; volcanic activity forms continuous mountain chains", "type": "leaf"},
                        {"label": "Seamounts & Guyots: Isolated volcanic peaks; seamounts are pointed, guyots have flat-topped erosion surfaces", "type": "leaf"},
                        {"label": "Oceanic Trenches: Convergent boundaries; subducting lithospheric slabs create deep linear troughs", "type": "leaf"}
                    ]
                },
                {
                    "label": "Economic & Ecological Value",
                    "type": "branch",
                    "date": "Resources",
                    "children": [
                        {"label": "Shelf Fisheries: 90% of global fish catch; rich in sunlight and upwelling nutrients", "type": "leaf"},
                        {"label": "Offshore Oil & Gas: Major oil/gas reserves (e.g., Mumbai High, North Sea, Persian Gulf) located in shelf basins", "type": "leaf"}
                    ]
                },
                {
                    "label": "UPSC Syllabus relevance",
                    "type": "branch",
                    "date": "UNCLOS & ISA",
                    "children": [
                        {"label": "UNCLOS Zones: Territorial Waters (12 NM), Contiguous Zone (24 NM), Exclusive Economic Zone (EEZ - 200 NM)", "type": "leaf"},
                        {"label": "Deep Sea Mining: ISA regulations for harvesting polymetallic nodules from international waters", "type": "leaf"}
                    ]
                }
            ]

    # 2. Ocean Deposits
    elif any(k in fl for k in ['deposit', 'sediment', 'abiotic', 'biotic', 'terrigenous', 'volcanic']):
        if is_hindi:
            return [
                {
                    "label": "अजैविक और जैविक निक्षेप",
                    "type": "branch",
                    "date": "प्रकार",
                    "children": [
                        {"label": "अजैविक निक्षेप: मैंगनीज नोड्यूल (Fe-Mn-Cu-Ni-Co), हाइड्रोथर्मल वेंट सल्फाइड (Black Smokers)", "type": "leaf"},
                        {"label": "जैविक (Biotic) निक्षेप: मृत जीवों के अवशेष; कैलकेरियस और सिलिसियस ऊज़", "type": "leaf"}
                    ]
                },
                {
                    "label": "गहरे समुद्री जैविक निक्षेप",
                    "type": "branch",
                    "date": "जैविक ऊज़",
                    "children": [
                        {"label": "कैलकेरियस ऊज़: ग्लोबिगेरिना और टेरोपोड ऊज़; चूने की प्रधानता; उथले गर्म पानी में", "type": "leaf"},
                        {"label": "सिलिसियस ऊज़: रेडियोलेरियन और डायटम ऊज़; सिलिका की प्रधानता; ठंडे गहरे पानी में स्थिर", "type": "leaf"}
                    ]
                },
                {
                    "label": "कार्बोनेट मुआवजा गहराई (CCD)",
                    "type": "branch",
                    "date": "भौतिकी",
                    "children": [
                        {"label": "CCD सीमा: लगभग 4000-5000 मीटर गहराई; नीचे उच्च दाब और कम तापमान पर चूना पत्थर पूरी तरह घुल जाता है", "type": "leaf"},
                        {"label": "CCD के नीचे: केवल सिलिसियस ऊज़ और लाल मृत्तिका (Red Clay) का संचय होता है", "type": "leaf"}
                    ]
                },
                {
                    "label": "यूपीएससी भारत मिशन (UPSC Focus)",
                    "type": "branch",
                    "date": "भारत मिशन",
                    "children": [
                        {"label": "केंद्रीय हिंद महासागर बेसिन (CIOB): भारत को पॉलीमेटालिक नोड्यूल्स खनन का अग्रणी अधिकार", "type": "leaf"},
                        {"label": "डीप ओशन मिशन (DOM): महासागरीय संसाधनों के दोहन हेतु पनडुब्बी 'मत्स्य 6000' (Matsyayana 6000) का विकास", "type": "leaf"}
                    ]
                }
            ]
        else:
            return [
                {
                    "label": "Abiotic & Biotic Deposits",
                    "type": "branch",
                    "date": "Classification",
                    "children": [
                        {"label": "Abiotic: Manganese nodules, cobalt-rich crusts, hydrothermal vent sulfide deposits", "type": "leaf"},
                        {"label": "Biotic (Pelagic Oozes): Accumulation of skeletal remains of micro-organisms covering ocean plains", "type": "leaf"}
                    ]
                },
                {
                    "label": "Siliceous vs Calcareous",
                    "type": "branch",
                    "date": "Pelagic Oozes",
                    "children": [
                        {"label": "Calcareous Oozes: Globigerina & Pteropod shells ($CaCO_3$); abundant in warm, shallow ocean floors", "type": "leaf"},
                        {"label": "Siliceous Oozes: Diatom & Radiolarian shells ($SiO_2$); stable in high latitude cold waters and deep seas", "type": "leaf"}
                    ]
                },
                {
                    "label": "Carbonate Compensation Depth",
                    "type": "branch",
                    "date": "CCD Mechanics",
                    "children": [
                        {"label": "CCD Level (~4000-5000m): Depth below which rate of dissolution of calcium carbonate exceeds rate of supply", "type": "leaf"},
                        {"label": "Red Clay: Covers deepest floor sections below CCD; rich in iron/aluminum silicates, very slow deposition", "type": "leaf"}
                    ]
                },
                {
                    "label": "UPSC & Indian Exploration",
                    "type": "branch",
                    "date": "India DOM",
                    "children": [
                        {"label": "CIOB Allocation: India allocated 75,000 sq km in Central Indian Ocean Basin by ISA for PMN harvesting", "type": "leaf"},
                        {"label": "Deep Ocean Mission: Ministry of Earth Sciences project; includes Samudrayaan and development of Matsyayana 6000 manned submersible", "type": "leaf"}
                    ]
                }
            ]

    # 3. Ocean Water Properties (Temperature, Salinity, Density)
    elif any(k in fl for k in ['density', 'temperature', 'salinity', 'properties', 'distribution', 'factors-affecting-temperature']):
        if is_hindi:
            return [
                {
                    "label": "तापमान वितरण के कारक",
                    "type": "branch",
                    "date": "तापमान",
                    "children": [
                        {"label": "अक्षांशीय परिवर्तन: भूमध्य रेखा से ध्रुवों की ओर तापमान घटता है", "type": "leaf"},
                        {"label": "लंबवत स्तरीकरण: मिश्रित परत (Surface), थर्मोक्लाइन (तीव्र गिरावट), गहरा ठंडा जल", "type": "leaf"}
                    ]
                },
                {
                    "label": "लवणता नियंत्रण कारक",
                    "type": "branch",
                    "date": "लवणता",
                    "children": [
                        {"label": "वाष्पीकरण और वर्षा: अधिक वाष्पीकरण = अधिक लवणता; अधिक वर्षा = कम लवणता (जैसे भूमध्य रेखा पर कम)", "type": "leaf"},
                        {"label": "लंबवत वितरण: हेलोक्लाइन (Halocline) लवणता में तीव्र बदलाव की परत को दर्शाता है", "type": "leaf"}
                    ]
                },
                {
                    "label": "घनत्व और पाइनोक्लाइन",
                    "type": "branch",
                    "date": "घनत्व",
                    "children": [
                        {"label": "घनत्व कारक: तापमान और लवणता पर निर्भर; ठंडा खारा जल सबसे सघन होता है", "type": "leaf"},
                        {"label": "पाइनोक्लाइन (Pycnocline): लंबवत घनत्व में तीव्र परिवर्तन की सीमा परत", "type": "leaf"}
                    ]
                },
                {
                    "label": "यूपीएससी वैश्विक गतिशीलता (UPSC Focus)",
                    "type": "branch",
                    "date": "संचरण",
                    "children": [
                        {"label": "थर्मोहेलाइन संचरण: तापमान और लवणता अंतर से संचालित वैश्विक महासागरीय जलधारा बेल्ट (Conveyor Belt)", "type": "leaf"},
                        {"label": "ध्रुवीय प्रभाव: ग्लोबल वार्मिंग से ग्लेशियरों का पिघलना सतह जल घनत्व कम कर प्रवाह को बाधित कर सकता है", "type": "leaf"}
                    ]
                }
            ]
        else:
            return [
                {
                    "label": "Temperature Distribution",
                    "type": "branch",
                    "date": "Temperature",
                    "children": [
                        {"label": "Horizontal Factors: Latitude, land-sea contrast, prevailing winds, and ocean currents", "type": "leaf"},
                        {"label": "Vertical Layers: Epilimnion (warm surface), Thermocline (rapid drop), Hypolimnion (cold deep)", "type": "leaf"}
                    ]
                },
                {
                    "label": "Salinity Controls",
                    "type": "branch",
                    "date": "Salinity",
                    "children": [
                        {"label": "Balance: Controlled by evaporation, precipitation, river runoff, and ice formation/melting", "type": "leaf"},
                        {"label": "Halocline: Vertical layer where salinity changes rapidly; highest salinity in enclosed seas (e.g., Red Sea)", "type": "leaf"}
                    ]
                },
                {
                    "label": "Ocean Density Factors",
                    "type": "branch",
                    "date": "Density",
                    "children": [
                        {"label": "Parameters: Function of temperature (negative relation) and salinity (positive relation)", "type": "leaf"},
                        {"label": "Pycnocline: Subsurface layer of rapid density change, separating light surface water from dense deep water", "type": "leaf"}
                    ]
                },
                {
                    "label": "UPSC Geostrophic Dynamics",
                    "type": "branch",
                    "date": "Thermohaline",
                    "children": [
                        {"label": "Thermohaline Circulation: Density-driven deep ocean currents ('Global Conveyor Belt') regulating planetary heat distribution", "type": "leaf"},
                        {"label": "Climate Impact: Melting of Arctic/Greenland ice caps adds fresh water, potentially slowing down Gulf Stream/AMOC", "type": "leaf"}
                    ]
                }
            ]

    # 4. Ocean Movements (Waves, Tides, Currents)
    elif any(k in fl for k in ['movement', 'wave', 'current', 'tide', 'tides']):
        if is_hindi:
            return [
                {
                    "label": "तरंगें और ज्वार-भाटा",
                    "type": "branch",
                    "date": "तरंग व ज्वार",
                    "children": [
                        {"label": "तरंगें: हवा की ऊर्जा का सतही संचरण; कण वृत्ताकार मार्ग में दोलन करते हैं", "type": "leaf"},
                        {"label": "ज्वार-भाटा: सूर्य और चंद्रमा के गुरुत्वाकर्षण खिंचाव से सागर जल का उत्थान और पतन", "type": "leaf"},
                        {"label": "प्रकार: वृहत ज्वार (Spring - युति-वियुति) और लघु ज्वार (Neap - समकोण स्थिति)", "type": "leaf"}
                    ]
                },
                {
                    "label": "महासागरीय जलधाराएं (Currents)",
                    "type": "branch",
                    "date": "जलधाराएं",
                    "children": [
                        {"label": "प्राथमिक चालक बल: सौर ऊर्जा, हवा की दिशा (व्यापारिक/पछुआ), कोरिओलिस बल", "type": "leaf"},
                        {"label": "द्वितियक कारक: तापमान और लवणता के अंतर से उत्पन्न घनत्व प्रवणता", "type": "leaf"}
                    ]
                },
                {
                    "label": "वैश्विक जलधारा प्रणालियां",
                    "type": "branch",
                    "date": "जलधारा चक्र",
                    "children": [
                        {"label": "अटलांटिक: गल्फ स्ट्रीम (गर्म), लैब्राडोर (ठंडी); प्रशांत: क्यूरोशियो (गर्म), ओयाशियो (ठंडी)", "type": "leaf"},
                        {"label": "हिंद महासागर: मानसून पवनों के कारण जलधाराओं की दिशा में मौसमी बदलाव (Monsoon Drift)", "type": "leaf"}
                    ]
                },
                {
                    "label": "यूपीएससी जलवायु संबंध (UPSC Focus)",
                    "type": "branch",
                    "date": "जलवायु प्रभाव",
                    "children": [
                        {"label": "ENSO और IOD: अल नीनो और हिंद महासागर द्विध्रुव का भारतीय मानसून पर प्रभाव", "type": "leaf"},
                        {"label": "रेगिस्तान निर्माण: ठंडी जलधाराएं तटीय क्षेत्रों में शुष्क वायु उत्पन्न कर मरुस्थलीकरण (जैसे अटाकामा) को बढ़ावा देती हैं", "type": "leaf"}
                    ]
                }
            ]
        else:
            return [
                {
                    "label": "Waves & Tides Dynamics",
                    "type": "branch",
                    "date": "Waves & Tides",
                    "children": [
                        {"label": "Waves: Wind energy transfer; orbital motion of water particles with no net forward mass transport", "type": "leaf"},
                        {"label": "Tides: Periodic rise and fall of sea levels due to gravitational forces of Moon, Sun, and Earth's rotation", "type": "leaf"},
                        {"label": "Spring vs Neap: Spring tides occur during Syzygy (highest tides); Neap tides occur during Quadrature (lowest range)", "type": "leaf"}
                    ]
                },
                {
                    "label": "Ocean Currents Drivers",
                    "type": "branch",
                    "date": "Currents",
                    "children": [
                        {"label": "Primary Factors: Prevailing planetary winds (Trade winds, Westerlies), Coriolis force deflecting flow, and insolation warming", "type": "leaf"},
                        {"label": "Secondary Factors: Gravity, coastal configuration, and salinity/temperature gradient variations", "type": "leaf"}
                    ]
                },
                {
                    "label": "Major Planetary Gyres",
                    "type": "branch",
                    "date": "Gyres",
                    "children": [
                        {"label": "Atlantic: Gulf Stream (warm, accelerates NE), Labrador Current (cold, polar feed)", "type": "leaf"},
                        {"label": "Pacific: Kuroshio (warm, north flow), Oyashio (cold, subarctic flow)", "type": "leaf"},
                        {"label": "Indian Ocean: Unique seasonal reversal of currents driven by Monsoon wind change", "type": "leaf"}
                    ]
                },
                {
                    "label": "UPSC Climatic Teleconnections",
                    "type": "branch",
                    "date": "ENSO & Monsoon",
                    "children": [
                        {"label": "ENSO Cycles: El Niño (weakens Indian Monsoon) and La Niña (strengthens it) teleconnections", "type": "leaf"},
                        {"label": "Indian Ocean Dipole: Positive IOD (warm Western Indian Ocean) offsets El Niño drought effects in India", "type": "leaf"},
                        {"label": "Desert Link: Cold currents on western coasts stabilize atmosphere, creating coastal deserts (e.g. Namib, Atacama)", "type": "leaf"}
                    ]
                }
            ]

    # 5. Coral Reefs & Great Barrier Reef
    elif any(k in fl for k in ['coral', 'reef', 'barrier', 'great-barrier-reef']):
        if is_hindi:
            return [
                {
                    "label": "प्रवाल भित्ति: प्रकार और वितरण",
                    "type": "branch",
                    "date": "वर्गीकरण",
                    "children": [
                        {"label": "तटीय प्रवाल भित्ति (Fringing): तट के समीप; लक्षद्वीप, मन्नार की खाड़ी", "type": "leaf"},
                        {"label": "अवरोधक प्रवाल भित्ति (Barrier): तट से दूर, चौड़ा लैगून; ग्रेट बैरियर रीफ (ऑस्ट्रेलिया)", "type": "leaf"},
                        {"label": "वलयाकार (Atoll): द्वीप के सबसिडेंस से वलयाकार आकृति; लक्षद्वीप के अधिकांश द्वीप", "type": "leaf"}
                    ]
                },
                {
                    "label": "विकास की आवश्यक परिस्थितियां",
                    "type": "branch",
                    "date": "परिस्थितियां",
                    "children": [
                        {"label": "तापमान: 20°C से 28°C; गहराई: उथला जल (<50m) ताकि सूर्यप्रकाश पहुंच सके", "type": "leaf"},
                        {"label": "लवणता: 27 से 30 ppt; स्वच्छ, अवसाद-मुक्त जल (ताकि प्रवाल के मुंह बंद न हों)", "type": "leaf"},
                        {"label": "सहजीवन: जूक्सैंथेले (Zooxanthellae) शैवाल प्रवाल को भोजन व रंग देता है", "type": "leaf"}
                    ]
                },
                {
                    "label": "खतरे और प्रवाल विरंजन",
                    "type": "branch",
                    "date": "खतरे",
                    "children": [
                        {"label": "प्रवाल विरंजन (Bleaching): तापमान वृद्धि से शैवाल का निष्कासन जिससे प्रवाल सफेद हो मर जाते हैं", "type": "leaf"},
                        {"label": "महासागरीय अम्लीकरण: CO₂ अवशोषण से pH कम होना; कैल्शियम कार्बोनेट खोल कमजोर पड़ना", "type": "leaf"}
                    ]
                },
                {
                    "label": "यूपीएससी परीक्षा दृष्टिकोण (UPSC Focus)",
                    "type": "branch",
                    "date": "भारत और नीतियां",
                    "children": [
                        {"label": "भारतीय प्रवाल क्षेत्र: लक्षद्वीप, मन्नार की खाड़ी, अंडमान व निकोबार, कच्छ की खाड़ी; तटीय विनियमन क्षेत्र (CRZ) के तहत संरक्षित", "type": "leaf"},
                        {"label": "ग्रेट बैरियर रीफ: यूनेस्को विश्व धरोहर संरक्षण चुनौतियाँ और जलवायु शमन कार्य", "type": "leaf"}
                    ]
                }
            ]
        else:
            return [
                {
                    "label": "Coral Reef Formations",
                    "type": "branch",
                    "date": "Classification",
                    "children": [
                        {"label": "Fringing Reefs: Directly fringe coastal margins; e.g. Gulf of Mannar, Andaman Islands", "type": "leaf"},
                        {"label": "Barrier Reefs: Off-shore walls separated by lagoons; Great Barrier Reef (Australia)", "type": "leaf"},
                        {"label": "Atolls: Circular rings enclosing deep lagoon; volcanic subsidence model by Darwin", "type": "leaf"}
                    ]
                },
                {
                    "label": "Ideal Growth Conditions",
                    "type": "branch",
                    "date": "Parameters",
                    "children": [
                        {"label": "Temperature: Warm ocean waters $20^\\circ\\text{C}-28^\\circ\\text{C}$; Depth: Photic zone < 50m", "type": "leaf"},
                        {"label": "Salinity: High but stable (27-30 ppt); Sediment-free waters: Mud chokes polyps", "type": "leaf"},
                        {"label": "Symbiosis: Zooxanthellae algae provides corals organic food; corals provide shelter", "type": "leaf"}
                    ]
                },
                {
                    "label": "Bleaching & Acidification",
                    "type": "branch",
                    "date": "Threats",
                    "children": [
                        {"label": "Coral Bleaching: Sea surface temperature anomaly forces expulsion of zooxanthellae", "type": "leaf"},
                        {"label": "Ocean Acidification: Higher atmospheric CO2 lowers ocean pH, limiting carbonate availability for reef calcification", "type": "leaf"}
                    ]
                },
                {
                    "label": "UPSC Conservation Focus",
                    "type": "branch",
                    "date": "India Reefs",
                    "children": [
                        {"label": "Indian Reef Areas: Andaman & Nicobar, Lakshadweep, Gulf of Mannar, Gulf of Kutch; protected under Wildlife Protection Act (Schedule I)", "type": "leaf"},
                        {"label": "GBR Threats: UNESCO World Heritage status reviews, crown-of-thorns starfish outbreaks, and climate restoration strategies", "type": "leaf"}
                    ]
                }
            ]

    # 6. Hydrological Cycle & Water Resources
    elif any(k in fl for k in ['cycle', 'process', 'conservation', 'inland', 'resource', 'resources', 'surface-water', 'consumption', 'water-on-the-surface', 'hydrological', 'underground']):
        if is_hindi:
            return [
                {
                    "label": "जल विज्ञान चक्र की प्रक्रियाएं",
                    "type": "branch",
                    "date": "प्रक्रियाएं",
                    "children": [
                        {"label": "घटक: वाष्पीकरण (80% महासागरों से), वाष्पोत्सर्जन (पौधों से), संघनन (बादल निर्माण), अवक्षेपण (वर्षा/हिम)", "type": "leaf"},
                        {"label": "अंतःस्यंदन (Infiltration): वर्षा जल का भूमि में प्रवेश जिससे भूजल रिचार्ज होता है", "type": "leaf"}
                    ]
                },
                {
                    "label": "मीठे जल के संसाधन (Freshwater)",
                    "type": "branch",
                    "date": "जल वितरण",
                    "children": [
                        {"label": "वैश्विक वितरण: 97.5% खारा पानी; केवल 2.5% मीठा पानी (जिसका 70% ग्लेशियरों में, 30% भूजल में है)", "type": "leaf"},
                        {"label": "सतही जल: नदियाँ, झीलें; भूजल: जलभृत (Aquifers) में संचित; भारत भूजल का सबसे बड़ा उपयोगकर्ता है", "type": "leaf"}
                    ]
                },
                {
                    "label": "संरक्षण विधियाँ और नीतियाँ",
                    "type": "branch",
                    "date": "शमन",
                    "children": [
                        {"label": "पारंपरिक तरीके: वर्षा जल संचयन, जोहड़, चेक डैम (राजस्थान), बावड़ी का पुनरुद्धार", "type": "leaf"},
                        {"label": "आधुनिक कृषि: ड्रिप सिंचाई, स्प्रिंकलर्स, मल्चिंग जो 40-70% जल की बचत करते हैं", "type": "leaf"},
                        {"label": "नीति: जल जीवन मिशन, पीएम कृषि सिंचाई योजना, अटल भूजल योजना", "type": "leaf"}
                    ]
                },
                {
                    "label": "यूपीएससी संकट आयाम (UPSC Focus)",
                    "type": "branch",
                    "date": "जल संकट",
                    "children": [
                        {"label": "नीति आयोग रिपोर्ट: 21 प्रमुख शहरों में भूजल समाप्त होने का खतरा; Day Zero परिदृश्य", "type": "leaf"},
                        {"label": "अंतर-राज्यीय जल विवाद: कावेरी, महादायी, कृष्णा नदी जल विवाद (अनुच्छेद 262)", "type": "leaf"}
                    ]
                }
            ]
        else:
            return [
                {
                    "label": "Hydrological Cycle Processes",
                    "type": "branch",
                    "date": "Processes",
                    "children": [
                        {"label": "Components: Evaporation (80% from oceans), Transpiration (flora), Condensation (clouds), Precipitation (rain/snow)", "type": "leaf"},
                        {"label": "Infiltration & Runoff: Water penetrating soil vs surface flow recharging lakes/rivers", "type": "leaf"}
                    ]
                },
                {
                    "label": "Global Freshwater Budget",
                    "type": "branch",
                    "date": "Water Budget",
                    "children": [
                        {"label": "Distribution: 97.5% saline; 2.5% freshwater. Of freshwater, 68.7% is in ice caps, 30.1% in groundwater, and only 1.2% is surface water", "type": "leaf"},
                        {"label": "Groundwater Crisis: Aquifer depletion due to over-extraction for agriculture; India is world's largest groundwater consumer", "type": "leaf"}
                    ]
                },
                {
                    "label": "Conservation & Policy",
                    "type": "branch",
                    "date": "Conservation",
                    "children": [
                        {"label": "Traditional Methods: Johads, Check Dams, stepwells, watershed management", "type": "leaf"},
                        {"label": "Micro-Irrigation: Drip and sprinkler systems under 'More Crop Per Drop' initiative", "type": "leaf"},
                        {"label": "Government Schemes: Jal Jeevan Mission, Atal Bhujal Yojana, and PM Krishi Sinchayee Yojana", "type": "leaf"}
                    ]
                },
                {
                    "label": "UPSC Exam Focus Dimensions",
                    "type": "branch",
                    "date": "Crisis & Law",
                    "children": [
                        {"label": "Composite Water Index: NITI Aayog warnings on groundwater exhaustion and Day Zero scenarios in major cities", "type": "leaf"},
                        {"label": "Inter-State River Disputes: Legal framework (Article 262, Inter-State River Water Disputes Act 1956) and tribunal cases (e.g. Cauvery, Krishna)", "type": "leaf"}
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

def main():
    total = 0
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
