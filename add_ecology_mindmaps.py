#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import re
import json

BASE_DIR = r"upsc/environment/Basic-Concepts-of-Ecology-Ecosystems"

def get_clean_title(folder_name):
    # Split camelCase words like EcologicalSuccession to Ecological Succession
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
    
    # 1. Ecology Foundations & Types
    if any(k in fl for k in ['difference-between-ecology', 'scope-of-ecology', 'types-of-ecology', 'deep-vs-shallow', 'ecological-principles']):
        if is_hindi:
            return [
                {
                    "label": "पारिस्थितिकी बनाम पर्यावरण बनाम पारितंत्र",
                    "type": "branch",
                    "date": "मूल बातें",
                    "children": [
                        {"label": "पारिस्थितिकी (Ecology): जीवों और उनके पर्यावरण के आपसी संबंधों का वैज्ञानिक अध्ययन", "type": "leaf"},
                        {"label": "पारितंत्र (Ecosystem): जीवमंडल की कार्यात्मक इकाई जिसमें जैविक और अजैविक घटक शामिल हैं", "type": "leaf"}
                    ]
                },
                {
                    "label": "पारिस्थितिकी के प्रकार (Types)",
                    "type": "branch",
                    "date": "प्रकार",
                    "children": [
                        {"label": "स्वपारिस्थितिकी (Autecology): एक ही प्रजाति का अध्ययन; समुदाय पारिस्थितिकी (Synecology): अनेक प्रजातियों का समूह अध्ययन", "type": "leaf"},
                        {"label": "गहन पारिस्थितिकी (Deep Ecology): प्रकृति-केंद्रित (Ecocentric); सभी जीवों का समान महत्व; प्रणेता - अर्ने नेस (1973)", "type": "leaf"},
                        {"label": "सतही पारिस्थितिकी (Shallow Ecology): मानव-केंद्रित (Anthropocentric); प्रकृति का उपयोग मानव विकास के लिए करना", "type": "leaf"}
                    ]
                },
                {
                    "label": "पारिस्थितिक सिद्धांत (Principles)",
                    "type": "branch",
                    "date": "सिद्धांत",
                    "children": [
                        {"label": "समस्थापन (Homeostasis): पारितंत्र की स्वतः नियंत्रण क्षमता (Self-regulation)", "type": "leaf"},
                        {"label": "वहन क्षमता (Carrying Capacity): किसी पर्यावरण द्वारा समर्थित जीवों की अधिकतम संख्या", "type": "leaf"}
                    ]
                },
                {
                    "label": "यूपीएससी परीक्षा दृष्टिकोण (UPSC Focus)",
                    "type": "branch",
                    "date": "विचारक",
                    "children": [
                        {"label": "इतिहास: अर्न्स्ट हेकेल ने 1866 में 'Ecology' शब्द दिया; ए.जी. टांसले ने 1935 में 'Ecosystem' शब्द दिया", "type": "leaf"},
                        {"label": "रेचल कार्सन: पुस्तक 'Silent Spring' (1962), जिसने वैश्विक पर्यावरण आंदोलन को जन्म दिया", "type": "leaf"}
                    ]
                }
            ]
        else:
            return [
                {
                    "label": "Ecology vs Environment vs Ecosystem",
                    "type": "branch",
                    "date": "Basics",
                    "children": [
                        {"label": "Ecology: Scientific study of interactions between organisms and their physical/biotic environment", "type": "leaf"},
                        {"label": "Ecosystem: Structural and functional unit of biosphere consisting of a community of living beings and abiotic components", "type": "leaf"}
                    ]
                },
                {
                    "label": "Deep vs Shallow Ecology",
                    "type": "branch",
                    "date": "Philosophies",
                    "children": [
                        {"label": "Deep Ecology (Ecocentric): Believes all life forms have intrinsic value; calls for radical change in human lifestyles; coined by Arne Naess", "type": "leaf"},
                        {"label": "Shallow Ecology (Anthropocentric): Focuses on conservation merely for human resource utility and survival", "type": "leaf"},
                        {"label": "Autecology vs Synecology: Study of individual species vs study of groups of species forming a community", "type": "leaf"}
                    ]
                },
                {
                    "label": "Ecological Principles",
                    "type": "branch",
                    "date": "Principles",
                    "children": [
                        {"label": "Homeostasis: Self-regulating feedback mechanisms that maintain stable equilibrium in ecosystems", "type": "leaf"},
                        {"label": "Limiting Factors: Liebig's Law of Minimum and Shelford's Law of Tolerance governing species distribution", "type": "leaf"}
                    ]
                },
                {
                    "label": "UPSC Core & Thinkers",
                    "type": "branch",
                    "date": "Timeline",
                    "children": [
                        {"label": "Terminology: Ernst Haeckel (1866 - 'Oekologie'); A.G. Tansley (1935 - 'Ecosystem'); Charles Elton (animal ecology)", "type": "leaf"},
                        {"label": "Rachel Carson: 'Silent Spring' (1962) exposing synthetic pesticide (DDT) hazards, starting modern environmentalism", "type": "leaf"}
                    ]
                }
            ]

    # 2. Ecosystem Structure & Components
    elif any(k in fl for k in ['definition', 'components', 'abiotic', 'biotic', 'niche', 'ecotone', 'stratification', 'tolerance', 'properties-of-ecosystem']):
        if is_hindi:
            return [
                {
                    "label": "जैविक और अजैविक घटक",
                    "type": "branch",
                    "date": "घटक",
                    "children": [
                        {"label": "अजैविक घटक: तापमान (सर्वाधिक महत्वपूर्ण), जल, प्रकाश, पवन, मृदा pH और लवणता", "type": "leaf"},
                        {"label": "जैविक घटक: उत्पादक (स्वपोषी), उपभोक्ता (परपोषी - शाकाहारी/मांसाहारी), अपघटक (कवक/जीवाणु)", "type": "leaf"}
                    ]
                },
                {
                    "label": "आवास बनाम पारिस्थितिक निकेत (Niche)",
                    "type": "branch",
                    "date": "निकेत",
                    "children": [
                        {"label": "आवास (Habitat): वह भौतिक स्थान जहाँ जीव रहता है (जीव का पता)", "type": "leaf"},
                        {"label": "पारिस्थितिक निकेत (Niche): जीव की क्रियात्मक भूमिका और संसाधन उपयोग (जीव का पेशा)", "type": "leaf"},
                        {"label": "गौस का प्रतिस्पर्धी अपवर्जन सिद्धांत: दो प्रजातियाँ एक ही निकेत में लंबे समय तक नहीं रह सकतीं", "type": "leaf"}
                    ]
                },
                {
                    "label": "संक्रमणिका (Ecotone) और कोर प्रभाव",
                    "type": "branch",
                    "date": "संक्रमणिका",
                    "children": [
                        {"label": "संक्रमणिका (Ecotone): दो अलग पारितंत्रों का मिलन क्षेत्र (जैसे मैंग्रोव, आर्द्रभूमि)", "type": "leaf"},
                        {"label": "कोर प्रभाव (Edge Effect): संक्रमणिका में दोनों पारितंत्रों की तुलना में अधिक प्रजाति घनत्व होना (जैसे पक्षी प्रजातियाँ)", "type": "leaf"}
                    ]
                },
                {
                    "label": "यूपीएससी परीक्षा दृष्टिकोण (UPSC Focus)",
                    "type": "branch",
                    "date": "शब्दावली",
                    "children": [
                        {"label": "पारिस्थितिक स्तरीकरण (Stratification): वनों में विभिन्न ऊंचाइयों पर वनस्पतियों की लंबवत परतें (जैसे वितान, झाड़ियां, जड़ी-बूटियां)", "type": "leaf"},
                        {"label": "सहनशीलता सीमा: शेलफोर्ड का सहनशीलता नियम; सीमा से बाहर जीव जीवित नहीं रह सकता", "type": "leaf"}
                    ]
                }
            ]
        else:
            return [
                {
                    "label": "Abiotic vs Biotic Factors",
                    "type": "branch",
                    "date": "Components",
                    "children": [
                        {"label": "Abiotic: Temperature (most critical), moisture/water, solar radiation, wind patterns, and soil profile characteristics", "type": "leaf"},
                        {"label": "Biotic: Primary producers (autotrophs), consumers (herbivores, carnivores, omnivores), and decomposers/detritivores", "type": "leaf"}
                    ]
                },
                {
                    "label": "Habitat vs Ecological Niche",
                    "type": "branch",
                    "date": "Niche",
                    "children": [
                        {"label": "Habitat: Physical address of an organism; Niche: Functional role and resource utility spectrum of a species", "type": "leaf"},
                        {"label": "Competitive Exclusion: Gause's Principle stating that two species competing for identical resources cannot coexist stably in the same niche", "type": "leaf"}
                    ]
                },
                {
                    "label": "Ecotone & Edge Effect",
                    "type": "branch",
                    "date": "Boundary",
                    "children": [
                        {"label": "Ecotone: Transition zone between two distinct ecosystems (e.g. estuaries, marshlands, forest edge)", "type": "leaf"},
                        {"label": "Edge Effect: Increased population density and diversity of species at the ecotone boundary (e.g. high avian species variety)", "type": "leaf"}
                    ]
                },
                {
                    "label": "UPSC Structural Dynamics",
                    "type": "branch",
                    "date": "Stratification",
                    "children": [
                        {"label": "Ecological Stratification: Vertical layering of vegetation based on light availability (e.g., Canopy, Understory, Forest Floor)", "type": "leaf"},
                        {"label": "Ecological Indicators: Species whose presence/absence indicates environmental health (e.g. lichens for sulfur dioxide pollution)", "type": "leaf"}
                    ]
                }
            ]

    # 3. Energy Flow & Trophic Dynamics
    elif any(k in fl for k in ['flow-of-energy', 'models-for-energy', 'food-chain', 'food-web', 'trophic-levels', 'pyramid', 'biomagnification', 'productivity']):
        if is_hindi:
            return [
                {
                    "label": "पारितंत्र में ऊर्जा प्रवाह",
                    "type": "branch",
                    "date": "ऊर्जा प्रवाह",
                    "children": [
                        {"label": "एकदिशीय प्रवाह: सूर्य से उत्पादक और फिर उपभोक्ताओं की ओर; वापस चक्रित नहीं होती", "type": "leaf"},
                        {"label": "लिंडमैन का 10% नियम: एक पोषण स्तर से अगले में केवल 10% ऊर्जा स्थानांतरित होती है; 90% श्वसन/ऊष्मा में नष्ट", "type": "leaf"}
                    ]
                },
                {
                    "label": "खाद्य श्रृंखला और खाद्य जाल",
                    "type": "branch",
                    "date": "खाद्य जाल",
                    "children": [
                        {"label": "चारण खाद्य श्रृंखला (Grazing): जीवित पौधों से शुरू; अपरद श्रृंखला (Detritus): मृत कार्बनिक पदार्थों से शुरू", "type": "leaf"},
                        {"label": "खाद्य जाल (Food Web): अनेक श्रृंखलाओं का नेटवर्क; पारितंत्र की स्थिरता बढ़ाता है", "type": "leaf"}
                    ]
                },
                {
                    "label": "पारिस्थितिक स्तूप (Pyramids)",
                    "type": "branch",
                    "date": "स्तूप",
                    "children": [
                        {"label": "संख्या स्तूप: सीधा या उल्टा (पेड़ पर परजीवी) हो सकता है; जैवभार स्तूप: जलीय पारितंत्र में उल्टा (फाइटोप्लांकटन < जूप्लांकटन)", "type": "leaf"},
                        {"label": "ऊर्जा स्तूप: सदैव सीधा (Upright) होता है; थर्मोडायनामिक्स के नियमों के कारण", "type": "leaf"}
                    ]
                },
                {
                    "label": "जैव-संचयन बनाम जैव-आवर्धन",
                    "type": "branch",
                    "date": "यूपीएससी परीक्षा",
                    "children": [
                        {"label": "जैव-संचयन (Bioaccumulation): एक जीव के शरीर में प्रदूषक (जैसे DDT, मरकरी) का समय के साथ जमा होना", "type": "leaf"},
                        {"label": "जैव-आवर्धन (Biomagnification): पोषण स्तरों में ऊपर जाने पर प्रदूषक सांद्रता का बढ़ना (जैसे बाज में सर्वाधिक DDT सांद्रता)", "type": "leaf"}
                    ]
                }
            ]
        else:
            return [
                {
                    "label": "Energy Flow Dynamics",
                    "type": "branch",
                    "date": "Energy Flow",
                    "children": [
                        {"label": "Unidirectional Flow: Energy moves linearly from Sun -> Producers -> Consumers -> Decomposers; never recycled", "type": "leaf"},
                        {"label": "Lindeman's 10% Law: Only ~10% of energy at one trophic level is transferred to the next; 90% lost as heat/respiration", "type": "leaf"}
                    ]
                },
                {
                    "label": "Trophic Structures",
                    "type": "branch",
                    "date": "Food Web",
                    "children": [
                        {"label": "Grazing Food Chain (GFC): Starts with autotrophs; Detritus Food Chain (DFC): Starts with dead organic matter/waste", "type": "leaf"},
                        {"label": "Food Web: Network of interlocking food chains; provides alternative feeding pathways, stabilizing the ecosystem", "type": "leaf"}
                    ]
                },
                {
                    "label": "Ecological Pyramids",
                    "type": "branch",
                    "date": "Pyramids",
                    "children": [
                        {"label": "Pyramid of Numbers: Can be upright or inverted (e.g. single oak tree supporting thousands of insects)", "type": "leaf"},
                        {"label": "Pyramid of Biomass: Upright on land; inverted in aquatic systems due to high turnover rates of tiny phytoplanktons", "type": "leaf"},
                        {"label": "Pyramid of Energy: Always upright without exception, conforming to the Second Law of Thermodynamics", "type": "leaf"}
                    ]
                },
                {
                    "label": "Bioaccumulation & Biomagnification",
                    "type": "branch",
                    "date": "Toxicology",
                    "children": [
                        {"label": "Bioaccumulation: Increase in concentration of a chemical in a single organism over time relative to environmental levels", "type": "leaf"},
                        {"label": "Biomagnification: Progressive increase in chemical concentration up the food chain (e.g. DDT thinning raptor eggshells, Mercury in fish)", "type": "leaf"}
                    ]
                }
            ]

    # 4. Population & Community Ecology
    elif any(k in fl for k in ['population', 'community', 'dominance', 'types-of-species', 'census']):
        if is_hindi:
            return [
                {
                    "label": "समष्टि पारिस्थितिकी (Population)",
                    "type": "branch",
                    "date": "समष्टि",
                    "children": [
                        {"label": "गुण: जन्म दर, मृत्यु दर, लिंग अनुपात और आयु पिरामिड (विस्तारित, स्थिर, घटता हुआ)", "type": "leaf"},
                        {"label": "जनसंख्या वृद्धि मॉडल: घातांकीय वृद्धि (J-आकार, असीमित संसाधन) और लॉजिस्टिक वृद्धि (S-आकार, वहन क्षमता K)", "type": "leaf"}
                    ]
                },
                {
                    "label": "महत्वपूर्ण प्रजातियों के प्रकार",
                    "type": "branch",
                    "date": "प्रजातियां",
                    "children": [
                        {"label": "कीस्टोन प्रजाति (Keystone): संख्या कम होने पर भी पारितंत्र पर अत्यधिक प्रभाव (जैसे बाघ, समुद्री ऊदबिलाव)", "type": "leaf"},
                        {"label": "सूचक प्रजाति (Indicator): पर्यावरण प्रदूषण के प्रति संवेदनशील (जैसे लाइकेन - SO2 प्रदूषण सूचक)", "type": "leaf"},
                        {"label": "फ्लेगशिप प्रजाति: संरक्षण हेतु चुनी गई लोकप्रिय प्रजाति (जैसे पांडा, बंगाल टाइगर)", "type": "leaf"}
                    ]
                },
                {
                    "label": "सामुदायिक संरचना (Community)",
                    "type": "branch",
                    "date": "समुदाय",
                    "children": [
                        {"label": "पारिस्थितिक प्रभुत्व (Dominance): किसी समुदाय में सबसे अधिक संख्या या जैवभार वाली प्रजाति", "type": "leaf"},
                        {"label": "सामुदायिक विशेषताएं: प्रजाति विविधता, स्तरीकरण और अंतःक्रियाएं", "type": "leaf"}
                    ]
                },
                {
                    "label": "यूपीएससी जनगणना (Census Focus)",
                    "type": "branch",
                    "date": "गणना",
                    "children": [
                        {"label": "बाघ जनगणना: NTCA द्वारा हर 4 साल में; M-STrIPES ऐप तकनीक और कैमरा ट्रैपिंग का उपयोग", "type": "leaf"},
                        {"label": "एशियाई शेर जनगणना: गुजरात वन विभाग द्वारा गिर वन क्षेत्र में प्रत्येक 5 वर्ष में (ब्लॉक काउंट विधि)", "type": "leaf"}
                    ]
                }
            ]
        else:
            return [
                {
                    "label": "Population Ecology Attributes",
                    "type": "branch",
                    "date": "Population",
                    "children": [
                        {"label": "Metrics: Density, natality (birth rate), mortality (death rate), sex ratio, and age distribution pyramids", "type": "leaf"},
                        {"label": "Growth Models: Exponential growth (J-curve; $dN/dt = rN$); Logistic growth (S-curve; $dN/dt = rN(1-N/K)$)", "type": "leaf"}
                    ]
                },
                {
                    "label": "Key Species Concept Types",
                    "type": "branch",
                    "date": "Species Roles",
                    "children": [
                        {"label": "Keystone Species: Crucial role in maintaining community structure; removal collapses system (e.g. Sea Otter, Tiger)", "type": "leaf"},
                        {"label": "Indicator Species: Presence/absence reveals environmental status (e.g. lichens for air quality; benthic macroinvertebrates for water)", "type": "leaf"},
                        {"label": "Foundation Species: Creates or defines the habitat (e.g. Kelp, Corals); Flagship: Icon for conservation (e.g. Giant Panda)", "type": "leaf"}
                    ]
                },
                {
                    "label": "Community Ecology Dynamics",
                    "type": "branch",
                    "date": "Community",
                    "children": [
                        {"label": "Species Richness: Number of different species in a community; Evenness: Relative abundance of individuals of each species", "type": "leaf"},
                        {"label": "Ecological Dominance: Species that exerts powerful control over community dynamics (typically largest biomass)", "type": "leaf"}
                    ]
                },
                {
                    "label": "UPSC Wildlife Census Focus",
                    "type": "branch",
                    "date": "Census Methods",
                    "children": [
                        {"label": "Tiger Census: Quadrennial (every 4 years) by NTCA/WII; utilizes M-STrIPES GIS tool and double-sampling camera trap grids", "type": "leaf"},
                        {"label": "Lion Census: Quintennial (every 5 years) in Gir Forest; uses direct sighting block count and waterhole telemetry", "type": "leaf"}
                    ]
                }
            ]

    # 5. Ecological Succession & Interactions
    elif any(k in fl for k in ['succession', 'climax', 'interaction', 'adaptation', 'biological-control', 'dynamics', 'interdependence', 'periodicity', 'fluctuation', 'turnover']):
        if is_hindi:
            return [
                {
                    "label": "पारिस्थितिक अनुक्रमण (Succession)",
                    "type": "branch",
                    "date": "अनुक्रमण",
                    "children": [
                        {"label": "प्राथमिक अनुक्रमण (Primary): पूरी तरह नग्न क्षेत्र (जैसे लावा, नग्न चट्टान) पर शुरू; अत्यधिक धीमा प्रक्रम", "type": "leaf"},
                        {"label": "द्वितीयक अनुक्रमण (Secondary): पहले से मौजूद मिट्टी पर शुरू (जैसे जला हुआ वन); अधिक तीव्र गति", "type": "leaf"},
                        {"label": "अनुक्रमण चरण: नग्नन (Nudation) -> आक्रमण (Invasion/Ecesis) -> प्रतिस्पर्धा -> प्रतिक्रिया -> चरम (Climax) समुदाय", "type": "leaf"}
                    ]
                },
                {
                    "label": "प्रजाति अंतःक्रियाएं (Interactions)",
                    "type": "branch",
                    "date": "अंतःक्रियाएं",
                    "children": [
                        {"label": "सकारात्मक अंतःक्रियाएं: सहोपकारिता (Mutualism - +/+; जैसे कवक और शैवाल का लाइकेन), सहभोजिता (Commensalism - +/0)", "type": "leaf"},
                        {"label": "नकारात्मक अंतःक्रियाएं: परजीविता (Parasitism - +/-), असहभोजिता (Amensalism - -/0; जैसे पेनिसिलियम जीवाणु नाशक)", "type": "leaf"}
                    ]
                },
                {
                    "label": "जैविक नियंत्रण (Biological Control)",
                    "type": "branch",
                    "date": "जैविक नियंत्रण",
                    "children": [
                        {"label": "अवधारणा: रासायनिक कीटनाशकों के स्थान पर प्राकृतिक शिकारियों (Predators) का उपयोग करना", "type": "leaf"},
                        {"label": "उदाहरण: गंबूशिया मछली (मच्छर लार्वा भक्षण), लेडीबग कीट (एफिड्स का जैविक नियंत्रण)", "type": "leaf"}
                    ]
                },
                {
                    "label": "पारितंत्र गतिशीलता और आवर्तता",
                    "type": "branch",
                    "date": "यूपीएससी परीक्षा",
                    "children": [
                        {"label": "पारिस्थितिक आवर्तता (Periodicity): मौसमी और दैनिक बदलावों के अनुसार जीवों की गतिविधि प्रवृत्तियां", "type": "leaf"},
                        {"label": "टर्नओवर (Turnover): झीलों में पानी का मौसमी मिश्रण (Thermal Stratification & Overturn) जो ऑक्सीजन और पोषक तत्वों का प्रसार करता है", "type": "leaf"}
                    ]
                }
            ]
        else:
            return [
                {
                    "label": "Ecological Succession Phases",
                    "type": "branch",
                    "date": "Succession",
                    "children": [
                        {"label": "Primary Succession: Initiates on barren substrate lacking soil (e.g. lava flows, sand dunes, bare rock); takes millennia", "type": "leaf"},
                        {"label": "Secondary Succession: Occurs where an ecosystem is disturbed but soil remains intact (e.g. abandoned farmland, burnt forest)", "type": "leaf"},
                        {"label": "Seral Stages: Nudation -> Invasion (Migration/Ecesis) -> Competition -> Reaction -> Climax Community (stable equilibrium)", "type": "leaf"}
                    ]
                },
                {
                    "label": "Biotic Species Interactions",
                    "type": "branch",
                    "date": "Interactions",
                    "children": [
                        {"label": "Positive: Mutualism (+/+; e.g. mycorrhizae, lichens), Commensalism (+/0; e.g. epiphytes, barnacles on whales)", "type": "leaf"},
                        {"label": "Negative: Parasitism (+/-), Competition (-/-), Amensalism (-/0; e.g., Penicillium producing penicillin inhibiting bacteria)", "type": "leaf"}
                    ]
                },
                {
                    "label": "Biological Control Models",
                    "type": "branch",
                    "date": "Bio-Control",
                    "children": [
                        {"label": "Mechanism: Regulating agricultural pests using natural predators/parasites instead of chemical pesticides", "type": "leaf"},
                        {"label": "Examples: Introducing Gambusia fish to consume mosquito larvae; Ladybugs to control crop aphids", "type": "leaf"}
                    ]
                },
                {
                    "label": "Dynamics & Turnover",
                    "type": "branch",
                    "date": "Periodicity",
                    "children": [
                        {"label": "Ecological Periodicity: Rhythmic behavior matched to diurnal (light/dark) or seasonal temperature cycles", "type": "leaf"},
                        {"label": "Lake Overturn: Semi-annual vertical mixing in temperate lakes replenishing oxygen to depth and nutrients to surface", "type": "leaf"}
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
