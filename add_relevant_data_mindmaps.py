#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import re
import json

BASE_DIR = r"upsc/environment/Relevant-Environmental-Data-Lists"

def get_clean_title(folder_name):
    # Strip "Data-List-" prefix
    clean = folder_name.replace("Data-List-", "")
    title = re.sub(r'([a-z])([A-Z])', r'\1 \2', clean)
    title = title.replace('-', ' ')
    words = []
    acronyms = {'unesco', 'map', 'mike', 'ramsar', 'wpa', 'ntca', 'mab', 'wnbr'}
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
        "keys": ["biosphere-reserves-in-unescos-map-list"],
        "en": [
            {"label": "UNESCO WNBR Reserves", "type": "branch", "date": "WNBR Network", "children": [
                {"label": "Definition: World Network of Biosphere Reserves; parts of India's biosphere reserves recognized globally under UNESCO's Man and Biosphere (MAB) programme", "type": "leaf"},
                {"label": "Current Status: 12 out of India's 18 biosphere reserves are included in the WNBR list", "type": "leaf"},
                {"label": "First & Latest: Nilgiri Biosphere Reserve was the first to be added (2000); Panna Biosphere Reserve in Madhya Pradesh is the latest addition (2020)", "type": "leaf"}
            ]},
            {"label": "Official List of WNBR Sites in India", "type": "branch", "date": "WNBR Sites", "children": [
                {"label": "WNBR Listed Sites: Nilgiri (2000); Gulf of Mannar (2001); Sundarbans (2001); Nanda Devi (2004); Nokrek (2009); Pachmarhi (2009); Similipal (2009); Achanakmar-Amarkantak (2012); Great Nicobar (2013); Agasthyamalai (2016); Khangchendzonga (2018); Panna (2020)", "type": "leaf"}
            ]}
        ],
        "hi": [
            {"label": "यूनेस्को WNBR आरक्षित क्षेत्र", "type": "branch", "date": "WNBR नेटवर्क", "children": [
                {"label": "परिभाषा: वर्ल्ड नेटवर्क ऑफ बायोस्फीयर रिजर्व; यूनेस्को के मैन एंड बायोस्फीयर (MAB) कार्यक्रम के तहत वैश्विक मान्यता प्राप्त क्षेत्र", "type": "leaf"},
                {"label": "वर्तमान स्थिति: भारत के 18 बायोस्फीयर रिजर्व में से 12 WNBR सूची में शामिल हैं", "type": "leaf"},
                {"label": "प्रथम और नवीनतम: नीलगिरी बायोस्फीयर रिजर्व सबसे पहले (2000) जोड़ा गया था; मध्य प्रदेश का पन्ना नवीनतम जुड़ाव (2020) है", "type": "leaf"}
            ]},
            {"label": "भारत में WNBR स्थलों की आधिकारिक सूची", "type": "branch", "date": "सूची", "children": [
                {"label": "WNBR सूचीबद्ध स्थल: नीलगिरी (2000); मन्नार की खाड़ी (2001); सुंदरवन (2001); नंदा देवी (2004); नोकरेक (2009); पंचमढ़ी (2009); सिमलीपाल (2009); अचानकमार-अमरकंटक (2012); ग्रेट निकोबार (2013); अगस्त्यमलाई (2016); कंचनजंगा (2018); पन्ना (2020)", "type": "leaf"}
            ]}
        ]
    },
    {
        "keys": ["biosphere-reserves"],
        "en": [
            {"label": "Biosphere Reserves Structure", "type": "branch", "date": "Zoning", "children": [
                {"label": "Core Zone: Strictly protected area; no human intervention or tourism allowed; monitors natural ecosystems", "type": "leaf"},
                {"label": "Buffer Zone: Surrounds core zone; limited educational research, tourism, and non-destructive activities allowed", "type": "leaf"},
                {"label": "Transition Zone: Outermost area; sustainable human settlements, cropping, and forestry practices are promoted", "type": "leaf"}
            ]},
            {"label": "Complete List of 18 Biosphere Reserves", "type": "branch", "date": "India List", "children": [
                {"label": "Key Biosphere Reserves: Nilgiri (First); Gulf of Mannar; Sundarbans; Nanda Devi; Nokrek; Pachmarhi; Similipal; Great Nicobar; Cold Desert; Kutch (Largest); Dibru-Saikhowa (Smallest); Seshachalam Hills; Panna; Manas; Dihang-Dibang; Achanakmar-Amarkantak; Khangchendzonga; Agasthyamalai", "type": "leaf"}
            ]}
        ],
        "hi": [
            {"label": "बायोस्फीयर रिजर्व की संरचना", "type": "branch", "date": "ज़ोनिंग", "children": [
                {"label": "कोर ज़ोन (Core Zone): पूर्णतः संरक्षित क्षेत्र; मानवीय गतिविधियों या पर्यटन पर पूरी तरह प्रतिबंध", "type": "leaf"},
                {"label": "बफर ज़ोन (Buffer Zone): कोर क्षेत्र के चारों ओर; सीमित शैक्षिक अनुसंधान, पर्यटन और नियंत्रित गतिविधियों की अनुमति", "type": "leaf"},
                {"label": "संक्रमण ज़ोन (Transition Zone): सबसे बाहरी क्षेत्र; सतत मानव बस्तियों, कृषि और वानिकी को बढ़ावा दिया जाता है", "type": "leaf"}
            ]},
            {"label": "सभी 18 जैवमंडल आरक्षित क्षेत्रों की सूची", "type": "branch", "date": "सूची", "children": [
                {"label": "प्रमुख जैवमंडल आरक्षित क्षेत्र: नीलगिरी (प्रथम); मन्नार की खाड़ी; सुंदरवन; नंदा देवी; नोकरेक; पंचमढ़ी; सिमलीपाल; ग्रेट निकोबार; शीत मरुस्थल; कच्छ का रन (सबसे बड़ा); डिब्रू-सैखोवा (सबसे छोटा); शेषाचलम पहाड़ियाँ; पन्ना; मानस; दिहांग-दिबांग; अचानकमार-अमरकंटक; कंचनजंगा; अगस्त्यमलाई", "type": "leaf"}
            ]}
        ]
    },
    {
        "keys": ["elephant-reserves"],
        "en": [
            {"label": "Project Elephant", "type": "branch", "date": "Initiatives", "children": [
                {"label": "Origins: Launched in 1992 as a Centrally Sponsored Scheme to protect Asiatic elephants, their habitats, and migratory corridors", "type": "leaf"},
                {"label": "Total Reserves: 33 designated Elephant Reserves in India, covering major ranges in Northeast, East-Central, and Southern India", "type": "leaf"}
            ]},
            {"label": "List of Key Elephant Reserves", "type": "branch", "date": "Reserves", "children": [
                {"label": "Key Elephant Reserves: Lemru (Chhattisgarh); Terai (Uttar Pradesh); Singhbhum (Jharkhand); Mayurbhanj (Odisha); Wayanad (Kerala); Periyar (Kerala); Mysore (Karnataka); Nilgiri (Tamil Nadu); Kameng (Arunachal Pradesh); Garo Hills (Meghalaya); Sonitpur (Assam); Dandeli (Karnataka)", "type": "leaf"}
            ]}
        ],
        "hi": [
            {"label": "प्रोजेक्ट एलीफेंट", "type": "branch", "date": "पहलें", "children": [
                {"label": "उत्पत्ति: एशियाई हाथियों, उनके आवासों और प्रवासी गलियारों की रक्षा के लिए 1992 में एक केंद्र प्रायोजित योजना के रूप में शुरू", "type": "leaf"},
                {"label": "कुल रिजर्व: भारत में 33 नामित हाथी रिजर्व (Elephant Reserves), जो पूर्वोत्तर, मध्य-पूर्वी और दक्षिणी भारत में फैले हैं", "type": "leaf"}
            ]},
            {"label": "प्रमुख हाथी आरक्षित क्षेत्रों की सूची", "type": "branch", "date": "सूची", "children": [
                {"label": "प्रमुख हाथी आरक्षित क्षेत्र: लेमरू (छत्तीसगढ़); तराई (उत्तर प्रदेश); सिंहभूम (झारखंड); मयूरभंज (ओडिशा); वायनाड (केरल); पेरियार (केरल); मैसूर (कर्नाटक); नीलगिरी (तमिलनाडु); कामेंग (अरुणाचल प्रदेश); गारो हिल्स (मेघालय); सोनितपुर (असम); दांदेली (कर्नाटक)", "type": "leaf"}
            ]}
        ]
    },
    {
        "keys": ["sacred-groves"],
        "en": [
            {"label": "Sacred Groves Concept", "type": "branch", "date": "Groves", "children": [
                {"label": "Definition: Forest fragments protected by local communities through religious taboos and traditional beliefs; act as biological sanctuaries", "type": "leaf"},
                {"label": "Legal Status: Can be declared as Community Reserves under Wildlife Protection Amendment Act 2002, securing state support", "type": "leaf"}
            ]},
            {"label": "List of Sacred Groves by State", "type": "branch", "date": "State Groves", "children": [
                {"label": "Sacred Groves by State: Maharashtra (Devrai); Kerala (Kavu); Rajasthan (Orans / Dev Vans); Jharkhand (Sarana); Karnataka (Devara Kadu); Meghalaya (Law Kyntang); Himachal Pradesh (Deo Van); Tamil Nadu (Kovil Kadu)", "type": "leaf"}
            ]}
        ],
        "hi": [
            {"label": "पवित्र उपवन (Sacred Groves) अवधारणा", "type": "branch", "date": "उपवन", "children": [
                {"label": "परिभाषा: धार्मिक मान्यताओं और पारंपरिक प्रथाओं के माध्यम से स्थानीय समुदायों द्वारा संरक्षित वन क्षेत्र; जैविक अभयारण्य के रूप में कार्य करते हैं", "type": "leaf"},
                {"label": "कानूनी स्थिति: वन्यजीव संरक्षण संशोधन अधिनियम 2002 के तहत सामुदायिक रिजर्व घोषित किए जा सकते हैं", "type": "leaf"}
            ]},
            {"label": "राज्यवार पवित्र उपवनों की सूची", "type": "branch", "date": "सूची", "children": [
                {"label": "राज्यवार पवित्र उपवन: महाराष्ट्र (देवराई); केरल (कावू); राजस्थान (ओरान / देव वन); झारखंड (सरना); कर्नाटक (देवरा काडू); मेघालय (लॉ किंतंग); हिमाचल प्रदेश (देव वन); तमिलनाडु (कोविल काडू)", "type": "leaf"}
            ]}
        ]
    },
    {
        "keys": ["mangrove-sites"],
        "en": [
            {"label": "Mangrove Adaptation", "type": "branch", "date": "Adaptations", "children": [
                {"label": "Pneumatophores: Specialized aerial breathing roots that grow upwards from the water to intake oxygen in saline anaerobic soils", "type": "leaf"},
                {"label": "Vivipary: Germination strategy where seeds germinate while still attached to the parent tree before falling into water", "type": "leaf"},
                {"label": "Halophytes: Salt-tolerant plants possessing salt glands to excrete excess salt absorbed from sea water", "type": "leaf"}
            ]},
            {"label": "List of Key Mangrove Sites in India", "type": "branch", "date": "Mangrove Sites", "children": [
                {"label": "Key Mangrove Sites: Sundarbans (West Bengal); Bhitarkanika (Odisha); Mahanadi (Odisha); Pichavaram (Tamil Nadu); Muthupet (Tamil Nadu); Coringa (Andhra Pradesh); Krishna (Andhra Pradesh); Goa Mangroves; Ratnagiri (Maharashtra); Karwar (Karnataka); Coondapur (Karnataka)", "type": "leaf"}
            ]}
        ],
        "hi": [
            {"label": "मैंग्रोव अनुकूलन", "type": "branch", "date": "अनुकूलन", "children": [
                {"label": "न्यूमैटोफोर्स (Pneumatophores): विशेष श्वसन जड़ें जो खारे अवायवीय दलदल में ऑक्सीजन लेने के लिए पानी से ऊपर की ओर बढ़ती हैं", "type": "leaf"},
                {"label": "जरायुजता (Vivipary): अंकुरण रणनीति जिसमें बीज मातृ वृक्ष से जुड़े रहने के दौरान ही अंकुरित हो जाते हैं", "type": "leaf"},
                {"label": "लवणमृदोद्भिद (Halophytes): लवण-सहिष्णु पौधे जिनमें अतिरिक्त नमक बाहर निकालने के लिए विशेष ग्रंथियाँ होती हैं", "type": "leaf"}
            ]},
            {"label": "भारत के प्रमुख मैंग्रोव स्थलों की सूची", "type": "branch", "date": "सूची", "children": [
                {"label": "प्रमुख मैंग्रोव स्थल: सुंदरवन (पश्चिम बंगाल); भितरकनिका (ओडिशा); महानदी (ओडिशा); पिचावरम (तमिलनाडु); मुथुपेट (तमिलनाडु); कोरिंगा (आंध्र प्रदेश); कृष्णा (आंध्र प्रदेश); गोवा मैंग्रोव; रत्नागिरी (महाराष्ट्र); कारवार (कर्नाटक); कुंडापुर (कर्नाटक)", "type": "leaf"}
            ]}
        ]
    },
    {
        "keys": ["mike-sites"],
        "en": [
            {"label": "MIKE Programme", "type": "branch", "date": "MIKE", "children": [
                {"label": "Definition: Monitoring the Illegal Killing of Elephants; international program established in 1997 under CITES", "type": "leaf"},
                {"label": "Objectives: Measures trends in elephant poaching, provides information for capacity building, and assists in law enforcement", "type": "leaf"}
            ]},
            {"label": "Complete List of 10 MIKE Sites in India", "type": "branch", "date": "10 Sites", "children": [
                {"label": "All 10 MIKE Sites: Shivalik (Uttarakhand); Mayurbhanj (Odisha); Garo Hills (Meghalaya); Sonitpur (Assam); Chirang-Ripu (Assam); Eastern Dooars (West Bengal); Deomali (Arunachal Pradesh); Mysore (Karnataka); Wayanad (Kerala); Nilgiri (Tamil Nadu)", "type": "leaf"}
            ]}
        ],
        "hi": [
            {"label": "माइक (MIKE) कार्यक्रम", "type": "branch", "date": "माइक", "children": [
                {"label": "परिभाषा: हाथियों की अवैध हत्या की निगरानी (MIKE); CITES के तहत 1997 में स्थापित एक अंतर्राष्ट्रीय कार्यक्रम", "type": "leaf"},
                {"label": "उद्देश्य: हाथियों के अवैध शिकार की प्रवृत्तियों को मापना, क्षमता निर्माण के लिए जानकारी प्रदान करना और कानून प्रवर्तन में सहायता करना", "type": "leaf"}
            ]},
            {"label": "भारत के सभी 10 माइक स्थलों की सूची", "type": "branch", "date": "10 स्थल", "children": [
                {"label": "सभी 10 माइक (MIKE) स्थल: शिवालिक (उत्तराखंड); मयूरभंज (ओडिशा); गारो हिल्स (मेघालय); सोनितपुर (असम); चिरांग-रिपू (असम); पूर्वी डुआर्स (पश्चिम बंगाल); देवमाली (अरुणाचल प्रदेश); मैसूर (कर्नाटक); वायनाड (केरल); नीलगिरी (तमिलनाडु)", "type": "leaf"}
            ]}
        ]
    },
    {
        "keys": ["national-parks"],
        "en": [
            {"label": "National Parks Framework", "type": "branch", "date": "WPA 1972", "children": [
                {"label": "Legal Status: Declared under Section 35 of the Wildlife Protection Act 1972 by state governments; high protection status", "type": "leaf"},
                {"label": "Restrictions: No human activity, forestry operations, or livestock grazing allowed inside boundaries; private rights are completely extinguished", "type": "leaf"}
            ]},
            {"label": "List of Key National Parks", "type": "branch", "date": "National Parks", "children": [
                {"label": "Key National Parks: Hailey/Jim Corbett (First, Uttarakhand); Hemis (Largest, Ladakh); South Button Island (Smallest, Andaman and Nicobar); Kaziranga (Assam); Keoladeo (Rajasthan); Gir (Gujarat); Kanha (Madhya Pradesh); Silent Valley (Kerala); Bandhavgarh (Madhya Pradesh); Namdapha (Arunachal Pradesh)", "type": "leaf"}
            ]}
        ],
        "hi": [
            {"label": "राष्ट्रीय उद्यान ढांचा", "type": "branch", "date": "WPA 1972", "children": [
                {"label": "कानूनी स्थिति: राज्य सरकारों द्वारा वन्यजीव संरक्षण अधिनियम 1972 की धारा 35 के तहत घोषित; उच्च संरक्षण स्तर", "type": "leaf"},
                {"label": "प्रतिबंध: सीमाओं के भीतर मानव निवास, वानिकी कार्य या पशु चराई की अनुमति नहीं है; निजी अधिकार समाप्त कर दिए जाते हैं", "type": "leaf"}
            ]},
            {"label": "प्रमुख राष्ट्रीय उद्यानों की सूची", "type": "branch", "date": "सूची", "children": [
                {"label": "प्रमुख राष्ट्रीय उद्यान: हैली/जिम कॉर्बेट (प्रथम, उत्तराखंड); हेमिस (सबसे बड़ा, लद्दाख); साउथ बटन द्वीप (सबसे छोटा, अंडमान और निकोबार); काजीरंगा (असम); केवलादेव (राजस्थान); गिर (गुजरात); कान्हा (मध्य प्रदेश); साइलेंट वैली (केरल); बांधवगढ़ (मध्य प्रदेश); नामदफा (अरुणाचल प्रदेश)", "type": "leaf"}
            ]}
        ]
    },
    {
        "keys": ["natural-world-heritage-sites"],
        "en": [
            {"label": "Natural Heritage Sites", "type": "branch", "date": "UNESCO Sites", "children": [
                {"label": "Definition: Sites inscribed by UNESCO World Heritage Convention for outstanding universal ecological, biological, or geological values", "type": "leaf"},
                {"label": "Mixed Site: Khangchendzonga National Park in Sikkim is India's only mixed (natural and cultural) world heritage site", "type": "leaf"}
            ]},
            {"label": "Complete List of UNESCO Natural Sites in India", "type": "branch", "date": "Natural Sites", "children": [
                {"label": "Natural & Mixed Sites: Kaziranga National Park (1985); Keoladeo National Park (1985); Manas Wildlife Sanctuary (1985); Sundarbans National Park (1987); Nanda Devi & Valley of Flowers NPs (1988/2005); Western Ghats (2012); Great Himalayan National Park (2014); Khangchendzonga National Park (Mixed, 2016)", "type": "leaf"}
            ]}
        ],
        "hi": [
            {"label": "प्राकृतिक विश्व विरासत स्थल", "type": "branch", "date": "यूनेस्को स्थल", "children": [
                {"label": "परिभाषा: उत्कृष्ट पारिस्थितिक, जैविक या भूवैज्ञानिक मूल्यों के लिए यूनेस्को विश्व विरासत कन्वेंशन द्वारा नामित स्थल", "type": "leaf"},
                {"label": "मिश्रित स्थल: सिक्किम का खांगचेंदजोंगा राष्ट्रीय उद्यान भारत का एकमात्र मिश्रित (प्राकृतिक और सांस्कृतिक) विरासत स्थल है", "type": "leaf"}
            ]},
            {"label": "यूनेस्को प्राकृतिक विश्व धरोहर स्थलों की सूची", "type": "branch", "date": "सूची", "children": [
                {"label": "प्राकृतिक और मिश्रित स्थल: काजीरंगा राष्ट्रीय उद्यान (1985); केवलादेव राष्ट्रीय उद्यान (1985); मानस वन्यजीव अभयारण्य (1985); सुंदरवन राष्ट्रीय उद्यान (1987); नंदा देवी और फूलों की घाटी (1988/2005); पश्चिमी घाट (2012); ग्रेट हिमालयन राष्ट्रीय उद्यान (2014); खांगचेंदजोंगा राष्ट्रीय उद्यान (मिश्रित, 2016)", "type": "leaf"}
            ]}
        ]
    },
    {
        "keys": ["ramsar-wetland-sites"],
        "en": [
            {"label": "Ramsar Sites", "type": "branch", "date": "Wetlands", "children": [
                {"label": "Convention: Ramsar Convention on Wetlands of International Importance, signed in 1971 in Ramsar, Iran; India ratified in 1982", "type": "leaf"},
                {"label": "Montreux Record: Register of wetland sites of international importance where changes in ecological character have occurred or are occurring (includes Keoladeo NP and Loktak Lake; Chilika Lake was removed)", "type": "leaf"}
            ]},
            {"label": "List of Key Ramsar Wetland Sites", "type": "branch", "date": "Wetland List", "children": [
                {"label": "Key Ramsar Sites: Chilika Lake (Odisha); Keoladeo National Park (Rajasthan); Loktak Lake (Manipur); Wular Lake (Jammu and Kashmir); Vembanad-Kol (Kerala); Renuka Wetland (Smallest, Himachal Pradesh); Sambhar Lake (Rajasthan); Sundarban Wetland (Largest, West Bengal); Bhoj Wetland (Madhya Pradesh); Ashtamudi Wetland (Kerala)", "type": "leaf"}
            ]}
        ],
        "hi": [
            {"label": "रामसर आर्द्रभूमि स्थल", "type": "branch", "date": "आर्द्रभूमि", "children": [
                {"label": "कन्वेंशन: अंतर्राष्ट्रीय महत्व की आर्द्रभूमियों पर रामसर कन्वेंशन, 1971 में ईरान के रामसर में हस्ताक्षरित; भारत ने 1982 में इसकी पुष्टि की", "type": "leaf"},
                {"label": "मॉन्ट्रिक्स रिकॉर्ड: उन आर्द्रभूमियों का रजिस्टर जहां पारिस्थितिक चरित्र में प्रतिकूल परिवर्तन हुए हैं (केवलादेव राष्ट्रीय उद्यान और लोकतक झील शामिल हैं)", "type": "leaf"}
            ]},
            {"label": "प्रमुख रामसर आर्द्रभूमि स्थलों की सूची", "type": "branch", "date": "सूची", "children": [
                {"label": "प्रमुख रामसर स्थल: चिल्का झील (ओडिशा); केवलादेव राष्ट्रीय उद्यान (राजस्थान); लोकतक झील (मणिपुर); वुलर झील (जम्मू और कश्मीर); वेम्बनाड-कोल (केरल); रेणुका आर्द्रभूमि (सबसे छोटी, हिमाचल प्रदेश); सांभर झील (राजस्थान); सुंदरवन आर्द्रभूमि (सबसे बड़ी, पश्चिम बंगाल); भोज आर्द्रभूमि (मध्य प्रदेश); अष्टमुडी आर्द्रभूमि (केरल)", "type": "leaf"}
            ]}
        ]
    },
    {
        "keys": ["tiger-reserves"],
        "en": [
            {"label": "Project Tiger", "type": "branch", "date": "Conservation", "children": [
                {"label": "Origins: Launched in 1973; administered by National Tiger Conservation Authority (NTCA), a statutory body under MoEFCC", "type": "leaf"},
                {"label": "Zoning Strategy: Implements Core-Buffer strategy; Core area has legal status of national park/sanctuary; Buffer area has multi-use forestry", "type": "leaf"},
                {"label": "Monitoring Tools: Uses M-STrIPES (Monitoring System for Tigers-Intensive Protection and Ecological Status) GPS app for patrolling and population estimation", "type": "leaf"}
            ]},
            {"label": "Complete List of Key Tiger Reserves", "type": "branch", "date": "Tiger Reserves", "children": [
                {"label": "Key Tiger Reserves: Bandipur (Karnataka); Corbett (Uttarakhand); Kanha (Madhya Pradesh); Manas (Assam); Melghat (Maharashtra); Palamau (Jharkhand); Ranthambore (Rajasthan); Similipal (Odisha); Sundarbans (West Bengal); Guru Ghasidas (Chhattisgarh); Dholpur-Karauli (Rajasthan); Nagarjunasagar-Srisailam (Largest, Andhra Pradesh); Orang (Smallest, Assam)", "type": "leaf"}
            ]}
        ],
        "hi": [
            {"label": "प्रोजेक्ट टाइगर", "type": "branch", "date": "संरक्षण", "children": [
                {"label": "उत्पत्ति: 1973 में शुरू; राष्ट्रीय बाघ संरक्षण प्राधिकरण (NTCA) द्वारा प्रशासित, जो MoEFCC के तहत एक वैधानिक निकाय है", "type": "leaf"},
                {"label": "ज़ोनिंग रणनीति: कोर-बफर रणनीति लागू करता है; कोर क्षेत्र में राष्ट्रीय उद्यान/अभयारण्य का कानूनी दर्जा होता है; बफर बहु-उपयोग वाला होता है", "type": "leaf"},
                {"label": "निगरानी उपकरण: गश्त और जनसंख्या गणना के लिए M-STrIPES (जीपीएस-आधारित ऐप) का उपयोग किया जाता है", "type": "leaf"}
            ]},
            {"label": "प्रमुख बाघ आरक्षित क्षेत्रों की पूरी सूची", "type": "branch", "date": "सूची", "children": [
                {"label": "प्रमुख टाइगर रिजर्व: बांदीपुर (कर्नाटक); कॉर्बेट (उत्तराखंड); कान्हा (मध्य प्रदेश); मानस (असम); मेलघाट (महाराष्ट्र); पलामू (झारखंड); रणथंभौर (राजस्थान); सिमलीपाल (ओडिशा); सुंदरवन (पश्चिम बंगाल); गुरु घासीदास (छत्तीसगढ़); धौलपुर-करौली (राजस्थान); नागार्जुनसागर-श्रीशैलम (सबसे बड़ा, आंध्र प्रदेश); ओरंग (सबसे छोटा, असम)", "type": "leaf"}
            ]}
        ]
    }
]

TRANSLATIONS = {
    "data": "डेटा",
    "list": "सूची",
    "biosphere": "बायोस्फीयर (जैवमंडल)",
    "reserves": "आरक्षित क्षेत्र (रिजर्व)",
    "unescos": "यूनेस्को की",
    "map": "MAB (मैप)",
    "elephant": "हाथी (एलीफेंट)",
    "sacred": "पवित्र",
    "groves": "उपवन (ग्रोव्स)",
    "mangrove": "मैंग्रोव",
    "sites": "स्थल",
    "mike": "माइक (MIKE)",
    "national": "राष्ट्रीय",
    "parks": "उद्यान (पार्क)",
    "natural": "प्राकृतिक",
    "world": "विश्व",
    "heritage": "विरासत",
    "ramsar": "रामसर",
    "wetland": "आर्द्रभूमि",
    "tiger": "बाघ (टाइगर)"
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
                {"label": f"Scientific Framework: Analyzing how {t} integrates with environmental data lists", "type": "leaf"}
            ]
        },
        {
            "label": f"Processes & Dynamics",
            "type": "branch",
            "date": "Mechanisms",
            "children": [
                {"label": f"Primary Drivers: Factors regulating the classification, implementation, and reporting of {t}", "type": "leaf"},
                {"label": f"Spatial Distribution: Exploring the national networks and regional frameworks of {t}", "type": "leaf"}
            ]
        },
        {
            "label": f"Ecological & Applied Values",
            "type": "branch",
            "date": "Applications",
            "children": [
                {"label": f"Impacts: How changes in {t} affect conservation, resource sustainability, and climate resilience", "type": "leaf"}
            ]
        },
        {
            "label": f"UPSC Exam Syllabus Relevance",
            "type": "branch",
            "date": "UPSC Core",
            "children": [
                {"label": f"Prelims Prep: Key protected areas, legal schedules, and locations associated with {t}", "type": "leaf"},
                {"label": f"Mains Answer Writing: Linking {t} with biodiversity conservation treaties and national policies", "type": "leaf"}
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
                {"label": f"वैज्ञानिक ढांचा: {t} पर्यावरण डेटा सूचियों के साथ कैसे कार्य करता है", "type": "leaf"}
            ]
        },
        {
            "label": f"प्रक्रियाएं और गतिकी",
            "type": "branch",
            "date": "क्रियाविधि",
            "children": [
                {"label": f"प्राथमिक कारक: {t} के वर्गीकरण, कार्यान्वयन और रिपोर्टिंग को नियंत्रित करने वाले तत्व", "type": "leaf"},
                {"label": f"स्थानिक वितरण: देश में {t} के प्रशासनिक नेटवर्क और क्षेत्रीय ढांचों का अध्ययन", "type": "leaf"}
            ]
        },
        {
            "label": f"पारिस्थितिक और व्यावहारिक महत्व",
            "type": "branch",
            "date": "महत्व",
            "children": [
                {"label": f"प्रभाव: {t} में परिवर्तन संरक्षण, resource sustainability, और जलवायु लचीलेपन को कैसे प्रभावित करते हैं", "type": "leaf"}
            ]
        },
        {
            "label": f"यूपीएससी परीक्षा दृष्टिकोण (UPSC Focus)",
            "type": "branch",
            "date": "परीक्षा",
            "children": [
                {"label": f"प्रारंभिक परीक्षा: {t} से जुड़े कानूनी प्रावधानों, आरक्षित क्षेत्रों और सामान्य परीक्षा भ्रम", "type": "leaf"},
                {"label": f"मुख्य परीक्षा उत्तर लेखन: {t} को जैव विविधता संरक्षण संधियों और राष्ट्रीय नीतियों से जोड़ना", "type": "leaf"}
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
