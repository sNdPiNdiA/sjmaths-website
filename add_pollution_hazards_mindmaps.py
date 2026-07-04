#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import re
import json

BASE_DIR = r"upsc/environment/Pollution-Occupational-Hazards"

def get_clean_title(folder_name):
    title = re.sub(r'([a-z])([A-Z])', r'\1 \2', folder_name)
    title = title.replace('-', ' ')
    words = []
    acronyms = {'dpsp', 'pri', 'ut', 'uts', 'sc', 'hc', 'cm', 'com', 'arc', 'inc', 'ias', 'sec', 'sfc', 'pej', 'tej', 'mjo', 'enso', 'iod', 'icar', 'gst', 'dpc', 'mpc', 'adc', 'tac', 'scs', 'pesa', 'icar', 'isfr', 'itcz', 'tej', 'iucn', 'wpa', 'grap', 'aqews', 'caaeqms', 'naqi', 'naaqs', 'rspm', 'bod', 'cod'}
    for w in title.split():
        if w.lower() in acronyms:
            words.append(w.upper())
        elif w.lower() in ['of', 'and', 'the', 'for', 'in', 'with', 'against', 'to', 'on', 'some', 'by', 'their', 'vs']:
            words.append(w.lower())
        else:
            words.append(w.capitalize())
    return ' '.join(words)

# Grouped dataset containing fact-rich mindmaps with colons to support sub-branch restructuring
GROUPS = [
    {
        "keys": ["air-pollution", "causes-of-air-pollution", "respirable-suspended-particulate-matter", "rspm"],
        "en": [
            {"label": "Particulate Matter (PM)", "type": "branch", "date": "PM Metrics", "children": [
                {"label": "PM2.5: Particulate matter with diameter <2.5 micrometers; penetrates deep into alveoli and enters bloodstream, causing cardiovascular disease", "type": "leaf"},
                {"label": "PM10: Coarse particulate matter with diameter <10 micrometers; trapped in nasal cavity and upper respiratory tract", "type": "leaf"}
            ]},
            {"label": "Primary vs Secondary", "type": "branch", "date": "Pollutants", "children": [
                {"label": "Primary Pollutants: Emitted directly from sources (e.g., Sulfur Dioxide (SO2) from coal plants, Carbon Monoxide (CO) from auto exhaust)", "type": "leaf"},
                {"label": "Secondary Pollutants: Formed in atmosphere via chemical reactions (e.g., Ground-level Ozone (O3) from NOx and VOC photochemical reactions; Acid Rain)", "type": "leaf"}
            ]},
            {"label": "Major Sources", "type": "branch", "date": "Sources", "children": [
                {"label": "Combustion: Coal-fired thermal power plants, vehicular exhaust, and industrial boilers", "type": "leaf"},
                {"label": "Agricultural burning: Stubble burning (parali) in Punjab and Haryana contributing to northern winter smog", "type": "leaf"}
            ]},
            {"label": "UPSC Exam Focus", "type": "branch", "date": "UPSC Focus", "children": [
                {"label": "National Clean Air Programme (NCAP): Targets 20-30% reduction in PM concentrations in 131 non-attainment cities", "type": "leaf"},
                {"label": "Soot/Black Carbon: Highly absorbing component of PM; accelerates glacier melt when deposited on Himalayan ice", "type": "leaf"}
            ]}
        ],
        "hi": [
            {"label": "कणिकीय पदार्थ (PM)", "type": "branch", "date": "कण", "children": [
                {"label": "PM2.5: व्यास <2.5 माइक्रोमीटर; फेफड़ों के एल्वियोली में प्रवेश कर हृदय रोगों का कारण बनता है", "type": "leaf"},
                {"label": "PM10: व्यास <10 माइक्रोमीटर; ऊपरी श्वसन मार्ग में फंस जाता है और अस्थमा को ट्रिगर करता है", "type": "leaf"}
            ]},
            {"label": "प्राथमिक बनाम द्वितीयक", "type": "branch", "date": "वर्गीकरण", "children": [
                {"label": "प्राथमिक प्रदूषक: सीधे स्रोतों से उत्सर्जित (जैसे कोयला संयंत्रों से SO2, ऑटो निकास से कार्बन मोनोऑक्साइड)", "type": "leaf"},
                {"label": "द्वितीयक प्रदूषक: रासायनिक प्रतिक्रियाओं से वायुमंडल में निर्मित (जैसे भू-स्तरीय ओजोन O3, सल्फ्यूरिक एसिड)", "type": "leaf"}
            ]},
            {"label": "प्रमुख स्रोत", "type": "branch", "date": "स्रोत", "children": [
                {"label": "दहन प्रक्रियाएं: कोयला आधारित बिजलीघर, वाहनों का धुआं और औद्योगिक भट्टियां", "type": "leaf"},
                {"label": "कृषि अवशेष दहन: पंजाब और हरियाणा में पराली जलाने से सर्दियों में सघन स्मॉग का निर्माण", "type": "leaf"}
            ]},
            {"label": "यूपीएससी परीक्षा दृष्टिकोण", "type": "branch", "date": "परीक्षा", "children": [
                {"label": "राष्ट्रीय स्वच्छ वायु कार्यक्रम (NCAP): 131 गैर-प्राप्ति वाले शहरों में PM सांद्रता में 20-30% की कमी का लक्ष्य", "type": "leaf"},
                {"label": "ब्लैक कार्बन: वायुमंडलीय अवशोषक; हिमालय के ग्लेशियरों पर जमा होकर बर्फ पिघलने को तेज करता है", "type": "leaf"}
            ]}
        ]
    },
    {
        "keys": ["graded-response-action-plan", "grap", "air-quality-early-warning"],
        "en": [
            {"label": "GRAP Implementation Stages", "type": "branch", "date": "Stages", "children": [
                {"label": "Stage I (Poor): Implemented when AQI is between 201-300; involves mechanical sweeping and dust control at sites", "type": "leaf"},
                {"label": "Stage II (Very Poor): AQI between 301-400; bans diesel generators, enhances parking fees to discourage private vehicles", "type": "leaf"},
                {"label": "Stage III (Severe): AQI between 401-450; bans non-essential construction and restricts BS-III petrol & BS-IV diesel vehicles", "type": "leaf"},
                {"label": "Stage IV (Severe Plus): AQI >450; bans entry of trucks into Delhi, halts clean construction, and initiates work from home", "type": "leaf"}
            ]},
            {"label": "Institutional Framework", "type": "branch", "date": "Institution", "children": [
                {"label": "CAQM: Commission for Air Quality Management in NCR and Adjoining Areas administers GRAP since 2021", "type": "leaf"},
                {"label": "Formulated originally by EPCA (Environment Pollution Prevention and Control Authority) under Supreme Court mandates", "type": "leaf"}
            ]},
            {"label": "Early Warning System (AQEWS)", "type": "branch", "date": "AQEWS", "children": [
                {"label": "Developed by Indian Institute of Tropical Meteorology (IITM) Pune to predict air quality indices 3 to 10 days in advance", "type": "leaf"},
                {"label": "Integrates satellite data on stubble burning and meteorological parameters (wind direction, mixing height)", "type": "leaf"}
            ]},
            {"label": "UPSC Exam Focus", "type": "branch", "date": "UPSC Focus", "children": [
                {"label": "Proactive vs Reactive: GRAP has transitioned from reactive (triggered after pollution spikes) to proactive (triggered by early warnings)", "type": "leaf"},
                {"label": "Delhi Smog factors: Low temperature, wind speed drop (<10 km/h), and thermal inversion trapping pollutants in winter", "type": "leaf"}
            ]}
        ],
        "hi": [
            {"label": "GRAP कार्यान्वयन के चरण", "type": "branch", "date": "चरण", "children": [
                {"label": "चरण I (खराब): AQI 201-300; निर्माण स्थलों पर धूल नियंत्रण और यांत्रिक सफाई शुरू करना", "type": "leaf"},
                {"label": "चरण II (बहुत खराब): AQI 301-400; डीजल जनरेटरों पर प्रतिबंध, पार्किंग शुल्क में वृद्धि", "type": "leaf"},
                {"label": "चरण III (गंभीर): AQI 401-450; गैर-आवश्यक निर्माण कार्यों और BS-III पेट्रोल व BS-IV डीजल वाहनों पर प्रतिबंध", "type": "leaf"},
                {"label": "चरण IV (अति गंभीर): AQI >450; दिल्ली में ट्रकों के प्रवेश पर रोक, सरकारी कार्यालयों में वर्क फ्रॉम होम", "type": "leaf"}
            ]},
            {"label": "संस्थागत ढांचा", "type": "branch", "date": "संस्थान", "children": [
                {"label": "CAQM: राष्ट्रीय राजधानी क्षेत्र और आसपास के क्षेत्रों में वायु गुणवत्ता प्रबंधन आयोग 2021 से GRAP संचालित करता है", "type": "leaf"},
                {"label": "मूल रूप से सुप्रीम कोर्ट के आदेशों के तहत EPCA द्वारा तैयार किया गया था", "type": "leaf"}
            ]},
            {"label": "प्रारंभिक चेतावनी प्रणाली (AQEWS)", "type": "branch", "date": "AQEWS", "children": [
                {"label": "भारतीय उष्णकटिबंधीय मौसम विज्ञान संस्थान (IITM) पुणे द्वारा 3 से 10 दिन पहले वायु गुणवत्ता का पूर्वानुमान लगाने हेतु विकसित", "type": "leaf"},
                {"label": "उपग्रहों द्वारा पराली जलाने के डेटा और मौसम कारकों (हवा की गति, मिश्रण ऊंचाई) को एकीकृत करता है", "type": "leaf"}
            ]},
            {"label": "यूपीएससी परीक्षा दृष्टिकोण", "type": "branch", "date": "परीक्षा", "children": [
                {"label": "सक्रिय शमन: GRAP अब प्रदूषण बढ़ने के बाद नहीं, बल्कि प्रारंभिक चेतावनी के आधार पर पहले ही लागू किया जाता है", "type": "leaf"},
                {"label": "दिल्ली स्मॉग के कारण: कम तापमान, हवा की गति में गिरावट (<10 किमी/घंटा) और तापीय प्रतिलोमन (Inversion)", "type": "leaf"}
            ]}
        ]
    },
    {
        "keys": ["basics-of-pollution", "sources-of-pollution", "classification-of-pollutants"],
        "en": [
            {"label": "Core Classifications", "type": "branch", "date": "Types", "children": [
                {"label": "Biodegradable: Broken down by microbial action into non-toxic residues (e.g. municipal sewage, paper)", "type": "leaf"},
                {"label": "Non-Biodegradable: Persist in environment, accumulating in trophic chains (e.g. DDT, heavy metals, plastics)", "type": "leaf"},
                {"label": "Quantitative: Natural compounds that turn into pollutants only when concentration exceeds thresholds (e.g. CO2, Nitrogen)", "type": "leaf"},
                {"label": "Qualitative: Synthetic compounds that are inherently toxic and do not exist in nature (e.g. DDT, pesticides)", "type": "leaf"}
            ]},
            {"label": "Sources of Pollutants", "type": "branch", "date": "Sources", "children": [
                {"label": "Point Sources: Discharging from a single, identifiable location (e.g. factory effluent pipe, smokestack)", "type": "leaf"},
                {"label": "Non-Point Sources: Diffuse emissions over large areas (e.g. agricultural runoff, urban street washings)", "type": "leaf"}
            ]},
            {"label": "Physical State", "type": "branch", "date": "States", "children": [
                {"label": "Gaseous Pollutants: SOx, NOx, Carbon Monoxide, and volatile organic compounds", "type": "leaf"},
                {"label": "Particulate Pollutants: Dust, fly ash, soot, and aerosol mists suspended in air", "type": "leaf"}
            ]},
            {"label": "UPSC Exam Focus", "type": "branch", "date": "UPSC Focus", "children": [
                {"label": "Bioaccumulation vs Biomagnification: Build-up in a single organism over time vs increase in concentration up the food chain", "type": "leaf"},
                {"label": "Synergistic effects: Two pollutants reacting to form a compound more toxic than either alone (e.g. SO2 and particulates)", "type": "leaf"}
            ]}
        ],
        "hi": [
            {"label": "मूल वर्गीकरण", "type": "branch", "date": "वर्गीकरण", "children": [
                {"label": "जैव-अपघटनीय: रोगाणुओं द्वारा हानिरहित अवशेषों में तोड़े जाने वाले पदार्थ (जैसे सीवेज, कागज)", "type": "leaf"},
                {"label": "गैर-जैव-अपघटनीय: वातावरण में लंबे समय तक बने रहने वाले और खाद्य जाल में जमा होने वाले पदार्थ (जैसे DDT, प्लास्टिक)", "type": "leaf"},
                {"label": "मात्रात्मक (Quantitative): प्राकृतिक गैसें जो सांद्रता बढ़ने पर प्रदूषक बनती हैं (जैसे CO2)", "type": "leaf"},
                {"label": "गुणात्मक (Qualitative): कृत्रिम रसायन जो स्वभाव से ही विषैले होते हैं और प्रकृति में नहीं पाए जाते (जैसे कीटनाशक)", "type": "leaf"}
            ]},
            {"label": "प्रदूषकों के स्रोत", "type": "branch", "date": "स्रोत", "children": [
                {"label": "बिंदु स्रोत (Point): एकल, पहचान योग्य स्थान से विसर्जन (जैसे कारखाने की पाइपलाइन, चिमनी)", "type": "leaf"},
                {"label": "गैर-बिंदु स्रोत (Non-Point): बड़े क्षेत्रों से होने वाला विसरित रिसाव (जैसे कृषि अपवाह, सड़कों का पानी)", "type": "leaf"}
            ]},
            {"label": "भौतिक अवस्था", "type": "branch", "date": "अवस्था", "children": [
                {"label": "गैसीय प्रदूषक: सल्फर डाइऑक्साइड (SOx), नाइट्रोजन ऑक्साइड (NOx) और कार्बन मोनोऑक्साइड", "type": "leaf"},
                {"label": "कणिकीय प्रदूषक: हवा में निलंबित धूल, कालिख, और एयरोसोल धुंध", "type": "leaf"}
            ]},
            {"label": "यूपीएससी परीक्षा दृष्टिकोण", "type": "branch", "date": "परीक्षा", "children": [
                {"label": "जैव-संचय बनाम जैव-आवर्धन: एक जीव के भीतर विष का संचय बनाम खाद्य श्रृंखला में ऊपर जाने पर सांद्रता में वृद्धि", "type": "leaf"},
                {"label": "सहक्रियात्मक प्रभाव (Synergy): दो प्रदूषक मिलकर अकेले की तुलना में अधिक घातक यौगिक बनाते हैं (जैसे SO2 + धूल कण)", "type": "leaf"}
            ]}
        ]
    },
    {
        "keys": ["noise-pollution", "noise-levels", "causes-of-noise", "effects-of-noise"],
        "en": [
            {"label": "Measurement & Limits", "type": "branch", "date": "Standards", "children": [
                {"label": "Decibel (dB): Logarithmic scale measuring sound pressure levels; exposure above 85 dB over long terms causes hearing loss", "type": "leaf"},
                {"label": "Industrial Zone Limits: 75 dB during day / 70 dB during night under Noise Rules 2000", "type": "leaf"},
                {"label": "Commercial Zone Limits: 65 dB during day / 55 dB during night", "type": "leaf"},
                {"label": "Residential & Silence Zones: Residential is 55/45 dB; Silence zones (100m around hospitals/courts) is 50/40 dB", "type": "leaf"}
            ]},
            {"label": "Primary Causes", "type": "branch", "date": "Causes", "children": [
                {"label": "Transport: Road traffic, aircraft takeoff/landing, and rail engines in urban areas", "type": "leaf"},
                {"label": "Industrial & Social: Heavy machinery, diesel generators, construction activity, and public loudspeakers", "type": "leaf"}
            ]},
            {"label": "Physiological Impacts", "type": "branch", "date": "Health Effects", "children": [
                {"label": "Cardiac stress: Chronic noise increases cortisol, elevating blood pressure and risk of ischemic heart disease", "type": "leaf"},
                {"label": "Cognitive deficits: Sleep disruption leading to fatigue, cognitive impairment in children, and chronic stress", "type": "leaf"}
            ]},
            {"label": "UPSC Exam Focus", "type": "branch", "date": "UPSC Focus", "children": [
                {"label": "Air Act Amendment 1987: Noise pollution was legally included under the definition of air pollutants in India", "type": "leaf"},
                {"label": "Green Muffler: Planting 4-6 rows of dense trees (e.g. Ashok, Neem) along roadsides to absorb/block sound waves", "type": "leaf"}
            ]}
        ],
        "hi": [
            {"label": "मापन और मानक", "type": "branch", "date": "मानक", "children": [
                {"label": "डेसिबल (dB): ध्वनि दबाव स्तर मापने का लघुगणकीय पैमाना; 85 dB से अधिक का स्तर बहरापन लाता है", "type": "leaf"},
                {"label": "औद्योगिक क्षेत्र सीमाएं: ध्वनि प्रदूषण नियम 2000 के तहत दिन में 75 dB / रात में 70 dB", "type": "leaf"},
                {"label": "वाणिज्यिक क्षेत्र सीमाएं: दिन में 65 dB / रात में 55 dB तक सीमित", "type": "leaf"},
                {"label": "आवासीय और शांत क्षेत्र: आवासीय 55/45 dB; शांत क्षेत्र (अस्पतालों/न्यायालयों के 100 मीटर दायरे में) 50/40 dB", "type": "leaf"}
            ]},
            {"label": "प्रमुख कारण", "type": "branch", "date": "कारण", "children": [
                {"label": "परिवहन: शहरी क्षेत्रों में सड़क यातायात, हवाई जहाजों की आवाज और रेलवे इंजन", "type": "leaf"},
                {"label": "औद्योगिक और सामाजिक: भारी मशीनें, डीजल जनरेटर, निर्माण गतिविधियां और सार्वजनिक लाउडस्पीकर", "type": "leaf"}
            ]},
            {"label": "स्वास्थ्य पर प्रभाव", "type": "branch", "date": "स्वास्थ्य प्रभाव", "children": [
                {"label": "कार्डियक तनाव: लगातार शोर कोर्टिसोल हार्मोन को बढ़ाता है, जिससे उच्च रक्तचाप और दिल का दौरा पड़ने का खतरा बढ़ता है", "type": "leaf"},
                {"label": "मानसिक प्रभाव: नींद में व्यवधान, थकान और बच्चों में एकाग्रता की कमी", "type": "leaf"}
            ]},
            {"label": "यूपीएससी परीक्षा दृष्टिकोण", "type": "branch", "date": "परीक्षा", "children": [
                {"label": "वायु अधिनियम संशोधन 1987: ध्वनि प्रदूषण को भारत में आधिकारिक तौर पर वायु प्रदूषकों के अंतर्गत शामिल किया गया था", "type": "leaf"},
                {"label": "ग्रीन मफलर: ध्वनि तरंगों को अवशोषित करने के लिए सड़कों के किनारे घने पेड़ों (जैसे अशोक, नीम) की 4-6 कतारें लगाना", "type": "leaf"}
            ]}
        ]
    },
    {
        "keys": ["thermal-pollution", "causes-of-thermal", "control-of-thermal", "effect-of-thermal"],
        "en": [
            {"label": "Thermal Mechanics", "type": "branch", "date": "Overview", "children": [
                {"label": "Definition: Degradation of water quality by any process that changes ambient water temperature", "type": "leaf"},
                {"label": "Primary Source: Cooling water discharged from coal-fired thermal power plants and nuclear reactors into natural rivers/seas", "type": "leaf"}
            ]},
            {"label": "Dissolved Oxygen Drop", "type": "branch", "date": "Oxygen Link", "children": [
                {"label": "Physical law: Solubility of gases (like oxygen) in water decreases as water temperature rises", "type": "leaf"},
                {"label": "Oxygen depletion: Higher temperature water holds less dissolved oxygen, causing suffocation of aquatic life", "type": "leaf"}
            ]},
            {"label": "Ecological Shock", "type": "branch", "date": "Impacts", "children": [
                {"label": "Thermal Shock: Sudden water temperature change kills stenothermal organisms adapted to stable ranges", "type": "leaf"},
                {"label": "Metabolism shift: Elevates metabolic rates in fish, forcing them to consume more oxygen in oxygen-depleted waters", "type": "leaf"}
            ]},
            {"label": "UPSC Exam Focus", "type": "branch", "date": "UPSC Focus", "children": [
                {"label": "Cooling Towers: Evaporative structures using air to cool heated water before it is released to environment", "type": "leaf"},
                {"label": "Artificial ponds: Man-made reservoirs storing warm water; cools via natural surface radiation before release", "type": "leaf"}
            ]}
        ],
        "hi": [
            {"label": "तापीय प्रदूषण की क्रियाविधि", "type": "branch", "date": "अवधारणा", "children": [
                {"label": "परिभाषा: किसी भी प्रक्रिया द्वारा पानी की गुणवत्ता में गिरावट जो पानी के सामान्य तापमान को बदल देती है", "type": "leaf"},
                {"label": "प्राथमिक स्रोत: कोयला आधारित बिजलीघरों और परमाणु रिएक्टरों से प्राकृतिक नदियों/समुद्रों में छोड़ा गया गर्म पानी", "type": "leaf"}
            ]},
            {"label": "घुलित ऑक्सीजन में गिरावट", "type": "branch", "date": "ऑक्सीजन संबंध", "children": [
                {"label": "भौतिक नियम: पानी का तापमान बढ़ने पर उसमें गैसों (जैसे ऑक्सीजन) की घुलनशीलता कम हो जाती है", "type": "leaf"},
                {"label": "ऑक्सीजन की कमी: गर्म पानी कम ऑक्सीजन रोक पाता है, जिससे जलीय जीवन का दम घुटता है", "type": "leaf"}
            ]},
            {"label": "पारिस्थितिक आघात", "type": "branch", "date": "प्रभाव", "children": [
                {"label": "तापीय आघात (Thermal Shock): पानी के तापमान में अचानक बदलाव से संकीर्णतापी (Stenothermal) जीव मर जाते हैं", "type": "leaf"},
                {"label": "चयापचय में बदलाव: मछलियों के चयापचय की दर को बढ़ाता है, जिससे उन्हें अधिक ऑक्सीजन की आवश्यकता होती है", "type": "leaf"}
            ]},
            {"label": "यूपीएससी परीक्षा दृष्टिकोण", "type": "branch", "date": "परीक्षा", "children": [
                {"label": "कूलिंग टावर (Cooling Towers): वाष्पीकरण संरचनाएं जो वातावरण में छोड़ने से पहले पानी को हवा से ठंडा करती हैं", "type": "leaf"},
                {"label": "कृत्रिम तालाब: मानव निर्मित जलाशय जो गर्म पानी को स्टोर करते हैं; प्राकृतिक विकिरण से ठंडा करने के बाद छोड़ते हैं", "type": "leaf"}
            ]}
        ]
    },
    {
        "keys": ["dead-zone", "dissolved-oxygen-bod-and-cod", "concept-of-dead-zone"],
        "en": [
            {"label": "Dead Zones Concept", "type": "branch", "date": "Dead Zones", "children": [
                {"label": "Definition: Hypoxic (low-oxygen) areas in the world's oceans and large lakes where aquatic life cannot survive", "type": "leaf"},
                {"label": "Mechanism: Eutrophication triggers massive algal blooms; algae die and sink; decomposing bacteria consume all oxygen", "type": "leaf"}
            ]},
            {"label": "Oxygen Indicators", "type": "branch", "date": "Water Quality", "children": [
                {"label": "DO (Dissolved Oxygen): Vital for fish; levels below 4 mg/L indicate severe pollution, leading to fish kills", "type": "leaf"},
                {"label": "BOD (Biochemical Oxygen Demand): Measures amount of oxygen consumed by bacteria to break down organic waste", "type": "leaf"},
                {"label": "COD (Chemical Oxygen Demand): Measures oxygen equivalent of organic/inorganic compounds oxidized chemically", "type": "leaf"}
            ]},
            {"label": "Global Examples", "type": "branch", "date": "Hotspots", "children": [
                {"label": "Gulf of Mexico: Massive seasonal dead zone driven by agricultural nutrient runoff from Mississippi River basin", "type": "leaf"},
                {"label": "Baltic Sea: Holds some of the world's largest semi-permanent dead zones due to heavy industrial runoff", "type": "leaf"}
            ]},
            {"label": "UPSC Exam Focus", "type": "branch", "date": "UPSC Focus", "children": [
                {"label": "Inverse Relation: High organic pollution causes high BOD, leading directly to a drop in Dissolved Oxygen (DO)", "type": "leaf"},
                {"label": "COD vs BOD: COD is always higher than BOD because it measures both biodegradable and non-biodegradable matter", "type": "leaf"}
            ]}
        ],
        "hi": [
            {"label": "डेड ज़ोन (Dead Zones) की अवधारणा", "type": "branch", "date": "डेड ज़ोन", "children": [
                {"label": "परिभाषा: महासागरों और बड़ी झीलों में कम ऑक्सीजन (Hypoxic) वाले क्षेत्र जहां जलीय जीवन जीवित नहीं रह सकता", "type": "leaf"},
                {"label": "क्रियाविधि: यूट्रोफिकेशन से शैवाल प्रस्फुटन होता है; मृत शैवाल के अपघटन के दौरान बैक्टीरिया सारी ऑक्सीजन सोख लेते हैं", "type": "leaf"}
            ]},
            {"label": "ऑक्सीजन संकेतक", "type": "branch", "date": "जल गुणवत्ता", "children": [
                {"label": "DO (घुलित ऑक्सीजन): मछलियों के लिए आवश्यक; 4 mg/L से कम का स्तर गंभीर प्रदूषण को दर्शाता है", "type": "leaf"},
                {"label": "BOD (जैव रासायनिक ऑक्सीजन मांग): कार्बनिक कचरे को तोड़ने के लिए बैक्टीरिया द्वारा उपभोग की जाने वाली ऑक्सीजन का माप", "type": "leaf"},
                {"label": "COD (रासायनिक ऑक्सीजन मांग): पानी में कार्बनिक और अकार्बनिक प्रदूषकों के रासायनिक ऑक्सीकरण के लिए आवश्यक ऑक्सीजन", "type": "leaf"}
            ]},
            {"label": "वैश्विक उदाहरण", "type": "branch", "date": "क्षेत्र", "children": [
                {"label": "मेक्सिको की खाड़ी: मिसिसिपी नदी बेसिन से कृषि पोषक तत्वों के बहने से निर्मित विशाल मौसमी डेड ज़ोन", "type": "leaf"},
                {"label": "बाल्टिक सागर: औद्योगिक कचरे और कृषि अपवाह के कारण दुनिया के सबसे बड़े स्थायी डेड ज़ोन का घर", "type": "leaf"}
            ]},
            {"label": "यूपीएससी परीक्षा दृष्टिकोण", "type": "branch", "date": "परीक्षा", "children": [
                {"label": "विपरीत संबंध: उच्च कार्बनिक प्रदूषण से BOD बढ़ता है, जिससे घुलित ऑक्सीजन (DO) में भारी गिरावट आती है", "type": "leaf"},
                {"label": "COD बनाम BOD: COD हमेशा BOD से अधिक होता है क्योंकि यह जैव-अपघटनीय और गैर-जैव-अपघटनीय दोनों कचरे को मापता है", "type": "leaf"}
            ]}
        ]
    },
    {
        "keys": ["ocean-acidification"],
        "en": [
            {"label": "Acidification Chemistry", "type": "branch", "date": "Chemistry", "children": [
                {"label": "CO2 Absorption: Oceans absorb ~25-30% of anthropogenic CO2 emissions from the atmosphere", "type": "leaf"},
                {"label": "Carbonic Acid: Dissolved CO2 reacts with water to form carbonic acid (H2CO3), releasing hydrogen ions (H+)", "type": "leaf"},
                {"label": "pH drop: Increase in H+ concentration decreases ocean pH; marine acidity has increased by ~30% since industrial revolution", "type": "leaf"}
            ]},
            {"label": "Carbonate Ion Depletion", "type": "branch", "date": "Calcification", "children": [
                {"label": "Mechanism: Free hydrogen ions bind with carbonate ions (CO3 2-) to form bicarbonate (HCO3-)", "type": "leaf"},
                {"label": "Shell damage: Depletes carbonate ions required by marine calcifiers (corals, shellfish, pteropods) to build calcium carbonate shells", "type": "leaf"}
            ]},
            {"label": "Ecological Consequences", "type": "branch", "date": "Impacts", "children": [
                {"label": "Coral Reefs: Bleaching and structural collapse; reefs dissolve faster than they can build skeletons", "type": "leaf"},
                {"label": "Marine food webs: Pteropods (sea butterflies, core food source for salmon/whales) experience shell dissolution", "type": "leaf"}
            ]},
            {"label": "UPSC Exam Focus", "type": "branch", "date": "UPSC Focus", "children": [
                {"label": "Aragonite Saturation: A measure of carbonate availability; drop in aragonite levels halts coral reef recovery", "type": "leaf"},
                {"label": "Link with warming: Warmer oceans absorb slightly less CO2, but higher thermal stress accelerates coral bleaching", "type": "leaf"}
            ]}
        ],
        "hi": [
            {"label": "अम्लीकरण का रसायन", "type": "branch", "date": "रसायन", "children": [
                {"label": "CO2 अवशोषण: महासागर वातावरण से मानवजनित CO2 उत्सर्जन का लगभग 25-30% अवशोषित करते हैं", "type": "leaf"},
                {"label": "कार्बोनिक एसिड: घुली हुई CO2 पानी के साथ प्रतिक्रिया करके कार्बोनिक एसिड (H2CO3) बनाती है, जिससे H+ आयन निकलते हैं", "type": "leaf"},
                {"label": "pH में गिरावट: H+ सांद्रता में वृद्धि से समुद्र का pH घटता है; औद्योगिक क्रांति से अब तक अम्लता ~30% बढ़ी है", "type": "leaf"}
            ]},
            {"label": "कार्बोनेट आयन की कमी", "type": "branch", "date": "कैल्सीकरण", "children": [
                {"label": "क्रियाविधि: मुक्त हाइड्रोजन आयन कार्बोनेट आयनों (CO3 2-) के साथ मिलकर बाइकार्बोनेट (HCO3-) बनाते हैं", "type": "leaf"},
                {"label": "कवचों को नुकसान: शंखधारी जीवों (मूंगा, घोंघे) को अपने कैल्शियम कार्बोनेट कवच बनाने के लिए कार्बोनेट आयन नहीं मिल पाते", "type": "leaf"}
            ]},
            {"label": "पारिस्थितिक परिणाम", "type": "branch", "date": "प्रभाव", "children": [
                {"label": "प्रवाल भित्तियाँ: विरंजन और संरचनात्मक पतन; प्रवाल भित्तियाँ बनने से अधिक तेजी से घुलने लगती हैं", "type": "leaf"},
                {"label": "समुद्री खाद्य जाल: टेरोपॉड्स (समुद्री तितलियां, जो मछलियों का भोजन हैं) के शंख घुलने लगते हैं", "type": "leaf"}
            ]},
            {"label": "यूपीएससी परीक्षा दृष्टिकोण", "type": "branch", "date": "परीक्षा", "children": [
                {"label": "एरागोनाइट संतृप्ति: कार्बोनेट उपलब्धता का माप; एरागोनाइट स्तर में गिरावट प्रवाल भित्तियों की बहाली को रोकती है", "type": "leaf"},
                {"label": "तापमान से संबंध: गर्म महासागर थोड़ी कम CO2 सोखते हैं, लेकिन उच्च तापीय तनाव प्रवाल विरंजन को बढ़ाता है", "type": "leaf"}
            ]}
        ]
    },
    {
        "keys": ["asbestosis"],
        "en": [
            {"label": "Definition & Cause", "type": "branch", "date": "Etiology", "children": [
                {"label": "Occupational disease: Chronic inflammatory and fibrotic lung condition caused by inhaling asbestos fibers", "type": "leaf"},
                {"label": "Asbestos fibers: Needle-like mineral crystals that deposit deep in alveoli, resisting immune destruction", "type": "leaf"}
            ]},
            {"label": "Pathology & Symptoms", "type": "branch", "date": "Clinical", "children": [
                {"label": "Fibrosis: Scars lung tissues, reducing elasticity and decreasing lung capacity over decades", "type": "leaf"},
                {"label": "Mesothelioma: Fatal cancer of the lung lining (pleura) strongly linked with asbestos exposure", "type": "leaf"}
            ]},
            {"label": "High-Risk Occupations", "type": "branch", "date": "Risk Groups", "children": [
                {"label": "Mining & Construction: Mining asbestos ore, roofing sheet installation, and insulation work", "type": "leaf"},
                {"label": "Shipbreaking: Scraping old insulation from ships (e.g. Alang shipbreaking yard in Gujarat)", "type": "leaf"}
            ]},
            {"label": "UPSC Exam Focus", "type": "branch", "date": "UPSC Focus", "children": [
                {"label": "Latency period: Asbestosis has a long latency period (symptoms appear 15-30 years after exposure)", "type": "leaf"},
                {"label": "Rotterdam Convention: Prior Informed Consent (PIC) treaty; covers chrysotile asbestos trade regulations", "type": "leaf"}
            ]}
        ],
        "hi": [
            {"label": "परिभाषा और कारण", "type": "branch", "date": "रोगजनन", "children": [
                {"label": "व्यावसायिक बीमारी: एस्बेस्टस के रेशों को सांस के माध्यम से अंदर लेने से फेफड़ों में सूजन और घाव (फाइब्रोसिस) होना", "type": "leaf"},
                {"label": "एस्बेस्टस रेशे: सुई जैसे खनिज क्रिस्टल जो फेफड़ों में गहरे जमा हो जाते हैं और श्वेत रक्त कोशिकाओं द्वारा नष्ट नहीं होते", "type": "leaf"}
            ]},
            {"label": "लक्षण और जटिलताएं", "type": "branch", "date": "लक्षण", "children": [
                {"label": "फाइब्रोसिस: फेफड़ों के ऊतकों को नुकसान पहुंचाता है, जिससे फेफड़ों की फैलने की क्षमता कम हो जाती है", "type": "leaf"},
                {"label": "मेसोथेलियोमा (Mesothelioma): फेफड़ों की बाहरी झिल्ली (प्लुरा) का घातक कैंसर जो एस्बेस्टस के संपर्क से जुड़ा है", "type": "leaf"}
            ]},
            {"label": "जोखिम वाले उद्योग", "type": "branch", "date": "उद्योग", "children": [
                {"label": "खनन और निर्माण: एस्बेस्टस अयस्क का खनन, छतों की चादरों का निर्माण और थर्मल इन्सुलेशन कार्य", "type": "leaf"},
                {"label": "जहाज तोड़ना (Shipbreaking): पुराने जहाजों से एस्बेस्टस हटाना (जैसे गुजरात में अलंग शिपब्रेकिंग यार्ड)", "type": "leaf"}
            ]},
            {"label": "यूपीएससी परीक्षा दृष्टिकोण", "type": "branch", "date": "परीक्षा", "children": [
                {"label": "विलंबता अवधि (Latency): बीमारी के लक्षण एस्बेस्टस के संपर्क में आने के 15-30 वर्ष बाद दिखाई देते हैं", "type": "leaf"},
                {"label": "रॉटरडैम कन्वेंशन: खतरनाक रसायनों के व्यापार पर पूर्व सूचित सहमति (PIC) संधि; क्रायसोटाइल एस्बेस्टस को कवर करती है", "type": "leaf"}
            ]}
        ]
    },
    {
        "keys": ["black-lung-disease"],
        "en": [
            {"label": "Definition & Etiology", "type": "branch", "date": "Concept", "children": [
                {"label": "Coal Workers' Pneumoconiosis (CWP): Occupational lung disease caused by long-term inhalation of coal dust", "type": "leaf"},
                {"label": "Dust build-up: Coal dust accumulates in lungs, triggering chronic immune response and tissue scarring", "type": "leaf"}
            ]},
            {"label": "Pathology Stages", "type": "branch", "date": "Clinical", "children": [
                {"label": "Simple CWP: Small coal macules form around bronchioles, causing mild chronic cough and shortness of breath", "type": "leaf"},
                {"label": "Complicated CWP: Progressive Massive Fibrosis (PMF); large areas of lung tissue turn black and scarred, leading to respiratory failure", "type": "leaf"}
            ]},
            {"label": "Prevention Measures", "type": "branch", "date": "Prevention", "children": [
                {"label": "Dust suppression: Wet drilling methods and water spraying at coal cutting faces inside mines", "type": "leaf"},
                {"label": "Personal Protection: Providing high-efficiency particulate respirators to underground workers", "type": "leaf"}
            ]},
            {"label": "UPSC Exam Focus", "type": "branch", "date": "UPSC Focus", "children": [
                {"label": "Mines Act 1952: Legal framework in India governing worker safety, health check-ups, and compensation in mines", "type": "leaf"},
                {"label": "Treatment: No cure exists for advanced PMF; management is purely supportive (oxygen therapy, lung transplant)", "type": "leaf"}
            ]}
        ],
        "hi": [
            {"label": "परिभाषा और कारण", "type": "branch", "date": "अवधारणा", "children": [
                {"label": "कोयला खनिक न्यूमोकोनियोसिस (CWP): कोयले की धूल को लंबे समय तक सांस के माध्यम से अंदर लेने से होने वाला रोग", "type": "leaf"},
                {"label": "धूल संचय: कोयले की धूल फेफड़ों में जमा हो जाती है, जिससे लगातार प्रतिरक्षा प्रतिक्रिया और फाइब्रोसिस होता है", "type": "leaf"}
            ]},
            {"label": "रोग के चरण", "type": "branch", "date": "लक्षण", "children": [
                {"label": "सरल CWP: ब्रोन्किओल्स के आसपास छोटे कोयले के धब्बे बनते हैं, जिससे पुरानी खांसी और सांस फूलने की समस्या होती है", "type": "leaf"},
                {"label": "जटिल CWP: प्रोग्रेसिव मैसिव फाइब्रोसिस (PMF); फेफड़े के बड़े हिस्से काले पड़ जाते हैं, जिससे सांस की विफलता होती है", "type": "leaf"}
            ]},
            {"label": "निवारक उपाय", "type": "branch", "date": "निवारण", "children": [
                {"label": "धूल दमन: खदानों के भीतर कोयला काटने वाली जगहों पर पानी का छिड़काव और गीली ड्रिलिंग विधियों का उपयोग", "type": "leaf"},
                {"label": "व्यक्तिगत सुरक्षा: भूमिगत श्रमिकों को उच्च दक्षता वाले पार्टिकुलेट रेस्पिरेटर्स (मास्क) प्रदान करना", "type": "leaf"}
            ]},
            {"label": "यूपीएससी परीक्षा दृष्टिकोण", "type": "branch", "date": "परीक्षा", "children": [
                {"label": "खान अधिनियम 1952: भारत में श्रमिकों की सुरक्षा, स्वास्थ्य जांच और मुआवजा देने का विनियामक ढांचा", "type": "leaf"},
                {"label": "उपचार: उन्नत PMF का कोई इलाज नहीं है; प्रबंधन केवल सहायक उपचार (ऑक्सीजन थेरेपी) तक सीमित है", "type": "leaf"}
            ]}
        ]
    },
    {
        "keys": ["byssinosis"],
        "en": [
            {"label": "Definition & Cause", "type": "branch", "date": "Etiology", "children": [
                {"label": "Brown Lung Disease: Occupational lung disease caused by inhaling dust from cotton, flax, hemp, and jute processing", "type": "leaf"},
                {"label": "Endotoxins: Induced primarily by bacterial endotoxins present on raw agricultural fibers, causing bronchoconstriction", "type": "leaf"}
            ]},
            {"label": "Symptoms & Progression", "type": "branch", "date": "Clinical", "children": [
                {"label": "Monday Fever: Classic symptom where chest tightness and dyspnea are worst on the first day of work week", "type": "leaf"},
                {"label": "Chronic stage: Permanent narrowing of airways over years of exposure, causing chronic bronchitis and emphysema", "type": "leaf"}
            ]},
            {"label": "High-Risk Industries", "type": "branch", "date": "Risk Groups", "children": [
                {"label": "Textile Mills: Spinning, carding, and weaving departments of cotton mills with poor ventilation", "type": "leaf"},
                {"label": "Jute industries: Processing raw jute fibers in West Bengal belt", "type": "leaf"}
            ]},
            {"label": "UPSC Exam Focus", "type": "branch", "date": "UPSC Focus", "children": [
                {"label": "Factories Act 1948: Mandates installation of exhaust ventilation and dust extraction systems in textile units", "type": "leaf"},
                {"label": "Difference from Silicosis: Byssinosis is caused by organic agricultural dusts; silicosis by inorganic mineral dusts", "type": "leaf"}
            ]}
        ],
        "hi": [
            {"label": "परिभाषा और कारण", "type": "branch", "date": "रोगजनन", "children": [
                {"label": "ब्राउन लंग डिजीज: कपास, सन (Flax), भांग और जूट के प्रसंस्करण से निकलने वाली धूल सांस के साथ अंदर लेने से होने वाला रोग", "type": "leaf"},
                {"label": "एंडोटॉक्सिन: कच्चे रेशों पर मौजूद बैक्टीरिया के एंडोटॉक्सिन श्वसन मार्ग को संकुचित कर सांस की नली में सूजन लाते हैं", "type": "leaf"}
            ]},
            {"label": "लक्षण और प्रगति", "type": "branch", "date": "लक्षण", "children": [
                {"label": "मंडे फीवर (Monday Fever): काम के सप्ताह के पहले दिन (सोमवार) छाती में जकड़न और सांस फूलना सबसे गंभीर होना", "type": "leaf"},
                {"label": "क्रोनिक चरण: वर्षों तक धूल के संपर्क में रहने से पुरानी ब्रोंकाइटिस और सांस लेने में स्थायी कठिनाई होना", "type": "leaf"}
            ]},
            {"label": "जोखिम वाले उद्योग", "type": "branch", "date": "उद्योग", "children": [
                {"label": "कपड़ा मिलें (Textile): खराब वेंटिलेशन वाली सूती मिलों के कताई और बुनाई विभाग", "type": "leaf"},
                {"label": "जूट उद्योग: पश्चिम बंगाल हुगली बेल्ट में कच्चे जूट के रेशों का प्रसंस्करण", "type": "leaf"}
            ]},
            {"label": "यूपीएससी परीक्षा दृष्टिकोण", "type": "branch", "date": "परीक्षा", "children": [
                {"label": "कारखाना अधिनियम 1948: कपड़ा इकाइयों में धूल निकालने वाले वेंटिलेशन सिस्टम की स्थापना अनिवार्य करता है", "type": "leaf"},
                {"label": "सिलिकोसिस से अंतर: बायसिनोसिस कार्बनिक कृषि धूल के कारण होता है; सिलिकोसिस अकार्बनिक खनिज धूल से", "type": "leaf"}
            ]}
        ]
    },
    {
        "keys": ["pneumoconiosis"],
        "en": [
            {"label": "Definition & Spectrum", "type": "branch", "date": "Concept", "children": [
                {"label": "Definition: Umbrella term for a group of interstitial lung diseases caused by inhalation of mineral or organic dusts", "type": "leaf"},
                {"label": "Reaction: Lung tissue reacts to dust accumulation by forming fibrotic nodules and scars, impairing oxygen exchange", "type": "leaf"}
            ]},
            {"label": "Major Types", "type": "branch", "date": "Types", "children": [
                {"label": "Silicosis: Caused by inhaling crystalline silica dust (stone crushing, sandblasting)", "type": "leaf"},
                {"label": "Asbestosis: Caused by inhaling asbestos fibers (shipbreaking, thermal insulation)", "type": "leaf"},
                {"label": "Coal Workers' Pneumoconiosis: Caused by inhaling coal mine dust (black lung)", "type": "leaf"}
            ]},
            {"label": "Clinical Features", "type": "branch", "date": "Symptoms", "children": [
                {"label": "Chronic dry cough, progressive shortness of breath during exertion, and chest tightness", "type": "leaf"},
                {"label": "Advanced stage leads to cor pulmonale (right-sided heart failure due to high lung pressure)", "type": "leaf"}
            ]},
            {"label": "UPSC Exam Focus", "type": "branch", "date": "UPSC Focus", "children": [
                {"label": "Incurable nature: Scarring of lung alveoli is permanent; prevention through safety protocols is the only effective defense", "type": "leaf"},
                {"label": "ILO Classification: International standard for classification of radiographs of pneumoconiosis to monitor worker health", "type": "leaf"}
            ]}
        ],
        "hi": [
            {"label": "परिभाषा और वर्गीकरण", "type": "branch", "date": "अवधारणा", "children": [
                {"label": "परिभाषा: खनिज या कार्बनिक धूल को सांस के साथ अंदर लेने से होने वाले फेफड़ों के रोगों का समूह", "type": "leaf"},
                {"label": "फेफड़ों की प्रतिक्रिया: धूल जमा होने से फेफड़ों में घाव (फाइब्रोसिस) बनते हैं, जिससे ऑक्सीजन का विनिमय रुकता है", "type": "leaf"}
            ]},
            {"label": "प्रमुख प्रकार", "type": "branch", "date": "प्रकार", "children": [
                {"label": "सिलिकोसिस: सिलिका धूल सांस के साथ अंदर लेने से होता है (पत्थर तोड़ना, खदानें)", "type": "leaf"},
                {"label": "एस्बेस्टोसिस: एस्बेस्टस के रेशों के कारण होता है (जहाज तोड़ना, छत निर्माण)", "type": "leaf"},
                {"label": "कोयला खनिक न्यूमोकोनियोसिस: कोयले की धूल के कारण होता है (ब्लैक लंग रोग)", "type": "leaf"}
            ]},
            {"label": "नैदानिक लक्षण", "type": "branch", "date": "लक्षण", "children": [
                {"label": "पुरानी सूखी खांसी, शारीरिक मेहनत के दौरान सांस फूलना और छाती में लगातार जकड़न महसूस होना", "type": "leaf"},
                {"label": "अंतिम चरण में फेफड़ों के उच्च रक्तचाप के कारण दिल का दौरा (Cor pulmonale) पड़ने का खतरा रहता है", "type": "leaf"}
            ]},
            {"label": "यूपीएससी परीक्षा दृष्टिकोण", "type": "branch", "date": "परीक्षा", "children": [
                {"label": "असाध्य रोग: फेफड़ों के घाव स्थायी होते हैं; सुरक्षा नियमों के माध्यम से बचाव ही एकमात्र उपाय है", "type": "leaf"},
                {"label": "ILO वर्गीकरण: श्रमिकों के स्वास्थ्य की निगरानी के लिए न्यूमोकोनियोसिस के रेडियोग्राफ के वर्गीकरण का अंतर्राष्ट्रीय मानक", "type": "leaf"}
            ]}
        ]
    },
    {
        "keys": ["silicosis"],
        "en": [
            {"label": "Definition & Etiology", "type": "branch", "date": "Cause", "children": [
                {"label": "Incurable lung disease: Caused by inhaling respirable crystalline silica (quartz) particles", "type": "leaf"},
                {"label": "Silica particles deposit in alveoli; macrophages ingest them but are destroyed, releasing lysosomal enzymes that scar tissue", "type": "leaf"}
            ]},
            {"label": "High-Risk Sectors", "type": "branch", "date": "Occupations", "children": [
                {"label": "Stone Crushing & Slate mining: High dust generation without water suppression (e.g. Rajasthan slate mines)", "type": "leaf"},
                {"label": "Sandblasting & Glass manufacturing: Inhalation of fine glass/quartz dust in closed factories", "type": "leaf"}
            ]},
            {"label": "Complications", "type": "branch", "date": "Complications", "children": [
                {"label": "Silicotuberculosis: Damage to macrophages decreases lung defenses, making silicosis patients 3 times more susceptible to tuberculosis", "type": "leaf"},
                {"label": "Progressive Massive Fibrosis (PMF): Complete loss of lung elasticity, causing respiratory failure", "type": "leaf"}
            ]},
            {"label": "UPSC Exam Focus", "type": "branch", "date": "UPSC Focus", "children": [
                {"label": "National Programme for Control of Silicosis: Launched to monitor worker health, enforce wet drilling, and provide compensation", "type": "leaf"},
                {"label": "Ocal Policy: Rajasthan was the first state to launch a dedicated Silicosis Policy in 2019, providing welfare funds", "type": "leaf"}
            ]}
        ],
        "hi": [
            {"label": "परिभाषा और कारण", "type": "branch", "date": "रोगजनन", "children": [
                {"label": "असाध्य फेफड़ों का रोग: हवा में उड़ने वाले क्रिस्टलीय सिलिका (क्वार्ट्ज) के महीन कणों को सांस से अंदर लेने से होता है", "type": "leaf"},
                {"label": "कोशिका क्षति: मैक्रोफेज सिलिका कणों को निगलते हैं लेकिन वे फट जाते हैं, जिससे फेफड़ों में घाव (Scars) बन जाते हैं", "type": "leaf"}
            ]},
            {"label": "जोखिम वाले क्षेत्र", "type": "branch", "date": "उद्योग", "children": [
                {"label": "पत्थर तोड़ना और स्लेट खनन: बिना पानी छिड़काव के अत्यधिक धूल पैदा करने वाली गतिविधियां (जैसे राजस्थान की खदानें)", "type": "leaf"},
                {"label": "सैंडब्लास्टिंग और ग्लास निर्माण: बंद कारखानों में महीन क्वार्ट्ज धूल को सांस के साथ अंदर लेना", "type": "leaf"}
            ]},
            {"label": "जटिलताएं", "type": "branch", "date": "जटिलताएं", "children": [
                {"label": "सिलिकोट्यूबरकुलोसिस: मैक्रोफेज के नष्ट होने से फेफड़ों की रक्षा प्रणाली कमजोर होती है, जिससे टीबी का खतरा 3 गुना बढ़ता है", "type": "leaf"},
                {"label": "प्रोग्रेसिव फाइब्रोसिस: फेफड़ों की लचीलापन पूरी तरह समाप्त हो जाती है, जिससे मृत्यु हो सकती है", "type": "leaf"}
            ]},
            {"label": "यूपीएससी परीक्षा दृष्टिकोण", "type": "branch", "date": "परीक्षा", "children": [
                {"label": "सिलिकोसिस नियंत्रण कार्यक्रम: श्रमिकों के स्वास्थ्य की निगरानी, गीली ड्रिलिंग लागू करने और मुआवजा देने हेतु कार्यरत", "type": "leaf"},
                {"label": "स्थानीय नीतियां: राजस्थान 2019 में एक समर्पित सिलिकोसिस नीति शुरू करने वाला पहला राज्य बना", "type": "leaf"}
            ]}
        ]
    },
    {
        "keys": ["oil-spill", "oilspill"],
        "en": [
            {"label": "Sources of Oil Spills", "type": "branch", "date": "Sources", "children": [
                {"label": "Offshore Blowouts: Drilling accidents at offshore oil rigs (e.g. Deepwater Horizon spill in Gulf of Mexico)", "type": "leaf"},
                {"label": "Tanker Accidents: Collisions or groundings of crude oil supertankers (e.g. Exxon Valdez spill)", "type": "leaf"}
            ]},
            {"label": "Ecological Destruction", "type": "branch", "date": "Impacts", "children": [
                {"label": "Marine Birds: Oil coats feathers, destroying insulating properties and buoyancy; leads to hypothermia and drowning", "type": "leaf"},
                {"label": "Ocean suffocation: Floating oil slick blocks sunlight, preventing phytoplankton photosynthesis and oxygen dissolution", "type": "leaf"}
            ]},
            {"label": "Cleanup Methods", "type": "branch", "date": "Cleanup", "children": [
                {"label": "Booms & Skimmers: Floating barriers (booms) concentrate oil, and mechanical pumps (skimmers) suck it off the surface", "type": "leaf"},
                {"label": "Chemical Dispersants: Spraying chemicals to break oil slicks into tiny droplets, though dispersants themselves can be toxic", "type": "leaf"},
                {"label": "Bioremediation: Using oil-eating bacteria (e.g. Oilzapper developed by TERI) to digest crude oil hydrocarbons into non-toxic waste", "type": "leaf"}
            ]},
            {"label": "UPSC Exam Focus", "type": "branch", "date": "UPSC Focus", "children": [
                {"label": "Oilzapper: Consortium of 5 bacterial strains that digest crude oil fractions rapidly, leaving no toxic residue", "type": "leaf"},
                {"label": "Coastal Vulnerability: Spills in mangrove zones (e.g. Sundarbans) clog respiratory roots (pneumatophores), killing trees", "type": "leaf"}
            ]}
        ],
        "hi": [
            {"label": "तेल रिसाव के स्रोत", "type": "branch", "date": "स्रोत", "children": [
                {"label": "अपतटीय विस्फोट: अपतटीय तेल रिसाव प्लेटफार्मों पर ड्रिलिंग दुर्घटनाएं (जैसे मेक्सिको की खाड़ी में डीपवाटर होरिज़न)", "type": "leaf"},
                {"label": "टैंकर दुर्घटनाएं: कच्चे तेल ले जाने वाले जहाजों की टक्कर या दुर्घटनाएं (जैसे एक्सॉन वाल्डेज़ तेल रिसाव)", "type": "leaf"}
            ]},
            {"label": "पारिस्थितिक विनाश", "type": "branch", "date": "प्रभाव", "children": [
                {"label": "समुद्री पक्षी: तेल पंखों पर चिपक जाता है, जिससे उनकी गर्मी रोकने की क्षमता और तैरने की क्षमता नष्ट हो जाती है", "type": "leaf"},
                {"label": "समुद्री दम घुटने: तैरता हुआ तेल सूर्य के प्रकाश को रोकता है, जिससे पादप प्लवक प्रकाश संश्लेषण नहीं कर पाते", "type": "leaf"}
            ]},
            {"label": "सफाई की विधियां", "type": "branch", "date": "सफाई", "children": [
                {"label": "बूम और स्किमर: तैरने वाले अवरोधक (Booms) तेल को इकट्ठा करते हैं, और यांत्रिक पंप (Skimmers) उसे सतह से खींचते हैं", "type": "leaf"},
                {"label": "रासायनिक विकीर्णक (Dispersants): तेल की परतों को छोटी बूंदों में तोड़ने के लिए रसायन छिड़कना", "type": "leaf"},
                {"label": "जैविक उपचार (Bioremediation): तेल खाने वाले बैक्टीरिया (जैसे TERI द्वारा विकसित ऑयलजैपर) का उपयोग करना", "type": "leaf"}
            ]},
            {"label": "यूपीएससी परीक्षा दृष्टिकोण", "type": "branch", "date": "परीक्षा", "children": [
                {"label": "ऑयलजैपर (Oilzapper): 5 जीवाणु उपभेदों का मिश्रण जो कच्चे तेल के अंशों को पचाकर पानी को साफ करता है", "type": "leaf"},
                {"label": "तटीय संवेदनशीलता: मैंग्रोव क्षेत्रों में तेल रिसाव उनकी जड़ों (श्वसन जड़ों) को अवरुद्ध कर वनों को नष्ट करता है", "type": "leaf"}
            ]}
        ]
    },
    {
        "keys": ["radioactive-pollution", "harmful-effects-of-radioactive-pollution", "sources-of-radioactive-pollution"],
        "en": [
            {"label": "Sources of Radiation", "type": "branch", "date": "Sources", "children": [
                {"label": "Natural: Cosmic rays from space, radon-222 gas leaking from underground granite rocks, and potassium-40 in soil", "type": "leaf"},
                {"label": "Anthropogenic: Uranium mining/milling tailings, nuclear fuel cycles, power plant accidents, and medical isotopes", "type": "leaf"}
            ]},
            {"label": "Ionizing Radiation Hazards", "type": "branch", "date": "Hazards", "children": [
                {"label": "Somatic Damage: Immediate burns, hair loss, and high risk of leukemia or thyroid cancer (due to Iodine-131 accumulation)", "type": "leaf"},
                {"label": "Genetic Damage: Ionizing radiation breaks DNA strands, inducing germ cell mutations that pass to next generations", "type": "leaf"}
            ]},
            {"label": "Famous Accidents", "type": "branch", "date": "Accidents", "children": [
                {"label": "Chernobyl (1986): Nuclear reactor meltdown in Ukraine; released massive radioactive plume across Europe", "type": "leaf"},
                {"label": "Fukushima Daiichi (2011): Tsunami-triggered reactor cooling failure in Japan; contaminated marine waters", "type": "leaf"}
            ]},
            {"label": "UPSC Exam Focus", "type": "branch", "date": "UPSC Focus", "children": [
                {"label": "Strontium-90: Behares like calcium; bioaccumulates in bones, causing bone cancer and leukemia", "type": "leaf"},
                {"label": "Radon: Odorless radioactive gas; second leading cause of lung cancer globally, building up in poorly ventilated basements", "type": "leaf"}
            ]}
        ],
        "hi": [
            {"label": "विकिरण के स्रोत", "type": "branch", "date": "स्रोत", "children": [
                {"label": "प्राकृतिक: अंतरिक्ष से ब्रह्मांडीय किरणें, भूमिगत ग्रेनाइट चट्टानों से रिसने वाली रेडॉन-222 गैस", "type": "leaf"},
                {"label": "मानवजनित: यूरेनियम खनन कचरा, परमाणु ऊर्जा संयंत्र दुर्घटनाएं और चिकित्सा समस्थानिक (Isotopes)", "type": "leaf"}
            ]},
            {"label": "आयनकारी विकिरण के खतरे", "type": "branch", "date": "खतरे", "children": [
                {"label": "कायिक क्षति (Somatic): तत्काल त्वचा जलना, बाल झड़ना और थायराइड कैंसर का खतरा (आयोडीन-131 के संचय के कारण)", "type": "leaf"},
                {"label": "आनुवंशिक क्षति (Genetic): आयनकारी विकिरण DNA संरचना को तोड़ता है, जिससे भावी पीढ़ी में उत्परिवर्तन होते हैं", "type": "leaf"}
            ]},
            {"label": "प्रसिद्ध दुर्घटनाएं", "type": "branch", "date": "दुर्घटनाएं", "children": [
                {"label": "चेरनोबिल (1986): यूक्रेन में परमाणु रिएक्टर मेल्टडाउन; पूरे यूरोप में बड़े पैमाने पर विकिरण फैला", "type": "leaf"},
                {"label": "फुकुशिमा (2011): जापान में सुनामी-प्रेरित रिएक्टर शीतलन विफलता; तटीय जल प्रदूषित हुआ", "type": "leaf"}
            ]},
            {"label": "यूपीएससी परीक्षा दृष्टिकोण", "type": "branch", "date": "परीक्षा", "children": [
                {"label": "स्ट्रोंटियम-90 (Strontium-90): कैल्शियम की तरह व्यवहार करता है; हड्डियों में जमा होकर कैंसर का कारण बनता है", "type": "leaf"},
                {"label": "रेडॉन गैस: गंधहीन गैस; खराब वेंटिलेशन वाले बेसमेंट में जमा होकर फेफड़ों के कैंसर का कारण बनती है", "type": "leaf"}
            ]}
        ]
    },
    {
        "keys": ["fly-ash", "flyash"],
        "en": [
            {"label": "Composition & Production", "type": "branch", "date": "Overview", "children": [
                {"label": "Definition: Fine residue particles carried out of coal-fired boilers with flue gases", "type": "leaf"},
                {"label": "Toxicity: Contains heavy metals like Lead, Arsenic, Cobalt, and Copper which can contaminate groundwater", "type": "leaf"}
            ]},
            {"label": "Environmental Impacts", "type": "branch", "date": "Impacts", "children": [
                {"label": "Air pollution: Fine suspended dust causes respiratory diseases in nearby populations", "type": "leaf"},
                {"label": "Land footprint: Disposed in large wet ash ponds, taking up fertile land and risking dyke breach disasters", "type": "leaf"}
            ]},
            {"label": "Productive Utilization", "type": "branch", "date": "Utilization", "children": [
                {"label": "Cement Industry: Used as a pozzolanic replacement for Portland cement, saving energy and limestone", "type": "leaf"},
                {"label": "Brick making: Fly ash clay bricks are lighter, stronger, and environmentally superior to red clay bricks", "type": "leaf"},
                {"label": "Infrastructure: Used in road embankments and concrete structures to reduce environmental footprint", "type": "leaf"}
            ]},
            {"label": "UPSC Exam Focus", "type": "branch", "date": "UPSC Focus", "children": [
                {"label": "Electrostatic Precipitators (ESP): Devices installed in smokestacks utilizing electric charge to capture 99% of fly ash", "type": "leaf"},
                {"label": "MoEFCC Notification: Mandates 100% utilization of fly ash by coal thermal plants to ensure zero waste", "type": "leaf"}
            ]}
        ],
        "hi": [
            {"label": "संरचना और उत्पादन", "type": "branch", "date": "संरचना", "children": [
                {"label": "परिभाषा: कोयला आधारित बिजलीघरों में कोयला जलने के बाद धुएँ के साथ निकलने वाली महीन राख", "type": "leaf"},
                {"label": "विषाक्तता: इसमें सीसा, आर्सेनिक, कोबाल्ट और तांबा जैसी भारी धातुएं होती हैं जो भूजल को प्रदूषित कर सकती हैं", "type": "leaf"}
            ]},
            {"label": "पर्यावरणीय प्रभाव", "type": "branch", "date": "प्रभाव", "children": [
                {"label": "वायु प्रदूषण: महीन निलंबित धूल आस-पास की आबादी में सांस की बीमारियों का कारण बनती है", "type": "leaf"},
                {"label": "भूमि का नुकसान: इसे बड़े राख तालाबों (Ash ponds) में जमा किया जाता है, जिससे उपजाऊ भूमि नष्ट होती है", "type": "leaf"}
            ]},
            {"label": "सकारात्मक उपयोग", "type": "branch", "date": "उपयोग", "children": [
                {"label": "सिमेंट उद्योग: सीमेंट के स्थान पर पोज़ोलानिक प्रतिस्थापन के रूप में उपयोग, जिससे चूना पत्थर की बचत होती है", "type": "leaf"},
                {"label": "ईंट निर्माण: फ्लाई ऐश ईंटें अधिक मजबूत, हल्की और पारंपरिक लाल ईंटों की तुलना में पर्यावरण के अनुकूल होती हैं", "type": "leaf"},
                {"label": "बुनियादी ढांचा: सड़क निर्माण और कंक्रीट संरचनाओं में भराव सामग्री के रूप में उपयोग", "type": "leaf"}
            ]},
            {"label": "यूपीएससी परीक्षा दृष्टिकोण", "type": "branch", "date": "परीक्षा", "children": [
                {"label": "स्थिर वैद्युत अवक्षेपित्र (ESP): चिमनियों में लगाए जाने वाले उपकरण जो विद्युत आवेश का उपयोग कर 99% फ्लाई ऐश पकड़ते हैं", "type": "leaf"},
                {"label": "MoEFCC अधिसूचना: कोयला ताप विद्युत संयंत्रों द्वारा शून्य कचरा सुनिश्चित करने के लिए फ्लाई ऐश के 100% उपयोग को अनिवार्य किया गया", "type": "leaf"}
            ]}
        ]
    },
    {
        "keys": ["indicator-species", "pollution-indicator"],
        "en": [
            {"label": "Indicator Concept", "type": "branch", "date": "Concept", "children": [
                {"label": "Species whose abundance or health serves as an index of environmental quality or pollution load", "type": "leaf"},
                {"label": "Provides a continuous biological assessment compared to periodic chemical tests", "type": "leaf"}
            ]},
            {"label": "Air Quality Indicators", "type": "branch", "date": "Air Indicators", "children": [
                {"label": "Lichens: Highly sensitive to Sulfur Dioxide (SO2); completely absent in zones with high coal combustion", "type": "leaf"},
                {"label": "Epiphytic mosses: Absorb heavy metal deposits directly from air, reflecting regional atmospheric toxins", "type": "leaf"}
            ]},
            {"label": "Water Quality Indicators", "type": "branch", "date": "Water Indicators", "children": [
                {"label": "Tubifex Worms: Thrive in anaerobic, highly organic muddy sediments; indicate severe organic/sewage pollution", "type": "leaf"},
                {"label": "E. Coli: Fecal coliform bacterium; presence in drinking water samples indicates sewage contamination", "type": "leaf"}
            ]},
            {"label": "UPSC Exam Focus", "type": "branch", "date": "UPSC Focus", "children": [
                {"label": "Macroinvertebrates: Benthic organisms used globally to determine River Water Quality Indices", "type": "leaf"},
                {"label": "Dilution effect: Loss of diverse indicator communities signals ecosystem degradation", "type": "leaf"}
            ]}
        ],
        "hi": [
            {"label": "संकेतक प्रजाति की अवधारणा", "type": "branch", "date": "अवधारणा", "children": [
                {"label": "वह प्रजाति जिसकी प्रचुरता या स्वास्थ्य पर्यावरणीय गुणवत्ता या प्रदूषण के स्तर को दर्शाता है", "type": "leaf"},
                {"label": "समय-समय पर होने वाले रासायनिक परीक्षणों की तुलना में निरंतर जैविक मूल्यांकन प्रदान करती है", "type": "leaf"}
            ]},
            {"label": "वायु गुणवत्ता संकेतक", "type": "branch", "date": "वायु संकेतक", "children": [
                {"label": "लाइकेन: सल्फर डाइऑक्साइड (SO2) के प्रति अत्यधिक संवेदनशील; कोयला दहन वाले प्रदूषित क्षेत्रों में पूरी तरह अनुपस्थित", "type": "leaf"},
                {"label": "एपिफाइटिक काई (Mosses): हवा से सीधे भारी धातु जमाव को अवशोषित कर वायु गुणवत्ता दर्शाते हैं", "type": "leaf"}
            ]},
            {"label": "जल गुणवत्ता संकेतक", "type": "branch", "date": "जल संकेतक", "children": [
                {"label": "ट्यूबीफेक्स कीड़े (Tubifex): अवायवीय जलीय तलछट में पनपते हैं; गंभीर सीवेज प्रदूषण का संकेत देते हैं", "type": "leaf"},
                {"label": "ई. कोलाई (E. Coli): पेयजल नमूनों में इसकी उपस्थिति सीवेज प्रदूषण को दर्शाती है", "type": "leaf"}
            ]},
            {"label": "यूपीएससी परीक्षा दृष्टिकोण", "type": "branch", "date": "परीक्षा", "children": [
                {"label": "तलहटी जीव (Macroinvertebrates): नदी जल गुणवत्ता सूचकांक निर्धारित करने के लिए वैश्विक स्तर पर उपयोग", "type": "leaf"},
                {"label": "डाइल्यूशन प्रभाव: विविध संकेतक समुदायों का ह्रास पारिस्थितिकी तंत्र के क्षरण का संकेत देता है", "type": "leaf"}
            ]}
        ]
    },
    {
        "keys": ["the-air-act-1981", "prevention-control-of-pollution-act-1981", "air-act"],
        "en": [
            {"label": "Act Provisions & Powers", "type": "branch", "date": "Overview", "children": [
                {"label": "Enacted in 1981 under Article 253 of the Constitution to implement decisions of the Stockholm Conference 1972", "type": "leaf"},
                {"label": "CPCB & SPCBs: Extended powers of Central and State Pollution Control Boards (created under Water Act 1974) to monitor air quality", "type": "leaf"}
            ]},
            {"label": "Key Mandates", "type": "branch", "date": "Mandates", "children": [
                {"label": "Consent to Establish (CTE): Industries must obtain permission from SPCBs before setting up units in Air Pollution Control Areas", "type": "leaf"},
                {"label": "Standards: SPCBs are empowered to set emission standards for industrial plants and automobiles in consultation with CPCB", "type": "leaf"}
            ]},
            {"label": "1987 Amendment", "type": "branch", "date": "Amendments", "children": [
                {"label": "Noise Pollution: Formally included noise within the definition of air pollutants under the Act", "type": "leaf"},
                {"label": "Penalties: Increased penalties for non-compliance and empowered SPCBs to cut off electricity/water supply to polluting units", "type": "leaf"}
            ]},
            {"label": "UPSC Exam Focus", "type": "branch", "date": "UPSC Focus", "children": [
                {"label": "Constitutional Link: Implemented under international obligations (Stockholm Declaration) via parliamentary legislation", "type": "leaf"},
                {"label": "Air Pollution Control Areas: States can declare any region as a control area, banning burning of polluting fuels", "type": "leaf"}
            ]}
        ],
        "hi": [
            {"label": "अधिनियम के प्रावधान और शक्तियां", "type": "branch", "date": "अवलोकन", "children": [
                {"label": "स्टॉकहोम सम्मेलन 1972 के निर्णयों को लागू करने के लिए संविधान के अनुच्छेद 253 के तहत 1981 में अधिनियमित", "type": "leaf"},
                {"label": "CPCB और SPCBs: वायु गुणवत्ता की निगरानी के लिए प्रदूषण नियंत्रण बोर्डों की शक्तियों का विस्तार किया", "type": "leaf"}
            ]},
            {"label": "मुख्य अधिदेश (Mandates)", "type": "branch", "date": "अधिदेश", "children": [
                {"label": "स्थापना की सहमति (CTE): उद्योगों को वायु प्रदूषण नियंत्रण क्षेत्रों में इकाइयां स्थापित करने से पहले SPCB से अनुमति लेना आवश्यक", "type": "leaf"},
                {"label": "मानक: SPCBs को CPCB के परामर्श से औद्योगिक इकाइयों और वाहनों के लिए उत्सर्जन मानक तय करने का अधिकार है", "type": "leaf"}
            ]},
            {"label": "1987 का संशोधन", "type": "branch", "date": "संशोधन", "children": [
                {"label": "ध्वनि प्रदूषण: अधिनियम के तहत वायु प्रदूषकों की परिभाषा के भीतर ध्वनि को औपचारिक रूप से शामिल किया गया", "type": "leaf"},
                {"label": "दंडात्मक प्रावधान: नियमों के उल्लंघन के लिए दंड बढ़ाया गया और प्रदूषणकारी इकाइयों की बिजली/पानी काटने का अधिकार दिया गया", "type": "leaf"}
            ]},
            {"label": "यूपीएससी परीक्षा दृष्टिकोण", "type": "branch", "date": "परीक्षा", "children": [
                {"label": "संवैधानिक संबंध: संसदीय कानून के माध्यम से अंतर्राष्ट्रीय दायित्वों (स्टॉकहोम घोषणा) के तहत लागू किया गया", "type": "leaf"},
                {"label": "वायु प्रदूषण नियंत्रण क्षेत्र: राज्य किसी भी क्षेत्र को नियंत्रण क्षेत्र घोषित कर प्रदूषणकारी ईंधन के दहन पर प्रतिबंध लगा सकते हैं", "type": "leaf"}
            ]}
        ]
    },
    {
        "keys": ["mining-and-environment", "mining-and-pollution", "sustainable-mining"],
        "en": [
            {"label": "Acid Mine Drainage", "type": "branch", "date": "Overview", "children": [
                {"label": "AMD: Outflow of acidic water from metal or coal mines, caused by chemical reaction of rainwater with iron sulfide minerals (pyrite), generating sulfuric acid that leaches heavy metals", "type": "leaf"}
            ]},
            {"label": "Environmental Hazards", "type": "branch", "date": "Hazards", "children": [
                {"label": "Fly-rock & Dust: Blasting generates high respirable silica dust (PM10) and fly-rock; tailing dams risk structural collapse, releasing toxic slurry into river basins", "type": "leaf"}
            ]},
            {"label": "Sustainable Mining", "type": "branch", "date": "Reclamation", "children": [
                {"label": "Reclamation: Backfilling mine voids, planting native species to restore topsoil, using dust suppressants, and implementing green mining technologies", "type": "leaf"}
            ]},
            {"label": "UPSC Exam Focus", "type": "branch", "date": "UPSC Focus", "children": [
                {"label": "District Mineral Foundation (DMF): Non-profit trust in mining districts funded by miners to work for the interest and benefit of mining-affected persons and areas", "type": "leaf"}
            ]}
        ],
        "hi": [
            {"label": "अम्लीय खान जल निकासी", "type": "branch", "date": "अवलोकन", "children": [
                {"label": "AMD: धातुओं या कोयले की खानों से अम्लीय जल का बहाव, वर्षा जल की आयरन सल्फाइड खनिज (पाइराइट) के साथ प्रतिक्रिया से होता है, जिससे सल्फ्यूरिक एसिड का निर्माण होता है", "type": "leaf"}
            ]},
            {"label": "पर्यावरण के खतरे", "type": "branch", "date": "खतरे", "children": [
                {"label": "महीन धूल और मलबे: विस्फोटों से भारी मात्रा में श्वसन योग्य सिलिका धूल निकलती है; टेलिंग बांधों के टूटने से विषाक्त घोल नदियों में मिल जाता है", "type": "leaf"}
            ]},
            {"label": "सतत खनन", "type": "branch", "date": "पुनर्प्राप्ति", "children": [
                {"label": "पुनर्प्राप्ति: खदानों के गड्ढों को भरना, देशी प्रजातियों का वृक्षारोपण और हरित खनन तकनीकों का उपयोग", "type": "leaf"}
            ]},
            {"label": "यूपीएससी परीक्षा दृष्टिकोण", "type": "branch", "date": "परीक्षा", "children": [
                {"label": "जिला खनिज फाउंडेशन (DMF): खनन प्रभावित लोगों और क्षेत्रों के कल्याण के लिए काम करने हेतु खनन जिलों में स्थापित गैर-लाभकारी ट्रस्ट", "type": "leaf"}
            ]}
        ]
    },
    {
        "keys": ["biological-pollution", "biological-contaminants", "sources-of-biological", "harmful-effects-from-biological"],
        "en": [
            {"label": "Primary Contaminants", "type": "branch", "date": "Agents", "children": [
                {"label": "Living agents: Molds, pollen, animal dander, bacteria, viruses, and house dust mites that act as bio-aerosols in the air", "type": "leaf"}
            ]},
            {"label": "Key Sources", "type": "branch", "date": "Sources", "children": [
                {"label": "Indoor environments: Poorly maintained air conditioners, humidifiers, damp walls, and animal shelters acting as breeding grounds", "type": "leaf"}
            ]},
            {"label": "Harmful Effects", "type": "branch", "date": "Allergies", "children": [
                {"label": "Allergies: Triggers allergic rhinitis, occupational asthma, hypersensitivity pneumonitis, and infectious diseases (e.g. Legionnaires' disease)", "type": "leaf"}
            ]},
            {"label": "UPSC Exam Focus", "type": "branch", "date": "UPSC Focus", "children": [
                {"label": "Bio-Aerosols: Airborne particles of biological origin; control via HEPA filtration, relative humidity maintenance (30-50%), and UV irradiation", "type": "leaf"}
            ]}
        ],
        "hi": [
            {"label": "प्राथमिक प्रदूषक", "type": "branch", "date": "कारक", "children": [
                {"label": "सजीव एजेंट: हवा में जैव-एयरोसोल के रूप में कार्य करने वाले मोल्ड, पराग, कवक, बैक्टीरिया, वायरस और धूल के कीड़े", "type": "leaf"}
            ]},
            {"label": "प्रमुख स्रोत", "type": "branch", "date": "स्रोत", "children": [
                {"label": "इनडोर वातावरण: खराब रखरखाव वाले एयर कंडीशनर, नमी वाली दीवारें और पालतू जानवरों के रहने की जगह", "type": "leaf"}
            ]},
            {"label": "हानिकारक प्रभाव", "type": "branch", "date": "लक्षण", "children": [
                {"label": "एलर्जी और रोग: एलर्जिक राइनाइटिस, व्यावसायिक अस्थमा, अतिसंवेदनशील न्यूमोनाइटिस और संक्रामक रोग (जैसे लीजियोनेयर्स रोग)", "type": "leaf"}
            ]},
            {"label": "यूपीएससी परीक्षा दृष्टिकोण", "type": "branch", "date": "परीक्षा", "children": [
                {"label": "बायो-एयरोसोल्स: जैविक मूल के हवा में उड़ने वाले कण; HEPA फिल्टर और यूवी विकिरण द्वारा नियंत्रण", "type": "leaf"}
            ]}
        ]
    },
    {
        "keys": ["ambient-air-quality-monitoring", "caaqms"],
        "en": [
            {"label": "CAAQMS Features", "type": "branch", "date": "Overview", "children": [
                {"label": "Real-time monitoring: Continuous Ambient Air Quality Monitoring System; provides instantaneous, automatic data for public AQI calculation", "type": "leaf"}
            ]},
            {"label": "Monitored Parameters", "type": "branch", "date": "Pollutants", "children": [
                {"label": "8 Key Pollutants: PM10, PM2.5, SO2, NOx, CO, O3, NH3, and Benzene tracked in real-time", "type": "leaf"}
            ]},
            {"label": "Data Application", "type": "branch", "date": "Application", "children": [
                {"label": "Decision support: Triggers Graded Response Action Plan (GRAP) actions when hourly averages cross warning thresholds", "type": "leaf"}
            ]},
            {"label": "UPSC Exam Focus", "type": "branch", "date": "UPSC Focus", "children": [
                {"label": "SPCB Network: Managed by State Pollution Control Boards; data is fed directly into CPCB's national portal to ensure transparent reporting", "type": "leaf"}
            ]}
        ],
        "hi": [
            {"label": "CAAQMS की विशेषताएं", "type": "branch", "date": "अवलोकन", "children": [
                {"label": "वास्तविक समय निगरानी: सतत परिवेशी वायु गुणवत्ता निगरानी प्रणाली; सार्वजनिक AQI की गणना के लिए तत्काल डेटा देती है", "type": "leaf"}
            ]},
            {"label": "निगरानी किए जाने वाले प्रदूषक", "type": "branch", "date": "प्रदूषक", "children": [
                {"label": "8 प्रमुख प्रदूषक: PM10, PM2.5, SO2, NOx, CO, O3, NH3 और बेंजीन की निगरानी", "type": "leaf"}
            ]},
            {"label": "डेटा अनुप्रयोग", "type": "branch", "date": "अनुप्रयोग", "children": [
                {"label": "निर्णय समर्थन: प्रति घंटा औसत चेतावनी सीमा को पार करने पर GRAP प्रतिबंधों को लागू करना", "type": "leaf"}
            ]},
            {"label": "यूपीएससी परीक्षा दृष्टिकोण", "type": "branch", "date": "परीक्षा", "children": [
                {"label": "SPCB नेटवर्क: राज्य प्रदूषण नियंत्रण बोर्डों द्वारा प्रबंधित; डेटा सीधे CPCB के पोर्टल पर जाता है", "type": "leaf"}
            ]}
        ]
    },
    {
        "keys": ["marine-pollution", "sources-of-marine", "effects-of-marine", "trash-and-other-debris"],
        "en": [
            {"label": "Sources of Pollution", "type": "branch", "date": "Sources", "children": [
                {"label": "Land-based runoff: Accounts for 80% of marine pollution; includes agricultural fertilizer runoff, sewage, and industrial heavy metals", "type": "leaf"}
            ]},
            {"label": "Debris & Trash", "type": "branch", "date": "Debris", "children": [
                {"label": "Macroplastics: Lost fishing gear (ghost nets), plastic bags, and bottles forming trash vortexes in oceanic gyres", "type": "leaf"}
            ]},
            {"label": "Ecological Damage", "type": "branch", "date": "Impacts", "children": [
                {"label": "Eutrophication: Coastal nutrient loading leading to massive algal blooms, hypoxia, and dead zone formations", "type": "leaf"}
            ]},
            {"label": "UPSC Exam Focus", "type": "branch", "date": "UPSC Focus", "children": [
                {"label": "London Convention 1972: Global treaty to protect the marine environment from human dumping activities; updated by the 1996 Protocol", "type": "leaf"}
            ]}
        ],
        "hi": [
            {"label": "प्रदूषण के स्रोत", "type": "branch", "date": "स्रोत", "children": [
                {"label": "भूमि आधारित अपवाह: समुद्री प्रदूषण का 80% हिस्सा; इसमें कृषि उर्वरकों का बहाव, अनुपचारित सीवेज और भारी धातु शामिल हैं", "type": "leaf"}
            ]},
            {"label": "कचरा और मलबा", "type": "branch", "date": "मलबा", "children": [
                {"label": "मैक्रोप्लास्टिक: खोए हुए मछली पकड़ने के जाल (घोस्ट नेट), प्लास्टिक बैग और बोतलें जो महासागरीय जायर में तैरती हैं", "type": "leaf"}
            ]},
            {"label": "पारिस्थितिक क्षति", "type": "branch", "date": "प्रभाव", "children": [
                {"label": "यूट्रोफिकेशन: तटीय पोषक तत्वों की वृद्धि से बड़े पैमाने पर शैवाल प्रस्फुटन और 'डेड ज़ोन' का निर्माण", "type": "leaf"}
            ]},
            {"label": "यूपीएससी परीक्षा दृष्टिकोण", "type": "branch", "date": "परीक्षा", "children": [
                {"label": "लंदन कन्वेंशन 1972: डंपिंग गतिविधियों से समुद्री पर्यावरण की रक्षा करने के लिए वैश्विक संधि; 1996 के प्रोटोकॉल द्वारा संशोधित", "type": "leaf"}
            ]}
        ]
    },
    {
        "keys": ["microplastics"],
        "en": [
            {"label": "Definition & Types", "type": "branch", "date": "Overview", "children": [
                {"label": "Microplastics: Plastic particles < 5mm in diameter; primary microplastics (microbeads in cosmetics) vs secondary (breakdown of larger plastics)", "type": "leaf"}
            ]},
            {"label": "Trophic Transfer", "type": "branch", "date": "Transfer", "children": [
                {"label": "Bioaccumulation: Ingested by zooplankton and small fish; biomagnified up the food chain, carrying persistent organic pollutants (POPs)", "type": "leaf"}
            ]},
            {"label": "Health Impacts", "type": "branch", "date": "Health", "children": [
                {"label": "Endocrine disruptors: Leaches toxic additives like phthalates and Bisphenol A (BPA) into organism tissues", "type": "leaf"}
            ]},
            {"label": "UPSC Exam Focus", "type": "branch", "date": "UPSC Focus", "children": [
                {"label": "Plastic Waste Management Rules: India banned single-use plastics and microbeads in personal care products to restrict microplastic leakage", "type": "leaf"}
            ]}
        ],
        "hi": [
            {"label": "परिभाषा और प्रकार", "type": "branch", "date": "अवलोकन", "children": [
                {"label": "माइक्रोप्लास्टिक्स: व्यास में < 5 मिमी के प्लास्टिक कण; प्राथमिक (कॉस्मेटिक्स में माइक्रोबीड्स) बनाम द्वितीयक (बड़े टुकड़ों का टूटना)", "type": "leaf"}
            ]},
            {"label": "खाद्य श्रृंखला स्थानांतरण", "type": "branch", "date": "स्थानांतरण", "children": [
                {"label": "जैव-आवर्धन: जंतु प्लवक और छोटी मछलियों द्वारा निगला जाना; खाद्य श्रृंखला में ऊपर जाने पर सांद्रता बढ़ना", "type": "leaf"}
            ]},
            {"label": "स्वास्थ्य पर प्रभाव", "type": "branch", "date": "प्रभाव", "children": [
                {"label": "अंतःस्रावी व्यवधान: थैलेट्स और बिस्फेनॉल ए (BPA) जैसे विषाक्त पदार्थों का रिसाव कर हार्मोनल संतुलन बिगाड़ना", "type": "leaf"}
            ]},
            {"label": "यूपीएससी परीक्षा दृष्टिकोण", "type": "branch", "date": "परीक्षा", "children": [
                {"label": "प्लास्टिक अपशिष्ट प्रबंधन नियम: भारत ने सौंदर्य उत्पादों में माइक्रोबीड्स और सिंगल-यूज़ प्लास्टिक को पूरी तरह प्रतिबंधित किया है", "type": "leaf"}
            ]}
        ]
    },
    {
        "keys": ["national-air-quality-index", "naqi", "naaqs"],
        "en": [
            {"label": "NAQI Framework", "type": "branch", "date": "Framework", "children": [
                {"label": "One Number-One Color-One Description: Launched in 2014; simplifies air quality reporting into 6 categories (Good to Severe)", "type": "leaf"}
            ]},
            {"label": "AQI 8 Pollutants", "type": "branch", "date": "8 Pollutants", "children": [
                {"label": "Key parameters: PM10, PM2.5, NO2, SO2, CO, O3, NH3, and Lead (Pb); requires at least 3 pollutants (with PM) to calculate AQI", "type": "leaf"}
            ]},
            {"label": "NAAQS Standard", "type": "branch", "date": "NAAQS", "children": [
                {"label": "National Ambient Air Quality Standards: Includes 12 pollutants (adding Benzene, Benzo-a-pyrene, Arsenic, Nickel to AQI list) monitored nationally", "type": "leaf"}
            ]},
            {"label": "UPSC Exam Focus", "type": "branch", "date": "UPSC Focus", "children": [
                {"label": "Exclusions: Carbon Dioxide (CO2) and Volatile Organic Compounds (VOCs) are NOT included in AQI or NAAQS lists", "type": "leaf"}
            ]}
        ],
        "hi": [
            {"label": "NAQI ढांचा", "type": "branch", "date": "ढांचा", "children": [
                {"label": "एक नंबर-एक रंग-एक विवरण: 2014 में लॉन्च; वायु गुणवत्ता को 6 श्रेणियों (अच्छे से गंभीर) में सरल बनाता है", "type": "leaf"}
            ]},
            {"label": "AQI के 8 प्रदूषक", "type": "branch", "date": "8 प्रदूषक", "children": [
                {"label": "मुख्य पैरामीटर: PM10, PM2.5, NO2, SO2, CO, O3, NH3 और सीसा (Pb); गणना के लिए कम से कम 3 प्रदूषक आवश्यक", "type": "leaf"}
            ]},
            {"label": "NAAQS मानक", "type": "branch", "date": "NAAQS", "children": [
                {"label": "राष्ट्रीय परिवेशी वायु गुणवत्ता मानक: 12 प्रदूषक शामिल हैं (AQI सूची में बेंजीन, आर्सेनिक, निकेल जोड़कर)", "type": "leaf"}
            ]},
            {"label": "यूपीएससी परीक्षा दृष्टिकोण", "type": "branch", "date": "परीक्षा", "children": [
                {"label": "अपवाद: कार्बन डाइऑक्साइड (CO2) और वाष्पशील कार्बनिक यौगिक (VOCs) AQI या NAAQS सूची में शामिल नहीं हैं", "type": "leaf"}
            ]}
        ]
    },
    {
        "keys": ["occupational-health-hazards", "occupational-hazard"],
        "en": [
            {"label": "Physical Hazards", "type": "branch", "date": "Physical", "children": [
                {"label": "Extreme exposures: Noise-induced hearing loss, heat stroke in boiler units, and ionizing radiation in nuclear facilities", "type": "leaf"}
            ]},
            {"label": "Chemical & Biological", "type": "branch", "date": "Chemical", "children": [
                {"label": "Toxic inhalations: Silicosis, asbestosis, lead poisoning (plumbism), and anthrax infection (wool sorter's disease) in tanneries", "type": "leaf"}
            ]},
            {"label": "Ergonomic Hazards", "type": "branch", "date": "Ergonomic", "children": [
                {"label": "Repetitive strain: Musculoskeletal disorders (MSDs) from poor posture, heavy lifting, and vibrating machinery", "type": "leaf"}
            ]},
            {"label": "UPSC Exam Focus", "type": "branch", "date": "UPSC Focus", "children": [
                {"label": "ILO Conventions: Convention 155 (Occupational Safety and Health) and Convention 187 (Promotional Framework for OSH)", "type": "leaf"}
            ]}
        ],
        "hi": [
            {"label": "भौतिक खतरे", "type": "branch", "date": "भौतिक", "children": [
                {"label": "अत्यधिक संपर्क: शोर-प्रेरित बहरापन, बॉयलर इकाइयों में हीट स्ट्रोक और परमाणु सुविधाओं में विकिरण जोखिम", "type": "leaf"}
            ]},
            {"label": "रासायनिक और जैविक", "type": "branch", "date": "रासायनिक", "children": [
                {"label": "विषाक्त श्वसन: सिलिकोसिस, एस्बेस्टोसिस, सीसा विषाक्तता और एंथ्रेक्स संक्रमण (ऊन छांटने की बीमारी)", "type": "leaf"}
            ]},
            {"label": "एर्गोनोमिक खतरे", "type": "branch", "date": "तनाव", "children": [
                {"label": "शारीरिक तनाव: खराब मुद्रा, भारी वजन उठाने और कंपन करने वाली मशीनों से मस्कुलोस्केलेटल विकार (MSDs) होना", "type": "leaf"}
            ]},
            {"label": "यूपीएससी परीक्षा दृष्टिकोण", "type": "branch", "date": "परीक्षा", "children": [
                {"label": "ILO कन्वेंशन: कन्वेंशन 155 (व्यावसायिक सुरक्षा और स्वास्थ्य) और कन्वेंशन 187 (OSH के लिए संवर्धनात्मक ढांचा)", "type": "leaf"}
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
    "pollution": "प्रदूषण",
    "occupational": "व्यावसायिक",
    "hazards": "खतरे",
    "hazard": "खतरा",
    "air": "वायु",
    "quality": "गुणवत्ता",
    "early": "प्रारंभिक",
    "warning": "चेतावनी",
    "system": "प्रणाली",
    "graded": "क्रमबद्ध",
    "response": "प्रतिक्रिया",
    "action": "कार्य",
    "plan": "योजना",
    "basics": "बुनियाद",
    "biological": "जैविक",
    "corrective": "सुधारात्मक",
    "actions": "कार्य",
    "causes": "कारण",
    "noise": "ध्वनि",
    "thermal": "तापीय",
    "classification": "वर्गीकरण",
    "pollutants": "प्रदूषक",
    "concept": "अवधारणा",
    "dead": "मृत",
    "zone": "ज़ोन",
    "acidification": "अम्लीकरण",
    "continuous": "सतत",
    "ambient": "परिवेशी",
    "monitoring": "निगरानी",
    "control": "नियंत्रण",
    "effect": "प्रभाव",
    "effects": "प्रभाव",
    "marine": "समुद्री",
    "health": "स्वास्थ्य",
    "fly": "फ्लाई",
    "ash": "ऐश",
    "harmful": "हानिकारक",
    "radioactive": "रेडियोधर्मी",
    "microplastics": "माइक्रोप्लास्टिक",
    "impact": "प्रभाव",
    "mining": "खनन",
    "environment": "पर्यावरण",
    "national": "राष्ट्रीय",
    "index": "सूचकांक",
    "standards": "मानक",
    "levels": "स्तर",
    "asbestosis": "एस्बेस्टोसिस",
    "black": "ब्लैक",
    "lung": "लंग (फेफड़ा)",
    "disease": "बीमारी",
    "byssinosis": "बायसिनोसिस",
    "pneumoconiosis": "न्यूमोकोनियोसिस",
    "silicosis": "सिलिकोसिस",
    "oil": "तेल",
    "spill": "रिसाव",
    "indicator": "संकेतक",
    "respirable": "श्वसन योग्य",
    "suspended": "निलंबित",
    "particulate": "कणिकीय",
    "matter": "पदार्थ",
    "sources": "स्रोत",
    "sustainable": "टिकाऊ",
    "prevention": "निवारण",
    "trash": "कचरा",
    "debris": "मलबे",
    "comparing": "तुलना",
    "dissolved": "घुलित",
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
                {"label": f"Scientific Framework: Analyzing how {t} interacts within pollution and occupational hazard systems", "type": "leaf"}
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
                {"label": f"Mains Answer Writing: Linking {t} with contemporary environmental policies and health regulations", "type": "leaf"}
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
                {"label": f"वैज्ञानिक ढांचा: {t} पर्यावरण, प्रदूषण और स्वास्थ्य प्रणालियों के भीतर कैसे कार्य करता है", "type": "leaf"}
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
                {"label": f"प्रभाव: {t} में परिवर्तन क्षेत्रीय जैव विविधता, स्वास्थ्य और मानवीय गतिविधियों को कैसे प्रभावित करते हैं", "type": "leaf"},
                {"label": f"क्षेत्रीय मामले: {t} से संबंधित उल्लेखनीय वैश्विक उदाहरण और संकेतक", "type": "leaf"}
            ]
        },
        {
            "label": f"यूपीएससी परीक्षा दृष्टिकोण (UPSC Focus)",
            "type": "branch",
            "date": "परीक्षा",
            "children": [
                {"label": f"प्रारंभिक परीक्षा: {t} से जुड़े महत्वपूर्ण तथ्य, शब्दावली और सामान्य परीक्षा भ्रम", "type": "leaf"},
                {"label": f"मुख्य परीक्षा उत्तर लेखन: {t} को समकालीन पर्यावरण नीतियों और स्वास्थ्य सुरक्षा नियमों से जोड़ना", "type": "leaf"}
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
    
    # Restructure branches dynamically to add more branches before leaves (multibranching!)
    def restructure_node(node):
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
