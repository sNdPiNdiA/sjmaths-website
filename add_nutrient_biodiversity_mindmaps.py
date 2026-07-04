#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import re
import json

BASE_DIR = r"upsc/environment/Nutrient-Cycling-Biodiversity"

def get_clean_title(folder_name):
    title = re.sub(r'([a-z])([A-Z])', r'\1 \2', folder_name)
    title = title.replace('-', ' ')
    words = []
    acronyms = {'dpsp', 'pri', 'ut', 'uts', 'sc', 'hc', 'cm', 'com', 'arc', 'inc', 'ias', 'sec', 'sfc', 'pej', 'tej', 'mjo', 'enso', 'iod', 'icar', 'gst', 'dpc', 'mpc', 'adc', 'tac', 'scs', 'pesa', 'icar', 'isfr', 'itcz', 'tej', 'iucn', 'wpa'}
    for w in title.split():
        if w.lower() in acronyms:
            words.append(w.upper())
        elif w.lower() in ['of', 'and', 'the', 'for', 'in', 'with', 'against', 'to', 'on', 'some', 'by', 'their', 'vs']:
            words.append(w.lower())
        else:
            words.append(w.capitalize())
    return ' '.join(words)

# Fully comprehensive, grouped fact-dense dataset mapping every folder to a specific scientific mindmap
GROUPS = [
    {
        "keys": ["in-situ", "ex-situ", "conservation-methods", "conservation-priorities"],
        "en": [
            {"label": "In-situ Conservation (On-Site)", "type": "branch", "date": "In-situ", "children": [
                {"label": "Definition: Protecting species in their natural habitats (National Parks, Biosphere Reserves, Sacred Groves)", "type": "leaf"},
                {"label": "Advantage: Maintains evolutionary processes, ecological niches, and food web dynamics intact", "type": "leaf"},
                {"label": "Disadvantage: Exposed to localized natural disasters, disease outbreaks, and poaching pressures", "type": "leaf"}
            ]},
            {"label": "Ex-situ Conservation (Off-Site)", "type": "branch", "date": "Ex-situ", "children": [
                {"label": "Definition: Protecting species outside natural habitats (Zoological Parks, Botanical Gardens, Seed Banks)", "type": "leaf"},
                {"label": "Advantage: High control, protection from predators, veterinary care, and genetic backup", "type": "leaf"},
                {"label": "Disadvantage: High maintenance cost, genetic bottleneck risks, and lack of natural selection", "type": "leaf"}
            ]},
            {"label": "Cryopreservation & Seed Banks", "type": "branch", "date": "Advanced Tech", "children": [
                {"label": "Cryopreservation: Storing gametes, pollen, or embryos in liquid nitrogen at -196°C for long periods", "type": "leaf"},
                {"label": "Seed Banks: Storing seeds under low humidity and temperature to preserve crop wild relatives", "type": "leaf"}
            ]},
            {"label": "UPSC Core Relevance", "type": "branch", "date": "UPSC Focus", "children": [
                {"label": "Reintroduction Programs: e.g., Captive breeding of Pygmy Hog in Assam and Vultures in Pinjore", "type": "leaf"},
                {"label": "National targets: Aligning protected areas with the Kunming-Montreal Global Biodiversity Framework", "type": "leaf"}
            ]}
        ],
        "hi": [
            {"label": "स्व-स्थाने संरक्षण (In-situ)", "type": "branch", "date": "स्व-स्थाने", "children": [
                {"label": "परिभाषा: प्रजातियों को उनके प्राकृतिक आवासों में संरक्षित करना (राष्ट्रीय उद्यान, अभयारण्य, पवित्र उपवन)", "type": "leaf"},
                {"label": "लाभ: विकासवादी प्रक्रियाओं, पारिस्थितिक क्षेत्रों और खाद्य जाल को बनाए रखता है", "type": "leaf"},
                {"label": "हानि: प्राकृतिक आपदाओं, बीमारी फैलने और अवैध शिकार के खतरों के प्रति संवेदनशील", "type": "leaf"}
            ]},
            {"label": "बाह्य-स्थाने संरक्षण (Ex-situ)", "type": "branch", "date": "बाह्य-स्थाने", "children": [
                {"label": "परिभाषा: प्राकृतिक आवासों से बाहर संरक्षण (प्राणी उद्यान, वनस्पति उद्यान, बीज बैंक, क्रायोप्रिजर्वेशन)", "type": "leaf"},
                {"label": "लाभ: अत्यधिक नियंत्रित वातावरण, पशु चिकित्सा देखभाल और आनुवंशिक बैकअप प्राप्त होना", "type": "leaf"},
                {"label": "हानि: उच्च रखरखाव लागत, इनब्रीडिंग डिप्रेशन का खतरा और प्राकृतिक चयन का अभाव", "type": "leaf"}
            ]},
            {"label": "क्रायोप्रिजर्वेशन और बीज बैंक", "type": "branch", "date": "तकनीक", "children": [
                {"label": "क्रायोप्रिजर्वेशन: तरल नाइट्रोजन में -196°C पर युग्मकों, पराग या भ्रूण का दीर्घकालिक भंडारण", "type": "leaf"},
                {"label": "बीज बैंक: फसलों के आनुवंशिक स्रोतों को संरक्षित करने के लिए कम आर्द्रता और तापमान पर भंडारण", "type": "leaf"}
            ]},
            {"label": "यूपीएससी परीक्षा दृष्टिकोण", "type": "branch", "date": "परीक्षा", "children": [
                {"label": "पुनर्प्रवेश कार्यक्रम: जैसे असम में पिग्मी हॉग और पिंजौर में गिद्धों का बंदी प्रजनन व विमुक्ति", "type": "leaf"},
                {"label": "वैश्विक लक्ष्य: कुनमिंग-मॉन्ट्रियल वैश्विक जैव विविधता ढांचे (30x30 लक्ष्य) के साथ राष्ट्रीय तालमेल", "type": "leaf"}
            ]}
        ]
    },
    {
        "keys": ["carbon-cycle"],
        "en": [
            {"label": "Global Reservoirs", "type": "branch", "date": "Reservoirs", "children": [
                {"label": "Lithosphere: Earth's crust holds largest carbon store in sedimentary rocks (carbonate/limestone)", "type": "leaf"},
                {"label": "Oceans: Largest active carbon sink; absorbs CO2 via physical solubility and biological pumps", "type": "leaf"},
                {"label": "Atmosphere: Smallest active pool but critical for temperature regulation (~0.04% of air)", "type": "leaf"}
            ]},
            {"label": "Biological Processes", "type": "branch", "date": "Bio-Flows", "children": [
                {"label": "Photosynthesis: Autotrophs fix atmospheric CO2 into organic carbon (glucose)", "type": "leaf"},
                {"label": "Respiration & Decomposition: Return of CO2 to air by organisms metabolizing organic matter", "type": "leaf"}
            ]},
            {"label": "Anthropogenic Shifts", "type": "branch", "date": "Human Impact", "children": [
                {"label": "Combustion: Fossil fuel burning releases lithospheric carbon back to active cycles rapidly", "type": "leaf"},
                {"label": "Deforestation: Loss of forest biomass reduces global carbon assimilation capacity", "type": "leaf"}
            ]},
            {"label": "UPSC Exam Focus", "type": "branch", "date": "UPSC Focus", "children": [
                {"label": "Blue Carbon: Carbon captured by coastal ecosystems (mangroves, seagrasses, salt marshes)", "type": "leaf"},
                {"label": "Ocean Acidification: Excess dissolved CO2 forms carbonic acid, hindering marine calcification", "type": "leaf"}
            ]}
        ],
        "hi": [
            {"label": "वैश्विक कार्बन भंडार", "type": "branch", "date": "भंडार", "children": [
                {"label": "लिथोस्फीयर: पृथ्वी की पपड़ी में अवसादी चट्टानों (कार्बोनेट/चुना पत्थर) में सबसे बड़ा कार्बन भंडार है", "type": "leaf"},
                {"label": "महासागर: सबसे बड़ा सक्रिय कार्बन सिंक; घुलनशीलता और जैविक पंपों द्वारा CO2 को अवशोषित करता है", "type": "leaf"},
                {"label": "वायुमंडल: छोटा सक्रिय पूल लेकिन तापमान विनियमन के लिए महत्वपूर्ण (हवा का ~0.04% हिस्सा)", "type": "leaf"}
            ]},
            {"label": "जैविक प्रक्रियाएं", "type": "branch", "date": "जैविक प्रवाह", "children": [
                {"label": "प्रकाश संश्लेषण: स्वपोषी पौधे वायुमंडलीय CO2 को कार्बनिक कार्बन (ग्लूकोज) में स्थिर करते हैं", "type": "leaf"},
                {"label": "श्वसन और अपघटन: कार्बनिक पदार्थों के उपभोग द्वारा CO2 का वायुमंडल में पुनः विमोचन", "type": "leaf"}
            ]},
            {"label": "मानवजनित बदलाव", "type": "branch", "date": "मानव प्रभाव", "children": [
                {"label": "दहन: जीवाश्म ईंधन जलने से संग्रहीत लिथोस्फेरिक कार्बन तेजी से सक्रिय चक्र में लौटता है", "type": "leaf"},
                {"label": "वनोन्मूलन: वन जैवभार के नुकसान से वैश्विक कार्बन अवशोषण क्षमता में कमी आती है", "type": "leaf"}
            ]},
            {"label": "यूपीएससी परीक्षा दृष्टिकोण", "type": "branch", "date": "परीक्षा", "children": [
                {"label": "ब्लू कार्बन: तटीय पारिस्थितिकी तंत्र (मैंग्रोव, समुद्री घास, लवण दलदल) द्वारा कैप्चर किया गया कार्बन", "type": "leaf"},
                {"label": "महासागरीय अम्लीकरण: अत्यधिक घुली हुई CO2 कार्बोनिक एसिड बनाती है, जो शंखधारी जीवों को नुकसान पहुँचाती है", "type": "leaf"}
            ]}
        ]
    },
    {
        "keys": ["nitrogen-cycle"],
        "en": [
            {"label": "Nitrogen Fixation", "type": "branch", "date": "Fixation", "children": [
                {"label": "Biological: Rhizobium (symbiotic in legume root nodules), Azotobacter (free-living soil bacteria)", "type": "leaf"},
                {"label": "Atmospheric & Industrial: Lightning discharges and Haber-Bosch chemical fertilizer synthesis", "type": "leaf"}
            ]},
            {"label": "Nitrification Processes", "type": "branch", "date": "Nitrification", "children": [
                {"label": "Ammonification: Decomposers convert organic nitrogen from waste/dead matter into ammonia", "type": "leaf"},
                {"label": "Nitrification: Ammonia is oxidized to Nitrite by Nitrosomonas, then to Nitrate by Nitrobacter", "type": "leaf"},
                {"label": "Assimilation: Plants absorb nitrates to form proteins, entering the food chain", "type": "leaf"}
            ]},
            {"label": "Denitrification", "type": "branch", "date": "Return", "children": [
                {"label": "Definition: Conversion of nitrates back into gaseous molecular nitrogen (N2) in anaerobic conditions", "type": "leaf"},
                {"label": "Microbes: Pseudomonas and Thiobacillus species operating in waterlogged/oxygen-deprived soils", "type": "leaf"}
            ]},
            {"label": "UPSC Exam Focus", "type": "branch", "date": "UPSC Focus", "children": [
                {"label": "Eutrophication: Excessive nitrogen runoff causes algal blooms, creating hypoxic dead zones", "type": "leaf"},
                {"label": "Greenhouse gas: Nitrous oxide (N2O) is a potent greenhouse gas and ozone-depleting substance", "type": "leaf"}
            ]}
        ],
        "hi": [
            {"label": "नाइट्रोजन स्थिरीकरण", "type": "branch", "date": "स्थिरीकरण", "children": [
                {"label": "जैविक: राइजोबियम (फलीदार पौधों की जड़ों में सहजीवी), एज़ोटोबैक्टर (मिट्टी में मुक्त-जीवी जीवाणु)", "type": "leaf"},
                {"label": "वायुमंडलीय और औद्योगिक: बिजली चमकने से और हैबर-बॉश रासायनिक उर्वरक संश्लेषण द्वारा", "type": "leaf"}
            ]},
            {"label": "नाइट्रीकरण प्रक्रियाएं", "type": "branch", "date": "नाइट्रीकरण", "children": [
                {"label": "अमोनीकरण: अपघटक मृत अपशिष्ट पदार्थों के नाइट्रोजन को अमोनिया में परिवर्तित करते हैं", "type": "leaf"},
                {"label": "नाइट्रीकरण: अमोनिया नाइट्रोसोमोनास द्वारा नाइट्राइट में, फिर नाइट्रोबैक्टर द्वारा नाइट्रेट में बदला जाता है", "type": "leaf"},
                {"label": "स्वांगीकरण (Assimilation): पौधे प्रोटीन बनाने के लिए नाइट्रेट्स को अवशोषित करते हैं", "type": "leaf"}
            ]},
            {"label": "विनाइट्रीकरण (Denitrification)", "type": "branch", "date": "वापसी", "children": [
                {"label": "परिभाषा: अवायवीय परिस्थितियों में नाइट्रेट्स का पुनः गैसीय नाइट्रोजन (N2) में परिवर्तन", "type": "leaf"},
                {"label": "सूक्ष्मजीव: जलभराव या ऑक्सीजन की कमी वाली मिट्टी में स्यूडोमोनास और थायोबैसिलस जीवाणु", "type": "leaf"}
            ]},
            {"label": "यूपीएससी परीक्षा दृष्टिकोण", "type": "branch", "date": "परीक्षा", "children": [
                {"label": "यूट्रोफिकेशन: अत्यधिक नाइट्रोजन बहने से शैवाल प्रस्फुटन होता है, जिससे जलीय ऑक्सीजन समाप्त होती है", "type": "leaf"},
                {"label": "नाइट्रस ऑक्साइड (N2O): एक शक्तिशाली ग्रीनहाउस गैस और ओजोन-घटाने वाला पदार्थ है", "type": "leaf"}
            ]}
        ]
    },
    {
        "keys": ["oxygen-cycle"],
        "en": [
            {"label": "Atmospheric Reservoirs", "type": "branch", "date": "Reservoir", "children": [
                {"label": "Diatomic Oxygen (O2) comprises 20.95% of Earth's dry atmosphere, vital for animal respiration", "type": "leaf"},
                {"label": "Lithosphere holds the largest reserve, bound in silicate and oxide minerals of the crust", "type": "leaf"}
            ]},
            {"label": "Photosynthesis Production", "type": "branch", "date": "Production", "children": [
                {"label": "Terrestrial Flora: Solar energy photolyzes water (H2O), releasing oxygen as a byproduct", "type": "leaf"},
                {"label": "Marine Phytoplankton: Contributes over 50% of global atmospheric oxygen production", "type": "leaf"}
            ]},
            {"label": "Consumption Pathways", "type": "branch", "date": "Consumption", "children": [
                {"label": "Aerobic Respiration: Organisms utilize O2 to oxidize organic carbon, yielding water and CO2", "type": "leaf"},
                {"label": "Chemical Weathering: Oxidation of crustal minerals (e.g., rust formation) consumes atmospheric oxygen", "type": "leaf"}
            ]},
            {"label": "UPSC Exam Focus", "type": "branch", "date": "UPSC Focus", "children": [
                {"label": "Stratospheric Ozone (O3) protects the biosphere by absorbing harmful solar UV radiation", "type": "leaf"},
                {"label": "Dissolved Oxygen (DO) levels define aquatic health; drop below 4 mg/L is lethal to fish", "type": "leaf"}
            ]}
        ],
        "hi": [
            {"label": "वायुमंडलीय ऑक्सीजन भंडार", "type": "branch", "date": "भंडार", "children": [
                {"label": "ऑक्सीजन (O2) पृथ्वी के शुष्क वायुमंडल का 20.95% हिस्सा बनाती है, जो श्वसन के लिए आवश्यक है", "type": "leaf"},
                {"label": "लिथोस्फीयर सबसे बड़ा भंडार है, जहां यह क्रस्ट के सिलिकेट और ऑक्साइड खनिजों में बंधी होती है", "type": "leaf"}
            ]},
            {"label": "उत्पादन (प्रकाश संश्लेषण)", "type": "branch", "date": "उत्पादन", "children": [
                {"label": "स्थलीय वनस्पतियां: सौर ऊर्जा जल (H2O) का प्रकाश अपघटन कर ऑक्सीजन विमुक्त करती हैं", "type": "leaf"},
                {"label": "समुद्री पादप प्लवक: वैश्विक वायुमंडलीय ऑक्सीजन उत्पादन में 50% से अधिक का योगदान करते हैं", "type": "leaf"}
            ]},
            {"label": "उपभोग के मार्ग", "type": "branch", "date": "उपभोग", "children": [
                {"label": "वायवीय श्वसन: जीव कार्बनिक पदार्थों को पचाने के लिए O2 का उपयोग करते हैं, जल और CO2 छोड़ते हैं", "type": "leaf"},
                {"label": "रासायनिक अपक्षय: चट्टानों में लौह खनिजों के ऑक्सीकरण (जंग लगना) से ऑक्सीजन का उपभोग होता है", "type": "leaf"}
            ]},
            {"label": "यूपीएससी परीक्षा दृष्टिकोण", "type": "branch", "date": "परीक्षा", "children": [
                {"label": "समतापमंडलीय ओजोन (O3) हानिकारक सौर यूवी विकिरण को अवशोषित कर जीवमंडल की रक्षा करती है", "type": "leaf"},
                {"label": "घुलित ऑक्सीजन (DO) जलीय स्वास्थ्य को दर्शाती है; 4 mg/L से कम का स्तर मछलियों के लिए घातक है", "type": "leaf"}
            ]}
        ]
    },
    {
        "keys": ["phosphorus-cycle"],
        "en": [
            {"label": "Sedimentary Reservoir", "type": "branch", "date": "Reservoir", "children": [
                {"label": "Mainly lithospheric: Found in phosphate rocks, minerals (apatite), and marine sediments", "type": "leaf"},
                {"label": "Lacks gaseous phase: No significant atmospheric pathway except windborne dust", "type": "leaf"}
            ]},
            {"label": "Release & Biological Flows", "type": "branch", "date": "Flows", "children": [
                {"label": "Weathering: Rainfall and acids dissolve phosphate minerals, releasing orthophosphate (PO4 3-)", "type": "leaf"},
                {"label": "Plant Uptake: Absorbed from soil water; converted to ATP, DNA, and phospholipids in food webs", "type": "leaf"},
                {"label": "Return: Microbes decompose organic detritus, returning inorganic phosphorus to soil", "type": "leaf"}
            ]},
            {"label": "Marine Sedimentation", "type": "branch", "date": "Sedimentation", "children": [
                {"label": "Runoff carries phosphorus to oceans; precipitates to bottom sediment forming new rocks", "type": "leaf"},
                {"label": "Upwelling currents bring deep sedimentary phosphorus back to euphotic zones to boost marine life", "type": "leaf"}
            ]},
            {"label": "UPSC Exam Focus", "type": "branch", "date": "UPSC Focus", "children": [
                {"label": "Limiting Factor: Phosphorus is the primary limiting nutrient in freshwater ecosystems", "type": "leaf"},
                {"label": "Eutrophication: Excessive phosphate fertilizer runoff triggers rapid cyanobacterial blooms", "type": "leaf"}
            ]}
        ],
        "hi": [
            {"label": "अवसादी चट्टानी भंडार", "type": "branch", "date": "भंडार", "children": [
                {"label": "मुख्य रूप से लिथोस्फीयर: फास्फेट चट्टानों, खनिजों (एपेटाइट) और समुद्री तलछटों में पाया जाता है", "type": "leaf"},
                {"label": "गैसीय चरण का अभाव: धूल कणों के अतिरिक्त इसका कोई वायुमंडलीय मार्ग नहीं है", "type": "leaf"}
            ]},
            {"label": "विमुक्ति और जैविक प्रवाह", "type": "branch", "date": "प्रवाह", "children": [
                {"label": "अपक्षय: वर्षा और अम्ल फास्फेट खनिजों को घोलते हैं, ऑर्थोफॉस्फेट (PO4 3-) छोड़ते हैं", "type": "leaf"},
                {"label": "पौधों द्वारा अवशोषण: मिट्टी से लेकर ATP, DNA और फॉस्फोलिपिड के रूप में खाद्य श्रृंखला में प्रवेश", "type": "leaf"},
                {"label": "अपघटन: सूक्ष्मजीव कार्बनिक पदार्थों को तोड़कर अकार्बनिक फास्फोरस को वापस मिट्टी में लौटाते हैं", "type": "leaf"}
            ]},
            {"label": "समुद्री अवसादन", "type": "branch", "date": "अवसादन", "children": [
                {"label": "अपवाह फास्फोरस को समुद्र में ले जाता है; तलछट में जमा होकर नई चट्टान परतें बनाता है", "type": "leaf"},
                {"label": "अपवेलिंग (Upwelling): समुद्री धाराएं गहरे फास्फोरस को प्रकाश क्षेत्र में लाती हैं जिससे उत्पादकता बढ़ती है", "type": "leaf"}
            ]},
            {"label": "यूपीएससी परीक्षा दृष्टिकोण", "type": "branch", "date": "परीक्षा", "children": [
                {"label": "सीमित कारक (Limiting Factor): फास्फोरस मीठे पानी के पारिस्थितिक तंत्र में प्राथमिक सीमित पोषक तत्व है", "type": "leaf"},
                {"label": "यूट्रोफिकेशन: अत्यधिक फास्फेट उर्वरकों के बहने से तेजी से नील-हरित शैवाल प्रस्फुटन होता है", "type": "leaf"}
            ]}
        ]
    },
    {
        "keys": ["sulfur-cycle"],
        "en": [
            {"label": "Reservoirs & Geological Sources", "type": "branch", "date": "Reservoirs", "children": [
                {"label": "Lithospheric: Earth's crust holds largest pool in pyrite (FeS2), gypsum (CaSO4), and coal deposits", "type": "leaf"},
                {"label": "Atmospheric: Exists as sulfur dioxide (SO2) and hydrogen sulfide (H2S) from volcanic/industrial sources", "type": "leaf"}
            ]},
            {"label": "Biological Transformations", "type": "branch", "date": "Microbiology", "children": [
                {"label": "Oxidation: Chemolithotrophic bacteria (e.g. Thiobacillus) convert H2S into sulfates (SO4 2-)", "type": "leaf"},
                {"label": "Reduction: Sulfate-reducing bacteria (e.g. Desulfovibrio) convert sulfates back to H2S in anaerobic soil", "type": "leaf"}
            ]},
            {"label": "Atmospheric Acid Rain", "type": "branch", "date": "Atmosphere", "children": [
                {"label": "SO2 reacts with water vapor to form sulfurous and sulfuric acid (H2SO4)", "type": "leaf"},
                {"label": "Acid precipitation (pH < 5.6) damages forests, aquatic life, and heritage monuments", "type": "leaf"}
            ]},
            {"label": "UPSC Exam Focus", "type": "branch", "date": "UPSC Focus", "children": [
                {"label": "Bio-indicators: Lichens are highly sensitive to SO2; disappear in high sulfur zones", "type": "leaf"},
                {"label": "Dimethyl Sulfide (DMS): Released by marine phytoplankton; acts as nuclei for cloud condensation", "type": "leaf"}
            ]}
        ],
        "hi": [
            {"label": "सल्फर भंडार और स्रोत", "type": "branch", "date": "भंडार", "children": [
                {"label": "क्रस्ट भंडार: पाइराइट (FeS2), जिप्सम (CaSO4) और कोयला निक्षेपों में सबसे बड़ा भंडार", "type": "leaf"},
                {"label": "वायुमंडलीय: ज्वालामुखीय/औद्योगिक स्रोतों से सल्फर डाइऑक्साइड (SO2) और हाइड्रोजन सल्फाइड (H2S) के रूप में", "type": "leaf"}
            ]},
            {"label": "जैविक रूपांतरण", "type": "branch", "date": "प्रक्रियाएं", "children": [
                {"label": "ऑक्सीकरण: कीमोलिथोट्रॉफिक जीवाणु (जैसे थायोबैसिलस) H2S को सल्फेट (SO4 2-) में बदलते हैं", "type": "leaf"},
                {"label": "अपचयन: सल्फेट-अपचायक जीवाणु (जैसे डिसल्फोविब्रियो) अवायवीय परिस्थितियों में सल्फेट को H2S में बदलते हैं", "type": "leaf"}
            ]},
            {"label": "वायुमंडलीय मार्ग और अम्लीय वर्षा", "type": "branch", "date": "अम्लीय वर्षा", "children": [
                {"label": "SO2 जलवाष्प के साथ मिलकर सल्फ्यूरिक एसिड (H2SO4) का निर्माण करती है", "type": "leaf"},
                {"label": "अम्लीय वर्षा (pH < 5.6) वनों, जलीय जीवन और ऐतिहासिक स्मारकों को गंभीर नुकसान पहुँचाती है", "type": "leaf"}
            ]},
            {"label": "यूपीएससी परीक्षा दृष्टिकोण", "type": "branch", "date": "परीक्षा", "children": [
                {"label": "जैव-संकेतक: लाइकेन SO2 के प्रति अत्यधिक संवेदनशील होते हैं; उच्च सल्फर क्षेत्रों में नष्ट हो जाते हैं", "type": "leaf"},
                {"label": "डाइमिथाइल सल्फाइड (DMS): समुद्री प्लवक द्वारा स्रावित; बादल संघनन नाभिक के रूप में कार्य करता है", "type": "leaf"}
            ]}
        ]
    },
    {
        "keys": ["biogeochemical", "hydrological", "nutrient", "cycling"],
        "en": [
            {"label": "Biogeochemical Cycles Overview", "type": "branch", "date": "Concept", "children": [
                {"label": "Definition: Movement and circulation of chemical nutrients between living organisms and abiotic pools", "type": "leaf"},
                {"label": "Homeostasis: Essential to maintain balanced biosphere and prevent depletion of essential life-building blocks", "type": "leaf"}
            ]},
            {"label": "Gaseous vs Sedimentary Cycles", "type": "branch", "date": "Types", "children": [
                {"label": "Gaseous: Reservoirs are in atmosphere/hydrosphere; rapid recycling (e.g. Carbon, Nitrogen, Oxygen, Water)", "type": "leaf"},
                {"label": "Sedimentary: Reservoirs are in lithosphere; slow recycling (e.g. Phosphorus, Sulfur, Calcium)", "type": "leaf"}
            ]},
            {"label": "Hydrological Cycle Mechanics", "type": "branch", "date": "Water Cycle", "children": [
                {"label": "Solar-driven: Evaporation and transpiration turn water into vapor; condensation forms precipitation", "type": "leaf"},
                {"label": "Infiltration & Runoff: Water penetrates soil to recharge groundwater or flows as runoff to rivers/oceans", "type": "leaf"}
            ]},
            {"label": "UPSC Exam Focus", "type": "branch", "date": "UPSC Focus", "children": [
                {"label": "Water Budget: Oceans hold 97.2%; ice caps 2.15%; groundwater 0.62%; rivers and lakes only 0.015%", "type": "leaf"},
                {"label": "Human disturbances: Mining sedimentary rocks accelerates chemical runoff, causing aquatic ecological collapse", "type": "leaf"}
            ]}
        ],
        "hi": [
            {"label": "जैव-भू-रासायनिक चक्र अवलोकन", "type": "branch", "date": "अवधारणा", "children": [
                {"label": "परिभाषा: सजीवों और निर्जीव पर्यावरण के बीच रासायनिक पोषक तत्वों का परिसंचरण", "type": "leaf"},
                {"label": "समस्थापन (Homeostasis): जीवमंडल को संतुलित रखने और जीवन-निर्माण तत्वों की कमी को रोकने के लिए आवश्यक", "type": "leaf"}
            ]},
            {"label": "गैसीय बनाम अवसादी चक्र", "type": "branch", "date": "प्रकार", "children": [
                {"label": "गैसीय चक्र: भंडार वायुमंडल/जलमंडल में; तीव्र पुनर्चक्रण (जैसे कार्बन, नाइट्रोजन, ऑक्सीजन, जल)", "type": "leaf"},
                {"label": "अवसादी चक्र: भंडार भूपर्पटी (लिथोस्फीयर) में; धीमा पुनर्चक्रण (जैसे फास्फोरस, सल्फर, कैल्शियम)", "type": "leaf"}
            ]},
            {"label": "जल चक्र की क्रियाविधि", "type": "branch", "date": "जल चक्र", "children": [
                {"label": "सौर-संचालित: वाष्पीकरण और वाष्पोत्सर्जन पानी को वाष्प में बदलते हैं; संघनन से वर्षा होती है", "type": "leaf"},
                {"label": "अंतःस्यंदन और अपवाह: पानी भूजल को रिचार्ज करने के लिए रिसता है या नदियों/समुद्रों में बहता है", "type": "leaf"}
            ]},
            {"label": "यूपीएससी परीक्षा दृष्टिकोण", "type": "branch", "date": "परीक्षा", "children": [
                {"label": "जल बजट: महासागर 97.2%; बर्फ की टोपियां 2.15%; भूजल 0.62%; नदियां और झीलें केवल 0.015%", "type": "leaf"},
                {"label": "मानवीय हस्तक्षेप: अवसादी चट्टानों का खनन रासायनिक अपवाह को तेज करता है, जिससे जलीय पारिस्थितिकी नष्ट होती है", "type": "leaf"}
            ]}
        ]
    },
    {
        "keys": ["basics-of-biodiversity", "functions-of-biodiversity", "biodiversity-conservation"],
        "en": [
            {"label": "Levels of Biodiversity", "type": "branch", "date": "Levels", "children": [
                {"label": "Genetic: Variation within a single species (e.g., thousands of distinct rice strains in India)", "type": "leaf"},
                {"label": "Species: Variety and abundance of species in an ecosystem, measured by richness and evenness", "type": "leaf"},
                {"label": "Ecosystem: Variety of habitats, niches, and food web networks across biosphere biomes", "type": "leaf"}
            ]},
            {"label": "Biodiversity Indices", "type": "branch", "date": "Measurement", "children": [
                {"label": "Alpha: Species richness in a single local community or habitat", "type": "leaf"},
                {"label": "Beta: Change or turnover in species composition between adjacent habitats", "type": "leaf"},
                {"label": "Gamma: Overall species richness across a large regional landscape", "type": "leaf"}
            ]},
            {"label": "Ecosystem Services", "type": "branch", "date": "Services", "children": [
                {"label": "Supporting & Regulating: Photosynthesis, water purification, flood control by wetlands, insect pollination", "type": "leaf"},
                {"label": "Provisioning & Cultural: Source of food, timber, genetic medicine resource, ecotourism value", "type": "leaf"}
            ]},
            {"label": "UPSC Exam Focus", "type": "branch", "date": "UPSC Focus", "children": [
                {"label": "Simpson vs Shannon Index: Mathematical measures assessing species dominance vs entropy/uncertainty", "type": "leaf"},
                {"label": "Biological Diversity Act 2002: Implements CBD; regulates access to biological resources through NBA", "type": "leaf"}
            ]}
        ],
        "hi": [
            {"label": "जैव विविधता के स्तर", "type": "branch", "date": "स्तर", "children": [
                {"label": "आनुवंशिक: एक प्रजाति के भीतर आनुवंशिक भिन्नता (जैसे भारत में धान की हजारों किस्में)", "type": "leaf"},
                {"label": "प्रजाति: पारिस्थितिकी तंत्र में प्रजातियों की समृद्धि (Richness) और समरूपता (Evenness)", "type": "leaf"},
                {"label": "पारितंत्र: जीवमंडल बायोम में विभिन्न आवासों, निकेतों और खाद्य जालों की विविधता", "type": "leaf"}
            ]},
            {"label": "जैव विविधता सूचकांक", "type": "branch", "date": "मापन", "children": [
                {"label": "अल्फा सूचकांक: एक ही स्थानीय समुदाय या आवास के भीतर प्रजातियों की कुल संख्या", "type": "leaf"},
                {"label": "बीटा सूचकांक: पड़ोसी आवासों के बीच प्रजातियों की संरचना में बदलाव की दर", "type": "leaf"},
                {"label": "गामा सूचकांक: एक बड़े क्षेत्रीय परिदृश्य में कुल प्रजातियों की समृद्धि", "type": "leaf"}
            ]},
            {"label": "पारिस्थितिकी तंत्र सेवाएँ", "type": "branch", "date": "सेवाएँ", "children": [
                {"label": "सहायक और नियामक: प्रकाश संश्लेषण, जल शुद्धिकरण, आर्द्रभूमि द्वारा बाढ़ नियंत्रण, कीट परागण", "type": "leaf"},
                {"label": "प्रावधान और सांस्कृतिक: भोजन, इमारती लकड़ी, आनुवंशिक दवाओं के स्रोत और पर्यावरण-पर्यटन का मूल्य", "type": "leaf"}
            ]},
            {"label": "यूपीएससी परीक्षा दृष्टिकोण", "type": "branch", "date": "परीक्षा", "children": [
                {"label": "शैनन बनाम सिम्पसन सूचकांक: प्रजाति प्रभुत्व बनाम यादृच्छिकता/अनिश्चितता का आकलन करने वाले गणितीय माप", "type": "leaf"},
                {"label": "जैव विविधता अधिनियम 2002: CBD को लागू करता है; NBA के माध्यम से जैविक संसाधनों तक पहुंच को नियंत्रित करता है", "type": "leaf"}
            ]}
        ]
    },
    {
        "keys": ["causes-of-biodiversity", "threats-to-biodiversity", "effects-of-loss"],
        "en": [
            {"label": "The 'Evil Quartet' Drivers", "type": "branch", "date": "Evil Quartet", "children": [
                {"label": "Habitat Loss & Fragmentation: Leading threat; clearing forests for crops and cities", "type": "leaf"},
                {"label": "Overexploitation: Unsustainable hunting, fishing, and poaching of timber and wildlife", "type": "leaf"},
                {"label": "Invasive Alien Species: Displacing native species through competition (e.g., Lantana, Water Hyacinth)", "type": "leaf"},
                {"label": "Co-extinctions: Extinction of host species triggers extinction of dependent parasites/mutualists", "type": "leaf"}
            ]},
            {"label": "Ecological Consequences", "type": "branch", "date": "Effects", "children": [
                {"label": "Resilience Drop: Ecosystems with lower species diversity show poor defense to droughts or pests", "type": "leaf"},
                {"label": "Trophic Cascade: Extinction of apex predators causes herbivore overpopulation and habitat degradation", "type": "leaf"}
            ]},
            {"label": "Atmospheric & Disease Impacts", "type": "branch", "date": "Impacts", "children": [
                {"label": "Decreased carbon sequestration capacity of degraded forests accelerates global warming", "type": "leaf"},
                {"label": "Dilution Effect Loss: Biodiverse systems buffer zoonotic pathogens; biodiversity loss increases zoonotic spillover", "type": "leaf"}
            ]},
            {"label": "UPSC Exam Focus", "type": "branch", "date": "UPSC Focus", "children": [
                {"label": "Rivet Popper Hypothesis: Comparing species to aircraft rivets; removing rivets weakens flight safety", "type": "leaf"},
                {"label": "Anthropocene: Current geological epoch characterized by human-induced mass extinctions", "type": "leaf"}
            ]}
        ],
        "hi": [
            {"label": "द 'इविल क्वार्टेट' कारक", "type": "branch", "date": "इविल क्वार्टेट", "children": [
                {"label": "आवास हानि और विखंडन: प्रमुख खतरा; फसलों और शहरों के लिए वनों की कटाई", "type": "leaf"},
                {"label": "अत्यधिक दोहन: इमारती लकड़ी और वन्यजीवों का निरंतर शिकार और अवैध शिकार", "type": "leaf"},
                {"label": "आक्रामक विदेशी प्रजातियां: मूल प्रजातियों को विस्थापित करना (जैसे लैंटाना कैमारा, जलकुंभी)", "type": "leaf"},
                {"label": "सह-विलुप्ति: मेजबान प्रजाति के विलुप्त होने से उस पर निर्भर परजीवियों की विलुप्ति होती है", "type": "leaf"}
            ]},
            {"label": "पारिस्थितिक परिणाम", "type": "branch", "date": "पारिस्थितिक प्रभाव", "children": [
                {"label": "लचीलेपन में कमी: कम विविधता वाले क्षेत्र सूखे या कीटों का मुकाबला नहीं कर पाते", "type": "leaf"},
                {"label": "ट्रॉफिक कैस्केड: शीर्ष शिकारियों के हटने से शाकाहारियों की संख्या अनियंत्रित हो जाती है", "type": "leaf"}
            ]},
            {"label": "जलवायु और रोग प्रभाव", "type": "branch", "date": "प्रभाव", "children": [
                {"label": "वनों की कार्बन पृथक्करण क्षमता में कमी से ग्लोबल वार्मिंग में तेजी आती है", "type": "leaf"},
                {"label": "डाइल्यूशन प्रभाव (Dilution Effect): जैव विविधता के नुकसान से वन्यजीवों से मनुष्यों में रोग फैलने का खतरा बढ़ता है", "type": "leaf"}
            ]},
            {"label": "यूपीएससी परीक्षा दृष्टिकोण", "type": "branch", "date": "परीक्षा", "children": [
                {"label": "रिवेट पॉपर परिकल्पना: पारिस्थितिकी तंत्र एक हवाई जहाज की तरह है; प्रजातियां इसके पेंच (Rivets) हैं", "type": "leaf"},
                {"label": "एंथ्रोपोसीन (Anthropocene): वर्तमान युग जो मानव-प्रेरित बड़े पैमाने पर जैव विविधता हानि से परिभाषित है", "type": "leaf"}
            ]}
        ]
    },
    {
        "keys": ["extinction", "mass-extinction"],
        "en": [
            {"label": "Background vs Mass Extinction", "type": "branch", "date": "Rates", "children": [
                {"label": "Background: Slow, natural loss of species due to evolutionary changes (~1-5 species/year)", "type": "leaf"},
                {"label": "Mass Extinction: Rapid, global event wiping out >75% of species in a short geological span", "type": "leaf"}
            ]},
            {"label": "The Big Five Events", "type": "branch", "date": "Big Five", "children": [
                {"label": "Permian Extinction (The Great Dying): Over 95% of marine species extinct due to Siberian Trap volcanic activity", "type": "leaf"},
                {"label": "Cretaceous (K-Pg) Extinction: Dinosaur extinction 66 million years ago due to asteroid impact in Yucatan", "type": "leaf"}
            ]},
            {"label": "The Sixth Extinction (Anthropocene)", "type": "branch", "date": "6th Extinction", "children": [
                {"label": "Human-driven: Rapid loss caused by habitat destruction, global warming, and hunting since industrial era", "type": "leaf"},
                {"label": "Rate: Current extinction rate is estimated at 100 to 1,000 times faster than natural background rates", "type": "leaf"}
            ]},
            {"label": "UPSC Exam Focus", "type": "branch", "date": "UPSC Focus", "children": [
                {"label": "IUCN Extinct (EX) Status: Declared only after exhaustive surveys in historical habitats fail to record a single individual", "type": "leaf"},
                {"label": "Planetary Boundaries: Loss of biosphere integrity has crossed the safe operational boundary limit", "type": "leaf"}
            ]}
        ],
        "hi": [
            {"label": "पृष्ठभूमि बनाम सामूहिक विलुप्ति", "type": "branch", "date": "दरें", "children": [
                {"label": "पृष्ठभूमि विलुप्ति: विकासवादी परिवर्तनों के कारण प्रजातियों का धीमा, प्राकृतिक नुकसान (~1-5 प्रजाति/वर्ष)", "type": "leaf"},
                {"label": "सामूहिक विलुप्ति: संक्षिप्त भूवैज्ञानिक काल में वैश्विक स्तर पर >75% प्रजातियों का तेजी से नष्ट होना", "type": "leaf"}
            ]},
            {"label": "पांच ऐतिहासिक घटनाएं (Big Five)", "type": "branch", "date": "इतिहास", "children": [
                {"label": "परमियन विलुप्ति (महान विलुप्ति): साइबेरियन ट्रैप्स में तीव्र ज्वालामुखी विस्फोट से 95% से अधिक समुद्री प्रजातियां लुप्त हुईं", "type": "leaf"},
                {"label": "क्रीटेशियस (K-Pg) विलुप्ति: एस्टेरॉयड प्रभाव से 66 मिलियन वर्ष पहले डायनासोरों की सामूहिक विलुप्ति", "type": "leaf"}
            ]},
            {"label": "छठी सामूहिक विलुप्ति (Anthropocene)", "type": "branch", "date": "छठी विलुप्ति", "children": [
                {"label": "मानव-प्रेरित: औद्योगिक युग के बाद से वनों की कटाई, ग्लोबल वार्मिंग और शिकार के कारण हो रही विलुप्ति", "type": "leaf"},
                {"label": "दर: वर्तमान विलुप्ति दर प्राकृतिक दर की तुलना में 100 से 1,000 गुना अधिक तीव्र है", "type": "leaf"}
            ]},
            {"label": "यूपीएससी परीक्षा दृष्टिकोण", "type": "branch", "date": "परीक्षा", "children": [
                {"label": "IUCN विलुप्त (EX) स्थिति: तभी घोषित की जाती है जब विस्तृत सर्वेक्षण में ऐतिहासिक आवासों में कोई जीव न मिले", "type": "leaf"},
                {"label": "ग्रहों की सीमाएं (Planetary Boundaries): जैवमंडल अखंडता का नुकसान सुरक्षित परिचालन सीमा को पार कर गया है", "type": "leaf"}
            ]}
        ]
    },
    {
        "keys": ["biogeographical-classification-of-india", "biomes-of-india", "plant-diversity-of-india", "wildlife-diversity-of-india"],
        "en": [
            {"label": "Ten Biogeographic Zones", "type": "branch", "date": "Classification", "children": [
                {"label": "Trans-Himalaya, Himalaya, Desert, Semi-Arid, Western Ghats, Deccan Peninsula, Gangetic Plain, Coast, Northeast, Islands", "type": "leaf"},
                {"label": "Developed by Rodgers and Panwar (WII) to ensure representation of all habitats in Protected Areas", "type": "leaf"}
            ]},
            {"label": "Taxonomic Richness", "type": "branch", "date": "Flora & Fauna", "children": [
                {"label": "Flora of India: Over 45,000 species; high gymnosperm diversity in Himalayan altitudinal zones", "type": "leaf"},
                {"label": "Fauna of India: Over 91,000 species; insects comprise over 70% of animal species richness", "type": "leaf"}
            ]},
            {"label": "Key Biomes in India", "type": "branch", "date": "Biomes", "children": [
                {"label": "Tropical Rainforests: Western Ghats, Northeast, Andaman Islands; high evergreen species richness", "type": "leaf"},
                {"label": "Tropical Deciduous: Most widespread biome in India; dominated by Teak, Sal, and Bamboo", "type": "leaf"},
                {"label": "Thorn Forests: Arid plains of Rajasthan and rain-shadow Deccan; xerophytic vegetation", "type": "leaf"}
            ]},
            {"label": "UPSC Exam Focus", "type": "branch", "date": "UPSC Focus", "children": [
                {"label": "Endemism: e.g. Lion-tailed Macaque (Western Ghats), Sangai Deer (Loktak Lake), Pygmy Hog (Manas)", "type": "leaf"},
                {"label": "ISFR Biennial Report: FSI survey; total forest/tree cover stands at ~24.62% of geographical area", "type": "leaf"}
            ]}
        ],
        "hi": [
            {"label": "दस जैव-भौगोलिक क्षेत्र", "type": "branch", "date": "वर्गीकरण", "children": [
                {"label": "ट्रांस-हिमालय, हिमालय, मरुस्थल, अर्ध-शुष्क, पश्चिमी घाट, दक्कन, गंगा का मैदान, तटीय क्षेत्र, पूर्वोत्तर, द्वीप समूह", "type": "leaf"},
                {"label": "सभी आवासों को संरक्षित क्षेत्रों में शामिल करने के लिए रॉजर्स और पंवार (WII) द्वारा विकसित वर्गीकरण", "type": "leaf"}
            ]},
            {"label": "वर्गीकरण समृद्धि", "type": "branch", "date": "वनस्पति और जंतु", "children": [
                {"label": "भारत की वनस्पतियां: 45,000 से अधिक प्रजातियां; हिमालय के ऊंचाई वाले क्षेत्रों में जिमनोस्पर्म की प्रचुरता", "type": "leaf"},
                {"label": "भारत के जंतु: 91,000 से अधिक प्रजातियां; प्रजातियों की समृद्धि में कीट जंतु जगत का 70% से अधिक हिस्सा हैं", "type": "leaf"}
            ]},
            {"label": "भारत के प्रमुख बायोम", "type": "branch", "date": "बायोम", "children": [
                {"label": "उष्णकटिबंधीय वर्षावन: पश्चिमी घाट, पूर्वोत्तर, अंडमान; उच्च सदाबहार प्रजातियों का घनत्व", "type": "leaf"},
                {"label": "उष्णकटिबंधीय पर्णपाती: भारत में सबसे व्यापक बायोम; सागौन, साल और बांस का प्रभुत्व", "type": "leaf"},
                {"label": "कांटेदार वन: राजस्थान के शुष्क मैदान और दक्कन के वृष्टि-छाया क्षेत्र; मरुद्भिद वनस्पतियां", "type": "leaf"}
            ]},
            {"label": "यूपीएससी परीक्षा दृष्टिकोण", "type": "branch", "date": "परीक्षा", "children": [
                {"label": "स्थानिक प्रजातियां: जैसे लायन-टेल्ड मकाक (पश्चिमी घाट), संगाई हिरण (लोकटक झील), पिग्मी हॉग (मानस)", "type": "leaf"},
                {"label": "ISFR रिपोर्ट: FSI का द्विवार्षिक सर्वेक्षण; कुल वन और वृक्ष आवरण देश के भौगोलिक क्षेत्र का ~24.62% है", "type": "leaf"}
            ]}
        ]
    },
    {
        "keys": ["biogeographical-classification-of-world"],
        "en": [
            {"label": "Eight Biogeographic Realms", "type": "branch", "date": "Realms", "children": [
                {"label": "Nearctic (North America), Palearctic (Europe/North Asia), Afrotropic, Neotropic (South America)", "type": "leaf"},
                {"label": "Indomalayan (South/Southeast Asia), Australasian, Oceanian, Antarctic", "type": "leaf"}
            ]},
            {"label": "Biogeographical Boundaries", "type": "branch", "date": "Boundaries", "children": [
                {"label": "Wallace's Line: Deep water trench separating Indomalayan and Australasian faunal realms in Indonesia", "type": "leaf"},
                {"label": "Explains sharp distinction between placental mammals of Asia and marsupials of Australia", "type": "leaf"}
            ]},
            {"label": "Major Global Biomes", "type": "branch", "date": "Biomes", "children": [
                {"label": "Tropical Rainforests, Taiga (Coniferous), Tundra (Cold Arid), Savanna (Grasslands), Desert", "type": "leaf"},
                {"label": "Regulated by latitude, temperature lapse rates, and precipitation gradients", "type": "leaf"}
            ]},
            {"label": "UPSC Exam Focus", "type": "branch", "date": "UPSC Focus", "children": [
                {"label": "Ecological Equivalents: e.g. Toucans (Neotropic) and Hornbills (Indomalayan) filling same niches", "type": "leaf"},
                {"label": "Sunderbans: World's largest contiguous mangrove forest realm spanning India and Bangladesh", "type": "leaf"}
            ]}
        ],
        "hi": [
            {"label": "आठ जैव-भौगोलिक डोमेन", "type": "branch", "date": "डोमेन", "children": [
                {"label": "निएरक्टिक (उत्तरी अमेरिका), पेलियरक्टिक (यूरोप/उत्तरी एशिया), अफ्रोट्रोपिक, निओट्रोपिक (दक्षिणी अमेरिका)", "type": "leaf"},
                {"label": "इंडोमलयन (दक्षिण/दक्षिण-पूर्व एशिया), ऑस्ट्रेलियन, ओशियनियन, अंटार्कटिक", "type": "leaf"}
            ]},
            {"label": "जैव-भौगोलिक सीमाएं", "type": "branch", "date": "सीमाएं", "children": [
                {"label": "वॉलेस रेखा (Wallace's Line): इंडोनेशिया में इंडोमलयन और ऑस्ट्रेलियन जीव क्षेत्रों को अलग करने वाली गहरी समुद्री खाई", "type": "leaf"},
                {"label": "यह स्पष्ट करती है कि क्यों एशियाई प्लेसेंटल स्तनधारी प्राकृतिक रूप से ऑस्ट्रेलियाई मार्सुपियल क्षेत्रों में नहीं जाते", "type": "leaf"}
            ]},
            {"label": "प्रमुख वैश्विक बायोम", "type": "branch", "date": "बायोम", "children": [
                {"label": "उष्णकटिबंधीय वर्षावन, टैगा (शंकुधारी), टुंड्रा (शीत मरुस्थल), सवाना (घास के मैदान), मरुस्थल", "type": "leaf"},
                {"label": "अक्षांश, ऊंचाई के तापमान ह्रास दर और वर्षा प्रवणता द्वारा नियंत्रित होते हैं", "type": "leaf"}
            ]},
            {"label": "यूपीएससी परीक्षा दृष्टिकोण", "type": "branch", "date": "परीक्षा", "children": [
                {"label": "पारिस्थितिक समतुल्य: जैसे निओट्रोपिक्स में टूकेन (Toucans) और इंडोमलयन क्षेत्र में हॉर्नबिल (Hornbills)", "type": "leaf"},
                {"label": "सुंदरवन: भारत और बांग्लादेश में फैला दुनिया का सबसे बड़ा निरंतर मैंग्रोव वन क्षेत्र", "type": "leaf"}
            ]}
        ]
    },
    {
        "keys": ["biosphere-reserves", "world-heritage", "geo-heritage"],
        "en": [
            {"label": "Biosphere Reserves (UNESCO)", "type": "branch", "date": "BR Structure", "children": [
                {"label": "Core: Strictly protected under WPA; Buffer: Limited research/tourism; Transition: Sustainable agriculture/settlements", "type": "leaf"},
                {"label": "UNESCO Man and Biosphere (MAB): 12 of India's 18 biosphere reserves are in global MAB network (e.g. Panna added 2020)", "type": "leaf"}
            ]},
            {"label": "World Heritage Sites", "type": "branch", "date": "Heritage Sites", "children": [
                {"label": "UNESCO World Heritage Convention 1972: Protects sites of outstanding universal cultural/natural value", "type": "leaf"},
                {"label": "Natural Sites in India: Great Himalayan NP, Kaziranga, Keoladeo, Manas, Nanda Devi, Sundarbans, Western Ghats", "type": "leaf"},
                {"label": "Mixed Site: Khangchendzonga National Park (Manipur/Sikkim) is India's only mixed heritage site", "type": "leaf"}
            ]},
            {"label": "Geo-Heritage Sites", "type": "branch", "date": "Geo-Heritage", "children": [
                {"label": "Definition: Geological features or landforms representing earth's evolutionary history, managed by GSI", "type": "leaf"},
                {"label": "Key Sites: Lonar Lake (basaltic impact crater), Akal Wood Fossil Park (Jurassic wood fossils in Jaisalmer)", "type": "leaf"}
            ]},
            {"label": "UPSC Exam Focus", "type": "branch", "date": "UPSC Focus", "children": [
                {"label": "Map locations: Matching biosphere reserves and national parks to their geographic states", "type": "leaf"},
                {"label": "Biodiversity Heritage Sites (BHS): Declared under Biological Diversity Act 2002 (e.g. Majuli, Nallur)", "type": "leaf"}
            ]}
        ],
        "hi": [
            {"label": "बायोस्फीयर रिजर्व (UNESCO)", "type": "branch", "date": "संरचना", "children": [
                {"label": "कोर: WPA के तहत पूर्ण सुरक्षित; बफर: सीमित पर्यटन/अनुसंधान; संक्रमण: मानव बस्तियां और टिकाऊ खेती", "type": "leaf"},
                {"label": "यूनेस्को MAB कार्यक्रम: भारत के 18 में से 12 बायोस्फीयर रिजर्व इस वैश्विक नेटवर्क में शामिल हैं (जैसे पन्ना 2020)", "type": "leaf"}
            ]},
            {"label": "विश्व धरोहर स्थल", "type": "branch", "date": "धरोहर", "children": [
                {"label": "यूनेस्को कन्वेंशन 1972: सांस्कृतिक/प्राकृतिक रूप से असाधारण वैश्विक मूल्य वाले स्थलों का संरक्षण", "type": "leaf"},
                {"label": "भारत के प्राकृतिक स्थल: महान हिमालयी राष्ट्रीय उद्यान, काजीरंगा, केवलादेव, मानस, नंदा देवी, सुंदरवन, पश्चिमी घाट", "type": "leaf"},
                {"label": "मिश्रित स्थल: कंचनजंगा राष्ट्रीय उद्यान (सिक्किम) भारत का एकमात्र मिश्रित धरोहर स्थल है", "type": "leaf"}
            ]},
            {"label": "भू-विरासत स्थल (Geo-Heritage)", "type": "branch", "date": "भू-विरासत", "children": [
                {"label": "परिभाषा: भारतीय भूवैज्ञानिक सर्वेक्षण (GSI) द्वारा संरक्षित पृथ्वी के भूवैज्ञानिक इतिहास को दर्शाने वाले स्थल", "type": "leaf"},
                {"label": "प्रमुख स्थल: लोनार झील (बेसाल्टिक प्रभाव गड्ढा), अकल वुड फॉसिल पार्क (जैसलमेर में जुरासिक जीवाश्म)", "type": "leaf"}
            ]},
            {"label": "यूपीएससी परीक्षा दृष्टिकोण", "type": "branch", "date": "परीक्षा", "children": [
                {"label": "मानचित्र अभ्यास: बायोस्फीयर रिजर्व और राष्ट्रीय उद्यानों को उनके संबंधित राज्यों से सुमेलित करना", "type": "leaf"},
                {"label": "जैव विविधता विरासत स्थल (BHS): जैव विविधता अधिनियम 2002 के तहत घोषित स्थल (जैसे माजुली द्वीप, नल्लूर इमली उपवन)", "type": "leaf"}
            ]}
        ]
    },
    {
        "keys": ["botanical-gardens", "zoological-parks", "seed-banks"],
        "en": [
            {"label": "Botanical Gardens", "type": "branch", "date": "Botanical", "children": [
                {"label": "Definition: Controlled collections of living plants outside natural habitats for taxonomy and conservation", "type": "leaf"},
                {"label": "AJC Bose Indian Botanic Garden (Howrah): Famous for the Great Banyan Tree (>250 years old)", "type": "leaf"},
                {"label": "Arboretum: Specialized botanical garden focused exclusively on cultivating woody trees and shrubs", "type": "leaf"}
            ]},
            {"label": "Zoological Parks", "type": "branch", "date": "Zoological", "children": [
                {"label": "Definition: Enclosures where living wild animals are kept for public exhibition, education, and captive breeding", "type": "leaf"},
                {"label": "Central Zoo Authority (CZA): Statutory body under WPA 1972 regulating zoo standards in India", "type": "leaf"}
            ]},
            {"label": "Seed & Gene Banks", "type": "branch", "date": "Gene Banks", "children": [
                {"label": "Maintains biological backup of crop seeds and wild relatives under controlled low moisture and temperature", "type": "leaf"},
                {"label": "Svalbard Global Seed Vault (Norway): Global seed backup facility built deep in Arctic permafrost", "type": "leaf"}
            ]},
            {"label": "UPSC Exam Focus", "type": "branch", "date": "UPSC Focus", "children": [
                {"label": "Distinction: Botanical gardens and zoos are ex-situ (off-site); gene sanctuaries are in-situ (on-site)", "type": "leaf"},
                {"label": "Role of BGCI (Botanic Gardens Conservation International) in coordinating plant conservation", "type": "leaf"}
            ]}
        ],
        "hi": [
            {"label": "वनस्पति उद्यान (Botanical Gardens)", "type": "branch", "date": "वनस्पति", "children": [
                {"label": "परिभाषा: वर्गीकरण और संरक्षण के लिए प्राकृतिक आवास से बाहर जीवित पौधों का नियंत्रित संग्रह", "type": "leaf"},
                {"label": "AJC बोस भारतीय वनस्पति उद्यान (हावड़ा): द ग्रेट बरगद वृक्ष (>250 वर्ष पुराना) के लिए प्रसिद्ध", "type": "leaf"},
                {"label": "आर्बोरेटम (Arboretum): केवल लकड़ीदार पेड़ों और झाड़ियों की खेती पर केंद्रित वनस्पति उद्यान", "type": "leaf"}
            ]},
            {"label": "प्राणी उद्यान (चिड़ियाघर)", "type": "branch", "date": "प्राणी उद्यान", "children": [
                {"label": "परिभाषा: सार्वजनिक प्रदर्शन, शिक्षा और बंदी प्रजनन के लिए जीवित जंगली जानवरों का परिसर", "type": "leaf"},
                {"label": "केंद्रीय चिड़ियाघर प्राधिकरण (CZA): WPA 1972 के तहत स्थापित वैधानिक निकाय जो चिड़ियाघरों को नियंत्रित करता है", "type": "leaf"}
            ]},
            {"label": "बीज और जीन बैंक", "type": "branch", "date": "जीन बैंक", "children": [
                {"label": "नियंत्रित कम आर्द्रता और तापमान पर फसलों के बीजों और उनके जंगली रिश्तेदारों का आनुवंशिक बैकअप", "type": "leaf"},
                {"label": "स्वालबार्ड ग्लोबल सीड वॉल्ट (नार्वे): आर्कटिक पर्माफ्रॉस्ट में निर्मित वैश्विक बीज बैकअप सुविधा", "type": "leaf"}
            ]},
            {"label": "यूपीएससी परीक्षा दृष्टिकोण", "type": "branch", "date": "परीक्षा", "children": [
                {"label": "अंतर: वनस्पति उद्यान और चिड़ियाघर बाह्य-स्थाने (ex-situ) हैं; जीन अभयारण्य स्व-स्थाने (in-situ) होते हैं", "type": "leaf"},
                {"label": "पौधों के संरक्षण के समन्वय में BGCI (बोटेनिक गार्डन्स कंजर्वेशन इंटरनेशनल) की भूमिका", "type": "leaf"}
            ]}
        ]
    },
    {
        "keys": ["national-parks", "wildlife-sanctuaries", "protected-area", "forms-of-protected"],
        "en": [
            {"label": "National Parks (IUCN Cat II)", "type": "branch", "date": "National Parks", "children": [
                {"label": "Declared under WPA 1972; absolute protection, no resource exploitation or livestock grazing permitted", "type": "leaf"},
                {"label": "Boundaries are fixed by legislation; cannot be altered without National Board for Wildlife (NBWL) approval", "type": "leaf"}
            ]},
            {"label": "Wildlife Sanctuaries (IUCN Cat IV)", "type": "branch", "date": "Sanctuaries", "children": [
                {"label": "Declared under WPA 1972; allows certain limited human activities (e.g. firewood collection, cattle grazing)", "type": "leaf"},
                {"label": "Focused on protecting a particular species or group of species; boundaries are relatively flexible", "type": "leaf"}
            ]},
            {"label": "Conservation & Community Reserves", "type": "branch", "date": "Reserves", "children": [
                {"label": "Conservation Reserves: Declared on government land adjacent to national parks to act as migratory corridors", "type": "leaf"},
                {"label": "Community Reserves: Declared on private/community land where local people volunteer to protect species and culture", "type": "leaf"}
            ]},
            {"label": "UPSC Exam Focus", "type": "branch", "date": "UPSC Focus", "children": [
                {"label": "Protected Area (PA) Network: Covers ~5.26% of India's geographical area under Wildlife Protection Act", "type": "leaf"},
                {"label": "Marine Protected Areas (MPAs): e.g. Gulf of Mannar, Gulf of Kutch Marine NP, Malvan Marine Sanctuary", "type": "leaf"}
            ]}
        ],
        "hi": [
            {"label": "राष्ट्रीय उद्यान (IUCN श्रेणी II)", "type": "branch", "date": "राष्ट्रीय उद्यान", "children": [
                {"label": "WPA 1972 के तहत घोषित; पूर्ण सुरक्षा, किसी भी संसाधन दोहन या मवेशी चराई की अनुमति नहीं", "type": "leaf"},
                {"label": "सीमाएं कानून द्वारा तय होती हैं; राष्ट्रीय वन्यजीव बोर्ड (NBWL) की अनुमति के बिना सीमा बदलाव संभव नहीं", "type": "leaf"}
            ]},
            {"label": "वन्यजीव अभयारण्य (IUCN श्रेणी IV)", "type": "branch", "date": "अभयारण्य", "children": [
                {"label": "WPA 1972 के तहत घोषित; स्थानीय लोगों को सीमित गतिविधियों (लकड़ी एकत्र करना, पशु चराना) की अनुमति", "type": "leaf"},
                {"label": "किसी विशेष प्रजाति के संरक्षण पर केंद्रित होता है; सीमाएं राष्ट्रीय उद्यानों की तुलना में अधिक लचीली होती हैं", "type": "leaf"}
            ]},
            {"label": "संरक्षण और सामुदायिक रिजर्व", "type": "branch", "date": "रिजर्व", "children": [
                {"label": "संरक्षण रिजर्व: राष्ट्रीय उद्यानों के निकट गलियारे के रूप में कार्य करने के लिए सरकारी भूमि पर घोषित", "type": "leaf"},
                {"label": "सामुदायिक रिजर्व: निजी/सामुदायिक भूमि पर घोषित जहां स्थानीय लोग वन्यजीवों की रक्षा का संकल्प लेते हैं", "type": "leaf"}
            ]},
            {"label": "यूपीएससी परीक्षा दृष्टिकोण", "type": "branch", "date": "परीक्षा", "children": [
                {"label": "संरक्षित क्षेत्र नेटवर्क: भारत के भौगोलिक क्षेत्र का लगभग 5.26% भाग WPA के तहत कवर करता है", "type": "leaf"},
                {"label": "समुद्री संरक्षित क्षेत्र (MPAs): जैसे मन्नार की खाड़ी, कच्छ की खाड़ी मरीन NP, मालवन अभयारण्य", "type": "leaf"}
            ]}
        ]
    },
    {
        "keys": ["wildlife-protection-act", "wpa-1972", "scheduled-animals"],
        "en": [
            {"label": "Legislative Landscape", "type": "branch", "date": "Overview", "children": [
                {"label": "Enacted in 1972 to protect wild animals, birds, and plants; extends to whole of India", "type": "leaf"},
                {"label": "Empowers declaration of Protected Areas (National Parks, Sanctuaries) by state governments", "type": "leaf"}
            ]},
            {"label": "Schedules Structure", "type": "branch", "date": "Schedules", "children": [
                {"label": "Schedule I: Absolute protection; highest penalties for hunting/trade (e.g., Tiger, Snow Leopard)", "type": "leaf"},
                {"label": "Schedule II: High protection; slightly lower penalties but strictly prohibited (e.g., King Cobra)", "type": "leaf"},
                {"label": "Schedule III & IV (Historical): Protected species; 2022 Amendment consolidated schedules from 6 to 4", "type": "leaf"}
            ]},
            {"label": "2022 Amendment Acts", "type": "branch", "date": "Amendments", "children": [
                {"label": "Consolidated Schedules: Reduced from 6 to 4 schedules; Schedule III is for protected plants; Schedule IV for CITES list", "type": "leaf"},
                {"label": "Secures management of invasive alien species; regulates export/import under CITES provisions", "type": "leaf"}
            ]},
            {"label": "UPSC Exam Focus", "type": "branch", "date": "UPSC Focus", "children": [
                {"label": "National Board for Wildlife (NBWL): Chaired by Prime Minister; approves boundary changes of Protected Areas", "type": "leaf"},
                {"label": "Vermin status: Only Central Government can declare a wild animal as vermin for a specific area/period", "type": "leaf"}
            ]}
        ],
        "hi": [
            {"label": "विधायी मील का पत्थर", "type": "branch", "date": "परिचय", "children": [
                {"label": "वन्य जीवों, पक्षियों और पौधों की रक्षा के लिए 1972 में अधिनियमित; पूरे भारत में लागू", "type": "leaf"},
                {"label": "राज्य सरकारों द्वारा संरक्षित क्षेत्रों (राष्ट्रीय उद्यान, अभयारण्य) की घोषणा को अधिकृत करता है", "type": "leaf"}
            ]},
            {"label": "अनुसूचियों की संरचना", "type": "branch", "date": "अनुसूचियां", "children": [
                {"label": "अनुसूची I: पूर्ण सुरक्षा; शिकार/व्यापार के लिए उच्चतम दंड का प्रावधान (जैसे बाघ, हिम तेंदुआ)", "type": "leaf"},
                {"label": "अनुसूची II: उच्च सुरक्षा; थोड़े कम दंड लेकिन शिकार पूर्णतः प्रतिबंधित (जैसे किंग कोबरा)", "type": "leaf"},
                {"label": "अनुसूची III और IV (ऐतिहासिक): संरक्षित प्रजातियां; 2022 के संशोधन ने अनुसूचियों को 6 से घटाकर 4 कर दिया", "type": "leaf"}
            ]},
            {"label": "2022 संशोधन अधिनियम", "type": "branch", "date": "संशोधन", "children": [
                {"label": "समेकित अनुसूचियाँ: अनुसूचियों को घटाकर 4 किया; अनुसूची III पौधों के लिए; अनुसूची IV CITES सूची के लिए", "type": "leaf"},
                {"label": "आक्रामक विदेशी प्रजातियों के प्रबंधन को सुरक्षित करता है; CITES के प्रावधानों के तहत निर्यात/आयात को नियंत्रित करता है", "type": "leaf"}
            ]},
            {"label": "यूपीएससी परीक्षा दृष्टिकोण", "type": "branch", "date": "यूपीएससी", "children": [
                {"label": "राष्ट्रीय वन्यजीव बोर्ड (NBWL): प्रधान मंत्री की अध्यक्षता में; संरक्षित क्षेत्रों की सीमा परिवर्तनों को मंजूरी देता है", "type": "leaf"},
                {"label": "वर्मिन (Vermin) स्थिति: केवल केंद्र सरकार ही किसी जंगली जानवर को एक विशिष्ट क्षेत्र/अवधि के लिए वर्मिन घोषित कर सकती है", "type": "leaf"}
            ]}
        ]
    },
    {
        "keys": ["iucn", "red-list"],
        "en": [
            {"label": "IUCN Structure", "type": "branch", "date": "Structure", "children": [
                {"label": "Founded in 1948 in Fontainebleau, France; headquarters in Gland, Switzerland", "type": "leaf"},
                {"label": "Unique union of government and NGO civil society members (not a UN agency)", "type": "leaf"}
            ]},
            {"label": "Red List Classification Scheme", "type": "branch", "date": "Red List", "children": [
                {"label": "Extinct (EX) & Extinct in Wild (EW); Critically Endangered (CR), Endangered (EN)", "type": "leaf"},
                {"label": "Vulnerable (VU), Near Threatened (NT), Least Concern (LC), Data Deficient (DD)", "type": "leaf"}
            ]},
            {"label": "Quantitative Criteria for CR", "type": "branch", "date": "CR Criteria", "children": [
                {"label": "Population reduction: >90% decline over 10 years or 3 generations", "type": "leaf"},
                {"label": "Geographic range restriction: Area of occupancy <10 sq km or extent of occurrence <100 sq km", "type": "leaf"},
                {"label": "Extinction probability: Quantitative analysis shows >50% chance of extinction in wild within 10 years", "type": "leaf"}
            ]},
            {"label": "UPSC Exam Focus", "type": "branch", "date": "UPSC Focus", "children": [
                {"label": "Pink Pages: Published in Red Data Book to represent critically endangered species", "type": "leaf"},
                {"label": "Green Status of Species: Measures species recovery progress and conservation impact relative to historic levels", "type": "leaf"}
            ]}
        ],
        "hi": [
            {"label": "IUCN संरचना", "type": "branch", "date": "संरचना", "children": [
                {"label": "1948 में फ्रांस के फॉनटेनब्लो में स्थापित; मुख्यालय ग्लैंड, स्विट्जरलैंड में है", "type": "leaf"},
                {"label": "सरकारी और नागरिक समाज सदस्य संगठनों का एक अनूठा संघ (संयुक्त राष्ट्र की एजेंसी नहीं)", "type": "leaf"}
            ]},
            {"label": "रेड लिस्ट वर्गीकरण योजना", "type": "branch", "date": "वर्गीकरण", "children": [
                {"label": "विलुप्त (EX) और जंगल से विलुप्त (EW); गंभीर रूप से लुप्तप्राय (CR), लुप्तप्राय (EN)", "type": "leaf"},
                {"label": "संवेदनशील (VU), संकट-निकट (NT), संकटमुक्त (LC), डेटा की कमी (DD)", "type": "leaf"}
            ]},
            {"label": "CR श्रेणी के मात्रात्मक मानदंड", "type": "branch", "date": "CR मानदंड", "children": [
                {"label": "आबादी में गिरावट: 10 वर्षों या 3 पीढ़ियों के भीतर आबादी में >90% की गिरावट", "type": "leaf"},
                {"label": "भौगोलिक सीमा का संकुचन: निवास क्षेत्र <10 वर्ग किमी या कुल प्रसार क्षेत्र <100 वर्ग किमी हो", "type": "leaf"},
                {"label": "विलुप्ति की संभावना: वैज्ञानिक विश्लेषण 10 वर्षों में जंगलों से विलुप्त होने की >50% संभावना दर्शाता है", "type": "leaf"}
            ]},
            {"label": "यूपीएससी परीक्षा दृष्टिकोण", "type": "branch", "date": "परीक्षा", "children": [
                {"label": "गुलाबी पन्ने (Pink Pages): गंभीर रूप से संकटग्रस्त प्रजातियों को दर्शाने के लिए रेड डाटा बुक में प्रकाशित", "type": "leaf"},
                {"label": "हरित स्थिति (Green Status): मानव प्रभाव से पूर्व के स्तर के सापेक्ष प्रजाति बहाली और संरक्षण प्रभाव मापन", "type": "leaf"}
            ]}
        ]
    },
    {
        "keys": ["marine", "coastal", "mammals", "dugong"],
        "en": [
            {"label": "Marine Mammal Groups", "type": "branch", "date": "Groups", "children": [
                {"label": "Cetacea: Whales, dolphins, porpoises; fully aquatic, undergo horizontal tail stroke", "type": "leaf"},
                {"label": "Sirenia: Dugongs (sea cows) and manatees; strictly herbivorous, shallow coastal dwellers", "type": "leaf"},
                {"label": "Pinnipedia: Seals, sea lions, and walruses; semi-aquatic mammals with flippers", "type": "leaf"}
            ]},
            {"label": "Key Species in India", "type": "branch", "date": "India Species", "children": [
                {"label": "Dugong (Dugong dugon): Vulnerable; feeds exclusively on seagrass in Gulf of Mannar and Palk Bay", "type": "leaf"},
                {"label": "Irrawaddy Dolphin: Found in Chilika Lake (Odisha); brackish water indicator species", "type": "leaf"}
            ]},
            {"label": "Marine Biodiversity Threats", "type": "branch", "date": "Threats", "children": [
                {"label": "Commercial Trawling: Bottom trawling destroys benthic communities and seagrass meadows", "type": "leaf"},
                {"label": "Bycatch: Entanglement in commercial gillnets leading to drowning of dolphins and dugongs", "type": "leaf"}
            ]},
            {"label": "UPSC Exam Focus", "type": "branch", "date": "UPSC Focus", "children": [
                {"label": "Dugong Conservation Reserve: Established in Palk Bay (Tamil Nadu) to protect seagrass habitats", "type": "leaf"},
                {"label": "Ganges River Dolphin: National Aquatic Animal of India; blind mammal utilizing echolocation (Susu)", "type": "leaf"}
            ]}
        ],
        "hi": [
            {"label": "समुद्री स्तनधारी समूह", "type": "branch", "date": "वर्ग", "children": [
                {"label": "सिटेशिया: व्हेल, डॉल्फ़िन; पूर्णतः जलीय, पूंछ की क्षैतिज गतियों का उपयोग करते हैं", "type": "leaf"},
                {"label": "साइरेनिया: डगोंग (समुद्री गाय) और मैनेट; विशुद्ध रूप से शाकाहारी, उथले तटों के निवासी", "type": "leaf"},
                {"label": "पिनिपेडिया: सील, सी लॉयन; फ्लिपर्स वाले अर्ध-जलीय स्तनधारी", "type": "leaf"}
            ]},
            {"label": "भारत की प्रमुख प्रजातियाँ", "type": "branch", "date": "भारत की प्रजातियां", "children": [
                {"label": "डगोंग (Dugong dugon): संवेदनशील (VU); मन्नार की खाड़ी और पाक खाड़ी में समुद्री घास खाता है", "type": "leaf"},
                {"label": "इरावदी डॉल्फ़िन: चिल्का झील (ओडिशा) में पाई जाती है; खारे पानी की संकेतक प्रजाति", "type": "leaf"}
            ]},
            {"label": "समुद्री जैव विविधता को खतरे", "type": "branch", "date": "खतरे", "children": [
                {"label": "व्यावसायिक मछली पकड़ना (Bottom Trawling): समुद्र के तलछटों और समुद्री घास के मैदानों को नष्ट करता है", "type": "leaf"},
                {"label": "बायकैच (Bycatch): वाणिज्यिक जालों में दुर्घटनावश फंसकर डॉल्फ़िन और डगोंग की दम घुटने से मौत होना", "type": "leaf"}
            ]},
            {"label": "यूपीएससी परीक्षा दृष्टिकोण", "type": "branch", "date": "परीक्षा", "children": [
                {"label": "डगोंग संरक्षण रिजर्व: समुद्री घास के आवासों की सुरक्षा के लिए तमिलनाडु की पाक खाड़ी में स्थापित", "type": "leaf"},
                {"label": "गंगा डॉल्फ़िन: भारत का राष्ट्रीय जलीय जीव; सूँस (Susu) नाम से प्रसिद्ध, शिकार के लिए प्रतिध्वनि का उपयोग", "type": "leaf"}
            ]}
        ]
    },
    {
        "keys": ["marsupials"],
        "en": [
            {"label": "Marsupial Anatomy", "type": "branch", "date": "Anatomy", "children": [
                {"label": "Pouched Mammals: Give birth to highly underdeveloped young that crawl into a pouch (marsupium)", "type": "leaf"},
                {"label": "Short gestation period: Lack complex placenta; embryo is nourished by yolk sac inside uterus", "type": "leaf"}
            ]},
            {"label": "Representative Species", "type": "branch", "date": "Species", "children": [
                {"label": "Red Kangaroo & Koala: Famous Australian herbivores; Koalas feed exclusively on Eucalyptus leaves", "type": "leaf"},
                {"label": "Tasmanian Devil: Largest surviving carnivorous marsupial, native to the island state of Tasmania", "type": "leaf"}
            ]},
            {"label": "Biogeographical Evolution", "type": "branch", "date": "Evolution", "children": [
                {"label": "Evolved in Gondwana; isolated in Australia when the continent broke away from Antarctica", "type": "leaf"},
                {"label": "Convergent Evolution: Developed similar forms to placental mammals (e.g., Marsupial Mole vs Placental Mole)", "type": "leaf"}
            ]},
            {"label": "UPSC Exam Focus", "type": "branch", "date": "UPSC Focus", "children": [
                {"label": "Marsupial vs Monotreme: Marsupials give birth to live young (tiny embryos); monotremes lay eggs", "type": "leaf"},
                {"label": "Threats: Introduction of placental predators (foxes, feral cats) in Australia caused massive marsupial declines", "type": "leaf"}
            ]}
        ],
        "hi": [
            {"label": "मार्सुपियल शरीर रचना", "type": "branch", "date": "शरीर रचना", "children": [
                {"label": "थैलीदार स्तनधारी: अत्यधिक अविकसित बच्चों को जन्म देते हैं जो रेंगकर पेट की थैली (Marsupium) में जाते हैं", "type": "leaf"},
                {"label": "लघु गर्भकाल: जटिल प्लेसेंटा का अभाव; भ्रूण को गर्भाशय के भीतर जर्दी थैली (Yolk sac) से पोषण मिलता है", "type": "leaf"}
            ]},
            {"label": "प्रतिनिधि प्रजातियां", "type": "branch", "date": "प्रजातियां", "children": [
                {"label": "लाल कंगारू और कोआला: प्रसिद्ध ऑस्ट्रेलियाई शाकाहारी जीव; कोआला केवल नीलगिरी की पत्तियां खाते हैं", "type": "leaf"},
                {"label": "तस्मानियन डेविल: सबसे बड़ा जीवित मांसाहारी मार्सुपियल, जो ऑस्ट्रेलिया के तस्मानिया द्वीप का मूल निवासी है", "type": "leaf"}
            ]},
            {"label": "जैव-भौगोलिक विकास", "type": "branch", "date": "विकास", "children": [
                {"label": "गोंडवाना में विकसित हुए; जब ऑस्ट्रेलियाई महाद्वीप अंटार्कटिका से अलग हुआ तो वहां इनका एकांत विकास हुआ", "type": "leaf"},
                {"label": "समानांतर विकास (Convergent Evolution): प्लेसेंटल स्तनधारियों के समान रूपों का विकास (जैसे मार्सुपियल मोल बनाम प्लेसेंटल मोल)", "type": "leaf"}
            ]},
            {"label": "यूपीएससी परीक्षा दृष्टिकोण", "type": "branch", "date": "परीक्षा", "children": [
                {"label": "मार्सुपियल बनाम मोनोट्रीम: मार्सुपियल छोटे बच्चों को जन्म देते हैं; मोनोट्रीम अंडे देते हैं", "type": "leaf"},
                {"label": "खतरे: ऑस्ट्रेलिया में प्लेसेंटल शिकारियों (लोमड़ी, जंगली बिल्लियां) के प्रवेश से कई मार्सुपियल विलुप्त हो गए", "type": "leaf"}
            ]}
        ]
    },
    {
        "keys": ["egg-laying"],
        "en": [
            {"label": "Monotremes Characteristics", "type": "branch", "date": "Monotremes", "children": [
                {"label": "Oviparous Mammals: Lay soft-shelled eggs instead of giving birth to live young, yet possess mammary glands", "type": "leaf"},
                {"label": "Cloaca present: Single common opening for digestive, excretory, and reproductive tracts (like reptiles)", "type": "leaf"},
                {"label": "Lack nipples: Milk is secreted onto skin surface/fur from modified sweat glands for young to lap", "type": "leaf"}
            ]},
            {"label": "Extant Species", "type": "branch", "date": "Species", "children": [
                {"label": "Platypus (Ornithorhynchus anatinus): Semi-aquatic, duck-billed, venomous mammal endemic to eastern Australia", "type": "leaf"},
                {"label": "Echidnas (Spiny Anteaters): Four species under Tachyglossidae; covered in spines, feed on ants/termites", "type": "leaf"}
            ]},
            {"label": "Evolutionary Significance", "type": "branch", "date": "Evolution", "children": [
                {"label": "Represent evolutionary link between therapsid reptiles and modern placental mammals", "type": "leaf"},
                {"label": "Retain primitive endothermy (lower and more fluctuating body temperature than other mammals)", "type": "leaf"}
            ]},
            {"label": "UPSC Exam Focus", "type": "branch", "date": "UPSC Focus", "children": [
                {"label": "Venom apparatus: Male Platypus has calcaneus spurs on hind limbs delivering painful non-lethal venom", "type": "leaf"},
                {"label": "Geographical distribution: Monotremes are exclusively endemic to Australia and New Guinea", "type": "leaf"}
            ]}
        ],
        "hi": [
            {"label": "मोनोट्रीम्स की विशेषताएं", "type": "branch", "date": "मोनोट्रीम्स", "children": [
                {"label": "अंडज स्तनधारी (Oviparous Mammals): जीवित बच्चों को जन्म देने के बजाय अंडे देते हैं, लेकिन इनमें स्तन ग्रंथियां होती हैं", "type": "leaf"},
                {"label": "क्लोअका (Cloaca) उपस्थित: पाचन, उत्सर्जन और प्रजनन पथ के लिए एक ही साझा मार्ग (सरीसृपों की तरह)", "type": "leaf"},
                {"label": "निप्पल (स्तनाग्र) का अभाव: दूध त्वचा की सतह/रोमों पर स्रावित होता है जिसे बच्चे चाटते हैं", "type": "leaf"}
            ]},
            {"label": "जीवित प्रजातियां", "type": "branch", "date": "प्रजातियां", "children": [
                {"label": "प्लैटिपस (Platypus): पूर्वी ऑस्ट्रेलिया के स्थानिक, बतख जैसी चोंच वाले, अर्ध-जलीय और जहरीले स्तनधारी", "type": "leaf"},
                {"label": "एकिडना (कांटेदार चींटीखोर): चार प्रजातियां; कांटों से ढके होते हैं और चींटियों/दीमकों को खाते हैं", "type": "leaf"}
            ]},
            {"label": "विकासवादी महत्व", "type": "branch", "date": "विकास", "children": [
                {"label": "थेरैप्सिड सरीसृपों और आधुनिक प्लेसेंटल स्तनधारियों के बीच विकासवादी कड़ी का प्रतिनिधित्व करते हैं", "type": "leaf"},
                {"label": "इनका शरीर का तापमान अन्य स्तनधारियों की तुलना में कम और अधिक उतार-चढ़ाव वाला होता है", "type": "leaf"}
            ]},
            {"label": "यूपीएससी परीक्षा दृष्टिकोण", "type": "branch", "date": "परीक्षा", "children": [
                {"label": "विष उपकरण: नर प्लैटिपस के पिछले अंगों पर जहरीले कांटे होते हैं जो अत्यधिक दर्दनाक जहर का स्राव करते हैं", "type": "leaf"},
                {"label": "भौगोलिक वितरण: मोनोट्रीम विशेष रूप से केवल ऑस्ट्रेलिया और न्यू गिनी के स्थानिक हैं", "type": "leaf"}
            ]}
        ]
    },
    {
        "keys": ["biopiracy"],
        "en": [
            {"label": "Definition & Mechanics", "type": "branch", "date": "Concept", "children": [
                {"label": "Commercial exploitation of indigenous biological resources and traditional knowledge without consent or compensation", "type": "leaf"},
                {"label": "Involves filing patents on natural products, gene sequences, or traditional uses (e.g., Neem, Turmeric)", "type": "leaf"}
            ]},
            {"label": "Historic Cases (India)", "type": "branch", "date": "Cases", "children": [
                {"label": "Turmeric Patent: US patent on wound-healing properties of turmeric successfully revoked by CSIR (1997)", "type": "leaf"},
                {"label": "Neem Patent: European patent on fungicidal properties of neem oil revoked after legal battle by India (2000)", "type": "leaf"},
                {"label": "Basmati Rice: US patent granted to RiceTec on Basmati lines challenged and partially revoked by India", "type": "leaf"}
            ]},
            {"label": "Defensive Measures", "type": "branch", "date": "Defense", "children": [
                {"label": "Traditional Knowledge Digital Library (TKDL): Database of traditional Indian medicine (Ayurveda, Unani, Siddha) to prevent wrongful patents", "type": "leaf"},
                {"label": "Biological Diversity Act 2002: Mandates National Biodiversity Authority approval for all patent applications using Indian biological resources", "type": "leaf"}
            ]},
            {"label": "UPSC Exam Focus", "type": "branch", "date": "UPSC Focus", "children": [
                {"label": "Nagoya Protocol: International treaty under CBD establishing binding Access and Benefit-Sharing (ABS) regulations", "type": "leaf"},
                {"label": "TRIPS Agreement: WTO intellectual property rules; conflict with CBD on traditional knowledge protection", "type": "leaf"}
            ]}
        ],
        "hi": [
            {"label": "परिभाषा और तंत्र", "type": "branch", "date": "अवधारणा", "children": [
                {"label": "सहमति या मुआवजे के बिना स्वदेशी जैविक संसाधनों और पारंपरिक ज्ञान का व्यावसायिक शोषण", "type": "leaf"},
                {"label": "प्राकृतिक उत्पादों, जीन अनुक्रमों या पारंपरिक उपयोगों (जैसे नीम, हल्दी) पर पेटेंट दाखिल करना शामिल है", "type": "leaf"}
            ]},
            {"label": "ऐतिहासिक मामले (भारत)", "type": "branch", "date": "मामले", "children": [
                {"label": "हल्दी पेटेंट: हल्दी के घाव भरने वाले गुणों पर अमेरिकी पेटेंट को CSIR द्वारा सफलतापूर्वक रद्द कराया गया (1997)", "type": "leaf"},
                {"label": "नीम पेटेंट: नीम के तेल के कवकनाशी गुणों पर यूरोपीय पेटेंट को भारत द्वारा कानूनी लड़ाई के बाद रद्द कराया गया (2000)", "type": "leaf"},
                {"label": "बासमती चावल: राइसटेक को बासमती लाइनों पर दिए गए अमेरिकी पेटेंट को भारत ने चुनौती दी और आंशिक रूप से रद्द कराया", "type": "leaf"}
            ]},
            {"label": "रक्षात्मक उपाय", "type": "branch", "date": "सुरक्षा", "children": [
                {"label": "पारंपरिक ज्ञान डिजिटल लाइब्रेरी (TKDL): गलत पेटेंट को रोकने के लिए पारंपरिक भारतीय चिकित्सा प्रणालियों का डेटाबेस", "type": "leaf"},
                {"label": "जैव विविधता अधिनियम 2002: भारतीय जैविक संसाधनों का उपयोग करने वाले सभी पेटेंट आवेदनों के लिए राष्ट्रीय जैव विविधता प्राधिकरण (NBA) की मंजूरी अनिवार्य करता है", "type": "leaf"}
            ]},
            {"label": "यूपीएससी परीक्षा दृष्टिकोण", "type": "branch", "date": "परीक्षा", "children": [
                {"label": "नागोया प्रोटोकॉल: CBD के तहत अंतरराष्ट्रीय संधि जो बाध्यकारी एक्सेस एंड बेनिफिट-शेयरिंग (ABS) नियमों को स्थापित करती है", "type": "leaf"},
                {"label": "TRIPS समझौता: WTO के बौद्धिक संपदा नियम; पारंपरिक ज्ञान के संरक्षण पर CBD के साथ संघर्ष", "type": "leaf"}
            ]}
        ]
    },
    {
        "keys": ["bioinformatics"],
        "en": [
            {"label": "Biological Databases", "type": "branch", "date": "Databases", "children": [
                {"label": "GenBank (NCBI) & EMBL-EBI: Primary nucleotide sequence repositories used for sequence mapping", "type": "leaf"},
                {"label": "UniProt & PDB (Protein Data Bank): Archives for protein sequences and 3D macromolecular structures", "type": "leaf"}
            ]},
            {"label": "Key Methods", "type": "branch", "date": "Methods", "children": [
                {"label": "Sequence Alignment: BLAST algorithm matches query DNA/protein sequences against database libraries", "type": "leaf"},
                {"label": "Phylogenetic Analysis: Reconstructing evolutionary lineages using sequence mutations (e.g., Clustal Omega)", "type": "leaf"}
            ]},
            {"label": "Environmental Biology", "type": "branch", "date": "Ecological", "children": [
                {"label": "Metagenomics: Sequencing DNA extracted directly from environmental samples (soil, seawater) to identify microbes", "type": "leaf"},
                {"label": "Barcoding: Using short genetic markers (e.g., COI gene) to rapidly identify species in conservation", "type": "leaf"}
            ]},
            {"label": "UPSC Exam Focus", "type": "branch", "date": "UPSC Focus", "children": [
                {"label": "Genomics applications: Crispr-Cas9 target design, synthetic biology, and drug discovery", "type": "leaf"},
                {"label": "Eco-Informatics: Using remote sensing data combined with GIS and species distribution models", "type": "leaf"}
            ]}
        ],
        "hi": [
            {"label": "जैविक डेटाबेस", "type": "branch", "date": "डेटाबेस", "children": [
                {"label": "GenBank (NCBI) और EMBL-EBI: अनुक्रम मानचित्रण के लिए उपयोग किए जाने वाले प्राथमिक न्यूक्लियोटाइड डेटाबेस", "type": "leaf"},
                {"label": "UniProt और PDB (Protein Data Bank): प्रोटीन अनुक्रमों और 3D मैक्रोमोलेक्यूलर संरचनाओं के लिए वैश्विक संग्रह", "type": "leaf"}
            ]},
            {"label": "प्रमुख विधियां", "type": "branch", "date": "विधियां", "children": [
                {"label": "अनुक्रम संरेखण: BLAST एल्गोरिदम डेटाबेस पुस्तकालयों के खिलाफ क्वेरी DNA/प्रोटीन अनुक्रमों का मिलान करता है", "type": "leaf"},
                {"label": "फाइलोजेनेटिक विश्लेषण: अनुक्रम उत्परिवर्तन का उपयोग करके विकासवादी वंशावली का पुनर्निर्माण", "type": "leaf"}
            ]},
            {"label": "पर्यावरण जीवविज्ञान", "type": "branch", "date": "पारिस्थितिक", "children": [
                {"label": "मेटाजेनोमिक्स: रोगाणुओं की पहचान करने के लिए पर्यावरणीय नमूनों से सीधे निकाले गए DNA का अनुक्रमण", "type": "leaf"},
                {"label": "बारकोडिंग: संरक्षण में प्रजातियों की तेजी से पहचान करने के लिए छोटे आनुवंशिक मार्करों (जैसे COI जीन) का उपयोग करना", "type": "leaf"}
            ]},
            {"label": "यूपीएससी परीक्षा दृष्टिकोण", "type": "branch", "date": "परीक्षा", "children": [
                {"label": "जीनोमिक्स अनुप्रयोग: Crispr-Cas9 लक्ष्य डिजाइन, सिंथेटिक जीवविज्ञान, और दवा की खोज", "type": "leaf"},
                {"label": "इको-इंफॉर्मेटिक्स: GIS और प्रजाति वितरण मॉडल के साथ रिमोट सेंसिंग डेटा का उपयोग", "type": "leaf"}
            ]}
        ]
    },
    {
        "keys": ["traditional-knowledge", "sacred-forests", "sacred-lakes", "traditional"],
        "en": [
            {"label": "Sacred Groves Concept", "type": "branch", "date": "Groves", "children": [
                {"label": "Forest patches traditionally protected by local communities due to religious beliefs/deities", "type": "leaf"},
                {"label": "Acts as crucial in-situ gene banks preserving ancient flora, medicines, and water channels", "type": "leaf"},
                {"label": "Regional names: Sarnas (Jharkhand), Devrai (Maharashtra), Devarakadu (Karnataka), Kavus (Kerala)", "type": "leaf"}
            ]},
            {"label": "Sacred Lakes", "type": "branch", "date": "Lakes", "children": [
                {"label": "Water bodies preserved traditionally, preventing fishing or washing (e.g. Khecheopalri Lake in Sikkim)", "type": "leaf"},
                {"label": "Maintains local microclimate, groundwater tables, and unique high-altitude aquatic life", "type": "leaf"}
            ]},
            {"label": "Traditional Knowledge (TK)", "type": "branch", "date": "Traditional Knowledge", "children": [
                {"label": "Knowledge system developed by indigenous communities over generations regarding nature and healing", "type": "leaf"},
                {"label": "Protects against biopiracy via institutional documentation (TKDL database)", "type": "leaf"}
            ]},
            {"label": "UPSC Exam Focus", "type": "branch", "date": "UPSC Focus", "children": [
                {"label": "Biodiversity Act 2002: Empowers local Biodiversity Management Committees (BMCs) to document PBRs", "type": "leaf"},
                {"label": "Forest Rights Act 2006: Recognizes community forest resource rights, supporting traditional conservation", "type": "leaf"}
            ]}
        ],
        "hi": [
            {"label": "पवित्र उपवन (Sacred Groves)", "type": "branch", "date": "उपवन", "children": [
                {"label": "धार्मिक मान्यताओं और स्थानीय देवताओं के कारण पारंपरिक रूप से समुदायों द्वारा संरक्षित वन क्षेत्र", "type": "leaf"},
                {"label": "प्राचीन वनस्पतियों, जड़ी-बूटियों और जल स्रोतों को संरक्षित करने वाले इन-सिटू जीन बैंक के रूप में कार्य करते हैं", "type": "leaf"},
                {"label": "क्षेत्रीय नाम: सरना (झारखंड), देवराई (महाराष्ट्र), देवराकाडू (कर्नाटक), कावुस (केरल)", "type": "leaf"}
            ]},
            {"label": "पवित्र झीलें", "type": "branch", "date": "झीलें", "children": [
                {"label": "पारंपरिक रूप से संरक्षित जल निकाय जहां मछली पकड़ना प्रतिबंधित है (जैसे सिक्किम में खेचियोपालरी झील)", "type": "leaf"},
                {"label": "स्थानीय सूक्ष्म जलवायु, भूजल स्तर और अद्वितीय उच्च ऊंचाई वाले जलीय जीवन को बनाए रखती हैं", "type": "leaf"}
            ]},
            {"label": "पारंपरिक ज्ञान (Traditional Knowledge)", "type": "branch", "date": "पारंपरिक ज्ञान", "children": [
                {"label": "प्रकृति, पारिस्थितिकी और चिकित्सा प्रणालियों के बारे में पीढ़ियों से विकसित ज्ञान प्रणाली", "type": "leaf"},
                {"label": "TKDL डेटाबेस जैसे संस्थागत प्रलेखन के माध्यम से बायो-पायरेसी से सुरक्षा प्रदान करता है", "type": "leaf"}
            ]},
            {"label": "यूपीएससी परीक्षा दृष्टिकोण", "type": "branch", "date": "परीक्षा", "children": [
                {"label": "जैव विविधता अधिनियम 2002: स्थानीय स्तर पर पीपुल्स बायोडायवर्सिटी रजिस्टर (PBR) तैयार करने का अधिकार देता है", "type": "leaf"},
                {"label": "वन अधिकार अधिनियम 2006: सामुदायिक वन संसाधन अधिकारों को मान्यता देता है, जो पारंपरिक संरक्षण का समर्थन करता है", "type": "leaf"}
            ]}
        ]
    },
    {
        "keys": ["animal-and-plant", "plant-and-animal", "kingdom", "flora", "fauna"],
        "en": [
            {"label": "Taxonomic Richness", "type": "branch", "date": "Richness", "children": [
                {"label": "India holds ~8.1% of global species diversity, with over 45,000 plant species and 91,000 animal species recorded", "type": "leaf"},
                {"label": "High rates of species endemism in Western Ghats, Eastern Himalayas, and Andaman Islands", "type": "leaf"}
            ]},
            {"label": "Flora Diversity Groups", "type": "branch", "date": "Flora", "children": [
                {"label": "Angiosperms: Flowering plants dominate; gymnosperms are primarily restricted to temperate Himalayan regions", "type": "leaf"},
                {"label": "Cryptogams: Lichens, mosses, and ferns dominate wet regions; act as air quality indicators", "type": "leaf"}
            ]},
            {"label": "Fauna Diversity Groups", "type": "branch", "date": "Fauna", "children": [
                {"label": "Invertebrates: Insects comprise over 70% of the animal kingdom in species richness", "type": "leaf"},
                {"label": "Vertebrates: Amphibians, reptiles, birds, and mammals show unique adaptations across biomes", "type": "leaf"}
            ]},
            {"label": "UPSC Exam Focus", "type": "branch", "date": "UPSC Focus", "children": [
                {"label": "Schedule I of WPA 1972: Provides absolute protection to species like Tiger, Lion, and Elephant", "type": "leaf"},
                {"label": "Major threats: Habitat fragmentation, invasive species, and climate-induced shift in ranges", "type": "leaf"}
            ]}
        ],
        "hi": [
            {"label": "वर्गीकरण समृद्धि", "type": "branch", "date": "समृद्धि", "children": [
                {"label": "भारत वैश्विक प्रजाति विविधता का लगभग 8.1% प्रतिनिधित्व करता है, जिसमें 45,000 पौधे और 91,000 जंतु प्रजातियां हैं", "type": "leaf"},
                {"label": "पश्चिमी घाट, पूर्वी हिमालय और अंडमान द्वीप समूह में उच्च स्थानिकता (Endemism) पाई जाती है", "type": "leaf"}
            ]},
            {"label": "वनस्पति विविधता", "type": "branch", "date": "वनस्पति", "children": [
                {"label": "आवृतबीजी (Angiosperms): पौधों का सबसे बड़ा समूह; अनावृतबीजी (Gymnosperms) मुख्य रूप से हिमालय तक सीमित हैं", "type": "leaf"},
                {"label": "क्रिप्टोगैम (Cryptogams): लाइकेन, काई और फ़र्न गीले क्षेत्रों में हावी हैं; ये वायु प्रदूषण के संकेतक हैं", "type": "leaf"}
            ]},
            {"label": "जंतु विविधता", "type": "branch", "date": "जंतु", "children": [
                {"label": "अकशेरुकी (Invertebrates): प्रजातियों की समृद्धि में कीट जंतु जगत का 70% से अधिक हिस्सा हैं", "type": "leaf"},
                {"label": "कशेरुकी (Vertebrates): उभयचर, सरीसृप, पक्षी और स्तनधारी विभिन्न बायोम में अद्वितीय अनुकूलन प्रदर्शित करते हैं", "type": "leaf"}
            ]},
            {"label": "यूपीएससी परीक्षा दृष्टिकोण", "type": "branch", "date": "परीक्षा", "children": [
                {"label": "WPA 1972 की अनुसूची I: बाघ, शेर, हाथी और ग्रेट इंडियन बस्टर्ड को पूर्ण कानूनी सुरक्षा प्रदान करती है", "type": "leaf"},
                {"label": "प्रमुख खतरे: आवास विखंडन, आक्रामक प्रजातियों का प्रसार और जलवायु जनित भौगोलिक विस्थापन", "type": "leaf"}
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
