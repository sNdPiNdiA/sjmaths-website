#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import re
import json

BASE_DIR = r"upsc/environment/Waste-Management"

def get_clean_title(folder_name):
    title = re.sub(r'([a-z])([A-Z])', r'\1 \2', folder_name)
    title = title.replace('-', ' ')
    words = []
    acronyms = {'dpsp', 'pri', 'ut', 'uts', 'sc', 'hc', 'cm', 'com', 'arc', 'inc', 'ias', 'sec', 'sfc', 'pej', 'tej', 'mjo', 'enso', 'iod', 'icar', 'gst', 'dpc', 'mpc', 'adc', 'tac', 'scs', 'pesa', 'icar', 'isfr', 'itcz', 'tej', 'iucn', 'wpa', 'grap', 'aqews', 'caaeqms', 'naqi', 'naaqs', 'rspm', 'bod', 'cod', 'swm', 'epr', 'rohs', 'pop', 'pops', 'unep'}
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
        "keys": ["basel-convention"],
        "en": [
            {"label": "Origins & Objectives", "type": "branch", "date": "1989 / 1992", "children": [
                {"label": "Basel Convention: Global treaty to regulate the transboundary movements of hazardous wastes and their disposal; adopted in 1989, entered into force in 1992", "type": "leaf"},
                {"label": "Core Aims: Minimize generation of hazardous wastes, dispose of wastes close to their source, and protect developing countries from toxic dumping", "type": "leaf"}
            ]},
            {"label": "Key Mechanisms", "type": "branch", "date": "Procedures", "children": [
                {"label": "Prior Informed Consent (PIC): Requires exporting states to notify and obtain written consent from transit and importing states before shipment", "type": "leaf"},
                {"label": "Illegal Traffic: Declares illegal export of hazardous wastes to be a criminal act, obligating the exporting state to take back the waste", "type": "leaf"}
            ]},
            {"label": "Scope & Ban Amendment", "type": "branch", "date": "Updates", "children": [
                {"label": "Ban Amendment (2019): Prohibits all transboundary exports of hazardous wastes from OECD/EU nations to developing countries", "type": "leaf"},
                {"label": "Exclusions: Radioactive wastes (covered by IAEA) and ship discharge (covered by MARPOL) are outside Basel's scope", "type": "leaf"}
            ]},
            {"label": "UPSC Exam Focus", "type": "branch", "date": "UPSC Focus", "children": [
                {"label": "India Status: India is a party to the Basel Convention; domestic Hazardous Waste Rules 2016 align with the convention's classification", "type": "leaf"},
                {"label": "E-waste link: Convention increasingly covers e-waste flows, defining when second-hand electronics count as waste vs products", "type": "leaf"}
            ]}
        ],
        "hi": [
            {"label": "उत्पत्ति और उद्देश्य", "type": "branch", "date": "1989 / 1992", "children": [
                {"label": "बेसल कन्वेंशन: खतरनाक कचरे के सीमा पार संचलन और उनके निपटान को विनियमित करने वाली वैश्विक संधि; 1989 में अपनाई गई, 1992 में लागू हुई", "type": "leaf"},
                {"label": "मुख्य उद्देश्य: खतरनाक कचरे के उत्पादन को न्यूनतम करना, उनके स्रोत के करीब निपटान करना और विकासशील देशों को कचरा डंपिंग से बचाना", "type": "leaf"}
            ]},
            {"label": "प्रमुख तंत्र", "type": "branch", "date": "प्रक्रिया", "children": [
                {"label": "पूर्व सूचित सहमति (PIC): निर्यात करने वाले देशों को शिपमेंट से पहले पारगमन और आयात करने वाले देशों से लिखित सहमति लेना आवश्यक है", "type": "leaf"},
                {"label": "अवैध व्यापार: खतरनाक कचरे के अवैध निर्यात को आपराधिक घोषित करता है, और निर्यातक देश को कचरा वापस लेने के लिए बाध्य करता है", "type": "leaf"}
            ]},
            {"label": "संशोधन और अपवाद", "type": "branch", "date": "अपडेट", "children": [
                {"label": "प्रतिबंध संशोधन (Ban Amendment 2019): विकसित (OECD/EU) देशों से विकासशील देशों में खतरनाक कचरे के निर्यात पर पूर्ण रोक लगाता है", "type": "leaf"},
                {"label": "अपवाद: रेडियोधर्मी कचरा (IAEA के तहत) और जहाजों से निकलने वाला कचरा (MARPOL के तहत) बेसल के दायरे से बाहर हैं", "type": "leaf"}
            ]},
            {"label": "यूपीएससी परीक्षा दृष्टिकोण", "type": "branch", "date": "परीक्षा", "children": [
                {"label": "भारत की स्थिति: भारत बेसल कन्वेंशन का हस्ताक्षरकर्ता है; घरेलू खतरनाक अपशिष्ट नियम 2016 इसी वर्गीकरण के अनुरूप हैं", "type": "leaf"},
                {"label": "ई-कचरा संबंध: उपयोग किए गए इलेक्ट्रॉनिक्स को कचरा माना जाए या उत्पाद, इसे तय करने हेतु कन्वेंशन का दायरा बढ़ाया गया है", "type": "leaf"}
            ]}
        ]
    },
    {
        "keys": ["bio-medical-waste-management-rules-2016", "biomedical-waste-management"],
        "en": [
            {"label": "Four Color Segregation", "type": "branch", "date": "Categories", "children": [
                {"label": "Yellow Bag: Human anatomical waste, animal waste, soiled dressings, chemical waste, and discarded medicines; disposed via incineration or deep burial", "type": "leaf"},
                {"label": "Red Bag: Recyclable contaminated plastic waste (tubings, IV bottles, syringes without needles, catheters); treated via autoclaving/microwaving", "type": "leaf"},
                {"label": "White Container (Translucent): Metal sharps, needles, syringes with fixed needles, and blades; treated via shredding/mutilation and autoclaving", "type": "leaf"},
                {"label": "Blue Box/Cardboard: Glassware, broken vials, and metallic body implants; treated via chemical disinfection or autoclaving", "type": "leaf"}
            ]},
            {"label": "Key Mandates", "type": "branch", "date": "Mandates", "children": [
                {"label": "Chlorinated bags ban: Complete phase-out of chlorinated plastic bags, gloves, and blood bags to prevent dioxin emissions during incineration", "type": "leaf"},
                {"label": "Barcoding system: Mandates GPS tracking and barcoding of waste bags to prevent illegal dumping in municipal streams", "type": "leaf"}
            ]},
            {"label": "Operator Duties", "type": "branch", "date": "Duties", "children": [
                {"label": "Pre-treatment: Lab waste, blood bags, and vaccines must undergo on-site chemical disinfection before sending to common treatment facilities", "type": "leaf"},
                {"label": "No storage: Medical waste must not be stored beyond 48 hours without SPCB approval", "type": "leaf"}
            ]},
            {"label": "UPSC Exam Focus", "type": "branch", "date": "UPSC Focus", "children": [
                {"label": "SPCB Role: State Pollution Control Boards grant authorizations and monitor emissions of Common Bio-medical Waste Treatment Facilities (CBWTF)", "type": "leaf"},
                {"label": "Environmental hazards: Open burning of biomedical waste emits highly toxic polychlorinated dibenzo-dioxins and furans", "type": "leaf"}
            ]}
        ],
        "hi": [
            {"label": "चार रंग कोड पृथक्करण", "type": "branch", "date": "श्रेणियां", "children": [
                {"label": "पीला बैग: मानव शारीरिक अपशिष्ट, मिट्टी की पट्टियाँ, रासायनिक कचरा और फेंकी गई दवाएं; भस्मीकरण (Incineration) द्वारा निपटान", "type": "leaf"},
                {"label": "लाल बैग: पुनर्चक्रण योग्य दूषित प्लास्टिक कचरा (IV बोतलें, ट्यूबिंग, बिना सुई के सिरिंज); ऑटोक्लेविंग द्वारा उपचार", "type": "leaf"},
                {"label": "सफेद कंटेनर (पारभासी): धातु की नुकीली चीजें, सुई, ब्लेड; कतरने (Shredding) और ऑटोक्लेविंग द्वारा निपटान", "type": "leaf"},
                {"label": "नीला बॉक्स/कार्डबोर्ड: कांच के बर्तन, टूटी शीशियाँ और धातु के बॉडी इम्प्लांट; रासायनिक कीटाणुशोधन या ऑटोक्लेविंग द्वारा उपचार", "type": "leaf"}
            ]},
            {"label": "मुख्य नियम", "type": "branch", "date": "नियम", "children": [
                {"label": "क्लोरीनेटेड बैग पर प्रतिबंध: भस्मीकरण के दौरान डाइऑक्सिन उत्सर्जन को रोकने के लिए क्लोरीनेटेड प्लास्टिक बैग और दस्ताने पर पूर्ण प्रतिबंध", "type": "leaf"},
                {"label": "बारकोडिंग प्रणाली: नगर निगम के कचरे में अवैध डंपिंग को रोकने के लिए अपशिष्ट बैग की बारकोडिंग और जीपीएस ट्रैकिंग अनिवार्य", "type": "leaf"}
            ]},
            {"label": "ऑपरेटर के कर्तव्य", "type": "branch", "date": "कर्तव्य", "children": [
                {"label": "पूर्व-उपचार: प्रयोगशाला कचरा, रक्त बैग और टीकों को भेजने से पहले साइट पर ही रासायनिक कीटाणुशोधन करना आवश्यक है", "type": "leaf"},
                {"label": "भंडारण सीमा: जैव-चिकित्सा कचरे को SPCB की अनुमति के बिना 48 घंटे से अधिक समय तक संग्रहीत नहीं किया जा सकता", "type": "leaf"}
            ]},
            {"label": "यूपीएससी परीक्षा दृष्टिकोण", "type": "branch", "date": "परीक्षा", "children": [
                {"label": "SPCB की भूमिका: राज्य प्रदूषण नियंत्रण बोर्ड जैव-चिकित्सा अपशिष्ट उपचार सुविधाओं (CBWTF) को अधिकृत और मॉनिटर करता है", "type": "leaf"},
                {"label": "पर्यावरणीय खतरे: जैव-चिकित्सा कचरे के खुले दहन से अत्यधिक विषैले डाइऑक्सिन और फ्यूरान उत्सर्जित होते हैं", "type": "leaf"}
            ]}
        ]
    },
    {
        "keys": ["e-waste-management", "e-waste-rules-2016", "e-waste-status-in-india", "importance-of-the-e-waste-management", "steps-taken-for-combating-mounting-e-waste", "e-waste-management-handling-rules-2016"],
        "en": [
            {"label": "Extended Producer Responsibility (EPR)", "type": "branch", "date": "EPR", "children": [
                {"label": "Definition: Policy where producers are given financial and physical responsibility for the treatment or disposal of post-consumer electronic products", "type": "leaf"},
                {"label": "EPR Authorization: Mandates producers to obtain authorization from CPCB, setting targets to collect 60-80% of their generated e-waste", "type": "leaf"}
            ]},
            {"label": "RoHS Provisions", "type": "branch", "date": "RoHS", "children": [
                {"label": "RoHS Target: Restriction of Hazardous Substances; mandates reduction of Lead, Mercury, Hexavalent Chromium, Polybrominated Biphenyls to <0.1% by weight, and Cadmium to <0.01%", "type": "leaf"},
                {"label": "Scope: Applies to all electrical and electronic equipment imported or manufactured in India", "type": "leaf"}
            ]},
            {"label": "India Status & Sectors", "type": "branch", "date": "India Status", "children": [
                {"label": "Informal recycling: Over 90-95% of India's e-waste is recycled by the informal sector using crude acid baths and open burning (e.g. Seelampur, Delhi)", "type": "leaf"},
                {"label": "Hazards: Releases heavy metals (Lead, Cadmium) into soil and water, causing neurological damage in waste workers", "type": "leaf"}
            ]},
            {"label": "UPSC Exam Focus", "type": "branch", "date": "UPSC Focus", "children": [
                {"label": "E-Waste Rules 2022 Updates: Expanded categories of covered items to 106, integrated registered recyclers, and introduced tradable EPR certificates", "type": "leaf"},
                {"label": "Urban Mining: Recovery of precious metals (gold, silver, copper, palladium) from printed circuit boards, reducing primary mining demand", "type": "leaf"}
            ]}
        ],
        "hi": [
            {"label": "विस्तारित उत्पादक उत्तरदायित्व (EPR)", "type": "branch", "date": "EPR", "children": [
                {"label": "परिभाषा: नीति जिसके तहत उत्पादकों को उपभोक्ता द्वारा उपयोग किए जा चुके इलेक्ट्रॉनिक उत्पादों के संग्रह और निपटान की वित्तीय और भौतिक जिम्मेदारी दी जाती है", "type": "leaf"},
                {"label": "EPR प्राधिकरण: उत्पादकों को CPCB से प्राधिकरण प्राप्त करना अनिवार्य है, जिसके तहत 60-80% ई-कचरा एकत्र करने का लक्ष्य रखा गया है", "type": "leaf"}
            ]},
            {"label": "RoHS के प्रावधान", "type": "branch", "date": "RoHS", "children": [
                {"label": "RoHS लक्ष्य: खतरनाक पदार्थों का प्रतिबंध; बिजली के उपकरणों में सीसा, पारा, क्रोमियम का स्तर <0.1% और कैडमियम का स्तर <0.01% तक सीमित करना", "type": "leaf"},
                {"label": "दायरा: भारत में आयातित या निर्मित होने वाले सभी विद्युत और इलेक्ट्रॉनिक उपकरणों पर लागू होता है", "type": "leaf"}
            ]},
            {"label": "भारत में स्थिति और क्षेत्र", "type": "branch", "date": "भारत में स्थिति", "children": [
                {"label": "अनौपचारिक क्षेत्र: भारत का 90-95% ई-कचरा अनौपचारिक क्षेत्र (जैसे सीलमपुर, दिल्ली) द्वारा खुले दहन और एसिड बाथ से संसाधित होता है", "type": "leaf"},
                {"label": "स्वास्थ्य खतरे: खदान श्रमिकों और कचरा बीनने वालों में भारी धातु प्रदूषण (सीसा, कैडमियम) से तंत्रिका तंत्र को नुकसान पहुंचना", "type": "leaf"}
            ]},
            {"label": "यूपीएससी परीक्षा दृष्टिकोण", "type": "branch", "date": "परीक्षा", "children": [
                {"label": "ई-कचरा नियम 2022 अपडेट: कवर्ड इलेक्ट्रॉनिक उपकरणों की श्रेणियों को 106 तक बढ़ाया, और व्यापार योग्य EPR प्रमाणपत्रों की शुरुआत की", "type": "leaf"},
                {"label": "शहरी खनन (Urban Mining): सर्किट बोर्ड से सोना, चांदी और तांबा जैसी मूल्यवान धातुओं को वापस प्राप्त करना, जिससे प्राथमिक खनन की आवश्यकता कम होती है", "type": "leaf"}
            ]}
        ]
    },
    {
        "keys": ["plastics-pollution", "effects-of-plastic-waste", "the-global-tourism-plastics-initiative"],
        "en": [
            {"label": "PWM Rules 2016 & Amendments", "type": "branch", "date": "PWM Rules", "children": [
                {"label": "Thickness limit: Ban on single-use plastic carry bags of thickness less than 120 microns (enforced from December 2022)", "type": "leaf"},
                {"label": "EPR Registry: Mandates producers, importers, and brand owners to register on CPCB's centralized portal to manage plastic packaging waste", "type": "leaf"}
            ]},
            {"label": "Global Initiatives", "type": "branch", "date": "Global", "children": [
                {"label": "UNEP Tourism Initiative: Global Tourism Plastics Initiative aiming to eliminate single-use plastics from hotel chains and travel operations by 2025", "type": "leaf"},
                {"label": "UNEA Resolution (2022): Historic resolution passed in Nairobi to draft a legally binding global treaty to end plastic pollution by 2024", "type": "leaf"}
            ]},
            {"label": "Environmental Damage", "type": "branch", "date": "Impacts", "children": [
                {"label": "Microplastic leakage: Breakdown of macroplastics into particles <5mm, bioaccumulating in marine food webs", "type": "leaf"},
                {"label": "Wildlife hazard: Ingestion of plastics blocks digestive tracts of marine turtles, cetaceans, and stray cattle", "type": "leaf"}
            ]},
            {"label": "UPSC Exam Focus", "type": "branch", "date": "UPSC Focus", "children": [
                {"label": "Categories of Plastic: Rigid (Cat I), Flexible (Cat II), Multilayered (Cat III), and Compostable plastics (Cat IV) under EPR guidelines", "type": "leaf"},
                {"label": "Alternative options: Polylactic Acid (PLA) compostable plastics, jute bags, and mycelium packaging as plastic replacements", "type": "leaf"}
            ]}
        ],
        "hi": [
            {"label": "प्लास्टिक अपशिष्ट प्रबंधन नियम", "type": "branch", "date": "PWM नियम", "children": [
                {"label": "मोटाई सीमा: 120 माइक्रोन से कम मोटाई वाले सिंगल-यूज़ प्लास्टिक ले जाने वाले बैग पर पूर्ण प्रतिबंध (दिसंबर 2022 से लागू)", "type": "leaf"},
                {"label": "EPR रजिस्ट्री: उत्पादकों, आयातकों और ब्रांड मालिकों को प्लास्टिक पैकेजिंग कचरे के प्रबंधन के लिए CPCB पोर्टल पर पंजीकृत होना अनिवार्य", "type": "leaf"}
            ]},
            {"label": "वैश्विक पहलें", "type": "branch", "date": "वैश्विक", "children": [
                {"label": "UNEP पर्यटन पहल: 2025 तक होटल श्रृंखलाओं और यात्रा संचालन से सिंगल-यूज़ प्लास्टिक को समाप्त करने का लक्ष्य", "type": "leaf"},
                {"label": "UNEA संकल्प (2022): नैरोबी में 2024 तक प्लास्टिक प्रदूषण को समाप्त करने के लिए कानूनी रूप से बाध्यकारी संधि तैयार करने का संकल्प", "type": "leaf"}
            ]},
            {"label": "पर्यावरणीय क्षति", "type": "branch", "date": "प्रभाव", "children": [
                {"label": "माइक्रोप्लास्टिक रिसाव: मैक्रोप्लास्टिक्स का <5 मिमी के कणों में टूटना, जो समुद्री खाद्य जाल में जमा हो जाते हैं", "type": "leaf"},
                {"label": "वन्यजीवों के लिए खतरा: प्लास्टिक खाने से समुद्री कछुओं, गायों और जलीय जीवों के पाचन तंत्र का अवरुद्ध होना", "type": "leaf"}
            ]},
            {"label": "यूपीएससी परीक्षा दृष्टिकोण", "type": "branch", "date": "परीक्षा", "children": [
                {"label": "प्लास्टिक की श्रेणियां: कठोर (Cat I), लचीला (Cat II), बहुस्तरीय (Cat III), और कम्पोस्टेबल प्लास्टिक (Cat IV) नियम के तहत निर्दिष्ट", "type": "leaf"},
                {"label": "वैकल्पिक समाधान: पॉलीलैक्टिक एसिड (PLA) आधारित कम्पोस्टेबल प्लास्टिक, जूट और कवक (Mycelium) पैकेजिंग", "type": "leaf"}
            ]}
        ]
    },
    {
        "keys": ["hazardous-and-other-wastes-rules-2016", "hazardous-and-other-wastes-management-trans-boundary-movement-rules-2016", "hazardous-waste-and-its-characteristics", "hazardous-waste-treatment"],
        "en": [
            {"label": "Hazardous Characteristics", "type": "branch", "date": "Properties", "children": [
                {"label": "Ignitability: Low flashpoint wastes (<60 deg C) capable of causing fires during transport or storage", "type": "leaf"},
                {"label": "Corrosivity: Highly acidic (pH <=2) or highly basic (pH >=12.5) wastes that corrode steel storage tanks", "type": "leaf"},
                {"label": "Reactivity: Wastes unstable under normal conditions, reacting violently with water or releasing toxic gases", "type": "leaf"},
                {"label": "Toxicity: Contains heavy metals or persistent organic pollutants that leach out (measured via TCLP test)", "type": "leaf"}
            ]},
            {"label": "Management Hierarchy", "type": "branch", "date": "Hierarchy", "children": [
                {"label": "Co-processing: Utilizing high-calorific hazardous wastes as alternative fuel in energy-intensive cement kilns", "type": "leaf"},
                {"label": "Secured Landfill: Double-composite lined containment facilities designed to prevent toxic leachate from entering aquifers", "type": "leaf"}
            ]},
            {"label": "Regulatory Control", "type": "branch", "date": "Control", "children": [
                {"label": "Manifest system: Requires a 7-copy color-coded document to track hazardous waste from generation to final disposal site", "type": "leaf"},
                {"label": "Import ban: Prohibits the import of hazardous wastes (like waste tires, plastic scraps) for disposal in India", "type": "leaf"}
            ]},
            {"label": "UPSC Exam Focus", "type": "branch", "date": "UPSC Focus", "children": [
                {"label": "Responsibility: Ministry of Environment, Forest and Climate Change (MoEFCC) defines rules; SPCBs enforce monitoring and grant authorizations", "type": "leaf"},
                {"label": "E-waste link: E-waste is categorized separately from industrial hazardous waste, but components (lead battery, CRT) fall under both", "type": "leaf"}
            ]}
        ],
        "hi": [
            {"label": "खतरनाक कचरे के लक्षण", "type": "branch", "date": "लक्षण", "children": [
                {"label": "ज्वलनशीलता: कम फ्लैशपॉइंट कचरा (<60 डिग्री सेल्सियस) जो परिवहन या भंडारण के दौरान आग का कारण बन सकता है", "type": "leaf"},
                {"label": "संक्षारणशीलता: अत्यधिक अम्लीय (pH <=2) या अत्यधिक क्षारीय (pH >=12.5) कचरा जो लोहे के टैंकों को संक्षारित करता है", "type": "leaf"},
                {"label": "रिएक्टिविटी: सामान्य परिस्थितियों में अस्थिर कचरा, जो पानी के साथ हिंसक प्रतिक्रिया करता है या विषैली गैसें छोड़ता है", "type": "leaf"},
                {"label": "विषाक्तता: भारी धातु या कीटनाशक युक्त कचरा जो रिसकर भूजल में मिल सकता है (TCLP परीक्षण द्वारा मापा जाता है)", "type": "leaf"}
            ]},
            {"label": "प्रबंधन पदानुक्रम", "type": "branch", "date": "पदानुक्रम", "children": [
                {"label": "सह-प्रसंस्करण (Co-processing): सीमेंट भट्टियों में वैकल्पिक ईंधन के रूप में उच्च-कैलोरी मूल्य वाले खतरनाक कचरे का उपयोग करना", "type": "leaf"},
                {"label": "सुरक्षित लैंडफिल (Secured Landfill): दोहरी परत वाले सुरक्षित ढांचे जहां भूजल में रिसाव रोकने की व्यवस्था होती है", "type": "leaf"}
            ]},
            {"label": "नियामक नियंत्रण", "type": "branch", "date": "नियंत्रण", "children": [
                {"label": "मैनिफेस्ट प्रणाली: खतरनाक कचरे के परिवहन पर नजर रखने के लिए एक 7-प्रतियों वाला रंग-कोडित दस्तावेज उपयोग करना", "type": "leaf"},
                {"label": "आयात पर प्रतिबंध: भारत में निपटान के लिए खतरनाक कचरे (जैसे पुराने टायर, प्लास्टिक कचरा) के आयात को प्रतिबंधित करता है", "type": "leaf"}
            ]},
            {"label": "यूपीएससी परीक्षा दृष्टिकोण", "type": "branch", "date": "परीक्षा", "children": [
                {"label": "जिम्मेदारी: पर्यावरण मंत्रालय (MoEFCC) नियम तय करता है; राज्य प्रदूषण बोर्ड (SPCB) इसकी निगरानी और प्राधिकरण देता है", "type": "leaf"},
                {"label": "ई-कचरा संबंध: ई-कचरे को औद्योगिक खतरनाक कचरे से अलग वर्गीकृत किया गया है, लेकिन घटक (सीसा, बैटरी) दोनों में आते हैं", "type": "leaf"}
            ]}
        ]
    },
    {
        "keys": ["hazards-associated-with-waste-management", "pollutants-and-their-health-impacts"],
        "en": [
            {"label": "Health Hazards", "type": "branch", "date": "Health", "children": [
                {"label": "Leachate: Liquid that extracts dissolved solids from landfills; carries heavy metals (Lead, Mercury, Cadmium) into aquifers, causing kidney/liver damage", "type": "leaf"},
                {"label": "Landfill gas: Composed of Methane (~50%) and Carbon Dioxide; Methane forms explosive mixtures and acts as a potent greenhouse gas", "type": "leaf"}
            ]},
            {"label": "Heavy Metal Poisoning", "type": "branch", "date": "Toxins", "children": [
                {"label": "Lead (Pb): Found in batteries/electronics; damages nervous system and causes anemia and cognitive defects in children", "type": "leaf"},
                {"label": "Cadmium (Cd): Found in nickel-cadmium batteries; causes renal dysfunction and osteomalacia (Itai-Itai disease)", "type": "leaf"},
                {"label": "Mercury (Hg): Found in thermometers/lamps; bioaccumulates as methylmercury, causing Minamata disease (neurological damage)", "type": "leaf"}
            ]},
            {"label": "Occupational Exposure", "type": "branch", "date": "Occupations", "children": [
                {"label": "Waste pickers: Exposure to sharp needles, chemical burns, bio-aerosols, and dermal infections without protective gear", "type": "leaf"},
                {"label": "Incinerator emissions: Releases particulate matter, fly ash, dioxins, and furans if stack scrubbers fail", "type": "leaf"}
            ]},
            {"label": "UPSC Exam Focus", "type": "branch", "date": "UPSC Focus", "children": [
                {"label": "Bioconcentration: Accumulation of heavy metals in food crops grown on soils irrigated with untreated industrial wastewater", "type": "leaf"},
                {"label": "Minamata Convention: Global treaty dedicated to reducing mercury emissions and phase out mercury-added products", "type": "leaf"}
            ]}
        ],
        "hi": [
            {"label": "स्वास्थ्य के खतरे", "type": "branch", "date": "स्वास्थ्य", "children": [
                {"label": "लीचेट (Leachate): लैंडफिल से रिसने वाला विषाक्त तरल; भारी धातुओं को भूजल में ले जाकर गुर्दे और यकृत को नुकसान पहुंचाता है", "type": "leaf"},
                {"label": "लैंडफिल गैसें: मुख्य रूप से मीथेन (~50%) और CO2; मीथेन विस्फोटक मिश्रण बनाती है और एक शक्तिशाली ग्रीनहाउस गैस है", "type": "leaf"}
            ]},
            {"label": "भारी धातु विषाक्तता", "type": "branch", "date": "विषाक्तता", "children": [
                {"label": "सीसा (Pb): बैटरी/इलेक्ट्रॉनिक्स में; तंत्रिका तंत्र को नष्ट करता है और बच्चों में मानसिक विकास को अवरुद्ध करता है", "type": "leaf"},
                {"label": "कैडमियम (Cd): रीचार्जेबल बैटरी में; गुर्दे की विफलता और हड्डियों में दर्द (इताई-इताई रोग) का कारण बनता है", "type": "leaf"},
                {"label": "पारा (Hg): थर्मामीटर में; मिथाइलमर्करी के रूप में संचय होकर मिनामाता रोग (मस्तिष्क विकार) का कारण बनता है", "type": "leaf"}
            ]},
            {"label": "व्यावसायिक जोखिम", "type": "branch", "date": "जोखिम", "children": [
                {"label": "कचरा बीनने वाले: बिना सुरक्षा उपकरणों के सुइयों, रसायनों और त्वचा संक्रमणों के सीधे संपर्क में आना", "type": "leaf"},
                {"label": "भस्मीकरण उत्सर्जन: चिमनियों के स्क्रबर खराब होने पर हवा में पार्टिकुलेट मैटर, डाइऑक्सिन और फ्यूरान का निकलना", "type": "leaf"}
            ]},
            {"label": "यूपीएससी परीक्षा दृष्टिकोण", "type": "branch", "date": "परीक्षा", "children": [
                {"label": "जैव-संचय: अनुपचारित औद्योगिक जल से सींचे गए खेतों में उगाई गई फसलों के माध्यम से भारी धातुओं का खाद्य श्रृंखला में प्रवेश", "type": "leaf"},
                {"label": "मिनामाता कन्वेंशन: पारे के उत्सर्जन को कम करने और पारा युक्त उत्पादों को चरणबद्ध तरीके से समाप्त करने की वैश्विक संधि", "type": "leaf"}
            ]}
        ]
    },
    {
        "keys": ["solid-waste-management", "issues-in-solid-waste-management-in-india", "salient-features-of-swm-rules-2016", "types-of-solid-waste"],
        "en": [
            {"label": "Three-Stream Segregation", "type": "branch", "date": "Segregation", "children": [
                {"label": "Wet Waste (Biodegradable): Kitchen waste, vegetables, food; processed via composting or biomethanation", "type": "leaf"},
                {"label": "Dry Waste (Recyclable): Paper, plastics, metals, wood, glass; sent to registered recycling facilities", "type": "leaf"},
                {"label": "Domestic Hazardous Waste: Discarded paint cans, pesticide bottles, mercury thermometers, and unused medicines; collected separately", "type": "leaf"}
            ]},
            {"label": "Salient Rules 2016", "type": "branch", "date": "SWM Rules", "children": [
                {"label": "Generator pays: Introduces 'user fee' for waste collection and 'spot fines' for littering and non-segregation", "type": "leaf"},
                {"label": "Integration: Local bodies must formally integrate informal waste pickers and scrap dealers into the solid waste management framework", "type": "leaf"},
                {"label": "Landfill Criteria: Set strict limits: buffer zones of 500m around waste plants, landfills 100m from rivers and 20km from airports", "type": "leaf"}
            ]},
            {"label": "Key Challenges in India", "type": "branch", "date": "Challenges", "children": [
                {"label": "Lack of segregation: Mixed waste arrives at landfills, rendering compost units inefficient and clogging recycling systems", "type": "leaf"},
                {"label": "Dumpyard fires: Uncontrolled methane generation in open dumps (e.g. Ghazipur, Deonar) causes persistent, toxic smoke fires", "type": "leaf"}
            ]},
            {"label": "UPSC Exam Focus", "type": "branch", "date": "UPSC Focus", "children": [
                {"label": "Solid Waste Rules Scope: Applies beyond municipal areas to urban agglomerations, census towns, defense sites, and pilgrimage spots", "type": "leaf"},
                {"label": "Swachh Bharat Mission 2.0: Focuses on 'Garbage Free Cities' and remediation of all legacy dumpsites through bioremediation", "type": "leaf"}
            ]}
        ],
        "hi": [
            {"label": "तीन-अपशिष्ट पृथक्करण", "type": "branch", "date": "पृथक्करण", "children": [
                {"label": "गीला कचरा (जैव-अपघटनीय): रसोई का कचरा, खाद्य सामग्री; खाद बनाने या बायोमेथेनेशन द्वारा उपचारित", "type": "leaf"},
                {"label": "सूखा कचरा (पुनर्चक्रण योग्य): कागज, प्लास्टिक, धातु, कांच; पंजीकृत रीसाइक्लिंग सुविधाओं को भेजा जाता है", "type": "leaf"},
                {"label": "घरेलू खतरनाक कचरा: पेंट के डिब्बे, कीटनाशक बोतलें, थर्मामीटर और दवाएं; अलग से एकत्र किए जाते हैं", "type": "leaf"}
            ]},
            {"label": "ठोस अपशिष्ट नियम 2016", "type": "branch", "date": "नियम", "children": [
                {"label": "उत्पादक भुगतान: कचरा संग्रह के लिए 'उपयोगकर्ता शुल्क' और कचरा फैलाने पर तत्काल जुर्माने (Spot fine) का प्रावधान", "type": "leaf"},
                {"label": "एकीकरण: स्थानीय निकायों को अनौपचारिक कचरा बीनने वालों को औपचारिक रूप से अपशिष्ट प्रबंधन प्रणाली में शामिल करना होगा", "type": "leaf"},
                {"label": "लैंडफिल मानदंड: कचरा संयंत्रों के आसपास 500 मीटर का बफर जोन; लैंडफिल नदियों से 100 मीटर और हवाई अड्डों से 20 किमी दूर होना चाहिए", "type": "leaf"}
            ]},
            {"label": "भारत में मुख्य चुनौतियाँ", "type": "branch", "date": "चुनौतियाँ", "children": [
                {"label": "पृथक्करण का अभाव: मिश्रित कचरा लैंडफिल में पहुंचता है, जिससे खाद इकाइयां अप्रभावी हो जाती हैं", "type": "leaf"},
                {"label": "डंपयार्ड में आग: खुले डंपयार्डों (जैसे गाजीपुर, देवनार) में अनियंत्रित मीथेन उत्पादन से जहरीली आग लगना", "type": "leaf"}
            ]},
            {"label": "यूपीएससी परीक्षा दृष्टिकोण", "type": "branch", "date": "परीक्षा", "children": [
                {"label": "ठोस अपशिष्ट नियमों का दायरा: नगर पालिकाओं के अलावा छावनी बोर्डों, रेलवे स्टेशनों और तीर्थ स्थलों पर भी लागू होते हैं", "type": "leaf"},
                {"label": "स्वच्छ भारत मिशन 2.0: 'कचरा मुक्त शहरों' और पुराने डंपयार्डों के जैव-उपचार (Bioremediation) पर ध्यान केंद्रित करना", "type": "leaf"}
            ]}
        ]
    },
    {
        "keys": ["policy-on-promotion-of-city-compost"],
        "en": [
            {"label": "Policy Objectives", "type": "branch", "date": "Overview", "children": [
                {"label": "Waste to Wealth: Promote the extraction of organic compost from urban solid waste to reduce landfill dependence", "type": "leaf"},
                {"label": "Soil health: Revitalize depleted agricultural soils with organic matter, increasing water retention capacity", "type": "leaf"}
            ]},
            {"label": "Financial Incentives", "type": "branch", "date": "Subsidies", "children": [
                {"label": "Market Development Assistance (MDA): Provision of Rs. 1500 per tonne of city compost as subsidy to lower price for farmers", "type": "leaf"},
                {"label": "Co-marketing: Mandates chemical fertilizer companies to bundle and market city compost alongside chemical fertilizers", "type": "leaf"}
            ]},
            {"label": "UPSC Exam Focus", "type": "branch", "date": "UPSC Focus", "children": [
                {"label": "Dual benefit: Addresses municipal solid waste management crises while reducing chemical fertilizer import burdens", "type": "leaf"},
                {"label": "Quality standards: Compost must comply with Heavy Metal threshold limits specified under SWM Rules 2016 to prevent soil contamination", "type": "leaf"}
            ]}
        ],
        "hi": [
            {"label": "नीति के उद्देश्य", "type": "branch", "date": "अवलोकन", "children": [
                {"label": "कचरे से कंचन: लैंडफिल पर निर्भरता कम करने के लिए शहरी ठोस कचरे से जैविक खाद के उत्पादन को बढ़ावा देना", "type": "leaf"},
                {"label": "मृदा स्वास्थ्य: जैविक पदार्थों के माध्यम से कृषि मिट्टी को समृद्ध करना, जिससे उसकी जल धारण क्षमता बढ़ती है", "type": "leaf"}
            ]},
            {"label": "वित्तीय प्रोत्साहन", "type": "branch", "date": "सब्सिडी", "children": [
                {"label": "बाजार विकास सहायता (MDA): किसानों के लिए कीमत कम करने हेतु शहर की खाद पर 1500 रुपये प्रति टन की सब्सिडी का प्रावधान", "type": "leaf"},
                {"label": "सह-विपणन: रासायनिक उर्वरक कंपनियों के लिए अनिवार्य किया गया है कि वे रासायनिक उर्वरकों के साथ शहर की खाद का भी विपणन करें", "type": "leaf"}
            ]},
            {"label": "यूपीएससी परीक्षा दृष्टिकोण", "type": "branch", "date": "परीक्षा", "children": [
                {"label": "दोहरा लाभ: रासायनिक उर्वरक आयात के बोझ को कम करने के साथ-साथ नगर निगम के कचरे का निपटान करना", "type": "leaf"},
                {"label": "गुणवत्ता मानक: खाद को भारी धातुओं की निर्धारित सीमा (SWM नियम 2016 के तहत) के अनुरूप होना चाहिए ताकि मिट्टी प्रदूषित न हो", "type": "leaf"}
            ]}
        ]
    },
    {
        "keys": ["rotterdam-convention"],
        "en": [
            {"label": "Core Objectives", "type": "branch", "date": "1998 / 2004", "children": [
                {"label": "Prior Informed Consent (PIC): Global treaty facilitating information exchange on import/export of hazardous industrial chemicals and pesticides; adopted in 1998, in force in 2004", "type": "leaf"},
                {"label": "Shared Responsibility: Enables importing countries to decide which hazardous chemicals they want to receive and exclude those they cannot manage safely", "type": "leaf"}
            ]},
            {"label": "Covered Substances", "type": "branch", "date": "Scope", "children": [
                {"label": "Annex III Chemicals: Lists pesticides and industrial chemicals that are banned or severely restricted for health or environmental reasons", "type": "leaf"},
                {"label": "Export obligation: If a chemical is exported, the exporting state must provide safety data sheets and label it with appropriate hazard warnings", "type": "leaf"}
            ]},
            {"label": "UPSC Exam Focus", "type": "branch", "date": "UPSC Focus", "children": [
                {"label": "Legally binding: Parties are legally bound to implement the PIC procedure for Annex III chemicals", "type": "leaf"},
                {"label": "Synergy: Operates in tandem with Basel (waste disposal) and Stockholm (persistent organic pollutants) conventions to regulate toxic cycles", "type": "leaf"}
            ]}
        ],
        "hi": [
            {"label": "मुख्य उद्देश्य", "type": "branch", "date": "1998 / 2004", "children": [
                {"label": "पूर्व सूचित सहमति (PIC): खतरनाक औद्योगिक रसायनों और कीटनाशकों के आयात/निर्यात पर सूचनाओं के आदान-प्रदान की वैश्विक संधि; 1998 में अपनाई गई, 2004 में लागू हुई", "type": "leaf"},
                {"label": "साझा जिम्मेदारी: आयात करने वाले देशों को यह तय करने का अधिकार देती है कि वे किन खतरनाक रसायनों को प्राप्त करना चाहते हैं", "type": "leaf"}
            ]},
            {"label": "कवर किए गए पदार्थ", "type": "branch", "date": "दायरा", "children": [
                {"label": "अनुसूची III रसायन: उन कीटनाशकों और रसायनों की सूची जो स्वास्थ्य या पर्यावरणीय कारणों से प्रतिबंधित या सीमित किए गए हैं", "type": "leaf"},
                {"label": "निर्यात दायित्व: यदि कोई रसायन निर्यात किया जाता है, तो निर्यातक देश को सुरक्षा डेटा शीट और खतरे की चेतावनी लेबल प्रदान करना होगा", "type": "leaf"}
            ]},
            {"label": "यूपीएससी परीक्षा दृष्टिकोण", "type": "branch", "date": "परीक्षा", "children": [
                {"label": "कानूनी रूप से बाध्यकारी: सदस्य देश अनुसूची III के रसायनों के लिए PIC प्रक्रिया को लागू करने के लिए कानूनी रूप से बाध्य हैं", "type": "leaf"},
                {"label": "त्रयी (Synergy): विषाक्त पदार्थों के चक्र को रोकने के लिए यह बेसल (कचरा) और स्टॉकहोम (POPs) सम्मेलनों के साथ मिलकर काम करता है", "type": "leaf"}
            ]}
        ]
    },
    {
        "keys": ["stockholm-convention-on-persistent-organic-pollutants"],
        "en": [
            {"label": "Persistent Organic Pollutants (POPs)", "type": "branch", "date": "2001 / 2004", "children": [
                {"label": "Definition: Organic compounds resistant to environmental degradation; bioaccumulate in fatty tissues and undergo long-range atmospheric transport (grasshopper effect)", "type": "leaf"},
                {"label": "Stockholm Convention: Legally binding global treaty dedicated to eliminating or restricting the production and use of POPs; adopted 2001, in force 2004", "type": "leaf"}
            ]},
            {"label": "Convention Annexes", "type": "branch", "date": "Annexes", "children": [
                {"label": "Annex A (Elimination): Parties must eliminate production and use of these chemicals (e.g., Aldrin, Endrin, Heptachlor)", "type": "leaf"},
                {"label": "Annex B (Restriction): Production and use are restricted for specific purposes (e.g. DDT utilized strictly for malaria vector control)", "type": "leaf"},
                {"label": "Annex C (Unintentional): Requires measures to reduce unintentional releases of byproducts (e.g. Dioxins, Furans from waste burning)", "type": "leaf"}
            ]},
            {"label": "UPSC Exam Focus", "type": "branch", "date": "UPSC Focus", "children": [
                {"label": "Dirty Dozen: The initial group of 12 highly toxic POPs targeted by the convention (including DDT, PCBs, Dioxins)", "type": "leaf"},
                {"label": "India updates: In 2020, India's Union Cabinet approved ratification of 7 newly listed POPs (including Chlordecone, Hexabromobiphenyl), banning their manufacture and trade", "type": "leaf"}
            ]}
        ],
        "hi": [
            {"label": "स्थायी कार्बनिक प्रदूषक (POPs)", "type": "branch", "date": "2001 / 2004", "children": [
                {"label": "परिभाषा: कार्बनिक यौगिक जो पर्यावरणीय क्षरण का विरोध करते हैं; वसायुक्त ऊतकों में जमा होते हैं और लंबी दूरी तक गमन करते हैं", "type": "leaf"},
                {"label": "स्टॉकहोम कन्वेंशन: POPs के उत्पादन और उपयोग को समाप्त या प्रतिबंधित करने वाली कानूनी रूप से बाध्यकारी वैश्विक संधि; 2001 में अपनाई गई, 2004 में लागू हुई", "type": "leaf"}
            ]},
            {"label": "कन्वेंशन की अनुसूचियां", "type": "branch", "date": "अनुसूचियां", "children": [
                {"label": "अनुसूची A (उन्मूलन): सदस्य देशों को इन रसायनों के उत्पादन और उपयोग को पूरी तरह समाप्त करना होगा (जैसे एल्ड्रिन, हेप्टाक्लोर)", "type": "leaf"},
                {"label": "अनुसूची B (प्रतिबंध): विशिष्ट उद्देश्यों के लिए उत्पादन और उपयोग सीमित करना (जैसे मलेरिया नियंत्रण के लिए विशेष रूप से DDT)", "type": "leaf"},
                {"label": "अनुसूची C (अनजाने में): कचरा जलाने से निकलने वाले उप-उत्पादों (डाइऑक्सिन, फ्यूरान) के अनजाने उत्सर्जन को कम करना", "type": "leaf"}
            ]},
            {"label": "यूपीएससी परीक्षा दृष्टिकोण", "type": "branch", "date": "परीक्षा", "children": [
                {"label": "डर्टी डज़न (Dirty Dozen): कन्वेंशन द्वारा लक्षित 12 अत्यधिक विषैले रासायनिक प्रदूषकों का प्रारंभिक समूह (DDT, PCBs सहित)", "type": "leaf"},
                {"label": "भारत अपडेट: 2020 में भारत ने नए सूचीबद्ध 7 रसायनों को मंजूरी दी और उनके घरेलू निर्माण व व्यापार को पूरी तरह प्रतिबंधित किया", "type": "leaf"}
            ]}
        ]
    },
    {
        "keys": ["technologies-for-the-generation-of-energy-from-waste", "treatments-methods-in-waste-management"],
        "en": [
            {"label": "Thermal Technologies", "type": "branch", "date": "Thermal", "children": [
                {"label": "Incineration: Direct combustion of waste at high temperatures (>850 deg C) to produce steam and electricity; requires extensive emission controls", "type": "leaf"},
                {"label": "Pyrolysis: Thermal degradation of waste in the complete absence of oxygen; produces liquid bio-oil and synthetic gas", "type": "leaf"},
                {"label": "Gasification: Converting carbonaceous materials into syngas (CO + H2) at high temperatures with restricted oxygen", "type": "leaf"}
            ]},
            {"label": "Biological Technologies", "type": "branch", "date": "Biological", "children": [
                {"label": "Biomethanation (Anaerobic): Decomposition of organic wet waste by anaerobic bacteria to produce biogas (rich in Methane) and nutrient-rich digestate", "type": "leaf"},
                {"label": "Windrow Composting: Piling organic waste in long rows (windrows) aerated periodically to produce agricultural compost", "type": "leaf"}
            ]},
            {"label": "Refuse Derived Fuel (RDF)", "type": "branch", "date": "RDF", "children": [
                {"label": "Pelletization: Compacting high-calorific fraction of dry waste (paper, plastic, textile) into fuel pellets for industrial boilers and cement kilns", "type": "leaf"}
            ]},
            {"label": "UPSC Exam Focus", "type": "branch", "date": "UPSC Focus", "children": [
                {"label": "Waste to Energy (WTE) challenges: Indian municipal waste has high moisture content (~50%) and low calorific value, making direct incineration inefficient", "type": "leaf"},
                {"label": "Fly ash and bottom ash: Residual residues of incineration; must be treated to prevent heavy metal leaching before disposal", "type": "leaf"}
            ]}
        ],
        "hi": [
            {"label": "तापीय तकनीकें", "type": "branch", "date": "तापीय", "children": [
                {"label": "भस्मीकरण (Incineration): बिजली पैदा करने के लिए उच्च तापमान (>850 डिग्री सेल्सियस) पर कचरे का प्रत्यक्ष दहन; उत्सर्जन नियंत्रण की आवश्यकता", "type": "leaf"},
                {"label": "पायरोलिसिस (Pyrolysis): ऑक्सीजन की पूर्ण अनुपस्थिति में कचरे का तापीय अपघटन; जैव-तेल और गैस का उत्पादन", "type": "leaf"},
                {"label": "गैसीकरण (Gasification): सीमित ऑक्सीजन में उच्च तापमान पर कार्बनिक पदार्थों को सिनगैस (CO + H2) में परिवर्तित करना", "type": "leaf"}
            ]},
            {"label": "जैविक तकनीकें", "type": "branch", "date": "जैविक", "children": [
                {"label": "बायोमेथेनेशन (अवायवीय): मीथेन युक्त बायोगैस और खाद का उत्पादन करने के लिए अवायवीय बैक्टीरिया द्वारा गीले कचरे का अपघटन", "type": "leaf"},
                {"label": "कम्पोस्टिंग (Composting): जैविक कचरे को ढेर में रखकर हवा की उपस्थिति में कृषि खाद का निर्माण करना", "type": "leaf"}
            ]},
            {"label": "आरडीएफ (RDF) तकनीक", "type": "branch", "date": "RDF", "children": [
                {"label": "पेलेटाइजेशन (Pelletization): औद्योगिक बॉयलरों के लिए सूखे कचरे (कागज, प्लास्टिक) को ईंधन की गोलियों (Pellets) में बदलना", "type": "leaf"}
            ]},
            {"label": "यूपीएससी परीक्षा दृष्टिकोण", "type": "branch", "date": "परीक्षा", "children": [
                {"label": "चुनौतियां: भारतीय नगरपालिका कचरे में नमी अधिक (~50%) और कैलोरी मान कम होता है, जिससे सीधे दहन करना कठिन होता है", "type": "leaf"},
                {"label": "उड़ती राख (Fly ash): भस्मीकरण के बाद बचने वाला कचरा; निपटान से पहले भारी धातुओं के रिसाव को रोकना आवश्यक", "type": "leaf"}
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
    "between": "के बीच",
    "waste": "अपशिष्ट (कचरा)",
    "management": "प्रबंधन",
    "basel": "बेसल",
    "convention": "कन्वेंशन (सम्मेलन)",
    "bio": "जैव",
    "medical": "चिकित्सा",
    "rules": "नियम",
    "biomedical": "जैव-चिकित्सा",
    "status": "स्थिति",
    "india": "भारत",
    "plastic": "प्लास्टिक",
    "plastics": "प्लास्टिक",
    "hazardous": "खतरनाक",
    "trans": "सीमा",
    "boundary": "पार",
    "movement": "संचलन",
    "characteristics": "लक्षण",
    "treatment": "उपचार",
    "associated": "संबद्ध",
    "importance": "महत्व",
    "issues": "चुनौतियाँ (मुद्दे)",
    "solid": "ठोस",
    "steps": "कदम",
    "taken": "उठाए गए",
    "combating": "निपटने",
    "mounting": "बढ़ते",
    "stockholm": "स्टॉकहोम",
    "persistent": "स्थायी",
    "organic": "कार्बनिक",
    "technologies": "तकनीकें",
    "generation": "उत्पादन",
    "energy": "ऊर्जा",
    "from": "से",
    "tourism": "पर्यटन",
    "initiative": "पहल",
    "treatments": "उपचार",
    "methods": "विधियाँ",
    "types": "प्रकार"
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
                {"label": f"Definition: Understanding the fundamental characteristics, regulatory parameters, and scope of {t}", "type": "leaf"},
                {"label": f"Scientific Framework: Analyzing how {t} integrates with environmental waste management systems", "type": "leaf"}
            ]
        },
        {
            "label": f"Processes & Dynamics",
            "type": "branch",
            "date": "Mechanisms",
            "children": [
                {"label": f"Primary Drivers: Factors regulating the generation, segregation, and processing of {t}", "type": "leaf"},
                {"label": f"Spatial Distribution: Exploring the national hotspots and regional handling structures of {t}", "type": "leaf"}
            ]
        },
        {
            "label": f"Ecological & Applied Values",
            "type": "branch",
            "date": "Applications",
            "children": [
                {"label": f"Impacts: How changes in {t} affect regional sanitation, soil/water resources, and public health", "type": "leaf"},
                {"label": f"Case Studies: Notable real-world initiatives and circular economy models relating to {t}", "type": "leaf"}
            ]
        },
        {
            "label": f"UPSC Exam Syllabus Relevance",
            "type": "branch",
            "date": "UPSC Core",
            "children": [
                {"label": f"Prelims Prep: Key regulatory limits, legal authorities, and compliance exceptions associated with {t}", "type": "leaf"},
                {"label": f"Mains Answer Writing: Linking {t} with contemporary zero-waste goals, urban local bodies, and national waste policies", "type": "leaf"}
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
                {"label": f"परिभाषा: {t} की बुनियादी विशेषताओं, विनियामक मानकों और कार्यक्षेत्र को समझना", "type": "leaf"},
                {"label": f"वैज्ञानिक ढांचा: {t} अपशिष्ट प्रबंधन और पर्यावरण स्वच्छता प्रणालियों के साथ कैसे कार्य करता है", "type": "leaf"}
            ]
        },
        {
            "label": f"प्रक्रियाएं और गतिकी",
            "type": "branch",
            "date": "क्रियाविधि",
            "children": [
                {"label": f"प्राथमिक कारक: {t} के उत्पादन, पृथक्करण और प्रसंस्करण को नियंत्रित करने वाले तत्व", "type": "leaf"},
                {"label": f"स्थानिक वितरण: देश में {t} के भौगोलिक हॉटस्पॉट और स्थानीय हैंडलिंग संरचनाओं का अध्ययन", "type": "leaf"}
            ]
        },
        {
            "label": f"पारिस्थितिक और व्यावहारिक महत्व",
            "type": "branch",
            "date": "महत्व",
            "children": [
                {"label": f"प्रभाव: {t} में परिवर्तन क्षेत्रीय स्वच्छता, संसाधन प्रदूषण और सार्वजनिक स्वास्थ्य को कैसे प्रभावित करते हैं", "type": "leaf"},
                {"label": f"क्षेत्रीय मामले: {t} से संबंधित उल्लेखनीय वैश्विक उदाहरण और चक्रीय अर्थव्यवस्था (Circular Economy) मॉडल", "type": "leaf"}
            ]
        },
        {
            "label": f"यूपीएससी परीक्षा दृष्टिकोण (UPSC Focus)",
            "type": "branch",
            "date": "परीक्षा",
            "children": [
                {"label": f"प्रारंभिक परीक्षा: {t} से जुड़े विनियामक नियम, कानूनी प्राधिकरण और सामान्य परीक्षा भ्रम", "type": "leaf"},
                {"label": f"मुख्य परीक्षा उत्तर लेखन: {t} को राष्ट्रीय अपशिष्ट नीतियों, शून्य-अपशिष्ट लक्ष्यों और शहरी स्थानीय निकायों से जोड़ना", "type": "leaf"}
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

    # Second pass: process and patch all index.html files
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
