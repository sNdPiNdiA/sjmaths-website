#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import re
import json

BASE_DIR = r"upsc/environment/Climate-Change-Environmental-Administration"

def get_clean_title(folder_name):
    title = re.sub(r'([a-z])([A-Z])', r'\1 \2', folder_name)
    title = title.replace('-', ' ')
    words = []
    acronyms = {'dpsp', 'pri', 'ut', 'uts', 'sc', 'hc', 'cm', 'com', 'arc', 'inc', 'ias', 'sec', 'sfc', 'pej', 'tej', 'mjo', 'enso', 'iod', 'icar', 'gst', 'dpc', 'mpc', 'adc', 'tac', 'scs', 'pesa', 'icar', 'isfr', 'itcz', 'tej', 'iucn', 'wpa', 'grap', 'aqews', 'caaeqms', 'naqi', 'naaqs', 'rspm', 'bod', 'cod', 'swm', 'epr', 'rohs', 'pop', 'pops', 'unep', 'undp', 'unfccc', 'unccd', 'ipcc', 'cop', 'eia', 'epa', 'campa', 'cza', 'awbi', 'bsi', 'zsi', 'fsi', 'nbwl', 'ntca', 'wccb', 'bnhs', 'sdg', 'sdgs', 'teeb', 'ecbc', 'bee', 'griha', 'nzeb', 'nicra', 'lteo', 'natcom', 'nggip'}
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
        "keys": ["adaptation-fund", "biocarbon-fund", "clean-technology-fund", "climate-investment-fund", "global-climate-finance", "global-environment-facility", "gef", "green-climate-fund", "gcf", "least-developed-countries-fund", "ldcf", "special-climate-change-fund", "sccf", "national-adaptation-fund-for-climate-change", "nafcc"],
        "en": [
            {"label": "Global Climate Finance", "type": "branch", "date": "UNFCCC Funds", "children": [
                {"label": "Green Climate Fund (GCF): Established under COP-16 in Cancun; channels finance from developed nations to help developing countries limit emissions and adapt to climate change", "type": "leaf"},
                {"label": "Global Environment Facility (GEF): Serves as financial mechanism for conventions like CBD, UNFCCC, UNCCD, Stockholm (POPs), and Minamata (Mercury)", "type": "leaf"},
                {"label": "Specialized Funds: Least Developed Countries Fund (LDCF) and Special Climate Change Fund (SCCF) are managed by GEF; Adaptation Fund (AF) operates under Kyoto Protocol", "type": "leaf"}
            ]},
            {"label": "India Adaptation Finance", "type": "branch", "date": "India NAFCC", "children": [
                {"label": "NAFCC: National Adaptation Fund for Climate Change; launched in 2015 to support adaptation projects across vulnerable Indian states, implemented via NABARD", "type": "leaf"}
            ]},
            {"label": "UPSC Exam Focus", "type": "branch", "date": "UPSC Focus", "children": [
                {"label": "GCF Target: Aimed to mobilize $100 billion per year by 2020; operates with a balanced allocation between adaptation and mitigation projects", "type": "leaf"}
            ]}
        ],
        "hi": [
            {"label": "वैश्विक जलवायु वित्त", "type": "branch", "date": "वैश्विक", "children": [
                {"label": "हरित जलवायु कोष (GCF): कैनकन में COP-16 के तहत स्थापित; विकासशील देशों को उत्सर्जन कम करने और अनुकूलन में मदद करता है", "type": "leaf"},
                {"label": "वैश्विक पर्यावरण सुविधा (GEF): CBD, UNFCCC, UNCCD और मिनामाता कन्वेंशनों के लिए वित्तीय तंत्र के रूप में कार्य करता है", "type": "leaf"},
                {"label": "विशिष्ट कोष: LDCF और SCCF का प्रबंधन GEF द्वारा किया जाता है; अनुकूलन कोष (AF) क्योटो प्रोटोकॉल के तहत काम करता है", "type": "leaf"}
            ]},
            {"label": "भारत अनुकूलन वित्त", "type": "branch", "date": "भारत NAFCC", "children": [
                {"label": "NAFCC: राष्ट्रीय जलवायु परिवर्तन अनुकूलन कोष; 2015 में संवेदनशील राज्यों के अनुकूलन कार्यों के लिए शुरू, नाबार्ड द्वारा कार्यान्वित", "type": "leaf"}
            ]},
            {"label": "यूपीएससी परीक्षा दृष्टिकोण", "type": "branch", "date": "परीक्षा", "children": [
                {"label": "GCF लक्ष्य: प्रति वर्ष $100 बिलियन जुटाने का संकल्प; अनुकूलन और शमन परियोजनाओं के बीच संतुलित आवंटन सुनिश्चित करना", "type": "leaf"}
            ]}
        ]
    },
    {
        "keys": ["bharat-stage-norms", "fame-india-programme"],
        "en": [
            {"label": "Bharat Stage (BS) Norms", "type": "branch", "date": "BS-VI", "children": [
                {"label": "BS-VI Transition: Implemented in April 2020 directly skipping BS-V; reduces sulfur content from 50 ppm (BS-IV) to 10 ppm, matching Euro-6 standards", "type": "leaf"},
                {"label": "Emission cuts: Reduces Particulate Matter (PM2.5) by 80% and Nitrogen Oxides (NOx) by 70% in diesel engines", "type": "leaf"}
            ]},
            {"label": "FAME India Scheme", "type": "branch", "date": "FAME", "children": [
                {"label": "FAME Scheme: Faster Adoption and Manufacturing of Hybrid and Electric Vehicles; launched under National Electric Mobility Mission Plan", "type": "leaf"},
                {"label": "Subsidy model: Promotes adoption of public transport electrification, electric 2/3/4-wheelers through demand incentives", "type": "leaf"}
            ]},
            {"label": "UPSC Exam Focus", "type": "branch", "date": "UPSC Focus", "children": [
                {"label": "Selective Catalytic Reduction (SCR): Technology used in BS-VI diesel vehicles injecting urea-based solution (AdBlue) to reduce NOx emissions", "type": "leaf"}
            ]}
        ],
        "hi": [
            {"label": "भारत स्टेज (BS) मानक", "type": "branch", "date": "BS-VI", "children": [
                {"label": "BS-VI संक्रमण: अप्रैल 2020 में BS-V को छोड़कर सीधे लागू; सल्फर सामग्री को 50 ppm से घटाकर 10 ppm करता है", "type": "leaf"},
                {"label": "उत्सर्जन में कमी: डीजल इंजनों में PM2.5 को 80% और नाइट्रोजन ऑक्साइड (NOx) को 70% तक कम करता है", "type": "leaf"}
            ]},
            {"label": "FAME इंडिया योजना", "type": "branch", "date": "FAME", "children": [
                {"label": "FAME योजना: हाइब्रिड और इलेक्ट्रिक वाहनों का तेजी से अपनाना और निर्माण; राष्ट्रीय इलेक्ट्रिक मोबिलिटी मिशन के तहत शुरू", "type": "leaf"},
                {"label": "सब्सिडी मॉडल: मांग प्रोत्साहनों के माध्यम से सार्वजनिक परिवहन के विद्युतीकरण, ई-वाहनों को बढ़ावा देता है", "type": "leaf"}
            ]},
            {"label": "यूपीएससी परीक्षा दृष्टिकोण", "type": "branch", "date": "परीक्षा", "children": [
                {"label": "चयनित उत्प्रेरक कमी (SCR): BS-VI diesel वाहनों में NOx को कम करने के लिए यूरिया आधारित घोल (AdBlue) इंजेक्ट करने की तकनीक", "type": "leaf"}
            ]}
        ]
    },
    {
        "keys": ["biological-diversity-act-2002", "national-biodiversity-authority", "nba"],
        "en": [
            {"label": "Three-Tier Structure", "type": "branch", "date": "Governance", "children": [
                {"label": "National level: National Biodiversity Authority (NBA) established in 2003, headquartered in Chennai; grants approval for bio-resource access", "type": "leaf"},
                {"label": "State level: State Biodiversity Boards (SBBs) regulating commercial utilization of bio-resources by Indians", "type": "leaf"},
                {"label": "Local level: Biodiversity Management Committees (BMCs) in local bodies; maintains Peoples' Biodiversity Registers (PBR) to document local flora/fauna", "type": "leaf"}
            ]},
            {"label": "Key Mandates", "type": "branch", "date": "Mandates", "children": [
                {"label": "Benefit Sharing: Fair sharing of benefits arising from access to genetic resources with local communities (traditional knowledge holders)", "type": "leaf"},
                {"label": "Biodiversity Heritage Sites (BHS): State governments can declare sites of high ecological significance as heritage zones (e.g. Majuli, Ameenpur lake)", "type": "leaf"}
            ]},
            {"label": "UPSC Exam Focus", "type": "branch", "date": "UPSC Focus", "children": [
                {"label": "Convention Link: Enacted in 2002 to give legal effect to India's obligations under United Nations Convention on Biological Diversity (CBD)", "type": "leaf"}
            ]}
        ],
        "hi": [
            {"label": "त्रि-स्तरीय ढांचा", "type": "branch", "date": "शासन", "children": [
                {"label": "राष्ट्रीय स्तर: राष्ट्रीय जैव विविधता प्राधिकरण (NBA) 2003 में स्थापित, मुख्यालय चेन्नई; जैव-संसाधन पहुंच को मंजूरी देता है", "type": "leaf"},
                {"label": "राज्य स्तर: राज्य जैव विविधता बोर्ड (SBBs) भारतीयों द्वारा जैव-संसाधनों के व्यावसायिक उपयोग को नियंत्रित करते हैं", "type": "leaf"},
                {"label": "स्थानीय स्तर: स्थानीय निकायों में जैव विविधता प्रबंधन समितियाँ (BMCs); स्थानीय प्रजातियों के प्रलेखन हेतु लोक जैव विविधता रजिस्टर (PBR) बनाती हैं", "type": "leaf"}
            ]},
            {"label": "मुख्य नियम", "type": "branch", "date": "नियम", "children": [
                {"label": "लाभ साझाकरण: स्थानीय समुदायों के साथ आनुवंशिक संसाधनों के उपयोग से प्राप्त लाभों का निष्पक्ष और न्यायसंगत बंटवारा", "type": "leaf"},
                {"label": "जैव विविधता विरासत स्थल (BHS): राज्य सरकारें उच्च पारिस्थितिक महत्व के स्थलों को विरासत क्षेत्र घोषित कर सकती हैं (जैसे मजुली)", "type": "leaf"}
            ]},
            {"label": "यूपीएससी परीक्षा दृष्टिकोण", "type": "branch", "date": "परीक्षा", "children": [
                {"label": "कन्वेंशन संबंध: जैव विविधता पर संयुक्त राष्ट्र कन्वेंशन (CBD) के तहत भारत के दायित्वों को पूरा करने के लिए 2002 में अधिनियमित", "type": "leaf"}
            ]}
        ]
    },
    {
        "keys": ["bombay-natural-history-society", "bnhs", "birdlife-international"],
        "en": [
            {"label": "BNHS Overview", "type": "branch", "date": "NGO", "children": [
                {"label": "Foundation: Founded in 1883; premier NGO engaged in conservation research of flora and fauna in India, based in Mumbai", "type": "leaf"},
                {"label": "Key Journal: Publishes the Journal of the Bombay Natural History Society and Hornbill magazine", "type": "leaf"}
            ]},
            {"label": "BirdLife Partnership", "type": "branch", "date": "Global Link", "children": [
                {"label": "Important Bird Areas (IBAs): Designated partner of BirdLife International; identifies and monitors IBAs critical for avian conservation", "type": "leaf"},
                {"label": "Vulture recovery: Plays central role in establishing vulture breeding centers in India to combat diclofenac toxicity", "type": "leaf"}
            ]}
        ],
        "hi": [
            {"label": "BNHS का अवलोकन", "type": "branch", "date": "गैर-सरकारी संगठन", "children": [
                {"label": "स्थापना: 1883 में स्थापित; मुंबई में स्थित भारत में वनस्पतियों और जीवों के संरक्षण अनुसंधान में संलग्न प्रमुख NGO", "type": "leaf"},
                {"label": "प्रमुख पत्रिका: जर्नल ऑफ द बॉम्बे नेचुरल हिस्ट्री सोसाइटी और हॉर्नबिल पत्रिका का प्रकाशन", "type": "leaf"}
            ]},
            {"label": "बर्डलाइफ साझेदारी", "type": "branch", "date": "साझेदारी", "children": [
                {"label": "महत्वपूर्ण पक्षी क्षेत्र (IBAs): बर्डलाइफ इंटरनेशनल का भागीदार; पक्षी संरक्षण के लिए महत्वपूर्ण IBAs की पहचान और निगरानी करता है", "type": "leaf"},
                {"label": "गिद्ध संरक्षण: डाइक्लोफेनाक विषाक्तता से निपटने के लिए भारत में गिद्ध प्रजनन केंद्रों की स्थापना में केंद्रीय भूमिका", "type": "leaf"}
            ]}
        ]
    },
    {
        "keys": ["botanical-survey-of-india", "bsi", "zoological-survey-of-india", "zsi", "forest-survey-of-india", "fsi"],
        "en": [
            {"label": "BSI & ZSI Surveys", "type": "branch", "date": "Surveys", "children": [
                {"label": "BSI (1890): Botanical Survey of India, headquartered in Kolkata; explores plant resources and identifies red-listed flora", "type": "leaf"},
                {"label": "ZSI (1916): Zoological Survey of India, headquartered in Kolkata; systematically surveys animal taxonomy and species inventory", "type": "leaf"}
            ]},
            {"label": "Forest Survey of India (FSI)", "type": "branch", "date": "FSI", "children": [
                {"label": "FSI (1981): Based in Dehradun; monitors forest resources using satellite remote sensing", "type": "leaf"},
                {"label": "ISFR: Publishes the India State of Forest Report biennially, detailing forest cover, tree cover, and carbon stock estimates", "type": "leaf"}
            ]}
        ],
        "hi": [
            {"label": "BSI और ZSI सर्वेक्षण", "type": "branch", "date": "सर्वेक्षण", "children": [
                {"label": "BSI (1890): भारतीय वनस्पति सर्वेक्षण, मुख्यालय कोलकाता; पादप संसाधनों की खोज और लाल सूची वाली वनस्पतियों की पहचान", "type": "leaf"},
                {"label": "ZSI (1916): भारतीय प्राणी सर्वेक्षण, मुख्यालय कोलकाता; पशु वर्गीकरण और प्रजातियों की सूची का व्यवस्थित सर्वेक्षण", "type": "leaf"}
            ]},
            {"label": "भारतीय वन सर्वेक्षण (FSI)", "type": "branch", "date": "FSI", "children": [
                {"label": "FSI (1981): देहरादून में स्थित; उपग्रह रिमोट सेंसिंग का उपयोग करके वन संसाधनों की निगरानी करता है", "type": "leaf"},
                {"label": "ISFR: द्विवार्षिक रूप से भारत वन स्थिति रिपोर्ट प्रकाशित करता है, जिसमें वन आवरण और कार्बन स्टॉक का विवरण होता है", "type": "leaf"}
            ]}
        ]
    },
    {
        "keys": ["campa"],
        "en": [
            {"label": "Compensatory Afforestation", "type": "branch", "date": "CAMPA Act 2016", "children": [
                {"label": "Core Mandate: Developers clearing forest land for non-forest projects must pay for afforestation on equivalent non-forest land", "type": "leaf"},
                {"label": "Net Present Value (NPV): Developers must pay the NPV of the diverted forest, which is calculated based on forest type and density", "type": "leaf"}
            ]},
            {"label": "Fund Sharing Model", "type": "branch", "date": "Funds", "children": [
                {"label": "90-10 split: 90% of CAMPA funds go directly to State Compensatory Afforestation Funds; 10% is retained by the Central National Fund", "type": "leaf"},
                {"label": "Audit: Funds are kept in public interest-bearing accounts under Public Account of India to prevent diversion of money", "type": "leaf"}
            ]}
        ],
        "hi": [
            {"label": "प्रतिपूरक वनीकरण", "type": "branch", "date": "कैम्पा अधिनियम 2016", "children": [
                {"label": "मुख्य नियम: गैर-वन परियोजनाओं के लिए वन भूमि काटने वाले विकासकर्ताओं को समकक्ष गैर-वन भूमि पर वनीकरण का भुगतान करना होगा", "type": "leaf"},
                {"label": "शुद्ध वर्तमान मूल्य (NPV): विकासकर्ताओं को डायवर्ट किए गए वन का NPV भुगतान करना होगा, जो वन प्रकार और घनत्व पर आधारित होता है", "type": "leaf"}
            ]},
            {"label": "फंड शेयरिंग Model", "type": "branch", "date": "फंड", "children": [
                {"label": "90-10 विभाजन: कैम्पा फंड का 90% सीधे राज्य प्रतिपूरक वनीकरण कोषों को जाता है; 10% केंद्रीय राष्ट्रीय कोष में रखा जाता है", "type": "leaf"},
                {"label": "लेखापरीक्षा: धन के दुरुपयोग को रोकने के लिए कैम्पा फंड को भारत के लोक खाते (Public Account) के तहत ब्याज वाले खातों में रखा जाता है", "type": "leaf"}
            ]}
        ]
    },
    {
        "keys": ["carbon-footprint", "ecological-footprint"],
        "en": [
            {"label": "Ecological Footprint", "type": "branch", "date": "Metrics", "children": [
                {"label": "Definition: Measures human demand on nature, comparing resource consumption to the Earth's regenerative biocapacity", "type": "leaf"},
                {"label": "Global Footprint Network: Standardizes measurement in global hectares (gha); shows how many Earths are needed to support humans", "type": "leaf"}
            ]},
            {"label": "Carbon Footprint", "type": "branch", "date": "GHG", "children": [
                {"label": "Definition: Total greenhouse gas emissions caused directly and indirectly by an individual, organization, or product, expressed in CO2 equivalents", "type": "leaf"}
            ]},
            {"label": "UPSC Exam Focus", "type": "branch", "date": "UPSC Focus", "children": [
                {"label": "Earth Overshoot Day: The date when humanity's resource consumption exceeds Earth's biocapacity for that year, calculated by Global Footprint Network", "type": "leaf"}
            ]}
        ],
        "hi": [
            {"label": "पारिस्थितिक पदचिह्न", "type": "branch", "date": "माप", "children": [
                {"label": "परिभाषा: प्रकृति पर मानव मांग का माप, जिसमें उपभोग की तुलना पृथ्वी की पुनर्योजी जैव-क्षमता (Biocapacity) से की जाती है", "type": "leaf"},
                {"label": "ग्लोबल फुटप्रिंट नेटवर्क: मापन को वैश्विक हेक्टेयर (gha) में मानकीकृत करता है; दर्शाता है कि मनुष्यों को बनाए रखने के लिए कितनी पृथ्वी की आवश्यकता है", "type": "leaf"}
            ]},
            {"label": "कार्बन पदचिह्न", "type": "branch", "date": "GHG", "children": [
                {"label": "परिभाषा: किसी व्यक्ति, संगठन या उत्पाद द्वारा प्रत्यक्ष और अप्रत्यक्ष रूप से उत्पन्न कुल ग्रीनहाउस गैस उत्सर्जन, CO2 समकक्ष में व्यक्त", "type": "leaf"}
            ]},
            {"label": "यूपीएससी परीक्षा दृष्टिकोण", "type": "branch", "date": "परीक्षा", "children": [
                {"label": "अर्थ ओवरशूट डे: वह तारीख जब मानवता का वार्षिक संसाधन उपभोग उस वर्ष के लिए पृथ्वी की जैव-क्षमता से अधिक हो जाता है", "type": "leaf"}
            ]}
        ]
    },
    {
        "keys": ["central-zoo-authority", "cza", "national-board-for-wildlife", "nbwl", "national-tiger-conservation-authority", "ntca", "wildlife-crime-control-bureau", "wccb"],
        "en": [
            {"label": "NBWL & CZA Bodies", "type": "branch", "date": "Statutory", "children": [
                {"label": "National Board for Wildlife (NBWL): Statutory body chaired by Prime Minister under WPA 1972; highest authority to approve projects in protected areas", "type": "leaf"},
                {"label": "Central Zoo Authority (CZA): Regulates zoo standards and animal exchange programs, established under WPA 1972", "type": "leaf"}
            ]},
            {"label": "NTCA & WCCB Bodies", "type": "branch", "date": "Statutory", "children": [
                {"label": "National Tiger Conservation Authority (NTCA): Statutory body under Ministry of Environment; coordinates Project Tiger and tiger censuses", "type": "leaf"},
                {"label": "Wildlife Crime Control Bureau (WCCB): Statutory body created to combat organized wildlife crime and illegal trade, collects intelligence", "type": "leaf"}
            ]}
        ],
        "hi": [
            {"label": "NBWL और CZA निकाय", "type": "branch", "date": "वैधानिक", "children": [
                {"label": "राष्ट्रीय वन्यजीव बोर्ड (NBWL): प्रधान मंत्री की अध्यक्षता में WPA 1972 के तहत वैधानिक निकाय; संरक्षित क्षेत्रों में परियोजनाओं को मंजूरी देने वाला सर्वोच्च निकाय", "type": "leaf"},
                {"label": "केंद्रीय चिड़ियाघर प्राधिकरण (CZA): चिड़ियाघरों के मानकों और पशु विनिमय कार्यक्रमों को नियंत्रित करता है, WPA 1972 के तहत स्थापित", "type": "leaf"}
            ]},
            {"label": "NTCA और WCCB निकाय", "type": "branch", "date": "वैधानिक", "children": [
                {"label": "राष्ट्रीय बाघ संरक्षण प्राधिकरण (NTCA): पर्यावरण मंत्रालय के तहत वैधानिक निकाय; प्रोजेक्ट टाइगर और बाघ गणना का समन्वय करता है", "type": "leaf"},
                {"label": "वन्यजीव अपराध नियंत्रण ब्यूरो (WCCB): संगठित वन्यजीव अपराध और अवैध व्यापार से निपटने के लिए बनाया गया वैधानिक निकाय", "type": "leaf"}
            ]}
        ]
    },
    {
        "keys": ["coastal-regulation-zone", "crz"],
        "en": [
            {"label": "CRZ Classifications", "type": "branch", "date": "CRZ Notification", "children": [
                {"label": "CRZ-I: Ecologically sensitive zones (mangroves, coral reefs, turtle nesting grounds); construction is strictly prohibited", "type": "leaf"},
                {"label": "CRZ-II: Urbanized coastal areas; construction of buildings is allowed only on the landward side of existing roads/structures", "type": "leaf"},
                {"label": "CRZ-III: Rural areas; divided into CRZ-III A (highly populated, 50m No Development Zone) and CRZ-III B (low population density, 200m NDZ)", "type": "leaf"},
                {"label": "CRZ-IV: Water areas from Low Tide Line (LTL) up to 12 nautical miles (territorial waters) and tidal water bodies", "type": "leaf"}
            ]},
            {"label": "Legal Foundation", "type": "branch", "date": "EPA 1986", "children": [
                {"label": "EIA Link: Promulgated under Environment Protection Act 1986; aims to secure livelihoods of fishing communities and conserve coastal morphology", "type": "leaf"}
            ]}
        ],
        "hi": [
            {"label": "CRZ का वर्गीकरण", "type": "branch", "date": "CRZ अधिसूचना", "children": [
                {"label": "CRZ-I: पारिस्थितिक रूप से संवेदनशील क्षेत्र (मैंग्रोव, प्रवाल भित्तियाँ, कछुआ घोंसला मैदान); निर्माण गतिविधियों पर पूर्ण प्रतिबंध", "type": "leaf"},
                {"label": "CRZ-II: शहरी तटीय क्षेत्र; मौजूदा सड़कों/संरचनाओं के केवल भू-भाग की ओर ही निर्माण की अनुमति दी जाती है", "type": "leaf"},
                {"label": "CRZ-III: ग्रामीण क्षेत्र; इसे CRZ-III A (अधिक आबादी, 50 मीटर का नो डेवलपमेंट ज़ोन) और CRZ-III B (कम आबादी, 200 मीटर का NDZ) में बांटा गया है", "type": "leaf"},
                {"label": "CRZ-IV: निम्न ज्वार रेखा (LTL) से 12 समुद्री मील (क्षेत्रीय जल) तक का जल क्षेत्र और ज्वारीय जल निकाय", "type": "leaf"}
            ]},
            {"label": "कानूनी आधार", "type": "branch", "date": "EPA 1986", "children": [
                {"label": "संबद्ध अधिनियम: पर्यावरण संरक्षण अधिनियम 1986 के तहत घोषित; मछली पकड़ने वाले समुदायों की आजीविका सुरक्षित करना और तटीय संरक्षण", "type": "leaf"}
            ]}
        ]
    },
    {
        "keys": ["constitutional-provisions-related-to-environment"],
        "en": [
            {"label": "Directive Principles (DPSP)", "type": "branch", "date": "Article 48A", "children": [
                {"label": "Article 48A: Mandates that the State shall endeavor to protect and improve the environment and safeguard forests and wildlife", "type": "leaf"}
            ]},
            {"label": "Fundamental Duties", "type": "branch", "date": "Article 51A(g)", "children": [
                {"label": "Article 51A(g): Duty of every citizen of India to protect and improve the natural environment including forests, lakes, rivers, and wildlife", "type": "leaf"}
            ]},
            {"label": "42nd Amendment 1976", "type": "branch", "date": "1976", "children": [
                {"label": "Transfer of subjects: Shifted 'Forests' and 'Protection of Wild Animals and Birds' from the State List to the Concurrent List, empowering Parliament to legislate", "type": "leaf"}
            ]}
        ],
        "hi": [
            {"label": "राज्य के नीति निर्देशक तत्व", "type": "branch", "date": "अनुच्छेद 48A", "children": [
                {"label": "अनुच्छेद 48A: प्रावधान करता है कि राज्य पर्यावरण के संरक्षण तथा संवर्धन का और वन तथा वन्यजीवों की रक्षा करने का प्रयास करेगा", "type": "leaf"}
            ]},
            {"label": "मौलिक कर्तव्य", "type": "branch", "date": "अनुच्छेद 51A(g)", "children": [
                {"label": "अनुच्छेद 51A(g): भारत के प्रत्येक नागरिक का यह कर्तव्य होगा कि वह वनों, झीलों, नदियों और वन्यजीवों सहित प्राकृतिक पर्यावरण की रक्षा और सुधार करे", "type": "leaf"}
            ]},
            {"label": "42वां संशोधन 1976", "type": "branch", "date": "1976", "children": [
                {"label": "विषयों का स्थानांतरण: 'वन' और 'वन्य जीवों तथा पक्षियों के संरक्षण' को राज्य सूची से समवर्ती सूची में स्थानांतरित किया, जिससे संसद को कानून बनाने का अधिकार मिला", "type": "leaf"}
            ]}
        ]
    },
    {
        "keys": ["environment-impact-assessment", "eia", "brief-history-of-eia", "drawback-in-eia", "recommendations-for-improvement-of-eia"],
        "en": [
            {"label": "Four Stages of EIA", "type": "branch", "date": "Process", "children": [
                {"label": "Screening: Determining if a project requires environmental clearance; splits projects into Category A (requires central clearance) and Category B (state level)", "type": "leaf"},
                {"label": "Scoping: Formulating terms of reference (ToR) detailing key environmental impacts that must be investigated in the EIA report", "type": "leaf"},
                {"label": "Public Consultation: Public hearing held near the project site where local communities voice concerns over proposed activities", "type": "leaf"},
                {"label": "Appraisal: Expert Appraisal Committee (EAC) reviews the EIA report and public comments to recommend approval or rejection to MoEFCC", "type": "leaf"}
            ]},
            {"label": "Legal Foundation & Issues", "type": "branch", "date": "EPA 1986", "children": [
                {"label": "EIA Notification 2006: Issued under Section 3 of the Environment Protection Act 1986; makes environmental clearance mandatory for 39 categories of projects", "type": "leaf"},
                {"label": "Weaknesses: Late public hearings (held after project planning is finished), lack of independent monitoring of EIA reports, and frequent exemptions for strategic projects", "type": "leaf"}
            ]}
        ],
        "hi": [
            {"label": "EIA के चार चरण", "type": "branch", "date": "प्रक्रिया", "children": [
                {"label": "स्क्रीनिंग (Screening): यह निर्धारित करना कि क्या परियोजना को मंजूरी की आवश्यकता है; परियोजनाओं को श्रेणी A (केंद्रीय) और श्रेणी B (राज्यीय) में विभाजित करता है", "type": "leaf"},
                {"label": "स्कोपिंग (Scoping): संदर्भ की शर्तों (ToR) को तैयार करना, जिसमें EIA रिपोर्ट में जांच किए जाने वाले पर्यावरणीय प्रभावों का विवरण होता है", "type": "leaf"},
                {"label": "जनसुनवाई (Public Hearing): परियोजना स्थल के पास आयोजित, जहां स्थानीय समुदाय प्रस्तावित गतिविधियों पर अपनी चिंताएं साझा करते हैं", "type": "leaf"},
                {"label": "मूल्यांकन (Appraisal): विशेषज्ञ मूल्यांकन समिति (EAC) मंजूरी या अस्वीकृति की सिफारिश करने के लिए रिपोर्ट और सार्वजनिक टिप्पणियों की समीक्षा करती है", "type": "leaf"}
            ]},
            {"label": "कानूनी आधार और कमियाँ", "type": "branch", "date": "नियम", "children": [
                {"label": "EIA अधिसूचना 2006: पर्यावरण संरक्षण अधिनियम 1986 की धारा 3 के तहत जारी; 39 श्रेणियों की परियोजनाओं के लिए पर्यावरण मंजूरी अनिवार्य बनाता है", "type": "leaf"},
                {"label": "कमियां: देर से जनसुनवाई (परियोजना योजना तैयार होने के बाद), स्वतंत्र मॉनिटरिंग की कमी और सामरिक परियोजनाओं को बार-बार मिलने वाली छूट", "type": "leaf"}
            ]}
        ]
    },
    {
        "keys": ["environmental-protection-act", "epa"],
        "en": [
            {"label": "Core Mandates & Origin", "type": "branch", "date": "EPA 1986", "children": [
                {"label": "Origin: Enacted in 1986 under Article 253 of the Constitution, following the Bhopal Gas Tragedy of 1984; implements decisions of the Stockholm Conference 1972", "type": "leaf"},
                {"label": "Umbrella Legislation: Provides a comprehensive framework for central government coordination of state boards (CPCB, SPCB) and fills legal gaps in Air/Water Acts", "type": "leaf"}
            ]},
            {"label": "Key Powers", "type": "branch", "date": "Powers", "children": [
                {"label": "Standards: Central government is empowered to lay down standards for emissions, discharge of environmental pollutants, and handling hazardous substances", "type": "leaf"},
                {"label": "Closure: Section 5 empowers the government to direct the closure, prohibition, or regulation of any industrial operation, and cut off electricity/water supply", "type": "leaf"}
            ]}
        ],
        "hi": [
            {"label": "मुख्य नियम और उत्पत्ति", "type": "branch", "date": "EPA 1986", "children": [
                {"label": "उत्पत्ति: 1984 की भोपाल गैस त्रासदी के बाद संविधान के अनुच्छेद 253 के तहत 1986 में अधिनियमित; स्टॉकहोम सम्मेलन 1972 के निर्णयों को लागू करता है", "type": "leaf"},
                {"label": "अम्ब्रेला कानून (Umbrella Act): केंद्रीय सरकार को राज्य बोर्डों के समन्वय के लिए एक व्यापक ढांचा प्रदान करता है और वायु/जल कानूनों की कानूनी कमियों को भरता है", "type": "leaf"}
            ]},
            {"label": "प्रमुख शक्तियाँ", "type": "branch", "date": "शक्तियाँ", "children": [
                {"label": "मानक: केंद्र सरकार को पर्यावरण प्रदूषकों के उत्सर्जन और खतरनाक पदार्थों के रखरखाव के लिए मानक तय करने का अधिकार है", "type": "leaf"},
                {"label": "बंद करना: धारा 5 सरकार को किसी भी औद्योगिक इकाई को बंद करने, प्रतिबंधित करने या उसका विनियमन करने तथा बिजली/पानी की आपूर्ति काटने का अधिकार देती है", "type": "leaf"}
            ]}
        ]
    },
    {
        "keys": ["national-action-plan-for-climate-change", "napcc", "national-solar-mission", "national-water-mission", "green-india", "enhanced-energy-efficiency", "sustaining-himalayan", "strategic-knowledge", "sustainable-agriculture", "sustainable-habitat", "national-bioenergy-mission"],
        "en": [
            {"label": "Eight Core Missions", "type": "branch", "date": "NAPCC 2008", "children": [
                {"label": "Solar & Energy: National Solar Mission (originally 100 GW target) and National Mission for Enhanced Energy Efficiency (NMEEE; runs the PAT scheme)", "type": "leaf"},
                {"label": "Water & Himalayan: National Water Mission (targets 20% water use efficiency increase) and National Mission for Sustaining the Himalayan Ecosystem (NMSHE)", "type": "leaf"},
                {"label": "Forests & Agriculture: National Mission for a Green India (aims for afforestation of 5m hectares) and National Mission for Sustainable Agriculture (NMSA)", "type": "leaf"},
                {"label": "Habitat & Strategic: National Mission on Sustainable Habitat and National Mission on Strategic Knowledge for Climate Change", "type": "leaf"}
            ]},
            {"label": "UPSC Exam Focus", "type": "branch", "date": "UPSC Focus", "children": [
                {"label": "PAT Scheme: Perform, Achieve, and Trade; market-based mechanism under NMEEE allowing energy-intensive units to trade energy saving certificates (ESCerts)", "type": "leaf"},
                {"label": "Bioenergy Mission: Added recently as the 9th mission to promote waste-to-energy technologies and biofuel blending", "type": "leaf"}
            ]}
        ],
        "hi": [
            {"label": "आठ मुख्य मिशन", "type": "branch", "date": "NAPCC 2008", "children": [
                {"label": "सौर और ऊर्जा: राष्ट्रीय सौर मिशन (100 GW का लक्ष्य) और राष्ट्रीय संवर्धित ऊर्जा दक्षता मिशन (NMEEE; जो PAT योजना चलाता है)", "type": "leaf"},
                {"label": "जल और हिमालयी: राष्ट्रीय जल मिशन (जल उपयोग दक्षता में 20% सुधार का लक्ष्य) और हिमालयी पारिस्थितिकी तंत्र को बनाए रखने का राष्ट्रीय मिशन (NMSHE)", "type": "leaf"},
                {"label": "वन और कृषि: हरित भारत के लिए राष्ट्रीय मिशन (5 मिलियन हेक्टेयर वनीकरण का लक्ष्य) और राष्ट्रीय सतत कृषि मिशन (NMSA)", "type": "leaf"},
                {"label": "आवास और ज्ञान: राष्ट्रीय सतत आवास मिशन और जलवायु परिवर्तन के लिए रणनीतिक ज्ञान पर राष्ट्रीय मिशन", "type": "leaf"}
            ]},
            {"label": "यूपीएससी परीक्षा दृष्टिकोण", "type": "branch", "date": "परीक्षा", "children": [
                {"label": "PAT योजना: परफॉर्म, अचीव एंड ट्रेड; NMEEE के तहत बाजार आधारित तंत्र जो ऊर्जा दक्षता बचत प्रमाण पत्रों (ESCerts) के व्यापार की अनुमति देता है", "type": "leaf"},
                {"label": "बायोएनर्जी मिशन: वेस्ट-टू-एनर्जी तकनीकों और जैव ईंधन सम्मिश्रण को बढ़ावा देने के लिए हाल ही में 9वें मिशन के रूप में जोड़ा गया", "type": "leaf"}
            ]}
        ]
    },
    {
        "keys": ["national-forest-policy"],
        "en": [
            {"label": "Key Targets & Goals", "type": "branch", "date": "Policy 1988", "children": [
                {"label": "Forest Target: Maintain a minimum of 33% of the total geographical area under forest and tree cover; 66% in mountainous/hilly regions", "type": "leaf"},
                {"label": "Ecological Priority: Priorities ecological balance, soil conservation, and genetic resource preservation over direct commercial revenue generation", "type": "leaf"}
            ]},
            {"label": "Social Forestry Link", "type": "branch", "date": "Social Forestry", "children": [
                {"label": "Definition: Management and protection of forests and afforestation on barren lands with the purpose of helping environmental, social, and rural development", "type": "leaf"},
                {"label": "Three types: Farm forestry (planting trees on farmland), community forestry (planting on village commons), and extension forestry (planting along canals/roads)", "type": "leaf"}
            ]}
        ],
        "hi": [
            {"label": "मुख्य लक्ष्य और उद्देश्य", "type": "branch", "date": "नीति 1988", "children": [
                {"label": "वन लक्ष्य: देश के कुल भौगोलिक क्षेत्र का न्यूनतम 33% वन और वृक्ष आवरण के तहत बनाए रखना; पहाड़ी क्षेत्रों में 66% का लक्ष्य", "type": "leaf"},
                {"label": "पारिस्थितिक प्राथमिकता: वाणिज्यिक राजस्व उत्पादन की तुलना में पारिस्थितिक संतुलन, मृदा संरक्षण और आनुवंशिक संसाधनों के संरक्षण को प्राथमिकता देना", "type": "leaf"}
            ]},
            {"label": "सामाजिक वानिकी संबंध", "type": "branch", "date": "सामाजिक वानिकी", "children": [
                {"label": "परिभाषा: बंजर भूमि पर वनों का प्रबंधन, संरक्षण और वनीकरण जिसका उद्देश्य पर्यावरणीय, सामाजिक और ग्रामीण विकास में मदद करना है", "type": "leaf"},
                {"label": "तीन प्रकार: कृषि वानिकी (खेतों पर पेड़ लगाना), सामुदायिक वानिकी (ग्राम सभा की भूमि पर), और विस्तार वानिकी (नहरों/सड़कों के किनारे)", "type": "leaf"}
            ]}
        ]
    },
    {
        "keys": ["national-ganga-river-basin-authority", "ngrba", "ganga-rejuvenation-plan", "benefits-of-river-ganga"],
        "en": [
            {"label": "Regulatory Bodies", "type": "branch", "date": "Institutions", "children": [
                {"label": "NMCG: National Mission for Clean Ganga; acts as the implementation wing of the National Ganga Council (established in 2016 to replace NGRBA)", "type": "leaf"},
                {"label": "Chairmanship: National Ganga Council is chaired directly by the Prime Minister of India to coordinate river rejuvenation actions", "type": "leaf"}
            ]},
            {"label": "Namami Gange Programme", "type": "branch", "date": "Namami Gange", "children": [
                {"label": "Integrated Conservation: Launched in 2014; focuses on sewage treatment infrastructure, river-front development, biodiversity conservation, and Ganga Gram (clean villages)", "type": "leaf"},
                {"label": "Major Pollutants: Untreated industrial effluents from tanneries (Kanpur) and chemical units, and domestic municipal sewage discharge", "type": "leaf"}
            ]}
        ],
        "hi": [
            {"label": "नियामक निकाय", "type": "branch", "date": "संस्थान", "children": [
                {"label": "NMCG: स्वच्छ गंगा के लिए राष्ट्रीय मिशन; राष्ट्रीय गंगा परिषद (NGRBA को बदलकर 2016 में स्थापित) की कार्यान्वयन शाखा के रूप में कार्य करता है", "type": "leaf"},
                {"label": "अध्यक्षता: नदी पुनरुद्धार कार्यों के समन्वय के लिए राष्ट्रीय गंगा परिषद की अध्यक्षता सीधे भारत के प्रधान मंत्री द्वारा की जाती है", "type": "leaf"}
            ]},
            {"label": "नमामि गंगे कार्यक्रम", "type": "branch", "date": "नमामि गंगे", "children": [
                {"label": "एकीकृत संरक्षण: 2014 में शुरू; सीवेज उपचार बुनियादी ढांचे, रिवर-फ्रंट विकास, जैव विविधता संरक्षण और गंगा ग्राम पर केंद्रित", "type": "leaf"},
                {"label": "प्रमुख प्रदूषक: चमड़ा कारखानों (कानपुर) से निकलने वाले अनुपचारित रसायन, और नगर पालिकाओं का घरेलू सीवेज कचरा", "type": "leaf"}
            ]}
        ]
    },
    {
        "keys": ["national-green-tribunal", "ngt"],
        "en": [
            {"label": "NGT Framework", "type": "branch", "date": "NGT Act 2010", "children": [
                {"label": "Definition: Special fast-track statutory tribunal established in 2010 for effective and expeditious disposal of environmental cases", "type": "leaf"},
                {"label": "Constitutional link: Enacted under Article 21 (Right to a healthy environment) of the Constitution of India", "type": "leaf"}
            ]},
            {"label": "Key Powers & Rules", "type": "branch", "date": "Jurisdiction", "children": [
                {"label": "Natural Justice: Bound by principles of natural justice, NOT by the Code of Civil Procedure 1908 (CPC); makes it highly flexible", "type": "leaf"},
                {"label": "Time Limit: Mandated to dispose of environmental applications and appeals within 6 months of filing", "type": "leaf"},
                {"label": "Structure: Headed by a Chairperson (retired Supreme Court Judge or Chief Justice of a High Court), with judicial and expert members", "type": "leaf"}
            ]},
            {"label": "UPSC Exam Focus", "type": "branch", "date": "UPSC Focus", "children": [
                {"label": "Acts Covered: NGT has jurisdiction over 7 laws: Water Act 1974, Water Cess Act 1977, Forest Conservation Act 1980, Air Act 1981, EPA 1986, Public Liability Insurance Act 1991, Biological Diversity Act 2002", "type": "leaf"},
                {"label": "Exclusions: Wildlife Protection Act 1972 and Forest Rights Act 2006 are completely outside NGT's jurisdiction", "type": "leaf"}
            ]}
        ],
        "hi": [
            {"label": "NGT का ढांचा", "type": "branch", "date": "NGT अधिनियम 2010", "children": [
                {"label": "परिभाषा: पर्यावरणीय मामलों के प्रभावी और त्वरित निपटान के लिए 2010 में स्थापित एक विशेष फास्ट-ट्रैक वैधानिक न्यायाधिकरण", "type": "leaf"},
                {"label": "संवैधानिक संबंध: भारत के संविधान के अनुच्छेद 21 (स्वस्थ पर्यावरण का अधिकार) के तहत अधिनियमित", "type": "leaf"}
            ]},
            {"label": "शक्तियां और कार्यप्रणाली", "type": "branch", "date": "अधिकार क्षेत्र", "children": [
                {"label": "प्राकृतिक न्याय: प्राकृतिक न्याय के सिद्धांतों द्वारा निर्देशित, न कि नागरिक प्रक्रिया संहिता 1908 (CPC) द्वारा; इसे अत्यधिक लचीला बनाता है", "type": "leaf"},
                {"label": "समय सीमा: पर्यावरणीय आवेदनों और अपीलों को दायर होने के 6 महीने के भीतर निपटाना अनिवार्य है", "type": "leaf"},
                {"label": "संरचना: एक अध्यक्ष (सेवानिवृत्त सुप्रीम कोर्ट जज) की अध्यक्षता में, जिसमें न्यायिक और विशेषज्ञ सदस्य शामिल होते हैं", "type": "leaf"}
            ]},
            {"label": "यूपीएससी परीक्षा दृष्टिकोण", "type": "branch", "date": "परीक्षा", "children": [
                {"label": "शामिल कानून: NGT का अधिकार क्षेत्र 7 कानूनों पर है: जल अधिनियम 1974, वन संरक्षण अधिनियम 1980, वायु अधिनियम 1981, EPA 1986, जैव विविधता अधिनियम 2002 आदि", "type": "leaf"},
                {"label": "बाहर रखे गए कानून: वन्यजीव संरक्षण अधिनियम 1972 और वन अधिकार अधिनियम (FRA) 2006 NGT के दायरे से पूरी तरह बाहर हैं", "type": "leaf"}
            ]}
        ]
    },
    {
        "keys": ["national-policy-on-biofuels-2018"],
        "en": [
            {"label": "Biofuel Classifications", "type": "branch", "date": "Policy 2018", "children": [
                {"label": "1G (First Generation): Bioethanol produced from food crops (sugarcane juice, corn, damaged food grains like broken rice)", "type": "leaf"},
                {"label": "2G (Second Generation): Ethanol produced from non-food lignocellulosic biomass (rice straw, wheat straw, bagasse)", "type": "leaf"},
                {"label": "3G (Third Generation): Biofuels derived from aquatic algae; can be grown on non-arable land without using fresh water", "type": "leaf"},
                {"label": "4G (Fourth Generation): Genetically engineered crops that capture carbon dioxide in their biomass, converted to fuel via pyrolysis", "type": "leaf"}
            ]},
            {"label": "Key Targets", "type": "branch", "date": "Targets", "children": [
                {"label": "Blending Target: Target of 20% ethanol blending in petrol and 5% biodiesel blending in diesel by 2025-26", "type": "leaf"}
            ]}
        ],
        "hi": [
            {"label": "जैव ईंधन का वर्गीकरण", "type": "branch", "date": "नीति 2018", "children": [
                {"label": "1G (प्रथम पीढ़ी): खाद्य फसलों से उत्पादित बायोएथेनॉल (गन्ने का रस, मक्का, क्षतिग्रस्त खाद्यान्न जैसे टूटा चावल)", "type": "leaf"},
                {"label": "2G (द्वितीय पीढ़ी): गैर-खाद्य लिग्नोसेल्युलोसिक बायोमास (धान की पराली, गेहूं का भूसा) से उत्पादित एथेनॉल", "type": "leaf"},
                {"label": "3G (तृतीय पीढ़ी): जलीय शैवाल (Algae) से प्राप्त जैव ईंधन; मीठे पानी के बिना बंजर भूमि पर उगाया जा सकता है", "type": "leaf"},
                {"label": "4G (चतुर्थ पीढ़ी): आनुवंशिक रूप से संशोधित फसलें जो हवा से CO2 अवशोषित करती हैं, पायरोलिसिस द्वारा ईंधन में बदली जाती हैं", "type": "leaf"}
            ]},
            {"label": "मुख्य लक्ष्य", "type": "branch", "date": "लक्ष्य", "children": [
                {"label": "सम्मिश्रण लक्ष्य: पेट्रोल में 20% एथेनॉल सम्मिश्रण और डीजल में 5% बायोडीजल सम्मिश्रण का लक्ष्य वर्ष 2025-26 तक पूरा करना", "type": "leaf"}
            ]}
        ]
    },
    {
        "keys": ["ozone-depleting-substance-rules", "ozone-depletion-and-human-health", "montreal-protocol-and-kigali-agreement"],
        "en": [
            {"label": "Vienna & Montreal Treaties", "type": "branch", "date": "Vienna / Montreal", "children": [
                {"label": "Vienna Convention 1985: Framework convention for protection of the ozone layer; does not contain legally binding reduction targets", "type": "leaf"},
                {"label": "Montreal Protocol 1987: Legally binding treaty designed to phase out production and consumption of ozone-depleting substances (like CFCs, Halons)", "type": "leaf"}
            ]},
            {"label": "Kigali Amendment 2016", "type": "branch", "date": "Kigali", "children": [
                {"label": "Hydrofluorocarbons (HFCs): Montreal Protocol phase-out of CFCs led to use of HFCs; HFCs do not deplete ozone but are potent greenhouse gases", "type": "leaf"},
                {"label": "Kigali target: Mandates global phase-down of HFCs by 80-85% by the late 2040s, helping prevent up to 0.5 degrees C of warming by 2100", "type": "leaf"}
            ]},
            {"label": "ODS Rules in India", "type": "branch", "date": "India Rules", "children": [
                {"label": "ODS Rules 2000: Framed under Environment Protection Act 1986; regulates production, import, and consumption of substances like CFCs, HCFCs, and carbon tetrachloride", "type": "leaf"}
            ]}
        ],
        "hi": [
            {"label": "वियना और मॉन्ट्रियल संधियाँ", "type": "branch", "date": "वियना / मॉन्ट्रियल", "children": [
                {"label": "वियना कन्वेंशन 1985: ओजोन परत के संरक्षण के लिए रूपरेखा समझौता; इसमें कानूनी रूप से बाध्यकारी कटौती लक्ष्य नहीं हैं", "type": "leaf"},
                {"label": "मॉन्ट्रियल प्रोटोकॉल 1987: ओजोन परत को नुकसान पहुंचाने वाले पदार्थों (CFCs) के उत्पादन को समाप्त करने वाली बाध्यकारी संधि", "type": "leaf"}
            ]},
            {"label": "किगाली संशोधन 2016", "type": "branch", "date": "किगाली", "children": [
                {"label": "हाइड्रोफ्लोरोकार्बन (HFCs): CFCs के हटने के बाद HFCs का उपयोग बढ़ा; ये ओजोन को नुकसान नहीं पहुंचाते लेकिन शक्तिशाली ग्रीनहाउस गैसें हैं", "type": "leaf"},
                {"label": "किगाली लक्ष्य: 2040 के दशक के अंत तक HFCs के उपयोग को 80-85% तक कम करना, जिससे 2100 तक 0.5 डिग्री सेल्सियस तापमान बढ़ने से रोका जा सके", "type": "leaf"}
            ]},
            {"label": "भारत में ODS नियम", "type": "branch", "date": "भारत", "children": [
                {"label": "ODS नियम 2000: पर्यावरण संरक्षण अधिनियम 1986 के तहत निर्मित; CFCs, HCFCs के निर्माण और आयात को विनियमित करते हैं", "type": "leaf"}
            ]}
        ]
    },
    {
        "keys": ["sustainable-development-goals", "sdg"],
        "en": [
            {"label": "17 Global Goals", "type": "branch", "date": "SDGs 2015-2030", "children": [
                {"label": "Origins: Adopted by all United Nations Member States in 2015 as part of the Agenda 2030, replacing Millennium Development Goals (MDGs)", "type": "leaf"},
                {"label": "Climate goal: SDG 13 (Climate Action) calls for urgent action to combat climate change and its impacts", "type": "leaf"},
                {"label": "Water goal: SDG 14 (Life Below Water) focuses on conservation and sustainable use of oceans, seas, and marine resources", "type": "leaf"},
                {"label": "Land goal: SDG 15 (Life on Land) targets sustainable forest management, combating desertification, and halting biodiversity loss", "type": "leaf"}
            ]}
        ],
        "hi": [
            {"label": "17 वैश्विक लक्ष्य", "type": "branch", "date": "SDGs 2015-2030", "children": [
                {"label": "उत्पत्ति: सहस्राब्दी विकास लक्ष्यों (MDGs) के स्थान पर एजेंडा 2030 के हिस्से के रूप में 2015 में संयुक्त राष्ट्र द्वारा अपनाए गए", "type": "leaf"},
                {"label": "जलवायु लक्ष्य: SDG 13 (जलवायु कार्रवाई) जलवायु परिवर्तन और इसके प्रभावों से निपटने के लिए तत्काल कार्रवाई का आह्वान करता है", "type": "leaf"},
                {"label": "जल लक्ष्य: SDG 14 (जल के नीचे जीवन) महासागरों, समुद्रों और समुद्री संसाधनों के संरक्षण और सतत उपयोग पर केंद्रित है", "type": "leaf"},
                {"label": "भूमि लक्ष्य: SDG 15 (भूमि पर जीवन) सतत वन प्रबंधन, मरुस्थलीकरण से निपटने और जैव विविधता के नुकसान को रोकने का लक्ष्य रखता है", "type": "leaf"}
            ]}
        ]
    },
    {
        "keys": ["the-earth-summit"],
        "en": [
            {"label": "Origins & Agenda 21", "type": "branch", "date": "Rio 1992", "children": [
                {"label": "UNCED: United Nations Conference on Environment and Development held in Rio de Janeiro, Brazil in 1992", "type": "leaf"},
                {"label": "Agenda 21: Non-binding action plan of the United Nations with regard to sustainable development", "type": "leaf"}
            ]},
            {"label": "Three Rio Conventions", "type": "branch", "date": "Rio Conventions", "children": [
                {"label": "UNFCCC: United Nations Framework Convention on Climate Change; framework to stabilize atmospheric GHG concentrations", "type": "leaf"},
                {"label": "CBD: Convention on Biological Diversity; focuses on biodiversity conservation, sustainable use, and fair benefit sharing", "type": "leaf"},
                {"label": "UNCCD: United Nations Convention to Combat Desertification; legally binding convention addressing dryland degradation", "type": "leaf"}
            ]}
        ],
        "hi": [
            {"label": "उत्पत्ति और एजेंडा 21", "type": "branch", "date": "रियो 1992", "children": [
                {"label": "UNCED: पर्यावरण और विकास पर संयुक्त राष्ट्र सम्मेलन, 1992 में ब्राजील के रियो डी जेनेरियो में आयोजित", "type": "leaf"},
                {"label": "एजेंडा 21: सतत विकास के संबंध में संयुक्त राष्ट्र की एक गैर-बाध्यकारी कार्य योजना", "type": "leaf"}
            ]},
            {"label": "तीन रियो कन्वेंशन", "type": "branch", "date": "कन्वेंशन", "children": [
                {"label": "UNFCCC: जलवायु परिवर्तन पर संयुक्त राष्ट्र फ्रेमवर्क कन्वेंशन; ग्रीनहाउस गैसों को स्थिर करने का ढांचा", "type": "leaf"},
                {"label": "CBD: जैव विविधता पर कन्वेंशन; जैव विविधता के संरक्षण और लाभों के निष्पक्ष बंटवारे पर केंद्रित", "type": "leaf"},
                {"label": "UNCCD: मरुस्थलीकरण से निपटने के लिए संयुक्त राष्ट्र कन्वेंशन; शुष्क भूमि क्षरण को संबोधित करने वाली बाध्यकारी संधि", "type": "leaf"}
            ]}
        ]
    },
    {
        "keys": ["the-economics-of-ecosystems-and-biodiversity", "teeb"],
        "en": [
            {"label": "TEEB Framework", "type": "branch", "date": "TEEB Initiative", "children": [
                {"label": "Definition: Global initiative hosted by UNEP, led by Pavan Sukhdev; focuses on making the economic values of nature visible to decision-makers", "type": "leaf"},
                {"label": "Core Approach: 3-tiered model: Recognize value (in ecosystems), Demonstrate value (via economic analysis), and Capture value (via policy tools like subsidies/PES)", "type": "leaf"}
            ]}
        ],
        "hi": [
            {"label": "TEEB का ढांचा", "type": "branch", "date": "पहल", "children": [
                {"label": "परिभाषा: UNEP द्वारा आयोजित वैश्विक पहल, पवन सुखदेव के नेतृत्व में; नीति निर्माताओं के सामने प्रकृति के आर्थिक मूल्य को प्रदर्शित करना", "type": "leaf"},
                {"label": "मुख्य दृष्टिकोण: 3-स्तरीय मॉडल: मूल्य पहचानना (पारितंत्र में), मूल्य प्रदर्शित करना (आर्थिक विश्लेषण से), और मूल्य को दर्ज करना (नीतियों द्वारा)", "type": "leaf"}
            ]}
        ]
    },
    {
        "keys": ["undp", "unep", "united-nations-programme-governance", "united-nations-programmes-and-assemblies"],
        "en": [
            {"label": "UNEP Governance", "type": "branch", "date": "UNEP 1972", "children": [
                {"label": "Origin: Established in 1972 at the Stockholm Conference; headquartered in Nairobi, Kenya", "type": "leaf"},
                {"label": "UNEA: United Nations Environment Assembly; governing body of UNEP, meets biennially to set global environmental priorities", "type": "leaf"}
            ]},
            {"label": "UNDP Role", "type": "branch", "date": "UNDP", "children": [
                {"label": "Governance: United Nations Development Programme; focuses on poverty eradication, reducing inequalities, and building resilience to climate change", "type": "leaf"}
            ]}
        ],
        "hi": [
            {"label": "UNEP का शासन", "type": "branch", "date": "UNEP 1972", "children": [
                {"label": "उत्पत्ति: स्टॉकहोम सम्मेलन में 1972 में स्थापित; मुख्यालय नैरोबी, केन्या में स्थित है", "type": "leaf"},
                {"label": "UNEA: संयुक्त राष्ट्र पर्यावरण सभा; UNEP का शासी निकाय, वैश्विक प्राथमिकताओं को निर्धारित करने के लिए द्विवार्षिक बैठक करता है", "type": "leaf"}
            ]},
            {"label": "UNDP की भूमिका", "type": "branch", "date": "UNDP", "children": [
                {"label": "शासन: संयुक्त राष्ट्र विकास कार्यक्रम; गरीबी उन्मूलन, असमानताओं को कम करने और जलवायु परिवर्तन के प्रति लचीलापन बढ़ाने पर केंद्रित", "type": "leaf"}
            ]}
        ]
    },
    {
        "keys": ["united-nations-conference-on-the-human-environment", "stockholm-conference"],
        "en": [
            {"label": "Stockholm Conference 1972", "type": "branch", "date": "1972", "children": [
                {"label": "History: Held in June 1972; first major global conference making environmental protection a core international issue", "type": "leaf"},
                {"label": "Stockholm Declaration: Contained 26 principles placing environmental issues at the forefront of international concerns", "type": "leaf"},
                {"label": "Legacy: Led to creation of UNEP and prompted India to enact the Water Act 1974 and Air Act 1981, and create the Ministry of Environment", "type": "leaf"}
            ]}
        ],
        "hi": [
            {"label": "स्टॉकहोम सम्मेलन 1972", "type": "branch", "date": "1972", "children": [
                {"label": "इतिहास: जून 1972 में आयोजित; पहला बड़ा वैश्विक सम्मेलन जिसने पर्यावरण संरक्षण को एक मुख्य अंतर्राष्ट्रीय मुद्दा बनाया", "type": "leaf"},
                {"label": "स्टॉकहोम घोषणा: इसमें 26 सिद्धांत शामिल थे जिन्होंने पर्यावरण को अंतर्राष्ट्रीय प्राथमिकताओं में सबसे आगे रखा", "type": "leaf"},
                {"label": "प्रभाव: इसके कारण UNEP का गठन हुआ और भारत को जल अधिनियम 1974, वायु अधिनियम 1981 और पर्यावरण मंत्रालय बनाने की प्रेरणा मिली", "type": "leaf"}
            ]}
        ]
    },
    {
        "keys": ["united-nations-convention-to-combat-desertification", "unccd", "national-action-programme-to-combat-desertification"],
        "en": [
            {"label": "UNCCD Objectives", "type": "branch", "date": "UNCCD 1994", "children": [
                {"label": "Definition: Legally binding international convention established to address land degradation and drought in drylands (arid, semi-arid, dry sub-humid areas)", "type": "leaf"},
                {"label": "Land Degradation Neutrality (LDN): Core goal to maintain or improve stable, healthy land resources globally by 2030", "type": "leaf"}
            ]},
            {"label": "UPSC Exam Focus", "type": "branch", "date": "UPSC Focus", "children": [
                {"label": "COP-14 New Delhi: Held in 2019; India launched a Legacy Programme to restore 26 million hectares of degraded land by 2030", "type": "leaf"},
                {"label": "Bonn Challenge: Global effort to restore degraded forests and lands; India committed to restoring 26m hectares", "type": "leaf"}
            ]}
        ],
        "hi": [
            {"label": "UNCCD के उद्देश्य", "type": "branch", "date": "UNCCD 1994", "children": [
                {"label": "परिभाषा: शुष्क और अर्ध-शुष्क क्षेत्रों में भूमि क्षरण और सूखे से निपटने के लिए स्थापित कानूनी रूप से बाध्यकारी अंतर्राष्ट्रीय कन्वेंशन", "type": "leaf"},
                {"label": "भूमि क्षरण तटस्थता (LDN): 2030 तक वैश्विक स्तर पर स्थिर, स्वस्थ भूमि संसाधनों को बनाए रखने या सुधारने का मुख्य लक्ष्य", "type": "leaf"}
            ]},
            {"label": "यूपीएससी परीक्षा दृष्टिकोण", "type": "branch", "date": "परीक्षा", "children": [
                {"label": "COP-14 नई दिल्ली: 2019 में आयोजित; भारत ने 2030 तक 26 मिलियन हेक्टेयर क्षरित भूमि को बहाल करने का कार्यक्रम शुरू किया", "type": "leaf"},
                {"label": "बॉन चुनौती: क्षरित वनों और भूमि को बहाल करने का वैश्विक प्रयास; भारत 26 मिलियन हेक्टेयर भूमि बहाल करने के लिए प्रतिबद्ध है", "type": "leaf"}
            ]}
        ]
    },
    {
        "keys": ["united-nations-framework-convention-on-climate-change-1992", "unfccc"],
        "en": [
            {"label": "Framework Overview", "type": "branch", "date": "UNFCCC 1992", "children": [
                {"label": "Rio Treaty: Adopted at the Rio Earth Summit in 1992; entered into force in 1994; framework to stabilize atmospheric GHG concentrations", "type": "leaf"},
                {"label": "Common but Differentiated Responsibilities (CBDR): Core principle acknowledging that while all nations must address climate change, developed countries bear greater historical responsibility", "type": "leaf"}
            ]},
            {"label": "Key Protocols & Accords", "type": "branch", "date": "COPs", "children": [
                {"label": "Kyoto Protocol (1997): Set legally binding emission reduction targets for Annex I (developed) countries", "type": "leaf"},
                {"label": "Paris Agreement (2015): Replaced Kyoto; asks all countries to submit Nationally Determined Contributions (NDCs) to limit global warming to well below 2 degrees C", "type": "leaf"}
            ]}
        ],
        "hi": [
            {"label": "फ्रेमवर्क का अवलोकन", "type": "branch", "date": "UNFCCC 1992", "children": [
                {"label": "रियो संधि: 1992 में रियो अर्थ समिट में अपनाया गया; 1994 में लागू हुआ; ग्रीनहाउस गैसों की सांद्रता को स्थिर करने का ढांचा", "type": "leaf"},
                {"label": "साझा लेकिन विभेदित जिम्मेदारियां (CBDR): सिद्धांत जो स्वीकार करता है कि विकसित देशों की ऐतिहासिक जिम्मेदारी अधिक है", "type": "leaf"}
            ]},
            {"label": "प्रमुख प्रोटोकॉल और समझौते", "type": "branch", "date": "COPs", "children": [
                {"label": "क्योटो प्रोटोकॉल (1997): विकसित (एनेक्स I) देशों के लिए कानूनी रूप से बाध्यकारी उत्सर्जन कटौती लक्ष्य निर्धारित किए", "type": "leaf"},
                {"label": "पेरिस समझौता (2015): क्योटो की जगह ली; वैश्विक तापमान वृद्धि को 2 डिग्री सेल्सियस से नीचे रखने के लिए सभी देशों से NDCs की मांग की", "type": "leaf"}
            ]}
        ]
    },
    {
        "keys": ["urban-heat-island", "urbanization-and-climate-change"],
        "en": [
            {"label": "Urban Heat Island (UHI)", "type": "branch", "date": "UHI", "children": [
                {"label": "Definition: Microclimate phenomenon where urban areas experience significantly higher temperatures than surrounding rural suburbs", "type": "leaf"},
                {"label": "Primary Causes: Dark asphalt/concrete surfaces absorbing solar radiation, lack of evapotranspiration from vegetation, and waste heat from ACs/vehicles", "type": "leaf"}
            ]},
            {"label": "Mitigation Strategies", "type": "branch", "date": "Mitigation", "children": [
                {"label": "Cool Roofs: Painting roofs with highly reflective white paint to bounce solar radiation back into space", "type": "leaf"},
                {"label": "Urban forestry: Creating green roofs, planting urban tree canopies (e.g. Miyawaki forests), and building linear parks", "type": "leaf"}
            ]}
        ],
        "hi": [
            {"label": "शहरी ऊष्मा द्वीप (UHI)", "type": "branch", "date": "UHI", "children": [
                {"label": "परिभाषा: सूक्ष्म जलवायु घटना जहां शहरी क्षेत्र अपने आसपास के ग्रामीण उपनगरों की तुलना में काफी अधिक तापमान का अनुभव करते हैं", "type": "leaf"},
                {"label": "प्राथमिक कारण: डामर/कंक्रीट सतहों द्वारा सौर विकिरण का अवशोषण, वनस्पतियों की कमी और एसी/वाहनों से निकलने वाली अपशिष्ट गर्मी", "type": "leaf"}
            ]},
            {"label": "शमन रणनीतियाँ", "type": "branch", "date": "शमन", "children": [
                {"label": "कूल रूफ (Cool Roofs): सौर विकिरण को वापस अंतरिक्ष में परावर्तित करने के लिए छतों पर अत्यधिक परावर्तक सफेद पेंट लगाना", "type": "leaf"},
                {"label": "शहरी वानिकी: ग्रीन रूफ बनाना, शहरी क्षेत्रों में पेड़ लगाना (जैसे मियावाकी वन) और पार्क बनाना", "type": "leaf"}
            ]}
        ]
    },
    {
        "keys": ["wetland-rules-2010"],
        "en": [
            {"label": "Rules & Coverage", "type": "branch", "date": "Wetlands", "children": [
                {"label": "Rules 2010: Restricts reclamation, solid waste dumping, and discharge of untreated waste in Ramsar and notified wetlands", "type": "leaf"},
                {"label": "Wetland Rules 2017 updates: Replaced 2010 rules; decentralized authority, transferring regulatory powers to State Wetland Authorities and removing CPCB appeal links", "type": "leaf"}
            ]}
        ],
        "hi": [
            {"label": "नियम और दायरा", "type": "branch", "date": "आर्द्रभूमि", "children": [
                {"label": "नियम 2010: रामसर और अधिसूचित आर्द्रभूमियों में डंपिंग, अनुपचारित कचरे के विसर्जन और भूमि अतिक्रमण को प्रतिबंधित करते हैं", "type": "leaf"},
                {"label": "आर्द्रभूमि नियम 2017 अपडेट: 2010 के नियमों को बदला; शक्तियों का विकेंद्रीकरण कर विनियामक अधिकार राज्य आर्द्रभूमि प्राधिकरणों को दिए", "type": "leaf"}
            ]}
        ]
    },
    {
        "keys": ["wildlife-protection-act-1972"],
        "en": [
            {"label": "WPA Schedules & Protection", "type": "branch", "date": "WPA 1972", "children": [
                {"label": "Definition: Primary legal framework in India for protecting wild animal and plant species, and managing protected areas (National Parks, Sanctuaries)", "type": "leaf"},
                {"label": "2022 Amendment updates: Rationalized schedules from 6 down to 4: Schedule I (highest protection), Schedule II (lesser protection), Schedule III (protected plants), Schedule IV (CITES species)", "type": "leaf"}
            ]},
            {"label": "Protected Area Types", "type": "branch", "date": "Protected Areas", "children": [
                {"label": "National Parks: High protection; no grazing or private rights allowed inside boundary", "type": "leaf"},
                {"label": "Sanctuaries: Lesser protection; limited grazing and collection of minor forest produce allowed under collector permissions", "type": "leaf"},
                {"label": "Reserves: Conservation Reserves (on government land adjacent to national parks/corridors) and Community Reserves (on private/community lands)", "type": "leaf"}
            ]}
        ],
        "hi": [
            {"label": "WPA अनुसूचियां और संरक्षण", "type": "branch", "date": "WPA 1972", "children": [
                {"label": "परिभाषा: जंगली जानवरों और पौधों के संरक्षण तथा राष्ट्रीय उद्यानों व अभ्यारण्यों के प्रबंधन के लिए भारत का प्राथमिक कानूनी ढांचा", "type": "leaf"},
                {"label": "2022 संशोधन अपडेट: अनुसूचियों को 6 से घटाकर 4 किया: अनुसूची I (सर्वोच्च संरक्षण), अनुसूची II (कम संरक्षण), अनुसूची III (संरक्षित पौधे), अनुसूची IV (CITES प्रजातियां)", "type": "leaf"}
            ]},
            {"label": "संरक्षित क्षेत्रों के प्रकार", "type": "branch", "date": "संरक्षित क्षेत्र", "children": [
                {"label": "राष्ट्रीय उद्यान: उच्च संरक्षण; सीमा के भीतर पशु चराई या किसी भी निजी अधिकार की अनुमति नहीं होती", "type": "leaf"},
                {"label": "अभयारण्य: कम संरक्षण; कलेक्टर की अनुमति से सीमित चराई और लघु वनोपज एकत्र करने की अनुमति दी जा सकती है", "type": "leaf"},
                {"label": "आरक्षित क्षेत्र: संरक्षण रिजर्व (राष्ट्रीय उद्यान के पास सरकारी भूमि पर) और सामुदायिक रिजर्व (निजी/सामुदायिक भूमि पर)", "type": "leaf"}
            ]}
        ]
    },
    {
        "keys": ["monoculture-practice"],
        "en": [
            {"label": "Ecological Risks", "type": "branch", "date": "Risks", "children": [
                {"label": "Soil Depletion: Cultivating a single species (e.g. Teak, Eucalyptus, or Oil Palm) repeatedly drains specific soil nutrients, decreasing microbial diversity", "type": "leaf"},
                {"label": "Pest Vulnerability: Lack of genetic variation allows pests and pathogens to spread rapidly across entire plantations, causing crop failure", "type": "leaf"},
                {"label": "Habitat Loss: Wipes out native undergrowth and nesting habitats, forcing local fauna and insect pollinators to migrate", "type": "leaf"}
            ]},
            {"label": "UPSC Exam Focus", "type": "branch", "date": "UPSC Focus", "children": [
                {"label": "Forest Fires: Eucalyptus monocultures dry up local aquifers and shed flammable oils, increasing forest fire frequencies", "type": "leaf"}
            ]}
        ],
        "hi": [
            {"label": "पारिस्थितिक खतरे", "type": "branch", "date": "खतरे", "children": [
                {"label": "मृदा क्षरण: एक ही फसल (जैसे सागौन या नीलगिरी) को बार-बार उगाने से विशिष्ट पोषक तत्व समाप्त हो जाते हैं", "type": "leaf"},
                {"label": "कीट संवेदनशीलता: आनुवंशिक विविधता की कमी से कीट और रोग पूरी फसल में तेजी से फैलते हैं", "type": "leaf"},
                {"label": "आवास का नुकसान: स्थानीय वनस्पतियों और घोंसले के मैदानों को नष्ट करता है, जिससे जीव पलायन के लिए मजबूर होते हैं", "type": "leaf"}
            ]},
            {"label": "यूपीएससी परीक्षा दृष्टिकोण", "type": "branch", "date": "परीक्षा", "children": [
                {"label": "वनाग्नि: नीलगिरी (Eucalyptus) की एकल खेती स्थानीय जलभृतों को सुखा देती है और ज्वलनशील तेल छोड़ती है, जिससे आग का खतरा बढ़ता है", "type": "leaf"}
            ]}
        ]
    },
    {
        "keys": ["agriculture-increases-carbon-dioxide-emissions", "impact-of-agriculture", "pollution-due-to-use-of-chemical-fertilizers", "soil-related-effects"],
        "en": [
            {"label": "Agricultural GHGs", "type": "branch", "date": "Emissions", "children": [
                {"label": "Methane (CH4): Flooded paddy fields provide anaerobic conditions for methanogenic bacteria, releasing huge amounts of methane", "type": "leaf"},
                {"label": "Nitrous Oxide (N2O): Over-application of synthetic nitrogen fertilizers triggers nitrification/denitrification, emitting N2O which has ~300 times the warming potential of CO2", "type": "leaf"}
            ]},
            {"label": "Soil Degradation", "type": "branch", "date": "Soil Impacts", "children": [
                {"label": "Tillage: Repeated mechanical soil disturbance oxidizes organic matter, releasing stored soil carbon into the atmosphere", "type": "leaf"},
                {"label": "Salinization: Excessive irrigation in arid zones (e.g. Punjab) causes waterlogging, leaving behind salts that ruin soil structure", "type": "leaf"}
            ]}
        ],
        "hi": [
            {"label": "कृषि जनित ग्रीनहाउस गैसें", "type": "branch", "date": "उत्सर्जन", "children": [
                {"label": "मीथेन (CH4): जलमग्न धान के खेत अवायवीय बैक्टीरिया के लिए परिस्थितियां बनाते हैं, जिससे प्रचुर मात्रा में मीथेन निकलती है", "type": "leaf"},
                {"label": "नाइट्रस ऑक्साइड (N2O): यूरिया उर्वरकों का अत्यधिक उपयोग N2O उत्सर्जित करता है, जिसका वार्मिंग प्रभाव CO2 से ~300 गुना अधिक है", "type": "leaf"}
            ]},
            {"label": "मृदा क्षरण", "type": "branch", "date": "मिट्टी पर प्रभाव", "children": [
                {"label": "जुताई (Tillage): बार-बार जुताई से कार्बनिक पदार्थों का ऑक्सीकरण होता है, जिससे मिट्टी में संचित कार्बन हवा में मिल जाता है", "type": "leaf"},
                {"label": "लवणीकरण: शुष्क क्षेत्रों (जैसे पंजाब) में अत्यधिक सिंचाई से जलभराव होता है और मिट्टी अनुपजाऊ हो जाती है", "type": "leaf"}
            ]}
        ]
    },
    {
        "keys": ["arctic-council"],
        "en": [
            {"label": "Structure & Mandate", "type": "branch", "date": "Arctic Council", "children": [
                {"label": "Origins: Established in 1996 by the Ottawa Declaration; intergovernmental forum addressing environmental issues and sustainable development in the Arctic", "type": "leaf"},
                {"label": "8 Member States: Canada, Denmark, Finland, Iceland, Norway, Russia, Sweden, and the United States", "type": "leaf"}
            ]},
            {"label": "India Presence", "type": "branch", "date": "India Observer", "children": [
                {"label": "Observer Status: India has held permanent observer status since 2013, coordinating polar research to understand monsoon links", "type": "leaf"},
                {"label": "Research Station: India operates 'Himadri' research station in Ny-Alesund, Svalbard, Norway to study glacier melt", "type": "leaf"}
            ]}
        ],
        "hi": [
            {"label": "ढांचा और अधिदेश", "type": "branch", "date": "आर्कटिक परिषद", "children": [
                {"label": "उत्पत्ति: 1996 में ओटावा घोषणा द्वारा स्थापित; आर्कटिक में पर्यावरणीय मुद्दों और सतत विकास को संबोधित करने वाला मंच", "type": "leaf"},
                {"label": "8 सदस्य देश: कनाडा, डेनमार्क, फिनलैंड, आइसलैंड, नॉर्वे, रूस, स्वीडन और संयुक्त राज्य अमेरिका", "type": "leaf"}
            ]},
            {"label": "भारत की उपस्थिति", "type": "branch", "date": "पर्यवेक्षक", "children": [
                {"label": "पर्यवेक्षक का दर्जा: भारत को 2013 से स्थायी पर्यवेक्षक का दर्जा प्राप्त है; मानसून के संबंधों को समझने के लिए ध्रुवीय अनुसंधान करता है", "type": "leaf"},
                {"label": "अनुसंधान स्टेशन: भारत ग्लेशियर पिघलने के अध्ययन के लिए स्वालबार्ड (नॉर्वे) में 'हिमाद्रि' अनुसंधान केंद्र संचालित करता है", "type": "leaf"}
            ]}
        ]
    },
    {
        "keys": ["bse-greenex"],
        "en": [
            {"label": "BSE GREENEX Concept", "type": "branch", "date": "Index", "children": [
                {"label": "Carbon Index: India's first carbon-efficient thematic index launched by Bombay Stock Exchange (BSE) in 2012", "type": "leaf"},
                {"label": "Index Base: Comprises top 25 carbon-efficient companies, helping fund managers identify energy-efficient businesses", "type": "leaf"}
            ]}
        ],
        "hi": [
            {"label": "BSE ग्रीनेक्स अवधारणा", "type": "branch", "date": "सूचकांक", "children": [
                {"label": "कार्बन सूचकांक: 2012 में बॉम्बे स्टॉक एक्सचेंज (BSE) द्वारा लॉन्च किया गया भारत का पहला कार्बन-दक्ष विषयगत सूचकांक", "type": "leaf"},
                {"label": "सूचकांक आधार: शीर्ष 25 कार्बन-कुशल कंपनियों को शामिल करता है, जिससे निवेशकों को पर्यावरण-अनुकूल विकल्प मिलते हैं", "type": "leaf"}
            ]}
        ]
    },
    {
        "keys": ["eco-mark"],
        "en": [
            {"label": "Ecomark Scheme", "type": "branch", "date": "Ecomark", "children": [
                {"label": "Administered by: Bureau of Indian Standards (BIS) in coordination with Ministry of Environment (MoEFCC)", "type": "leaf"},
                {"label": "Eco Logo: Uses an earthen pot (ghara) as its logo, symbolizing soil/clay and environmental friendliness", "type": "leaf"},
                {"label": "Objective: Guides consumers to purchase products that have less environmental impact across their lifecycle", "type": "leaf"}
            ]}
        ],
        "hi": [
            {"label": "इकोमार्क योजना", "type": "branch", "date": "इकोमार्क", "children": [
                {"label": "प्रशासक: पर्यावरण मंत्रालय (MoEFCC) के समन्वय में भारतीय मानक ब्यूरो (BIS) द्वारा संचालित", "type": "leaf"},
                {"label": "इको लोगो: मिट्टी के घड़े (Ghara) को लोगो के रूप में उपयोग करता है, जो मिट्टी और पर्यावरण-अनुकूलता का प्रतीक है", "type": "leaf"},
                {"label": "उद्देश्य: उपभोक्ताओं को उन उत्पादों को खरीदने के लिए निर्देशित करना जिनका पर्यावरण पर कम प्रभाव पड़ता है", "type": "leaf"}
            ]}
        ]
    },
    {
        "keys": ["energy-conservation-building-code", "ecbc", "net-zero-energy", "nzeb", "standard-and-labeling", "bee-star", "green-buildings", "griha"],
        "en": [
            {"label": "BEE Appliance Labeling", "type": "branch", "date": "Standards", "children": [
                {"label": "BEE Star Label: Bureau of Energy Efficiency (BEE) labels appliances (1 to 5 stars) based on energy saving performances", "type": "leaf"},
                {"label": "Mandatory appliances: Includes frost-free refrigerators, tubular fluorescent lamps, room ACs, and distribution transformers", "type": "leaf"}
            ]},
            {"label": "ECBC & NZEB Codes", "type": "branch", "date": "Buildings", "children": [
                {"label": "ECBC Code: Formulated by BEE under Energy Conservation Act 2001; sets minimum energy performance standards for commercial buildings", "type": "leaf"},
                {"label": "Net Zero (NZEB): Buildings designed to produce as much energy on-site (via solar/wind) as they consume annually", "type": "leaf"}
            ]},
            {"label": "GRIHA Rating System", "type": "branch", "date": "GRIHA", "children": [
                {"label": "Definition: Green Rating for Integrated Habitat Assessment; India's national rating tool developed by TERI and MoEFCC to evaluate green building compliance", "type": "leaf"}
            ]}
        ],
        "hi": [
            {"label": "BEE उपकरण लेबलिंग", "type": "branch", "date": "मानक", "children": [
                {"label": "BEE स्टार लेबल: ऊर्जा दक्षता ब्यूरो (BEE) ऊर्जा बचत प्रदर्शन के आधार पर उपकरणों को 1 से 5 स्टार तक लेबल करता है", "type": "leaf"},
                {"label": "अनिवार्य उपकरण: रेफ्रिजरेटर, फ्लोरोसेंट लैंप, रूम एसी और वितरण ट्रांसफार्मर शामिल हैं", "type": "leaf"}
            ]},
            {"label": "ECBC और NZEB कोड", "type": "branch", "date": "भवन", "children": [
                {"label": "ECBC कोड: BEE द्वारा ऊर्जा संरक्षण अधिनियम 2001 के तहत तैयार; वाणिज्यिक भवनों के लिए न्यूनतम ऊर्जा मानक तय करता है", "type": "leaf"},
                {"label": "नेट जीरो (NZEB): ऐसे भवन जो सालाना उपभोग की जाने वाली ऊर्जा के बराबर ऊर्जा साइट पर (सौर/पवन से) खुद उत्पन्न करते हैं", "type": "leaf"}
            ]},
            {"label": "GRIHA रेटिंग प्रणाली", "type": "branch", "date": "GRIHA", "children": [
                {"label": "परिभाषा: ग्रीन रेटिंग फॉर इंटीग्रेटेड हैबिटेट असेसमेंट; भारत का राष्ट्रीय रेटिंग टूल जो हरित भवन अनुपालन का मूल्यांकन करता है", "type": "leaf"}
            ]}
        ]
    },
    {
        "keys": ["climate-change-basics", "greenhouse-effect", "global-warming-potential", "gwp", "global-warming-health", "impacts-of-the-climate-change", "observed-climate", "urbanization-and-climate-change", "strategies-to-address-climate-change", "actions-for-adaptation-mitigation", "indian-climate-change-assessment", "india-and-climate-change", "indias-position-with-regards"],
        "en": [
            {"label": "Greenhouse Effect Mechanics", "type": "branch", "date": "GHGs", "children": [
                {"label": "Mechanism: Solar shortwave radiation passes through atmosphere; Earth absorbs and re-emits longwave infrared radiation, trapped by greenhouse gases (water vapor, CO2, CH4, N2O, SF6)", "type": "leaf"},
                {"label": "Global Warming Potential (GWP): CO2 GWP is 1 (baseline); Methane GWP is ~28, Nitrous Oxide is ~265, and Sulfur Hexafluoride (SF6) is ~23,500 over a 100-year scale", "type": "leaf"}
            ]},
            {"label": "Adaptation vs Mitigation", "type": "branch", "date": "Strategies", "children": [
                {"label": "Adaptation: Adjusting to actual or expected climate changes (e.g. building sea walls, developing drought-resistant crops)", "type": "leaf"},
                {"label": "Mitigation: Actions to reduce source emissions or enhance greenhouse gas sinks (e.g. transitioning to solar energy, afforestation)", "type": "leaf"}
            ]},
            {"label": "Urbanization Links", "type": "branch", "date": "Urban Impacts", "children": [
                {"label": "Heat inversion: Trapping of warm polluted air under cold air layers in concrete urban environments, degrading local air quality", "type": "leaf"}
            ]}
        ],
        "hi": [
            {"label": "ग्रीनहाउस प्रभाव की कार्यप्रणाली", "type": "branch", "date": "GHGs", "children": [
                {"label": "क्रियाविधि: सौर लघु तरंगें वायुमंडल से गुजरती हैं; पृथ्वी उन्हें अवशोषित कर दीर्घ तरंग इन्फ्रारेड विकिरण उत्सर्जित करती है, जो गैसों (CO2, CH4, N2O) द्वारा सोख ली जाती हैं", "type": "leaf"},
                {"label": "ग्लोबल वार्मिंग क्षमता (GWP): CO2 का GWP 1 है; मीथेन का GWP ~28 है, नाइट्रस ऑक्साइड का ~265 है, और SF6 का ~23,500 है", "type": "leaf"}
            ]},
            {"label": "अनुकूलन बनाम शमन", "type": "branch", "date": "रणनीतियां", "children": [
                {"label": "अनुकूलन (Adaptation): वास्तविक या संभावित जलवायु परिवर्तनों के अनुसार ढलना (जैसे समुद्र की दीवारें बनाना, सूखा-रोधी फसलें)", "type": "leaf"},
                {"label": "शमन (Mitigation): ग्रीनहाउस गैसों के उत्सर्जन को कम करने या सिंक बढ़ाने के कार्य (जैसे सौर ऊर्जा अपनाना, वनीकरण)", "type": "leaf"}
            ]},
            {"label": "शहरीकरण संबंध", "type": "branch", "date": "शहरी प्रभाव", "children": [
                {"label": "तापीय प्रतिलोमन: कंक्रीट के शहरी वातावरण में ठंडी हवा के नीचे गर्म प्रदूषित हवा का फंसना, जिससे स्थानीय वायु गुणवत्ता खराब होती है", "type": "leaf"}
            ]}
        ]
    },
    {
        "keys": ["climate-and-clean-air-coalition", "ccac"],
        "en": [
            {"label": "CCAC Overview", "type": "branch", "date": "CCAC", "children": [
                {"label": "Definition: Global partnership of governments, intergovernmental bodies, and NGOs launched in 2012; hosted by UNEP", "type": "leaf"},
                {"label": "Short-Lived Climate Pollutants (SLCPs): Focuses on reducing black carbon, methane, tropospheric ozone, and hydrofluorocarbons (HFCs) to achieve rapid warming reductions", "type": "leaf"}
            ]}
        ],
        "hi": [
            {"label": "CCAC का अवलोकन", "type": "branch", "date": "पहल", "children": [
                {"label": "परिभाषा: 2012 में शुरू सरकारों, अंतर-सरकारी निकायों और NGOs की वैश्विक साझेदारी; UNEP द्वारा आयोजित", "type": "leaf"},
                {"label": "अल्पकालिक प्रदूषक (SLCPs): त्वरित तापमान नियंत्रण के लिए ब्लैक कार्बन, मीथेन, ओजोन और हाइड्रोफ्लोरोकार्बन को कम करने पर ध्यान केंद्रित करता है", "type": "leaf"}
            ]}
        ]
    },
    {
        "keys": ["commission-on-sustainable-development", "csd"],
        "en": [
            {"label": "CSD History", "type": "branch", "date": "UN CSD", "children": [
                {"label": "Origins: Established in 1992 by UN General Assembly to monitor implementation of Rio Earth Summit outcomes and Agenda 21", "type": "leaf"},
                {"label": "Replacement: Replaced in 2013 by the High-Level Political Forum on Sustainable Development (HLPF) to monitor SDGs progress", "type": "leaf"}
            ]}
        ],
        "hi": [
            {"label": "CSD का इतिहास", "type": "branch", "date": "UN CSD", "children": [
                {"label": "उत्पत्ति: रियो शिखर सम्मेलन के परिणामों और एजेंडा 21 के कार्यान्वयन की निगरानी के लिए 1992 में संयुक्त राष्ट्र महासभा द्वारा स्थापित", "type": "leaf"},
                {"label": "प्रतिस्थापन: SDGs की प्रगति की निगरानी के लिए 2013 में सतत विकास पर उच्च-स्तरीय राजनीतिक मंच (HLPF) द्वारा प्रतिस्थापित किया गया", "type": "leaf"}
            ]}
        ]
    },
    {
        "keys": ["corporate-social-responsibility"],
        "en": [
            {"label": "CSR Regulations", "type": "branch", "date": "Section 135", "children": [
                {"label": "Companies Act 2013: Section 135 mandates companies with net worth >=500cr, turnover >=1000cr, or net profit >=5cr to spend 2% of average net profits on CSR", "type": "leaf"},
                {"label": "Schedule VII: Environment protection, restoring ecological balance, agroforestry, and wildlife conservation are approved activities under CSR rules", "type": "leaf"}
            ]}
        ],
        "hi": [
            {"label": "CSR नियम", "type": "branch", "date": "धारा 135", "children": [
                {"label": "कंपनी अधिनियम 2013: धारा 135 के तहत नेट वर्थ >=500 करोड़ या टर्नओवर >=1000 करोड़ वाली कंपनियों के लिए 2% CSR खर्च अनिवार्य", "type": "leaf"},
                {"label": "अनुसूची VII: पर्यावरण संरक्षण, पारिस्थितिक संतुलन की बहाली, कृषि वानिकी और वन्यजीव संरक्षण CSR के तहत स्वीकृत गतिविधियां हैं", "type": "leaf"}
            ]}
        ]
    },
    {
        "keys": ["eu-initiatives"],
        "en": [
            {"label": "EU Climate Programs", "type": "branch", "date": "EU Programs", "children": [
                {"label": "Green Deal: Commits EU to reducing net greenhouse gas emissions by 55% by 2030 and reaching net-zero carbon by 2050", "type": "leaf"},
                {"label": "CBAM: Carbon Border Adjustment Mechanism; taxes carbon-intensive imports (steel, cement, electricity) entering the EU market", "type": "leaf"}
            ]}
        ],
        "hi": [
            {"label": "यूरोपीय संघ के कार्यक्रम", "type": "branch", "date": "EU पहलें", "children": [
                {"label": "ग्रीन डील: 2030 तक शुद्ध ग्रीनहाउस गैस उत्सर्जन को 55% कम करने और 2050 तक नेट-जीरो कार्बन हासिल करने की प्रतिबद्धता", "type": "leaf"},
                {"label": "CBAM: कार्बन बॉर्डर एडजस्टमेंट मैकेनिज्म; यूरोपीय संघ में प्रवेश करने वाले कार्बन-गहन आयातों (इस्पात, सीमेंट) पर टैक्स लगाना", "type": "leaf"}
            ]}
        ]
    },
    {
        "keys": ["forest-carbon-partnership", "redd"],
        "en": [
            {"label": "REDD & REDD+ Concepts", "type": "branch", "date": "REDD+", "children": [
                {"label": "REDD: Reducing Emissions from Deforestation and Forest Degradation in developing countries under UNFCCC", "type": "leaf"},
                {"label": "REDD+: Goes beyond deforestation to include forest carbon stock conservation, sustainable forest management, and enhancement of carbon sinks", "type": "leaf"}
            ]},
            {"label": "FCPF Framework", "type": "branch", "date": "FCPF", "children": [
                {"label": "FCPF: Forest Carbon Partnership Facility; World Bank-managed global partnership helping developing countries implement REDD+ policies", "type": "leaf"}
            ]}
        ],
        "hi": [
            {"label": "REDD और REDD+ की अवधारणा", "type": "branch", "date": "REDD+", "children": [
                {"label": "REDD: विकासशील देशों में वनों की कटाई से उत्सर्जन को कम करने का UNFCCC कार्यक्रम", "type": "leaf"},
                {"label": "REDD+: वनों की कटाई के अलावा वन कार्बन स्टॉक संरक्षण, टिकाऊ वन प्रबंधन और कार्बन सिंक के संवर्धन को शामिल करता है", "type": "leaf"}
            ]},
            {"label": "FCPF ढांचा", "type": "branch", "date": "FCPF", "children": [
                {"label": "FCPF: वन कार्बन साझेदारी सुविधा; विश्व बैंक द्वारा प्रबंधित वैश्विक साझेदारी जो विकासशील देशों को REDD+ लागू करने में मदद करती है", "type": "leaf"}
            ]}
        ]
    },
    {
        "keys": ["india-state-of-forest-report"],
        "en": [
            {"label": "ISFR 2021 Data", "type": "branch", "date": "ISFR 2021", "children": [
                {"label": "Total Cover: Forest and tree cover accounts for 24.62% of India's total geographical area (target is 33% under Forest Policy 1988)", "type": "leaf"},
                {"label": "Top States: Madhya Pradesh has the largest forest cover by area; Mizoram has the highest forest cover by percentage (84.53%)", "type": "leaf"},
                {"label": "Mangrove Cover: India's total mangrove cover stands at 4,992 sq km, showing a minor increase of 17 sq km in 2021 assessment", "type": "leaf"}
            ]}
        ],
        "hi": [
            {"label": "ISFR 2021 डेटा", "type": "branch", "date": "ISFR 2021", "children": [
                {"label": "कुल आवरण: देश का कुल वन और वृक्ष आवरण भौगोलिक क्षेत्र का 24.62% है (राष्ट्रीय वन नीति 1988 का लक्ष्य 33% है)", "type": "leaf"},
                {"label": "शीर्ष राज्य: क्षेत्रफल के हिसाब से मध्य प्रदेश में सबसे बड़ा वन क्षेत्र है; प्रतिशत के हिसाब से मिजोरम (84.53%) शीर्ष पर है", "type": "leaf"},
                {"label": "मैंग्रोव आवरण: भारत का कुल मैंग्रोव आवरण 4,992 वर्ग किमी है, जिसमें 2021 के आकलन में 17 वर्ग किमी की मामूली वृद्धि हुई है", "type": "leaf"}
            ]}
        ]
    },
    {
        "keys": ["intergovernmental-panel", "ipcc"],
        "en": [
            {"label": "IPCC Overview", "type": "branch", "date": "IPCC 1988", "children": [
                {"label": "Origins: Established in 1988 by the World Meteorological Organization (WMO) and United Nations Environment Programme (UNEP)", "type": "leaf"},
                {"label": "Assessment Reports: Does not conduct original research; synthesizes published scientific literature into Assessment Reports (e.g. AR6 report in 2021/2022)", "type": "leaf"}
            ]}
        ],
        "hi": [
            {"label": "IPCC का अवलोकन", "type": "branch", "date": "IPCC 1988", "children": [
                {"label": "उत्पत्ति: विश्व मौसम विज्ञान संगठन (WMO) और संयुक्त राष्ट्र पर्यावरण कार्यक्रम (UNEP) द्वारा 1988 में स्थापित", "type": "leaf"},
                {"label": "मूल्यांकन रिपोर्ट: खुद अनुसंधान नहीं करता; प्रकाशित वैज्ञानिक साहित्य की समीक्षा कर मूल्यांकन रिपोर्ट (जैसे AR6) जारी करता है", "type": "leaf"}
            ]}
        ]
    },
    {
        "keys": ["joint-forest-management", "social-forestry"],
        "en": [
            {"label": "Joint Forest Management (JFM)", "type": "branch", "date": "JFM", "children": [
                {"label": "Concept: Partnership between local village communities and state forest departments to protect and manage degraded forests", "type": "leaf"},
                {"label": "Benefit: Local communities receive non-timber forest produce (grass, fuel wood) and share of timber sales in return for protection duties", "type": "leaf"}
            ]},
            {"label": "Social Forestry Classes", "type": "branch", "date": "Social Forestry", "children": [
                {"label": "Categories: Formally classified into Farm forestry, Community forestry, and Extension forestry under National Forest Commission plans", "type": "leaf"}
            ]}
        ],
        "hi": [
            {"label": "संयुक्त वन प्रबंधन (JFM)", "type": "branch", "date": "JFM", "children": [
                {"label": "अवधारणा: बंजर वन भूमि के संरक्षण और प्रबंधन के लिए स्थानीय ग्राम समुदायों और राज्य वन विभागों के बीच साझेदारी", "type": "leaf"},
                {"label": "लाभ: स्थानीय समुदायों को गैर-इमारती वनोपज (घास, ईंधन की लकड़ी) और सुरक्षा के बदले इमारती लकड़ी की बिक्री का हिस्सा मिलता है", "type": "leaf"}
            ]},
            {"label": "सामाजिक वानिकी श्रेणियां", "type": "branch", "date": "सामाजिक वानिकी", "children": [
                {"label": "श्रेणियां: राष्ट्रीय वन आयोग की योजनाओं के तहत इसे कृषि वानिकी, सामुदायिक वानिकी और विस्तार वानिकी में वर्गीकृत किया गया है", "type": "leaf"}
            ]}
        ]
    },
    {
        "keys": ["long-term-ecological-observatories", "lteo"],
        "en": [
            {"label": "LTEO Programme", "type": "branch", "date": "LTEO", "children": [
                {"label": "Definition: National program launched by MoEFCC to establish a network of long-term ecological monitoring sites across 8 Indian biomes", "type": "leaf"},
                {"label": "Monitoring areas: Focuses on studying climate change impacts on soil, forests, grasslands, grasslands, and Himalayan glaciers", "type": "leaf"}
            ]}
        ],
        "hi": [
            {"label": "LTEO कार्यक्रम", "type": "branch", "date": "LTEO", "children": [
                {"label": "परिभाषा: 8 भारतीय बायोम में दीर्घकालिक पारिस्थितिक निगरानी स्थलों का नेटवर्क स्थापित करने के लिए MoEFCC की राष्ट्रीय पहल", "type": "leaf"},
                {"label": "निगरानी क्षेत्र: मिट्टी, जंगलों, घास के मैदानों और हिमालयी ग्लेशियरों पर जलवायु परिवर्तन के प्रभाव के अध्ययन पर केंद्रित", "type": "leaf"}
            ]}
        ]
    },
    {
        "keys": ["national-communication", "natcom"],
        "en": [
            {"label": "NATCOM Reports", "type": "branch", "date": "NATCOM", "children": [
                {"label": "UNFCCC Requirement: Official reporting submitted by India to UNFCCC detailing national GHG inventories and vulnerability/adaptation assessments", "type": "leaf"}
            ]}
        ],
        "hi": [
            {"label": "NATCOM रिपोर्ट", "type": "branch", "date": "NATCOM", "children": [
                {"label": "UNFCCC आवश्यकता: राष्ट्रीय GHG सूची और अनुकूलन आकलनों का विवरण देने वाली भारत की आधिकारिक रिपोर्ट", "type": "leaf"}
            ]}
        ]
    },
    {
        "keys": ["national-greenhouse-gas-inventories-programme", "nggip"],
        "en": [
            {"label": "NGGIP Framework", "type": "branch", "date": "NGGIP", "children": [
                {"label": "IPCC Program: IPCC programme managing database of emission factors and greenhouse gas inventory methodologies to assist member nations", "type": "leaf"}
            ]}
        ],
        "hi": [
            {"label": "NGGIP फ्रेमवर्क", "type": "branch", "date": "NGGIP", "children": [
                {"label": "IPCC कार्यक्रम: राष्ट्रीय उत्सर्जन कारकों और सूची पद्धतियों के डेटाबेस का प्रबंधन करने वाला कार्यक्रम", "type": "leaf"}
            ]}
        ]
    },
    {
        "keys": ["national-initiative-on-climate-resilient-agriculture", "nicra"],
        "en": [
            {"label": "NICRA Framework", "type": "branch", "date": "ICAR 2011", "children": [
                {"label": "Launch: Launched by Indian Council of Agricultural Research (ICAR) in 2011 to enhance agriculture resilience to climate vulnerability", "type": "leaf"},
                {"label": "Core Pillars: Strategic research on crops, technology demonstration on farmers' fields, and capacity building for extreme weather adaptation", "type": "leaf"}
            ]}
        ],
        "hi": [
            {"label": "NICRA का ढांचा", "type": "branch", "date": "ICAR 2011", "children": [
                {"label": "शुभारंभ: भारतीय कृषि अनुसंधान परिषद (ICAR) द्वारा 2011 में कृषि को जलवायु परिवर्तन के प्रति लचीला बनाने के लिए शुरू", "type": "leaf"},
                {"label": "मुख्य स्तंभ: फसलों पर रणनीतिक अनुसंधान, किसानों के खेतों पर तकनीकों का प्रदर्शन और मौसम अनुकूलन क्षमता निर्माण", "type": "leaf"}
            ]}
        ]
    },
    {
        "keys": ["pollution-control-boards"],
        "en": [
            {"label": "CPCB & SPCB Roles", "type": "branch", "date": "Pollution Boards", "children": [
                {"label": "Establishment: Central Pollution Control Board (CPCB) established under Water Act 1974; advises Central Government on air/water quality", "type": "leaf"},
                {"label": "Powers: SPCBs grant consent to establish/operate industrial units and monitor compliance with national emission standards", "type": "leaf"}
            ]}
        ],
        "hi": [
            {"label": "CPCB और SPCB की भूमिका", "type": "branch", "date": "नियंत्रण बोर्ड", "children": [
                {"label": "स्थापना: केंद्रीय प्रदूषण नियंत्रण बोर्ड (CPCB) जल अधिनियम 1974 के तहत स्थापित; केंद्र सरकार को सलाह देता है", "type": "leaf"},
                {"label": "शक्तियां: SPCB औद्योगिक इकाइयों को स्थापित/संचालित करने की सहमति देते हैं और उत्सर्जन मानकों की निगरानी करते हैं", "type": "leaf"}
            ]}
        ]
    },
    {
        "keys": ["schedule-tribes-and-other-forest-dwellers"],
        "en": [
            {"label": "Forest Rights Act 2006", "type": "branch", "date": "FRA 2006", "children": [
                {"label": "Individual Rights (IFR): Grants title to land held by Scheduled Tribes and Traditional Forest Dwellers prior to December 2005 (up to 4 hectares)", "type": "leaf"},
                {"label": "Community Rights (CFR): Recognizes community ownership of minor forest produce (MFP) like bamboo, tendu leaves, and grazing grounds", "type": "leaf"},
                {"label": "Critical Wildlife Habitats (CWH): Declared under the Act inside protected areas, allowing for relocation only with Gram Sabha consent", "type": "leaf"}
            ]}
        ],
        "hi": [
            {"label": "वन अधिकार अधिनियम 2006", "type": "branch", "date": "FRA 2006", "children": [
                {"label": "व्यक्तिगत अधिकार (IFR): दिसंबर 2005 से पहले वन भूमि पर काबिज जनजातियों और पारंपरिक वनवासियों को (4 हेक्टेयर तक) भूमि पट्टा देना", "type": "leaf"},
                {"label": "सामुदायिक अधिकार (CFR): बांस, तेंदू पत्ते और चराई जैसे लघु वनोपज (MFP) पर समुदाय के स्वामित्व को मान्यता देना", "type": "leaf"},
                {"label": "क्रिटिकल वाइल्डलाइफ हैबिटेट (CWH): संरक्षित क्षेत्रों के भीतर घोषित, ग्राम सभा की सहमति से ही पुनर्वास की अनुमति", "type": "leaf"}
            ]}
        ]
    },
    {
        "keys": ["schemes-in-india-regarding-environmental-protection"],
        "en": [
            {"label": "National Protection Schemes", "type": "branch", "date": "Schemes", "children": [
                {"label": "National Green Corps: Eco-clubs established in schools to build student environmental awareness", "type": "leaf"},
                {"label": "Nagar Van Scheme: Launched to develop urban forests in cities, helping build green buffers", "type": "leaf"},
                {"label": "NPCA Scheme: National Plan for Conservation of Aquatic Ecosystems, coordinating wetland/lake restoration", "type": "leaf"}
            ]}
        ],
        "hi": [
            {"label": "राष्ट्रीय संरक्षण योजनाएं", "type": "branch", "date": "योजनाएं", "children": [
                {"label": "नेशनल ग्रीन कोर (Eco-clubs): छात्रों में पर्यावरणीय जागरूकता पैदा करने के लिए स्कूलों में इको-क्लब बनाना", "type": "leaf"},
                {"label": "नगर वन योजना: शहरों में शहरी वनों को विकसित करने की पहल, जो हरित बफर जोन बनाती है", "type": "leaf"},
                {"label": "NPCA योजना: जलीय पारिस्थितिकी प्रणालियों के संरक्षण की राष्ट्रीय योजना, जो आर्द्रभूमि/झीलों के जीर्णोद्धार का समन्वय करती है", "type": "leaf"}
            ]}
        ]
    },
    {
        "keys": ["swachh-bharat-mission"],
        "en": [
            {"label": "SBM Framework", "type": "branch", "date": "SBM", "children": [
                {"label": "Launch: Launched on October 2, 2014, to eliminate open defecation and improve municipal solid waste management", "type": "leaf"},
                {"label": "SBM 2.0 targets: Focuses on sustainability of ODF status, waste water treatment, greywater management, and bioremediation of legacy dumps", "type": "leaf"}
            ]}
        ],
        "hi": [
            {"label": "SBM का ढांचा", "type": "branch", "date": "SBM", "children": [
                {"label": "शुभारंभ: खुले में शौच को समाप्त करने और ठोस कचरा प्रबंधन में सुधार के लिए 2 अक्टूबर 2014 को शुरू", "type": "leaf"},
                {"label": "SBM 2.0 लक्ष्य: ODF स्थिति की निरंतरता, गंदे पानी का उपचार, धूसर जल प्रबंधन और पुराने कचरे के जैव-उपचार पर ध्यान", "type": "leaf"}
            ]}
        ]
    },
    {
        "keys": ["world-environmental-governance", "international-environmental-governance"],
        "en": [
            {"label": "Global Governance Institutions", "type": "branch", "date": "IEG", "children": [
                {"label": "UNEP: United Nations Environment Programme; coordinates global policy responses, environmental treaties, and publishes Global Environment Outlook", "type": "leaf"},
                {"label": "GEF: Financial mechanism; funds environmental projects in developing countries supporting CBD, UNFCCC, UNCCD, and POPs", "type": "leaf"}
            ]}
        ],
        "hi": [
            {"label": "वैश्विक शासन संस्थान", "type": "branch", "date": "IEG", "children": [
                {"label": "UNEP: संयुक्त राष्ट्र पर्यावरण कार्यक्रम; वैश्विक नीतियों और संधियों का समन्वय करता है, रिपोर्ट जारी करता है", "type": "leaf"},
                {"label": "GEF: वित्तीय तंत्र; विकासशील देशों में जैव विविधता, UNFCCC और मरुस्थलीकरण परियोजनाओं को वित्तपोषित करता है", "type": "leaf"}
            ]}
        ]
    },
    {
        "keys": ["world-meteorological-organization", "wmo"],
        "en": [
            {"label": "WMO Overview", "type": "branch", "date": "WMO", "children": [
                {"label": "Definition: Specialized agency of the UN established in 1950; coordinates international weather forecasting, water resources, and climate monitoring", "type": "leaf"},
                {"label": "Programs: Runs the World Weather Watch and Global Atmosphere Watch to monitor GHG concentrations globally", "type": "leaf"}
            ]}
        ],
        "hi": [
            {"label": "WMO का अवलोकन", "type": "branch", "date": "WMO", "children": [
                {"label": "परिभाषा: 1950 में स्थापित संयुक्त राष्ट्र की विशिष्ट एजेंसी; अंतर्राष्ट्रीय मौसम पूर्वानुमान और जलवायु निगरानी का समन्वय करती है", "type": "leaf"},
                {"label": "कार्यक्रम: वैश्विक स्तर पर ग्रीनहाउस गैसों की सांद्रता की निगरानी के लिए ग्लोबल एटमॉस्फियर वॉच चलाता है", "type": "leaf"}
            ]}
        ]
    },
    {
        "keys": ["wwf-for-nature"],
        "en": [
            {"label": "WWF Profile", "type": "branch", "date": "WWF", "children": [
                {"label": "Foundation: Founded in 1961, based in Gland, Switzerland; uses Giant Panda logo and acts as premier global conservation NGO", "type": "leaf"},
                {"label": "Key Projects: Runs 'Earth Hour' global lights-off initiative and publishes the biennial 'Living Planet Report'", "type": "leaf"}
            ]}
        ],
        "hi": [
            {"label": "WWF प्रोफाइल", "type": "branch", "date": "WWF", "children": [
                {"label": "स्थापना: 1961 में स्थापित, ग्लैंड (स्विट्जरलैंड) में स्थित; प्रसिद्ध पांडा लोगो का उपयोग करता है", "type": "leaf"},
                {"label": "प्रमुख परियोजनाएं: वैश्विक 'अर्थ आवर' (Earth Hour) पहल चलाता है और 'लिविंग प्लैनेट रिपोर्ट' प्रकाशित करता है", "type": "leaf"}
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
    "types": "प्रकार",
    "change": "परिवर्तन",
    "environmental": "पर्यावरणीय",
    "administration": "प्रशासन",
    "adaptation": "अनुकूलन",
    "mitigation": "शमन",
    "fund": "कोष",
    "increases": "बढ़ाता है",
    "dioxide": "डाइऑक्साइड",
    "emissions": "उत्सर्जन",
    "animal": "जंतु",
    "welfare": "कल्याण",
    "board": "बोर्ड",
    "arctic": "आर्कटिक",
    "council": "परिषद",
    "benefits": "लाभ",
    "river": "नदी",
    "ganga": "गंगा",
    "facts": "तथ्य",
    "about": "के बारे में",
    "bharat": "भारत",
    "stage": "स्टेज",
    "norms": "मानक",
    "biocarbon": "बायोकार्बन",
    "diversity": "विविधता",
    "act": "अधिनियम",
    "birdlife": "बर्डलाइफ",
    "international": "अंतर्राष्ट्रीय",
    "bombay": "बॉम्बे",
    "natural": "प्राकृतिक",
    "history": "इतिहास",
    "society": "सोसाइटी",
    "botanical": "वनस्पति",
    "survey": "सर्वेक्षण",
    "brief": "संक्षिप्त",
    "bse": "BSE",
    "greenex": "ग्रीनेक्स",
    "central": "केंद्रीय",
    "zoo": "चिड़ियाघर",
    "authority": "प्राधिकरण",
    "centre": "केंद्र",
    "clean": "स्वच्छ",
    "technology": "तकनीक",
    "coastal": "तटीय",
    "regulation": "विनियमन",
    "commission": "आयोग",
    "provisions": "प्रावधान",
    "related": "संबंधित",
    "corporate": "कॉर्पोरेट",
    "social": "सामाजिक",
    "responsibility": "उत्तरदायित्व",
    "protection": "संरक्षण",
    "drawback": "कमियाँ",
    "process": "प्रक्रिया",
    "eco": "इको",
    "mark": "मार्क",
    "scheme": "योजना",
    "ecological": "पारिस्थितिक",
    "building": "भवन",
    "code": "कोड",
    "impact": "प्रभाव",
    "assessment": "मूल्यांकन",
    "institutions": "संस्थान",
    "eu": "यूरोपीय संघ (EU)",
    "initiatives": "पहलें",
    "factors": "कारक",
    "affecting": "प्रभावित करने वाले",
    "fame": "FAME",
    "partnership": "साझेदारी",
    "facility": "सुविधा",
    "rejuvenation": "कायाकल्प",
    "finance": "वित्त",
    "architecture": "संरचना",
    "global": "वैश्विक",
    "warming": "तापमान (ग्लोबल वार्मिंग)",
    "potential": "क्षमता",
    "green": "हरित",
    "rating": "रेटिंग",
    "integrated": "एकीकृत",
    "habitat": "आवास",
    "greenhouse": "ग्रीनहाउस",
    "observatories": "वेधशालाएं",
    "monoculture": "एकल कृषि",
    "practice": "प्रथा",
    "impacts": "प्रभाव",
    "biodiversity": "जैव विविधता",
    "agreement": "समझौता",
    "mission": "मिशन",
    "enhanced": "संवर्धित",
    "efficiency": "दक्षता",
    "sustaining": "बनाए रखना",
    "himalayan": "हिमालयी",
    "strategic": "रणनीतिक",
    "knowledge": "ज्ञान",
    "solar": "सौर",
    "action": "कार्रवाई",
    "programme": "कार्यक्रम",
    "combat": "मुकाबला",
    "desertification": "मरुस्थलीकरण",
    "board": "बोर्ड",
    "communication": "संचार",
    "policy": "नीति",
    "tiger": "बाघ",
    "wildlife": "वनयजीव",
    "net": "नेट",
    "zero": "जीरो",
    "buildings": "भवन",
    "observed": "अवलोकित",
    "weather": "मौसम",
    "changes": "परिवर्तन",
    "ozone": "ओजोन",
    "depleting": "क्षयकारी",
    "substance": "पदार्थ",
    "depletion": "क्षय",
    "boards": "बोर्ड",
    "chemical": "रासायनिक",
    "fertilizers": "उर्वरक",
    "recommendations": "सिफारिशें",
    "improvement": "सुधार",
    "redd": "REDD",
    "schedule": "अनुसूचित",
    "tribes": "जनजाति",
    "dwellers": "निवासी",
    "schemes": "योजनाएं",
    "forestry": "वानिकी",
    "special": "विशेष",
    "labeling": "लेबलिंग",
    "star": "स्टार",
    "label": "लेबल",
    "strategies": "रणनीतियां",
    "address": "संबोधित करना",
    "techniques": "तकनीकें",
    "goals": "लक्ष्य",
    "swachh": "स्वच्छ",
    "bharat": "भारत",
    "earth": "पृथ्वी",
    "summit": "शिखर सम्मेलन (समिट)",
    "economics": "अर्थशास्त्र",
    "assemblies": "सभाएं",
    "united": "संयुक्त",
    "nations": "राष्ट्र",
    "framework": "फ्रेमवर्क",
    "urban": "शहरी",
    "heat": "ऊष्मा",
    "island": "द्वीप (आइलैंड)",
    "urbanization": "शहरीकरण",
    "various": "विभिन्न",
    "indices": "सूचकांक",
    "relate": "संबंधित",
    "wetland": "आ्र्द्रभूमि",
    "crime": "अपराध",
    "wmo": "WMO",
    "world": "विश्व",
    "minor": "लघु",
    "produce": "उत्पाद",
    "meteorological": "मौसम विज्ञान",
    "organization": "संगठन",
    "wwf": "WWF",
    "nature": "प्रकृति",
    "zoological": "प्राणी"
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
                {"label": f"Definition: Understanding the fundamental characteristics, administrative bodies, and scope of {t}", "type": "leaf"},
                {"label": f"Scientific Framework: Analyzing how {t} integrates with climate change and environmental administration", "type": "leaf"}
            ]
        },
        {
            "label": f"Processes & Dynamics",
            "type": "branch",
            "date": "Mechanisms",
            "children": [
                {"label": f"Primary Drivers: Factors regulating the governance, implementation, and reporting of {t}", "type": "leaf"},
                {"label": f"Spatial Distribution: Exploring the national networks and regional frameworks of {t}", "type": "leaf"}
            ]
        },
        {
            "label": f"Ecological & Applied Values",
            "type": "branch",
            "date": "Applications",
            "children": [
                {"label": f"Impacts: How changes in {t} affect environmental protection, resource sustainability, and climate resilience", "type": "leaf"},
                {"label": f"Case Studies: Notable real-world initiatives and policy models relating to {t}", "type": "leaf"}
            ]
        },
        {
            "label": f"UPSC Exam Syllabus Relevance",
            "type": "branch",
            "date": "UPSC Core",
            "children": [
                {"label": f"Prelims Prep: Key statutory clauses, legal authorities, and regulatory bodies associated with {t}", "type": "leaf"},
                {"label": f"Mains Answer Writing: Linking {t} with international treaties, India's NDCs, and national climate strategies", "type": "leaf"}
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
                {"label": f"परिभाषा: {t} की बुनियादी विशेषताओं, प्रशासनिक निकायों और कार्यक्षेत्र को समझना", "type": "leaf"},
                {"label": f"वैज्ञानिक ढांचा: {t} जलवायु परिवर्तन और पर्यावरणीय प्रशासन प्रणालियों के साथ कैसे कार्य करता है", "type": "leaf"}
            ]
        },
        {
            "label": f"प्रक्रियाएं और गतिकी",
            "type": "branch",
            "date": "क्रियाविधि",
            "children": [
                {"label": f"प्राथमिक कारक: {t} के शासन, कार्यान्वयन और रिपोर्टिंग को नियंत्रित करने वाले तत्व", "type": "leaf"},
                {"label": f"स्थानिक वितरण: देश में {t} के प्रशासनिक नेटवर्क और क्षेत्रीय ढांचों का अध्ययन", "type": "leaf"}
            ]
        },
        {
            "label": f"पारिस्थितिक और व्यावहारिक महत्व",
            "type": "branch",
            "date": "महत्व",
            "children": [
                {"label": f"प्रभाव: {t} में परिवर्तन पर्यावरण संरक्षण, संसाधन स्थिरता और जलवायु लचीलेपन को कैसे प्रभावित करते हैं", "type": "leaf"},
                {"label": f"क्षेत्रीय मामले: {t} से संबंधित उल्लेखनीय वैश्विक उदाहरण और राष्ट्रीय नीति मॉडल", "type": "leaf"}
            ]
        },
        {
            "label": f"यूपीएससी परीक्षा दृष्टिकोण (UPSC Focus)",
            "type": "branch",
            "date": "परीक्षा",
            "children": [
                {"label": f"प्रारंभिक परीक्षा: {t} से जुड़े कानूनी प्रावधानों, वैधानिक निकायों और सामान्य परीक्षा भ्रम", "type": "leaf"},
                {"label": f"मुख्य परीक्षा उत्तर लेखन: {t} को अंतर्राष्ट्रीय संधियों, भारत के NDCs और राष्ट्रीय जलवायु रणनीतियों से जोड़ना", "type": "leaf"}
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
