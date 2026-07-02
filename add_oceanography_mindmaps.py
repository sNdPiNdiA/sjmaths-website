#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import re
import json

BASE = r"upsc/geography/Oceanography"

def get_clean_title(folder_name):
    title = folder_name.replace('-', ' ')
    skip = {'of', 'and', 'the', 'for', 'in', 'with', 'to', 'on', 'by', 'or', 'a', 'an'}
    return ' '.join(w if w.lower() in skip else w.capitalize() for w in title.split())

def get_custom_branches(folder_name, is_hindi):
    fl = folder_name.lower()

    # 1. Abiotic Deposits
    if 'abiotic' in fl:
        if is_hindi:
            return [
                {"label": "अजैविक निक्षेप: परिभाषा और प्रकार", "type": "branch", "date": "प्रकार", "children": [
                    {"label": "मैंगनीज नोड्यूल: प्रशांत महासागर तल पर; Fe-Mn-Cu-Ni-Co से समृद्ध; औद्योगिक महत्व; ISA (International Seabed Authority) द्वारा नियंत्रण", "type": "leaf"},
                    {"label": "फेरोमैंगनीज क्रस्ट: समुद्री पर्वतों पर; गहरे समुद्र तल; कोबाल्ट से समृद्ध; भविष्य के खनिज संसाधन", "type": "leaf"},
                    {"label": "हाइड्रोथर्मल वेंट्स: मध्य-महासागरीय कटकों पर; जिंक, कॉपर, गोल्ड, सिल्वर सल्फाइड निक्षेप", "type": "leaf"},
                    {"label": "लाल मृत्तिका (Red Clay): गहरे समुद्र में; रेडियोलेरिया, मुख्यतः अजैविक; बहुत धीमी जमाव दर", "type": "leaf"}
                ]},
                {"label": "भारत का गहरे समुद्र में खनन", "type": "branch", "date": "भारत", "children": [
                    {"label": "भारत ISA का अग्रणी निवेशक: केंद्रीय हिंद महासागर बेसिन (CIOB) में पॉलीमेटालिक नोड्यूल खनन अधिकार", "type": "leaf"},
                    {"label": "Deep Ocean Mission 2021: 6000 मीटर गहराई; मानवयुक्त पनडुब्बी (Matsyayana 6000) विकास", "type": "leaf"}
                ]}
            ]
        else:
            return [
                {"label": "Abiotic Deposits: Types", "type": "branch", "date": "Types", "children": [
                    {"label": "Manganese Nodules: Pacific Ocean floor; rich in Fe-Mn-Cu-Ni-Co; regulated by ISA (International Seabed Authority)", "type": "leaf"},
                    {"label": "Ferromanganese Crusts: On seamounts; cobalt-rich; considered future deep-sea mineral resources", "type": "leaf"},
                    {"label": "Hydrothermal Vents: Mid-ocean ridges; zinc, copper, gold, silver sulfide deposits ('Black Smokers')", "type": "leaf"},
                    {"label": "Red Clay (Pelagic): Deep-sea abyssal plains; slow deposition; mainly inorganic fine-grained clay", "type": "leaf"}
                ]},
                {"label": "India's Deep-Sea Mining", "type": "branch", "date": "India", "children": [
                    {"label": "India as ISA pioneer investor: Polymetallic nodule mining rights in Central Indian Ocean Basin (CIOB)", "type": "leaf"},
                    {"label": "Deep Ocean Mission 2021: 6000m depth; Matsyayana 6000 manned submersible development", "type": "leaf"}
                ]}
            ]

    # 2. Biotic Deposits
    elif 'biotic' in fl:
        if is_hindi:
            return [
                {"label": "जैविक निक्षेप: प्रकार", "type": "branch", "date": "प्रकार", "children": [
                    {"label": "ग्लोबिगेरिना ऊज़: 47% महासागर तल; उथले गर्म पानी; CaCO₃ कंकालों से; कैलकेरियस ऊज़", "type": "leaf"},
                    {"label": "टेरोपोड ऊज़: गर्म अटलांटिक और भूमध्यसागर; तैरने वाले मोलस्क; तेज़ घुलनशीलता से CCD के ऊपर", "type": "leaf"},
                    {"label": "रेडियोलेरियन ऊज़: गहरे उष्णकटिबंधीय समुद्र; सिलिका कंकाल; CCD से नीचे भी स्थिर", "type": "leaf"},
                    {"label": "डायटम ऊज़: ध्रुवीय/उपध्रुवीय क्षेत्र; सिलिका; अंटार्कटिक महासागर में प्रचुर; तेल और गैस का प्राकृतिक स्रोत", "type": "leaf"}
                ]},
                {"label": "कार्बोनेट मुआवजा गहराई (CCD)", "type": "branch", "date": "CCD", "children": [
                    {"label": "CCD = ~4000-5000 मीटर: इस गहराई के नीचे CaCO₃ घुल जाता है; कैलकेरियस ऊज़ केवल CCD के ऊपर", "type": "leaf"},
                    {"label": "CCD के नीचे: केवल सिलिका निक्षेप (रेडियोलेरियन/डायटम) या लाल मृत्तिका मिलती है", "type": "leaf"}
                ]}
            ]
        else:
            return [
                {"label": "Biotic Deposits: Types", "type": "branch", "date": "Types", "children": [
                    {"label": "Globigerina Ooze: 47% of ocean floor; warm shallow waters; CaCO₃ foraminiferal shells; calcareous", "type": "leaf"},
                    {"label": "Pteropod Ooze: Warm Atlantic & Mediterranean; planktonic mollusc shells; found above CCD", "type": "leaf"},
                    {"label": "Radiolarian Ooze: Deep tropical seas; siliceous skeletons; stable below CCD unlike calcareous ooze", "type": "leaf"},
                    {"label": "Diatom Ooze: Polar/sub-polar seas; siliceous; abundant in Antarctic Ocean; source of oil/gas", "type": "leaf"}
                ]},
                {"label": "Carbonate Compensation Depth (CCD)", "type": "branch", "date": "CCD", "children": [
                    {"label": "CCD ~4000-5000m: Below this depth CaCO₃ dissolves completely; calcareous ooze only above CCD", "type": "leaf"},
                    {"label": "Below CCD: Only siliceous deposits (Radiolarian/Diatom ooze) or Red Clay accumulate", "type": "leaf"}
                ]}
            ]

    # 3. Component Processes (General)
    elif fl == 'component-processes':
        if is_hindi:
            return [
                {"label": "जल चक्र के घटक प्रक्रियाएँ", "type": "branch", "date": "चक्र", "children": [
                    {"label": "वाष्पीकरण (Evaporation): सूर्य ऊर्जा से महासागरों/नदियों का पानी वाष्प बनना; 80% सागर से", "type": "leaf"},
                    {"label": "वाष्पोत्सर्जन (Transpiration): पौधों से वाष्प का निकलना; वनस्पति आवरण पर निर्भर", "type": "leaf"},
                    {"label": "संघनन (Condensation): वाष्प → बादल → ओस/पाला; ऊपर उठने पर तापमान गिरना", "type": "leaf"},
                    {"label": "अवक्षेपण (Precipitation): वर्षा, हिमपात, ओले; भारत में मानसून = 80% वर्षा", "type": "leaf"},
                    {"label": "अंतःस्यंदन (Infiltration): जमीन में जल प्रवेश; भूजल पुनर्भरण; मृदा प्रकार और वनस्पति पर निर्भर", "type": "leaf"}
                ]},
                {"label": "अपवाह और भूजल", "type": "branch", "date": "अपवाह", "children": [
                    {"label": "सतही अपवाह: ढाल के साथ जल का बहाव; नदियाँ और नाले; बाढ़ से संबंध", "type": "leaf"},
                    {"label": "भूजल प्रवाह: धीमी; जलभृत (Aquifer) में; आर्टेशियन कूप; झरने (Springs)", "type": "leaf"}
                ]}
            ]
        else:
            return [
                {"label": "Component Processes of Hydrological Cycle", "type": "branch", "date": "Cycle", "children": [
                    {"label": "Evaporation: Solar energy converts ocean/lake/river water to vapour; 80% from ocean surfaces", "type": "leaf"},
                    {"label": "Transpiration: Water vapour release by plants; depends on vegetation type and density", "type": "leaf"},
                    {"label": "Condensation: Vapour → clouds → dew/frost; occurs as rising air cools to dew point", "type": "leaf"},
                    {"label": "Precipitation: Rain, snow, sleet, hail; India gets ~80% rainfall from SW Monsoon", "type": "leaf"},
                    {"label": "Infiltration: Water entering soil; groundwater recharge; depends on soil permeability", "type": "leaf"}
                ]},
                {"label": "Runoff & Groundwater", "type": "branch", "date": "Runoff", "children": [
                    {"label": "Surface Runoff: Water flowing downslope into streams and rivers; causes flood events", "type": "leaf"},
                    {"label": "Groundwater Flow: Slow subsurface movement; aquifer storage; artesian wells; springs", "type": "leaf"}
                ]}
            ]

    # 4. Component Processes Hydrological Cycle
    elif 'component' in fl and 'hydrological' in fl:
        if is_hindi:
            return [
                {"label": "जल विज्ञान चक्र: ऊर्जा और जल संतुलन", "type": "branch", "date": "विस्तृत चक्र", "children": [
                    {"label": "वैश्विक जल वितरण: 97.5% खारा; 2.5% मीठा; मीठे पानी का 70% हिमनद और बर्फ में; 30% भूजल", "type": "leaf"},
                    {"label": "सौर ऊर्जा की भूमिका: जल चक्र का इंजन; वाष्पीकरण में कुल सौर ऊर्जा का 23% उपयोग", "type": "leaf"},
                    {"label": "वैश्विक वर्षा: औसत 1000 mm/वर्ष; विषुवत रेखा पर 2000+ mm; उष्ण मरुस्थलों में <250 mm", "type": "leaf"}
                ]},
                {"label": "जल चक्र और जलवायु परिवर्तन", "type": "branch", "date": "जलवायु प्रभाव", "children": [
                    {"label": "तापमान वृद्धि → अधिक वाष्पीकरण → अधिक तीव्र वर्षा लेकिन असमान वितरण", "type": "leaf"},
                    {"label": "हिमनद पिघलना: जल संग्रह कम; नदियों में मौसमी प्रवाह असंतुलित; बाढ़ और सूखे दोनों", "type": "leaf"},
                    {"label": "मानसून व्यवधान: ENSO (El Niño) से भारतीय मानसून प्रभावित; सूखा और अतिवृष्टि", "type": "leaf"}
                ]}
            ]
        else:
            return [
                {"label": "Hydrological Cycle: Energy & Water Balance", "type": "branch", "date": "Detailed Cycle", "children": [
                    {"label": "Global Water Distribution: 97.5% saline; 2.5% freshwater; 70% of freshwater locked in glaciers/ice caps", "type": "leaf"},
                    {"label": "Solar Energy as Driver: Powers evaporation; ~23% of incoming solar energy drives the water cycle", "type": "leaf"},
                    {"label": "Global Precipitation: Average ~1000 mm/yr; 2000+ mm at equator; <250 mm in hot deserts", "type": "leaf"}
                ]},
                {"label": "Water Cycle & Climate Change", "type": "branch", "date": "Climate Link", "children": [
                    {"label": "Warming → more evaporation → more intense but uneven precipitation events globally", "type": "leaf"},
                    {"label": "Glacial Melt: Reduces stored freshwater; disrupts seasonal river flow; flash floods then drought", "type": "leaf"},
                    {"label": "Monsoon disruption: ENSO/El Niño affects Indian monsoon; deficit years and flood years", "type": "leaf"}
                ]}
            ]

    # 5. Conservation of Water Resources
    elif 'conservation' in fl and 'water' in fl:
        if is_hindi:
            return [
                {"label": "जल संसाधन संरक्षण: आवश्यकता", "type": "branch", "date": "आवश्यकता", "children": [
                    {"label": "भारत की स्थिति: विश्व की 17% जनसंख्या; केवल 4% मीठे जल संसाधन; 2025 तक जल-संकट की आशंका", "type": "leaf"},
                    {"label": "NITI Aayog: 21 शहर 2020 तक भूजल शून्य होने की स्थिति में; Day Zero परिदृश्य", "type": "leaf"}
                ]},
                {"label": "संरक्षण के तरीके और नीतियाँ", "type": "branch", "date": "उपाय", "children": [
                    {"label": "वर्षा जल संचयन: छत से वर्षा जल संग्रह; दिल्ली, चेन्नई में अनिवार्य; 'हर घर जल' लक्ष्य", "type": "leaf"},
                    {"label": "ड्रिप/स्प्रिंकलर सिंचाई: परंपरागत की तुलना में 40-70% जल बचत; PM कृषि सिंचाई योजना", "type": "leaf"},
                    {"label": "चेक डैम और जोहड़: राजस्थान का पारंपरिक जल संचयन; तरुण भारत संघ का कार्य", "type": "leaf"},
                    {"label": "जल शक्ति मंत्रालय (2019): जल जीवन मिशन; 2024 तक हर घर को नल कनेक्शन", "type": "leaf"}
                ]}
            ]
        else:
            return [
                {"label": "Water Conservation: Need", "type": "branch", "date": "Need", "children": [
                    {"label": "India's Crisis: 17% of world's population but only 4% of global freshwater resources", "type": "leaf"},
                    {"label": "NITI Aayog Warning: 21 cities to reach groundwater zero by 2020; Day Zero scenario", "type": "leaf"}
                ]},
                {"label": "Conservation Methods & Policies", "type": "branch", "date": "Methods", "children": [
                    {"label": "Rainwater Harvesting: Rooftop collection mandatory in Delhi, Chennai; 'Har Ghar Jal' target", "type": "leaf"},
                    {"label": "Drip/Sprinkler Irrigation: 40-70% water saving vs flood irrigation; PM Krishi Sinchai Yojana", "type": "leaf"},
                    {"label": "Check Dams & Johads: Rajasthan traditional water harvesting; Tarun Bharat Sangh revival model", "type": "leaf"},
                    {"label": "Jal Shakti Ministry (2019): Jal Jeevan Mission; tap water to every household by 2024", "type": "leaf"}
                ]}
            ]

    # 6. Continental Shelf
    elif fl == 'continental-shelf':
        if is_hindi:
            return [
                {"label": "महाद्वीपीय मग्नतट: भौगोलिक विशेषताएँ", "type": "branch", "date": "विशेषताएँ", "children": [
                    {"label": "परिभाषा: महाद्वीपों के किनारे का उथला समुद्री क्षेत्र; 0-200 मीटर गहराई; 200 nautical miles EEZ से जुड़ा", "type": "leaf"},
                    {"label": "ढाल: बहुत कम; 1:500 से 1:1000; औसत चौड़ाई 70 किमी; सबसे चौड़ा: साइबेरियाई आर्कटिक शेल्फ (1500 किमी)", "type": "leaf"},
                    {"label": "Break Point: शेल्फ एज पर अचानक ढाल बढ़ता है → continental slope शुरू", "type": "leaf"}
                ]},
                {"label": "आर्थिक और पारिस्थितिक महत्व", "type": "branch", "date": "महत्व", "children": [
                    {"label": "मत्स्य पालन: विश्व की 90% मछली यहाँ मिलती है; सूर्य प्रकाश प्रवेश और पोषक तत्वों की प्रचुरता", "type": "leaf"},
                    {"label": "तेल और गैस: विश्व के 30% तेल-गैस भंडार; मुंबई हाई, कृष्णा-गोदावरी बेसिन, उत्तरी सागर", "type": "leaf"},
                    {"label": "UNCLOS अनुच्छेद 76: तटीय देश 350 नॉटिकल मील तक विस्तारित शेल्फ का दावा कर सकते हैं", "type": "leaf"}
                ]}
            ]
        else:
            return [
                {"label": "Continental Shelf: Geographic Features", "type": "branch", "date": "Features", "children": [
                    {"label": "Definition: Shallow submerged margin of continents; 0-200m depth; gentle gradient average 1:500", "type": "leaf"},
                    {"label": "Width: Average 70 km; widest = Siberian Arctic Shelf (1500 km); narrowest off steep coasts", "type": "leaf"},
                    {"label": "Shelf Edge/Break: Depth ~150-200m where gradient suddenly steepens → Continental Slope begins", "type": "leaf"}
                ]},
                {"label": "Economic & Ecological Significance", "type": "branch", "date": "Importance", "children": [
                    {"label": "Fisheries: 90% of world's fish catch from continental shelves; sunlight + nutrients abundant", "type": "leaf"},
                    {"label": "Oil & Gas: 30% of world's petroleum reserves; Mumbai High, K-G Basin, North Sea", "type": "leaf"},
                    {"label": "UNCLOS Article 76: States can claim extended continental shelf up to 350 nautical miles", "type": "leaf"}
                ]}
            ]

    # 7. Continental Slope
    elif 'continental-slope' in fl:
        if is_hindi:
            return [
                {"label": "महाद्वीपीय ढाल: विशेषताएँ", "type": "branch", "date": "विशेषताएँ", "children": [
                    {"label": "स्थिति: continental shelf के किनारे से गहरे समुद्र तल तक; 200-3000 मीटर गहराई; तीव्र ढाल (2-5°)", "type": "leaf"},
                    {"label": "पनडुब्बी घाटियाँ (Submarine Canyons): ढाल पर V-आकार की गहरी खड्डें; हडसन और कांगो कैनयन प्रसिद्ध", "type": "leaf"},
                    {"label": "अशांत धाराएँ (Turbidity Currents): गाद से भरे पानी का तीव्र प्रवाह; जमीन के भूस्खलन जैसा; अंडरसी केबल काटती हैं", "type": "leaf"}
                ]},
                {"label": "महाद्वीपीय उत्थान (Continental Rise)", "type": "branch", "date": "Continental Rise", "children": [
                    {"label": "ढाल के नीचे का क्रमिक हिस्सा; turbidity currents द्वारा लाई गई तलछट; अबिस्सल मैदान से मिलन", "type": "leaf"},
                    {"label": "तेल और गैस: ढाल के तलहटी भाग में जैविक तलछट से हाइड्रोकार्बन निर्माण", "type": "leaf"}
                ]}
            ]
        else:
            return [
                {"label": "Continental Slope: Features", "type": "branch", "date": "Features", "children": [
                    {"label": "Location: Seaward of shelf break; 200-3000m depth; steep gradient of 2-5° (vs 0.1° for shelf)", "type": "leaf"},
                    {"label": "Submarine Canyons: V-shaped gorges cutting through the slope; Hudson Canyon, Congo Canyon", "type": "leaf"},
                    {"label": "Turbidity Currents: Dense sediment-laden water flows rapidly downslope; can sever undersea cables", "type": "leaf"}
                ]},
                {"label": "Continental Rise", "type": "branch", "date": "Continental Rise", "children": [
                    {"label": "Gradual transition from slope to abyssal plain; turbidite sediment fans deposited at base", "type": "leaf"},
                    {"label": "Petroleum potential: Organic-rich sediments in slope/rise generate hydrocarbon reservoirs", "type": "leaf"}
                ]}
            ]

    # 8. Coral Reefs
    elif 'coral' in fl and 'barrier' not in fl:
        if is_hindi:
            return [
                {"label": "प्रवाल भित्ति: प्रकार और वितरण", "type": "branch", "date": "3 प्रकार", "children": [
                    {"label": "झालर भित्ति (Fringing Reef): तट के बिल्कुल समीप; उथले लैगून; लक्षद्वीप, मन्नार की खाड़ी में", "type": "leaf"},
                    {"label": "बाधा भित्ति (Barrier Reef): तट से दूर; गहरा लैगून बीच में; महान बाधा भित्ति (Great Barrier Reef), ऑस्ट्रेलिया", "type": "leaf"},
                    {"label": "प्रवाल द्वीप (Atoll): ज्वालामुखी द्वीप के डूबने से वलयाकार भित्ति; मालदीव, लक्षद्वीप का निर्माण", "type": "leaf"}
                ]},
                {"label": "प्रवाल विरंजन और खतरे", "type": "branch", "date": "खतरे", "children": [
                    {"label": "प्रवाल विरंजन: तापमान 1-2°C बढ़ने से ज़ूक्सैंथेले शैवाल बाहर; प्रवाल सफेद और मृत", "type": "leaf"},
                    {"label": "समुद्री अम्लीकरण: CO₂ वृद्धि → pH कम → CaCO₃ का घुलना → भित्ति निर्माण अवरोधित", "type": "leaf"},
                    {"label": "भारत में: Lakshadweep Islands, Gulf of Mannar, Gulf of Kutch, Andaman - सभी IUCN द्वारा संकटग्रस्त", "type": "leaf"}
                ]}
            ]
        else:
            return [
                {"label": "Coral Reefs: Types & Distribution", "type": "branch", "date": "3 Types", "children": [
                    {"label": "Fringing Reef: Grows directly from shore; shallow lagoon; Lakshadweep, Gulf of Mannar (India)", "type": "leaf"},
                    {"label": "Barrier Reef: Separated from coast by deep lagoon; Great Barrier Reef (Australia) — world's largest", "type": "leaf"},
                    {"label": "Atoll: Ring-shaped reef formed as volcanic island subsides; Maldives, Lakshadweep atolls", "type": "leaf"}
                ]},
                {"label": "Coral Bleaching & Threats", "type": "branch", "date": "Threats", "children": [
                    {"label": "Coral Bleaching: Temperature rise of 1-2°C expels symbiotic zooxanthellae algae; coral turns white", "type": "leaf"},
                    {"label": "Ocean Acidification: Rising CO₂ → lower pH → CaCO₃ dissolution → reef building impaired", "type": "leaf"},
                    {"label": "India's Reefs: Lakshadweep, Gulf of Mannar, Gulf of Kutch, Andamans — all severely threatened", "type": "leaf"}
                ]}
            ]

    # 9. Deep Sea Plain
    elif 'deep-sea' in fl:
        if is_hindi:
            return [
                {"label": "गहरे समुद्र के मैदान (Abyssal Plains)", "type": "branch", "date": "विशेषताएँ", "children": [
                    {"label": "परिभाषा: 3000-6000 मीटर गहराई पर समतल क्षेत्र; पृथ्वी का सर्वाधिक समतल भूभाग", "type": "leaf"},
                    {"label": "निर्माण: turbidity currents से लाई तलछट से भरे; बहुत धीमी जमाव; मिलियन वर्षों में निर्मित", "type": "leaf"},
                    {"label": "Abyssal Hills: मैदान पर बिखरे छोटे पहाड़; ज्वालामुखी मूल; प्रशांत में सर्वाधिक", "type": "leaf"}
                ]},
                {"label": "जीवन और संसाधन", "type": "branch", "date": "महत्व", "children": [
                    {"label": "अति गहरे समुद्री जीव: रोशनी रहित; रसायनसंश्लेषण (Chemosynthesis); विचित्र मछलियाँ जैसे Anglerfish, Gulper Eel", "type": "leaf"},
                    {"label": "मैंगनीज नोड्यूल: अबिस्सल मैदान पर सर्वाधिक; भविष्य के खनिज स्रोत; भारत का CIOB में अधिकार", "type": "leaf"}
                ]}
            ]
        else:
            return [
                {"label": "Deep-Sea Plains (Abyssal Plains)", "type": "branch", "date": "Features", "children": [
                    {"label": "Definition: Flat terrain at 3000-6000m depth; Earth's flattest surfaces; formed by sediment infill", "type": "leaf"},
                    {"label": "Formation: Turbidites from turbidity currents smooth out oceanic ridges; very slow deposition", "type": "leaf"},
                    {"label": "Abyssal Hills: Low volcanic mounds scattered across plains; most abundant in the Pacific", "type": "leaf"}
                ]},
                {"label": "Life & Resources", "type": "branch", "date": "Importance", "children": [
                    {"label": "Deep-Sea Life: No sunlight; chemosynthesis at vents; Anglerfish, Gulper Eel, bioluminescence", "type": "leaf"},
                    {"label": "Manganese Nodules: Most concentrated on abyssal plains; India's CIOB mining rights", "type": "leaf"}
                ]}
            ]

    # 10. Density of Ocean Waters
    elif 'density' in fl:
        if is_hindi:
            return [
                {"label": "महासागरीय जल का घनत्व: निर्धारक कारक", "type": "branch", "date": "कारक", "children": [
                    {"label": "लवणता (Salinity): सर्वाधिक प्रभावशाली; खारा = अधिक घना; औसत: 35 ppt; मृत सागर = 340 ppt", "type": "leaf"},
                    {"label": "तापमान: ठंडा जल = अधिक घना; 4°C पर अधिकतम घनत्व; ध्रुवीय जल सबसे घना", "type": "leaf"},
                    {"label": "दबाव: गहराई बढ़ने पर दबाव बढ़ता है → घनत्व थोड़ा बढ़ता है", "type": "leaf"}
                ]},
                {"label": "थर्मोहेलाइन परिसंचरण (THC)", "type": "branch", "date": "THC / महासागरीय कन्वेयर बेल्ट", "children": [
                    {"label": "घनत्व अंतर से संचालित: ध्रुवीय क्षेत्रों में ठंडा और खारा (घना) पानी डूबता है → गहरे समुद्र में बहता है", "type": "leaf"},
                    {"label": "AMOC (Atlantic Meridional Overturning Circulation): यूरोप को गर्म रखने वाली धारा; जलवायु परिवर्तन से खतरा", "type": "leaf"},
                    {"label": "Halocline और Thermocline: लवणता और तापमान परिवर्तन की सीमा रेखाएँ; जल स्तंभ में मिश्रण रोकती हैं", "type": "leaf"}
                ]}
            ]
        else:
            return [
                {"label": "Density of Ocean Water: Governing Factors", "type": "branch", "date": "Factors", "children": [
                    {"label": "Salinity: Most dominant factor; saltier = denser; average 35 ppt; Dead Sea = 340 ppt", "type": "leaf"},
                    {"label": "Temperature: Colder = denser; maximum density at 4°C; polar waters densest in world oceans", "type": "leaf"},
                    {"label": "Pressure: Increases with depth; slightly compresses water → marginal density increase", "type": "leaf"}
                ]},
                {"label": "Thermohaline Circulation (THC)", "type": "branch", "date": "THC / Conveyor Belt", "children": [
                    {"label": "Density-driven: Cold, salty (dense) polar water sinks → flows along deep ocean floor globally", "type": "leaf"},
                    {"label": "AMOC: Atlantic Meridional Overturning Circulation; keeps NW Europe warm; threatened by glacial melt", "type": "leaf"},
                    {"label": "Halocline & Thermocline: Boundary layers of salinity/temperature change; inhibit vertical mixing", "type": "leaf"}
                ]}
            ]

    # 11. Factors affecting Temperature distribution
    elif 'temperature' in fl:
        if is_hindi:
            return [
                {"label": "महासागरीय तापमान वितरण को प्रभावित करने वाले कारक", "type": "branch", "date": "कारक", "children": [
                    {"label": "अक्षांश: विषुवत पर 27°C; ध्रुवों पर -2°C; सूर्यताप कोण घटने से तापमान कम", "type": "leaf"},
                    {"label": "महासागरीय धाराएँ: गर्म धाराएँ (Gulf Stream, Kuroshio) तटों को गर्म करती हैं; ठंडी (Labrador, Canary) तटों को ठंडा", "type": "leaf"},
                    {"label": "गहराई: सतह पर अधिक; थर्मोक्लाइन (200-1000 मीटर) पर तेज़ गिरावट; गहरे समुद्र में 2-4°C", "type": "leaf"},
                    {"label": "वायु परिसंचरण और वाष्पीकरण: व्यापारिक हवाएँ गर्म जल को पश्चिम की ओर धकेलती हैं; ENSO", "type": "leaf"}
                ]},
                {"label": "तापमान विसंगतियाँ और महत्व", "type": "branch", "date": "विसंगतियाँ", "children": [
                    {"label": "आइसोथर्म (Isotherm): समान तापमान वाले बिंदुओं को जोड़ने वाली रेखाएँ; पश्चिम तटों पर ध्रुव की ओर मुड़ती हैं", "type": "leaf"},
                    {"label": "El Niño प्रभाव: पूर्वी प्रशांत असामान्य रूप से गर्म; पर्यावरण और मानसून पर वैश्विक प्रभाव", "type": "leaf"}
                ]}
            ]
        else:
            return [
                {"label": "Factors Affecting Ocean Temperature Distribution", "type": "branch", "date": "Factors", "children": [
                    {"label": "Latitude: Equator ~27°C; poles ~-2°C; solar angle reduces insolation at higher latitudes", "type": "leaf"},
                    {"label": "Ocean Currents: Warm currents (Gulf Stream, Kuroshio) warm coasts; Cold (Labrador, Canary) cool them", "type": "leaf"},
                    {"label": "Depth: Thermocline at 200-1000m has rapid temperature drop; deep ocean 2-4°C year-round", "type": "leaf"},
                    {"label": "Wind Circulation: Trade winds push warm water westward; ENSO disrupts normal pattern", "type": "leaf"}
                ]},
                {"label": "Temperature Anomalies & Significance", "type": "branch", "date": "Anomalies", "children": [
                    {"label": "Isotherms: Lines connecting equal-temperature points; bend poleward on west coasts (warm currents)", "type": "leaf"},
                    {"label": "El Niño Effect: Anomalous warming of eastern Pacific; global monsoon and drought disruptions", "type": "leaf"}
                ]}
            ]

    # 12. Great Barrier Reef
    elif 'great-barrier' in fl:
        if is_hindi:
            return [
                {"label": "महान बाधा भित्ति: परिचय", "type": "branch", "date": "विश्व की सबसे बड़ी", "children": [
                    {"label": "स्थान: उत्तर-पूर्वी ऑस्ट्रेलिया; क्वींसलैंड; 2300 किमी लंबी; 344,400 वर्ग किमी क्षेत्र; अंतरिक्ष से दिखती है", "type": "leaf"},
                    {"label": "UNESCO विश्व धरोहर (1981): 900+ द्वीप; 600 प्रकार की प्रवाल; 1500+ मछली प्रजातियाँ; 4000+ मोलस्क", "type": "leaf"},
                    {"label": "आर्थिक महत्व: $6.4 अरब AUD पर्यटन; 64,000 रोजगार; मत्स्य उद्योग", "type": "leaf"}
                ]},
                {"label": "खतरे और संरक्षण", "type": "branch", "date": "खतरे", "children": [
                    {"label": "प्रवाल विरंजन: 2016, 2017, 2020, 2022 में व्यापक विरंजन; 50%+ भित्ति प्रभावित", "type": "leaf"},
                    {"label": "Crown-of-Thorns Starfish: प्रवाल का सबसे बड़ा जैविक शिकारी; जनसंख्या विस्फोट हानिकारक", "type": "leaf"},
                    {"label": "UNESCO 'In Danger' सूची: 2021-22 में सूचीबद्ध करने का प्रस्ताव; ऑस्ट्रेलिया का विरोध", "type": "leaf"}
                ]}
            ]
        else:
            return [
                {"label": "Great Barrier Reef: Overview", "type": "branch", "date": "World's Largest", "children": [
                    {"label": "Location: NE Australia (Queensland); 2300 km long; 344,400 sq km; visible from space", "type": "leaf"},
                    {"label": "UNESCO WHS (1981): 900+ islands; 600 coral species; 1500+ fish; 4000+ mollusc species", "type": "leaf"},
                    {"label": "Economic Value: AU$6.4 billion from tourism; 64,000 jobs; significant fisheries", "type": "leaf"}
                ]},
                {"label": "Threats & Conservation", "type": "branch", "date": "Threats", "children": [
                    {"label": "Mass Bleaching: 2016, 2017, 2020, 2022 events; 50%+ of reef affected by back-to-back bleaching", "type": "leaf"},
                    {"label": "Crown-of-Thorns Starfish: Largest biological predator of coral; population outbreaks cause major damage", "type": "leaf"},
                    {"label": "UNESCO 'In Danger': 2021-22 proposal to list as endangered; Australia lobbied against listing", "type": "leaf"}
                ]}
            ]

    # 13. Hydrological Cycle
    elif fl == 'hydrological-cycle':
        if is_hindi:
            return [
                {"label": "जलवैज्ञानिक चक्र: अवधारणा", "type": "branch", "date": "अवधारणा", "children": [
                    {"label": "जल चक्र: पृथ्वी पर जल का निरंतर आदान-प्रदान; महासागर ↔ वायुमंडल ↔ स्थल ↔ जीवमंडल", "type": "leaf"},
                    {"label": "भंडार और प्रवाह: महासागर (97.5%) → वाष्पीकरण → संघनन → वर्षा → अपवाह → वापस महासागर", "type": "leaf"},
                    {"label": "निवास काल (Residence Time): महासागर = 3200 वर्ष; नदियाँ = 16 दिन; वायुमंडल = 8-9 दिन", "type": "leaf"}
                ]},
                {"label": "जल चक्र का पारिस्थितिक और जलवायु महत्व", "type": "branch", "date": "महत्व", "children": [
                    {"label": "ऊर्जा परिवहन: वाष्पीकरण के दौरान ऊष्मा अवशोषण और संघनन पर ऊष्मा मुक्त; जलवायु को संतुलित करता है", "type": "leaf"},
                    {"label": "पोषक तत्व चक्र: नदियाँ खनिज और पोषक तत्व महासागरों तक ले जाती हैं; खाद्य जाल", "type": "leaf"},
                    {"label": "जलवायु परिवर्तन और जल चक्र: तापमान वृद्धि से चक्र तीव्र; वर्षा में अस्थिरता", "type": "leaf"}
                ]}
            ]
        else:
            return [
                {"label": "Hydrological Cycle: Concept", "type": "branch", "date": "Concept", "children": [
                    {"label": "Water Cycle: Continuous movement of water through ocean ↔ atmosphere ↔ land ↔ biosphere", "type": "leaf"},
                    {"label": "Reservoirs: Oceans (97.5%) → evaporation → condensation → precipitation → runoff → ocean", "type": "leaf"},
                    {"label": "Residence Time: Ocean = 3200 yrs; Rivers = 16 days; Atmosphere = 8-9 days; Glaciers = 20-100 yrs", "type": "leaf"}
                ]},
                {"label": "Ecological & Climate Importance", "type": "branch", "date": "Importance", "children": [
                    {"label": "Energy Transport: Evaporation absorbs latent heat; condensation releases it; stabilizes climate", "type": "leaf"},
                    {"label": "Nutrient Cycling: Rivers carry minerals to oceans; supports marine food webs", "type": "leaf"},
                    {"label": "Climate Change: Warming intensifies cycle; more extreme precipitation and droughts", "type": "leaf"}
                ]}
            ]

    # 14. Inland water resources
    elif 'inland' in fl:
        if is_hindi:
            return [
                {"label": "आंतरिक जल संसाधन: प्रकार", "type": "branch", "date": "प्रकार", "children": [
                    {"label": "नदियाँ: भारत में 12 प्रमुख नदी बेसिन (>20,000 वर्ग किमी); गंगा, ब्रह्मपुत्र, सिंधु, गोदावरी, कृष्णा", "type": "leaf"},
                    {"label": "झीलें: प्राकृतिक/कृत्रिम; वूलर, चिल्का, डल, नैनीताल; वेटलैंड पारिस्थितिकी; रामसर स्थल", "type": "leaf"},
                    {"label": "भूजल: जलभृत (Aquifer); भारत में 63% सिंचाई; अत्यधिक दोहन = भूजल संकट", "type": "leaf"},
                    {"label": "हिमनद और बर्फ: हिमालयी जल टंकी; 33 अरब टन बर्फ; प्रमुख नदियों का स्रोत", "type": "leaf"}
                ]},
                {"label": "भारत में जल उपलब्धता की स्थिति", "type": "branch", "date": "स्थिति", "children": [
                    {"label": "प्रति व्यक्ति जल उपलब्धता: 1947 में 5177 m³/व्यक्ति/वर्ष → 2021 में ~1440 m³; जल तनाव सीमा <1700 m³", "type": "leaf"},
                    {"label": "असमान वितरण: 60% जल ब्रह्मपुत्र और गंगा में; राजस्थान/गुजरात में न्यूनतम; अंतर-राज्य जल विवाद", "type": "leaf"}
                ]}
            ]
        else:
            return [
                {"label": "Inland Water Resources: Types", "type": "branch", "date": "Types", "children": [
                    {"label": "Rivers: 12 major basins in India (>20,000 sq km); Ganga, Brahmaputra, Indus, Godavari, Krishna", "type": "leaf"},
                    {"label": "Lakes: Natural and artificial; Wular, Chilika, Dal, Naini; Ramsar wetland sites", "type": "leaf"},
                    {"label": "Groundwater: Aquifers; 63% of India's irrigation; over-exploitation causes depletion crisis", "type": "leaf"},
                    {"label": "Glaciers & Snow: Himalayan water tower; 33 billion tonnes of ice; feeds perennial rivers", "type": "leaf"}
                ]},
                {"label": "India's Water Availability", "type": "branch", "date": "Status", "children": [
                    {"label": "Per capita water: 5177 m³/person/yr (1947) → ~1440 m³ (2021); water stress below 1700 m³", "type": "leaf"},
                    {"label": "Unequal distribution: 60% in Brahmaputra+Ganga basins; Rajasthan/Gujarat minimal; interstate disputes", "type": "leaf"}
                ]}
            ]

    # 15. Minor Relief Features
    elif 'minor-relief' in fl:
        if is_hindi:
            return [
                {"label": "महासागरीय तल की लघु उच्चावच विशेषताएँ", "type": "branch", "date": "प्रकार", "children": [
                    {"label": "समुद्री पर्वत (Seamount): जलमग्न ज्वालामुखी; 1000+ मीटर ऊँचे; शीर्ष पानी में; मत्स्य पालन क्षेत्र", "type": "leaf"},
                    {"label": "गुयोट (Guyot/Tablemount): समुद्री पर्वत का शीर्ष समुद्र सतह से कटकर चपटा; प्रशांत में सर्वाधिक", "type": "leaf"},
                    {"label": "महासागरीय कटक (Oceanic Ridge): मध्य-महासागरीय पर्वत श्रेणी; मिड-अटलांटिक रिज; विवर्तनिक सीमा", "type": "leaf"},
                    {"label": "एबिस्सल हिल्स (Abyssal Hills): छोटे-छोटे ज्वालामुखी टीले; गहरे समुद्र मैदान पर; प्रशांत में सर्वाधिक", "type": "leaf"}
                ]},
                {"label": "अन्य लघु स्थलाकृतियाँ", "type": "branch", "date": "अन्य", "children": [
                    {"label": "महासागरीय खाई (Trench): प्रशांत का मारियाना (11,034 मीटर); सबडक्शन जोन; सर्वाधिक गहरा", "type": "leaf"},
                    {"label": "एटोल (Atoll): प्रवाल वलयाकार द्वीप; ज्वालामुखी के डूबने के बाद; लक्षद्वीप, मालदीव", "type": "leaf"}
                ]}
            ]
        else:
            return [
                {"label": "Minor Ocean Floor Relief Features", "type": "branch", "date": "Types", "children": [
                    {"label": "Seamount: Submerged volcanic mountain >1000m; not reaching surface; rich fishing grounds", "type": "leaf"},
                    {"label": "Guyot (Tablemount): Flat-topped seamount eroded by waves before subsiding; abundant in Pacific", "type": "leaf"},
                    {"label": "Oceanic Ridge: Mid-ocean mountain chain; Mid-Atlantic Ridge; divergent plate boundary", "type": "leaf"},
                    {"label": "Abyssal Hills: Small volcanic bumps on deep-sea plains; most common in Pacific ocean", "type": "leaf"}
                ]},
                {"label": "Other Minor Features", "type": "branch", "date": "Others", "children": [
                    {"label": "Trench: Pacific's Mariana (11,034m); deepest point on Earth; subduction zone feature", "type": "leaf"},
                    {"label": "Atoll: Ring-shaped coral island after volcanic island subsidence; Lakshadweep, Maldives", "type": "leaf"}
                ]}
            ]

    # 16. Movements of Ocean Water
    elif 'movements' in fl:
        if is_hindi:
            return [
                {"label": "महासागरीय जल की गतियाँ: तीन प्रकार", "type": "branch", "date": "3 प्रकार", "children": [
                    {"label": "तरंगें (Waves): पवन द्वारा उत्पन्न; ऊर्जा का प्रसार; जल का स्थान परिवर्तन नहीं; Swell, Tsunami", "type": "leaf"},
                    {"label": "ज्वार-भाटा (Tides): चंद्रमा और सूर्य का गुरुत्वाकर्षण; Spring Tide (अमावस/पूर्णिमा); Neap Tide (अष्टमी)", "type": "leaf"},
                    {"label": "धाराएँ (Currents): जल का क्षैतिज बड़े पैमाने पर प्रवाह; सतही (हवा) और गहरी (घनत्व) धाराएँ", "type": "leaf"}
                ]},
                {"label": "प्रमुख महासागरीय धाराएँ", "type": "branch", "date": "प्रमुख धाराएँ", "children": [
                    {"label": "Gulf Stream: अटलांटिक; उत्तर-पश्चिम यूरोप को गर्म रखती है; गर्म धारा; AMOC का भाग", "type": "leaf"},
                    {"label": "Humboldt/Peru Current: पश्चिमी दक्षिण अमेरिका; ठंडी; अपवेलिंग; El Niño से बाधित", "type": "leaf"},
                    {"label": "हिंद महासागर धाराएँ: मानसून पर आधारित; गर्मी में दक्षिण-पश्चिम; सर्दी में उत्तर-पूर्व", "type": "leaf"}
                ]}
            ]
        else:
            return [
                {"label": "Ocean Water Movements: Three Types", "type": "branch", "date": "3 Types", "children": [
                    {"label": "Waves: Wind-generated; energy travels not water; types: swell, breakers, tsunami (seismic)", "type": "leaf"},
                    {"label": "Tides: Moon + Sun gravity; Spring tide (New/Full Moon); Neap tide (Quarter Moon)", "type": "leaf"},
                    {"label": "Currents: Large-scale horizontal water flow; surface (wind-driven) and deep (density-driven)", "type": "leaf"}
                ]},
                {"label": "Major Ocean Currents", "type": "branch", "date": "Key Currents", "children": [
                    {"label": "Gulf Stream: Atlantic warm current; keeps NW Europe warm; part of AMOC thermohaline system", "type": "leaf"},
                    {"label": "Humboldt/Peru Current: Cold; SW South America; upwelling; disrupted by El Niño causing droughts", "type": "leaf"},
                    {"label": "Indian Ocean Currents: Monsoon-driven; reverses seasonally; SW in summer, NE in winter", "type": "leaf"}
                ]}
            ]

    # 17. Oceanic Deep and Trenches
    elif 'trenches' in fl or 'oceanic-deep' in fl:
        if is_hindi:
            return [
                {"label": "महासागरीय खाइयाँ: विशेषताएँ", "type": "branch", "date": "सबसे गहरे स्थान", "children": [
                    {"label": "मारियाना ट्रेंच: प्रशांत महासागर; 11,034 मीटर (Challenger Deep); पृथ्वी का सबसे गहरा स्थान", "type": "leaf"},
                    {"label": "प्यूर्टो रिको ट्रेंच: अटलांटिक; 8,376 मीटर; कैरेबियन प्लेट-नॉर्थ अमेरिकन प्लेट सीमा", "type": "leaf"},
                    {"label": "जावा ट्रेंच (Sunda Trench): हिंद महासागर; 7,290 मीटर; 2004 के सुनामी का स्रोत", "type": "leaf"},
                    {"label": "टोंगा ट्रेंच: दक्षिण प्रशांत; 10,882 मीटर; सबसे तेज़ सबडक्शन दर", "type": "leaf"}
                ]},
                {"label": "खाइयों का निर्माण और महत्व", "type": "branch", "date": "भूगर्भीय महत्व", "children": [
                    {"label": "सबडक्शन: महासागरीय प्लेट महाद्वीपीय प्लेट के नीचे डूबती है → खाई निर्माण; भूकंप और ज्वालामुखी", "type": "leaf"},
                    {"label": "Ring of Fire: प्रशांत खाइयों का तटीय क्षेत्र; 75% ज्वालामुखी; 90% भूकंप; 'आग की अंगूठी'", "type": "leaf"}
                ]}
            ]
        else:
            return [
                {"label": "Oceanic Trenches: Features", "type": "branch", "date": "Deepest Points", "children": [
                    {"label": "Mariana Trench: Pacific Ocean; 11,034m (Challenger Deep); Earth's deepest point", "type": "leaf"},
                    {"label": "Puerto Rico Trench: Atlantic; 8376m; boundary of Caribbean and North American plates", "type": "leaf"},
                    {"label": "Java/Sunda Trench: Indian Ocean; 7290m; source of devastating 2004 Indian Ocean Tsunami", "type": "leaf"},
                    {"label": "Tonga Trench: South Pacific; 10,882m; fastest subduction rate on Earth", "type": "leaf"}
                ]},
                {"label": "Formation & Significance", "type": "branch", "date": "Geological Importance", "children": [
                    {"label": "Subduction: Oceanic plate dives under continental plate → trench; causes earthquakes and volcanoes", "type": "leaf"},
                    {"label": "Ring of Fire: Pacific trench zone; 75% of world's volcanoes; 90% of earthquakes occur here", "type": "leaf"}
                ]}
            ]

    # 18. Oceanic Water Resources
    elif 'oceanic-water' in fl:
        if is_hindi:
            return [
                {"label": "महासागरीय जल संसाधन: प्रकार", "type": "branch", "date": "संसाधन", "children": [
                    {"label": "मत्स्य संसाधन: 80 मिलियन टन/वर्ष; भारत 4th सबसे बड़ा उत्पादक; EEZ में 2.02 मिलियन वर्ग किमी", "type": "leaf"},
                    {"label": "खनिज संसाधन: नमक (NaCl), मैग्नीशियम, ब्रोमीन; पॉलीमेटालिक नोड्यूल; हाइड्रोथर्मल वेंट खनिज", "type": "leaf"},
                    {"label": "ऊर्जा संसाधन: OTEC (Ocean Thermal Energy Conversion); ज्वारीय ऊर्जा; लहर ऊर्जा; अपतटीय पवन", "type": "leaf"},
                    {"label": "जल विलवणीकरण: खारे पानी से पीने योग्य जल; Middle East में सर्वाधिक; India में JNNSM प्रयास", "type": "leaf"}
                ]},
                {"label": "Blue Economy की अवधारणा", "type": "branch", "date": "Blue Economy", "children": [
                    {"label": "परिभाषा: समुद्री संसाधनों का टिकाऊ उपयोग; पारिस्थितिकी तंत्र की रक्षा करते हुए आर्थिक विकास", "type": "leaf"},
                    {"label": "भारत की नीति: Sagarmala परियोजना; अटलांटिक और हिंद महासागर में ब्लू इकोनॉमी विस्तार", "type": "leaf"}
                ]}
            ]
        else:
            return [
                {"label": "Oceanic Water Resources: Types", "type": "branch", "date": "Resources", "children": [
                    {"label": "Fisheries: 80 million tonnes/yr globally; India 4th largest producer; 2.02 mn sq km EEZ", "type": "leaf"},
                    {"label": "Mineral Resources: Salt, Magnesium, Bromine; polymetallic nodules; hydrothermal vent minerals", "type": "leaf"},
                    {"label": "Energy: OTEC (Ocean Thermal Energy Conversion); tidal energy; wave energy; offshore wind", "type": "leaf"},
                    {"label": "Desalination: Converting seawater to freshwater; dominant in Middle East; growing in India", "type": "leaf"}
                ]},
                {"label": "Blue Economy Concept", "type": "branch", "date": "Blue Economy", "children": [
                    {"label": "Definition: Sustainable use of marine resources while preserving ecosystem health", "type": "leaf"},
                    {"label": "India's Policy: Sagarmala Project; Deep Ocean Mission; Blue Economy expansion in IOR", "type": "leaf"}
                ]}
            ]

    # 19. Oceans Relief of the Ocean Floor
    elif 'oceans-relief' in fl or ('oceans' in fl and 'relief' in fl):
        if is_hindi:
            return [
                {"label": "महासागरीय तल की उच्चावच: प्रमुख विभाजन", "type": "branch", "date": "4 क्षेत्र", "children": [
                    {"label": "महाद्वीपीय मग्नतट (Continental Shelf): 0-200 मीटर; उथला; सर्वाधिक जैविक और आर्थिक महत्व", "type": "leaf"},
                    {"label": "महाद्वीपीय ढाल (Continental Slope): 200-3000 मीटर; तीव्र ढाल; submarine canyons; turbidity currents", "type": "leaf"},
                    {"label": "गहरे समुद्र के मैदान (Abyssal Plains): 3000-6000 मीटर; सबसे समतल; मैंगनीज नोड्यूल", "type": "leaf"},
                    {"label": "महासागरीय खाइयाँ (Ocean Trenches): 6000+ मीटर; सबडक्शन जोन; Ring of Fire; Mariana 11,034 मीटर", "type": "leaf"}
                ]},
                {"label": "मध्य-महासागरीय कटक", "type": "branch", "date": "Mid-Ocean Ridges", "children": [
                    {"label": "मिड-अटलांटिक रिज: विश्व का सबसे लंबा पर्वत (16,000 किमी); अपसारी प्लेट सीमा; Iceland पर धरातल पर", "type": "leaf"},
                    {"label": "हाइड्रोथर्मल वेंट: कटकों पर; Black Smokers; केमोसिंथेसिस; अद्वितीय जीव समुदाय", "type": "leaf"}
                ]}
            ]
        else:
            return [
                {"label": "Ocean Floor Relief: Major Divisions", "type": "branch", "date": "4 Zones", "children": [
                    {"label": "Continental Shelf: 0-200m; shallow; maximum biological productivity and economic importance", "type": "leaf"},
                    {"label": "Continental Slope: 200-3000m; steep gradient; submarine canyons cut through; turbidity currents", "type": "leaf"},
                    {"label": "Abyssal Plains: 3000-6000m; flattest terrain on Earth; manganese nodule fields", "type": "leaf"},
                    {"label": "Ocean Trenches: 6000m+; subduction zones; Ring of Fire; Mariana at 11,034m", "type": "leaf"}
                ]},
                {"label": "Mid-Ocean Ridges", "type": "branch", "date": "MOR", "children": [
                    {"label": "Mid-Atlantic Ridge: World's longest mountain range (16,000 km); divergent boundary; emerges in Iceland", "type": "leaf"},
                    {"label": "Hydrothermal Vents: Along ridges; Black Smokers; chemosynthesis; unique deep-sea ecosystems", "type": "leaf"}
                ]}
            ]

    # 20. Surface Water Resources
    elif 'surface-water' in fl:
        if is_hindi:
            return [
                {"label": "सतही जल संसाधन: भारत में", "type": "branch", "date": "संसाधन", "children": [
                    {"label": "नदी अपवाह: भारत में 1869 BCM वार्षिक सतही जल; उपयोग योग्य: केवल 690 BCM (भंडारण/भूगोल की सीमा)", "type": "leaf"},
                    {"label": "प्रमुख नदी बेसिन: गंगा (26%), ब्रह्मपुत्र-बराक (30%), दक्षिणी नदियाँ (44%); जल उपलब्धता असमान", "type": "leaf"},
                    {"label": "भंडार और जलाशय: बड़े बाँध; भाखड़ा-नंगल, हीराकुड, नर्मदा; सिंचाई और पनबिजली", "type": "leaf"}
                ]},
                {"label": "प्रमुख चुनौतियाँ", "type": "branch", "date": "चुनौतियाँ", "children": [
                    {"label": "प्रदूषण: औद्योगिक और घरेलू; गंगा (BOD 3+ mg/L); जल जनित रोग; नमामि गंगे", "type": "leaf"},
                    {"label": "अंतर-राज्य जल विवाद: कावेरी (TN-KA), SYL नहर (Punjab-Haryana), Krishna (AP-Telangana)", "type": "leaf"}
                ]}
            ]
        else:
            return [
                {"label": "Surface Water Resources: India", "type": "branch", "date": "Resources", "children": [
                    {"label": "River Runoff: India has 1869 BCM annual surface water; only 690 BCM usable due to topography/storage", "type": "leaf"},
                    {"label": "River Basins: Ganga (26%), Brahmaputra-Barak (30%), peninsular rivers (44%); uneven distribution", "type": "leaf"},
                    {"label": "Reservoirs & Dams: Bhakra-Nangal, Hirakud, Narmada (Sardar Sarovar); irrigation + hydropower", "type": "leaf"}
                ]},
                {"label": "Key Challenges", "type": "branch", "date": "Challenges", "children": [
                    {"label": "Pollution: Industrial and domestic effluents; Ganga BOD >3 mg/L; Namami Gange Mission", "type": "leaf"},
                    {"label": "Interstate Water Disputes: Cauvery (TN-KA), SYL Canal (Punjab-Haryana), Krishna (AP-TG)", "type": "leaf"}
                ]}
            ]

    # 21. Techniques of Water Conservation
    elif 'techniques' in fl and 'water' in fl:
        if is_hindi:
            return [
                {"label": "पारंपरिक जल संरक्षण तकनीकें", "type": "branch", "date": "पारंपरिक", "children": [
                    {"label": "बावड़ी (Stepwell): राजस्थान-गुजरात; सीढ़ीदार कुएँ; रानी की वाव (UNESCO WHS); भूजल तक पहुँच", "type": "leaf"},
                    {"label": "जोहड़: राजस्थान; मिट्टी का छोटा बाँध; तरुण भारत संघ; अलवर में 1000+ जोहड़ पुनर्जीवित", "type": "leaf"},
                    {"label": "कुंड/टांका: राजस्थान; छत से वर्षा जल संचयन; रेगिस्तानी क्षेत्रों में पीने के लिए", "type": "leaf"},
                    {"label": "आहर-पाइन: बिहार; सिंचाई के लिए; नदी अपवाह संचयन; मैदानी इलाकों में प्रचलित", "type": "leaf"}
                ]},
                {"label": "आधुनिक जल संरक्षण तकनीकें", "type": "branch", "date": "आधुनिक", "children": [
                    {"label": "ड्रिप सिंचाई: इज़राइल मॉडल; 40-70% जल बचत; महाराष्ट्र और गुजरात में व्यापक उपयोग", "type": "leaf"},
                    {"label": "जल ATM: ULBs द्वारा 24x7 जल वितरण; Rajkot मॉडल; स्मार्ट मीटरिंग", "type": "leaf"},
                    {"label": "बाँध और जलाशय: भंडारण क्षमता बढ़ाना; इंटरलिंकिंग ऑफ रिवर्स; Ken-Betwa पहली परियोजना", "type": "leaf"}
                ]}
            ]
        else:
            return [
                {"label": "Traditional Water Conservation Techniques", "type": "branch", "date": "Traditional", "children": [
                    {"label": "Stepwells (Bawdi): Rajasthan-Gujarat; Rani ki Vav (UNESCO WHS); groundwater access", "type": "leaf"},
                    {"label": "Johad: Rajasthan earthen check dams; Tarun Bharat Sangh revived 1000+ in Alwar district", "type": "leaf"},
                    {"label": "Kund/Tanka: Underground cisterns; rooftop rainwater harvesting; desert drinking water", "type": "leaf"},
                    {"label": "Ahar-Pyne: Bihar; river runoff harvesting system; traditional plains irrigation", "type": "leaf"}
                ]},
                {"label": "Modern Water Conservation Techniques", "type": "branch", "date": "Modern", "children": [
                    {"label": "Drip Irrigation: Israel model; 40-70% water saving; widely adopted in Maharashtra, Gujarat", "type": "leaf"},
                    {"label": "Smart Metering & Water ATMs: 24x7 supply; Rajkot model; reduces NRW (Non-Revenue Water)", "type": "leaf"},
                    {"label": "River Interlinking: Ken-Betwa as first ILR project; transfers surplus to deficit basins", "type": "leaf"}
                ]}
            ]

    # 22. Terrigenous Deposits
    elif 'terrigenous' in fl:
        if is_hindi:
            return [
                {"label": "स्थलीय निक्षेप (Terrigenous): परिभाषा", "type": "branch", "date": "परिभाषा", "children": [
                    {"label": "भूमि से समुद्र में आने वाले तलछट; नदियाँ, पवन, हिमनद मुख्य स्रोत; महाद्वीपीय शेल्फ और ढाल पर", "type": "leaf"},
                    {"label": "प्रकार: बजरी/रेत (उथले), गाद/मिट्टी (गहरे), हिमनद जलोढ़ (ध्रुवीय)", "type": "leaf"}
                ]},
                {"label": "प्रमुख स्थलीय निक्षेप और उनके स्रोत", "type": "branch", "date": "स्रोत", "children": [
                    {"label": "नदी-जनित: गंगा-ब्रह्मपुत्र डेल्टा में विशाल निक्षेप; बंगाल की खाड़ी में भारत का स्थलीय तलछट", "type": "leaf"},
                    {"label": "पवन-जनित (Aeolian): सहारा की धूल अटलांटिक में; थार की धूल हिंद महासागर में; Loess निक्षेप", "type": "leaf"},
                    {"label": "हिमनद जलोढ़: ध्रुवीय और उप-ध्रुवीय; 'Dropstones' — हिमखंड से गिरी चट्टानें", "type": "leaf"},
                    {"label": "तटीय निक्षेप: तरंगों द्वारा लाई रेत; बार, स्पिट, टॉम्बोलो; डेल्टा निर्माण", "type": "leaf"}
                ]}
            ]
        else:
            return [
                {"label": "Terrigenous Deposits: Definition", "type": "branch", "date": "Definition", "children": [
                    {"label": "Land-derived sediments; rivers, wind, glaciers are main sources; deposited on continental margins", "type": "leaf"},
                    {"label": "Types: Gravels/sands (shallow), silts/clays (deeper), glacial outwash (polar regions)", "type": "leaf"}
                ]},
                {"label": "Major Terrigenous Sources", "type": "branch", "date": "Sources", "children": [
                    {"label": "River-borne: Ganga-Brahmaputra delta; massive sediment delivery to Bay of Bengal", "type": "leaf"},
                    {"label": "Wind-borne (Aeolian): Saharan dust across Atlantic; Thar dust into Indian Ocean; Loess deposits", "type": "leaf"},
                    {"label": "Glacial Outwash: Polar/sub-polar; 'Dropstones' dropped from melting icebergs far from land", "type": "leaf"},
                    {"label": "Coastal Deposits: Wave-transported sand; bars, spits, tombolos, beach formation, delta building", "type": "leaf"}
                ]}
            ]

    # 23. Underground water resource
    elif 'underground' in fl:
        if is_hindi:
            return [
                {"label": "भूजल: परिभाषा और वितरण", "type": "branch", "date": "भूजल", "children": [
                    {"label": "जलभृत (Aquifer): जल धारण करने वाली पारगम्य शैल/मिट्टी परत; आर्टेशियन, कंफाइंड, अनकंफाइंड", "type": "leaf"},
                    {"label": "भारत में भूजल: 432 BCM भूजल संभावना; इसमें से 393 BCM उपयोग योग्य; 63% सिंचाई उपयोग", "type": "leaf"},
                    {"label": "अत्यधिक दोहन: पंजाब, हरियाणा, राजस्थान, गुजरात में जल तालिका 3-5 मीटर/वर्ष गिर रही है", "type": "leaf"}
                ]},
                {"label": "भूजल प्रबंधन की चुनौतियाँ", "type": "branch", "date": "चुनौतियाँ", "children": [
                    {"label": "आर्सेनिक प्रदूषण: पश्चिम बंगाल, बिहार में; गंगा डेल्टा क्षेत्र; जल जनित रोग", "type": "leaf"},
                    {"label": "फ्लोराइड: राजस्थान, तेलंगाना, UP के कुछ क्षेत्रों में; अत्यधिक फ्लोराइड → फ्लोरोसिस", "type": "leaf"},
                    {"label": "Atal Bhujal Yojana (2019): 7 राज्यों में; सामुदायिक भागीदारी से भूजल प्रबंधन; World Bank सहायता", "type": "leaf"}
                ]}
            ]
        else:
            return [
                {"label": "Underground Water: Definition & Distribution", "type": "branch", "date": "Groundwater", "children": [
                    {"label": "Aquifer: Permeable rock/sediment storing water; types: Artesian, Confined, Unconfined", "type": "leaf"},
                    {"label": "India: 432 BCM groundwater potential; 393 BCM usable; 63% used for irrigation", "type": "leaf"},
                    {"label": "Over-exploitation: Punjab, Haryana, Rajasthan, Gujarat water table falling 3-5m/year", "type": "leaf"}
                ]},
                {"label": "Groundwater Management Challenges", "type": "branch", "date": "Challenges", "children": [
                    {"label": "Arsenic Contamination: West Bengal, Bihar; Ganga delta; causes arsenicosis disease", "type": "leaf"},
                    {"label": "Fluoride: Rajasthan, Telangana, parts of UP; excess fluoride causes fluorosis (dental/skeletal)", "type": "leaf"},
                    {"label": "Atal Bhujal Yojana (2019): 7 states; community-led groundwater management; World Bank funded", "type": "leaf"}
                ]}
            ]

    # 24. Volcanic Deposits
    elif 'volcanic' in fl:
        if is_hindi:
            return [
                {"label": "ज्वालामुखीय निक्षेप: महासागर में", "type": "branch", "date": "प्रकार", "children": [
                    {"label": "हाइड्रोथर्मल वेंट निक्षेप: मध्य-महासागरीय कटकों पर; ब्लैक स्मोकर; Zn, Cu, Fe, Ag, Au सल्फाइड", "type": "leaf"},
                    {"label": "ज्वालामुखीय राख: महासागर तल पर; 'टेफ्रा' (Tephra); कालाकाल का कालक्रम निर्धारण में उपयोगी", "type": "leaf"},
                    {"label": "पिलो लावा: पानी के नीचे लावा; तकिया आकार; मध्य-महासागरीय कटकों पर प्रचुर", "type": "leaf"}
                ]},
                {"label": "भूमि पर ज्वालामुखीय मृदा", "type": "branch", "date": "ज्वालामुखीय मृदा", "children": [
                    {"label": "रेगुर (काली मृदा): दक्कन ट्रैप; बेसाल्ट से निर्मित; Ca, Mg, Fe से भरपूर; स्वयं जुताई करने वाली", "type": "leaf"},
                    {"label": "सबसे उपजाऊ: ज्वालामुखीय मृदा खनिज समृद्ध; Java (Indonesia), Sicily (Italy) में घनी आबादी", "type": "leaf"}
                ]}
            ]
        else:
            return [
                {"label": "Volcanic Deposits in Oceans", "type": "branch", "date": "Types", "children": [
                    {"label": "Hydrothermal Vent Deposits: Mid-ocean ridges; Black Smokers; Zn, Cu, Fe, Ag, Au sulfides", "type": "leaf"},
                    {"label": "Volcanic Ash (Tephra): Settles on ocean floor; useful for paleoclimate chronology and dating", "type": "leaf"},
                    {"label": "Pillow Lavas: Underwater lava solidifying in pillow-shapes; abundant at mid-ocean ridge crests", "type": "leaf"}
                ]},
                {"label": "Volcanic Soils on Land", "type": "branch", "date": "Volcanic Soils", "children": [
                    {"label": "Regur/Black Soil: Deccan Trap basalt; rich in Ca, Mg, Fe; self-ploughing; ideal for cotton", "type": "leaf"},
                    {"label": "Fertility: Volcanic soils mineral-rich; hence dense populations on Java (Indonesia) and Sicily", "type": "leaf"}
                ]}
            ]

    # 25. Water consumption patterns
    elif 'consumption' in fl:
        if is_hindi:
            return [
                {"label": "जल उपभोग पैटर्न: वैश्विक", "type": "branch", "date": "वैश्विक", "children": [
                    {"label": "कृषि: 70% वैश्विक जल उपयोग; सिंचाई सर्वाधिक; भारत में 80% जल कृषि में", "type": "leaf"},
                    {"label": "उद्योग: 20% वैश्विक; थर्मल पावर प्लांट में शीतलन; कागज, वस्त्र, धातु उद्योग", "type": "leaf"},
                    {"label": "घरेलू/नगरपालिका: 10% वैश्विक; भारत में WHO मानक 150 लीटर/व्यक्ति/दिन; ग्रामीण <40 लीटर", "type": "leaf"}
                ]},
                {"label": "भारत में जल उपभोग संकट", "type": "branch", "date": "भारत", "children": [
                    {"label": "जल तनावग्रस्त राज्य: राजस्थान, गुजरात, पंजाब (भूजल ह्रास), AP, तेलंगाना", "type": "leaf"},
                    {"label": "पानी का बाजार: बोतलबंद पानी उद्योग; जल निजीकरण का विरोध; WASH संकट", "type": "leaf"},
                    {"label": "वर्चुअल वाटर: खाद्य व्यापार में निहित जल; भारत चावल निर्यात से बड़ा वर्चुअल वाटर निर्यातक", "type": "leaf"}
                ]}
            ]
        else:
            return [
                {"label": "Water Consumption Patterns: Global", "type": "branch", "date": "Global", "children": [
                    {"label": "Agriculture: 70% of global water use; irrigation dominant; India uses 80% in agriculture", "type": "leaf"},
                    {"label": "Industry: 20% globally; thermal power plant cooling; paper, textile, metallurgy", "type": "leaf"},
                    {"label": "Domestic/Municipal: 10% globally; WHO standard 150 L/capita/day; rural India <40 L/day", "type": "leaf"}
                ]},
                {"label": "India's Water Consumption Challenges", "type": "branch", "date": "India", "children": [
                    {"label": "Water-stressed states: Rajasthan, Gujarat, Punjab (groundwater depletion), AP, Telangana", "type": "leaf"},
                    {"label": "Virtual Water: Water embedded in traded food; India exports large virtual water through rice exports", "type": "leaf"},
                    {"label": "WASH Crisis: Water, Sanitation, Hygiene gaps; rural-urban divide; Jal Jeevan Mission response", "type": "leaf"}
                ]}
            ]

    # 26. Water on the Surface of the Earth
    elif 'water-on' in fl or ('water' in fl and 'surface' in fl and 'earth' in fl):
        if is_hindi:
            return [
                {"label": "पृथ्वी पर जल: वितरण", "type": "branch", "date": "वितरण", "children": [
                    {"label": "कुल जल: 1.38 अरब घन किमी; 97.5% महासागरों में (खारा); 2.5% मीठा", "type": "leaf"},
                    {"label": "मीठे जल का वितरण: 70% हिमनद/बर्फ → 30% भूजल → <1% नदियाँ/झीलें/वायुमंडल", "type": "leaf"},
                    {"label": "महासागर: अटलांटिक, प्रशांत, हिंद, आर्कटिक, अंटार्कटिक; प्रशांत सबसे बड़ा (165 मिलियन वर्ग किमी)", "type": "leaf"}
                ]},
                {"label": "जल का पारिस्थितिक महत्व", "type": "branch", "date": "महत्व", "children": [
                    {"label": "जीवन का आधार: सभी जैविक क्रियाओं के लिए आवश्यक; कोशिकीय विलायक; pH संतुलन", "type": "leaf"},
                    {"label": "जलवायु नियंत्रण: महासागर ताप को संग्रहीत करते हैं; उच्च विशिष्ट ऊष्मा; तटीय क्षेत्र समशीतोष्ण", "type": "leaf"},
                    {"label": "भारत में: 3287590 वर्ग किमी; 7516 किमी तटरेखा; तीन ओर से समुद्र; 'प्रायद्वीप'", "type": "leaf"}
                ]}
            ]
        else:
            return [
                {"label": "Water on Earth: Distribution", "type": "branch", "date": "Distribution", "children": [
                    {"label": "Total Water: 1.38 billion km³; 97.5% in oceans (saline); only 2.5% freshwater", "type": "leaf"},
                    {"label": "Freshwater Split: 70% glaciers/ice → 30% groundwater → <1% rivers/lakes/atmosphere", "type": "leaf"},
                    {"label": "Oceans: Atlantic, Pacific, Indian, Arctic, Antarctic; Pacific largest (165 million sq km)", "type": "leaf"}
                ]},
                {"label": "Ecological Importance of Water", "type": "branch", "date": "Importance", "children": [
                    {"label": "Basis of Life: Universal solvent for biological reactions; cellular medium; pH buffer", "type": "leaf"},
                    {"label": "Climate Regulator: Oceans store heat; high specific heat capacity; moderates coastal climates", "type": "leaf"},
                    {"label": "India: 7516 km coastline; surrounded on 3 sides; 'Peninsula'; monsoon driven by ocean evaporation", "type": "leaf"}
                ]}
            ]

    # 27. Waves Ocean Currents Tides
    elif 'waves' in fl:
        if is_hindi:
            return [
                {"label": "तरंगें (Waves): विशेषताएँ", "type": "branch", "date": "तरंगें", "children": [
                    {"label": "तरंग दीर्घता (Wavelength): दो शीर्षों के बीच की दूरी; तरंग ऊँचाई (Amplitude); गहरे जल में ऊर्जा यात्रा", "type": "leaf"},
                    {"label": "Tsunami: भूकंप/ज्वालामुखी/भूस्खलन से; 2004 हिंद महासागर Tsunami; 800 किमी/घंटा गति", "type": "leaf"},
                    {"label": "Storm Surge: चक्रवात से जल उठाव; Fani (2019), Amphan (2020); तटीय विनाश", "type": "leaf"}
                ]},
                {"label": "ज्वार-भाटा और महासागरीय धाराएँ", "type": "branch", "date": "ज्वार और धाराएँ", "children": [
                    {"label": "वृहद ज्वार (Spring Tide): पूर्णिमा/अमावस; सूर्य-पृथ्वी-चंद्रमा एक रेखा में; उच्चतम ज्वार", "type": "leaf"},
                    {"label": "लघु ज्वार (Neap Tide): प्रथमा/अष्टमी; सूर्य-पृथ्वी-चंद्रमा समकोण; निम्नतम ज्वार", "type": "leaf"},
                    {"label": "Coriolis Effect: धाराओं को उत्तरी गोलार्ध में दाईं ओर, दक्षिणी में बाईं ओर मोड़ता है", "type": "leaf"},
                    {"label": "ज्वारीय ऊर्जा: Gulf of Kutch; Cambay में संभावना; France का La Rance प्लांट", "type": "leaf"}
                ]}
            ]
        else:
            return [
                {"label": "Waves: Characteristics", "type": "branch", "date": "Waves", "children": [
                    {"label": "Wavelength: Distance between two crests; height = amplitude; energy travels but water doesn't move forward", "type": "leaf"},
                    {"label": "Tsunami: Caused by earthquake/volcano/submarine landslide; 2004 Indian Ocean Tsunami; 800 km/hr speed", "type": "leaf"},
                    {"label": "Storm Surge: Cyclone-driven coastal flooding; Fani (2019), Amphan (2020); devastating damage", "type": "leaf"}
                ]},
                {"label": "Tides & Ocean Currents", "type": "branch", "date": "Tides & Currents", "children": [
                    {"label": "Spring Tide: Full/New Moon; Sun-Earth-Moon alignment; highest tidal range", "type": "leaf"},
                    {"label": "Neap Tide: Quarter Moon; Sun-Earth-Moon at 90°; lowest tidal range", "type": "leaf"},
                    {"label": "Coriolis Effect: Deflects currents right in NH, left in SH; creates gyres in each ocean basin", "type": "leaf"},
                    {"label": "Tidal Energy: Gulf of Kutch potential; Gulf of Cambay; France's La Rance tidal power plant", "type": "leaf"}
                ]}
            ]

    # Fallback
    else:
        if is_hindi:
            return [{"label": "समुद्र विज्ञान", "type": "branch", "date": "भूगोल", "children": [
                {"label": "महासागरीय भूगोल और जल संसाधन से संबंधित UPSC विषय", "type": "leaf"}]}]
        else:
            return [{"label": "Oceanography", "type": "branch", "date": "Geography", "children": [
                {"label": "UPSC topics related to ocean geography and water resources", "type": "leaf"}]}]

def process_file(html_path, is_hindi):
    print(f"Processing: {html_path} (hindi={is_hindi})")
    with open(html_path, 'r', encoding='utf-8') as f:
        html = f.read()
    html = html.replace('\r\n', '\n')
    for old in ['    <link rel="stylesheet" href="/assets/css/mindmap.min.css?v=2">\n',
                '    <link rel="stylesheet" href="/assets/css/mindmap.min.css?v=1">\n',
                '    <link rel="stylesheet" href="/assets/css/mindmap.min.css">\n']:
        html = html.replace(old, '')
    html = re.sub(r'\s*<!-- Interactive Mindmap -->.*?<!-- Deep-Dive Study Guide \(Dynamically Rendered\) -->', '\n            <!-- Deep-Dive Study Guide (Dynamically Rendered) -->', html, flags=re.DOTALL)
    html = re.sub(r'\s*<!-- Interactive Mindmap -->.*?renderMindmap\(.*?\);\s*</script>', '', html, flags=re.DOTALL)

    folder_name = os.path.basename(os.path.dirname(html_path))
    if folder_name == 'hi':
        folder_name = os.path.basename(os.path.dirname(os.path.dirname(html_path)))

    clean_title = get_clean_title(folder_name)
    topic_name = clean_title
    cj = os.path.join(os.path.dirname(html_path), "content.json")
    if os.path.exists(cj):
        try:
            topic_name = json.load(open(cj, encoding='utf-8')).get('hero', {}).get('title', topic_name)
        except Exception:
            pass

    branches = get_custom_branches(folder_name, is_hindi)
    mindmap_data = {"label": clean_title, "type": "root", "children": branches}

    css_link = '    <link rel="stylesheet" href="/assets/css/mindmap.min.css?v=2">\n'
    if css_link not in html:
        html = html.replace('</head>', css_link + '</head>')

    if is_hindi:
        instr = 'किसी <strong style="color:#a78bfa;">बैंगनी</strong> या <strong style="color:#2ecc71;">हरे</strong> <strong>+</strong> पर क्लिक करें।'
        title_text = f"{topic_name} &mdash; इंटरैक्टिव माइंडमैप"
    else:
        instr = 'Tap a <strong style="color:#a78bfa;">purple</strong> or <strong style="color:#2ecc71;">green</strong> <strong>+</strong> to expand.'
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
    if re.search(r'<!-- Deep-Dive Study Guide \(Dynamically Rendered\) -->\s*<div class="card-premium" id="deep-dive-section">', html):
        html = re.sub(r'(<!-- Deep-Dive Study Guide \(Dynamically Rendered\) -->\s*<div class="card-premium" id="deep-dive-section">)', mindmap_card + r'\1', html)
    else:
        marker = '<div class="tab-panel active" id="notes-panel" role="tabpanel" aria-labelledby="notes-panel">'
        if marker in html:
            html = html.replace(marker, marker + '\n' + mindmap_card, 1)

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

def main():
    total = 0
    for root, dirs, files in os.walk(BASE):
        parts = os.path.relpath(root, BASE).split(os.sep)
        is_hindi = 'hi' in parts
        for file in files:
            if file == "index.html":
                process_file(os.path.join(root, file), is_hindi)
                total += 1
    print(f"\nDone! Patched {total} files.")

if __name__ == '__main__':
    main()
