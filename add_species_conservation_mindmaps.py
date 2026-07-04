#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import re
import json

BASE_DIR = r"upsc/environment/Species-Related-Terminologies-Conservation-Programs"

def get_clean_title(folder_name):
    # Split camelCase words like ProjectTiger to Project Tiger
    title = re.sub(r'([a-z])([A-Z])', r'\1 \2', folder_name)
    title = title.replace('-', ' ')
    words = []
    acronyms = {'dpsp', 'pri', 'ut', 'uts', 'sc', 'hc', 'cm', 'com', 'arc', 'inc', 'ias', 'sec', 'sfc', 'pej', 'tej', 'mjo', 'enso', 'iod', 'icar', 'gst', 'dpc', 'mpc', 'adc', 'tac', 'scs', 'pesa', 'icar', 'isfr', 'itcz', 'tej', 'iucn', 'wpa', 'sawen', 'mab', 'cbd'}
    for w in title.split():
        if w.lower() in acronyms:
            words.append(w.upper())
        elif w.lower() in ['of', 'and', 'the', 'for', 'in', 'with', 'against', 'to', 'on', 'some', 'by', 'their', 'vs']:
            words.append(w.lower())
        else:
            words.append(w.capitalize())
    return ' '.join(words)

# Fully comprehensive, grouped fact-dense dataset mapping every folder to a specific conservation/species mindmap
GROUPS = [
    {
        "keys": ["action-plan-for-vulture", "vulture-conservation"],
        "en": [
            {"label": "Vulture Decline & Cause", "type": "branch", "date": "Threats", "children": [
                {"label": "Diclofenac: Non-Steroidal Anti-Inflammatory Drug (NSAID) given to cattle; causes renal failure and visceral gout in vultures", "type": "leaf"},
                {"label": "Vulture populations declined by over 99% in India between 1990s and 2000s, leading to ecological sanitation crises", "type": "leaf"}
            ]},
            {"label": "Action Plan for Vulture Conservation 2020-2025", "type": "branch", "date": "Action Plan", "children": [
                {"label": "Drug Regulation: Banning veterinary use of diclofenac, aceclofenac, ketoprofen, and nimesulide", "type": "leaf"},
                {"label": "Vulture Conservation Breeding Centres (VCBC): 8 VCBCs in India (e.g. Pinjore, Rajabhatkhawa) breeding Gyps vultures", "type": "leaf"},
                {"label": "Vulture Safe Zones: Area with zero diclofenac usage within a 100km radius of vulture nesting sites", "type": "leaf"}
            ]},
            {"label": "Vulture Species in India", "type": "branch", "date": "Species", "children": [
                {"label": "Critically Endangered: White-rumped Vulture, Indian Vulture, Slender-billed Vulture, Red-headed Vulture", "type": "leaf"},
                {"label": "Migratory: Eurasian Griffon, Himalayan Griffon, and Cinereous Vultures visit during winter", "type": "leaf"}
            ]},
            {"label": "UPSC Exam Focus", "type": "branch", "date": "UPSC Focus", "children": [
                {"label": "Meloxicam & Tolfenamic Acid: Identified as safe alternative veterinary drugs to replace toxic NSAIDs", "type": "leaf"},
                {"label": "Scavenger services: Vultures prevent carcass decay and control feral dog populations, checking rabies spread", "type": "leaf"}
            ]}
        ],
        "hi": [
            {"label": "गिद्धों में गिरावट और कारण", "type": "branch", "date": "खतरे", "children": [
                {"label": "डाइक्लोफेनाक (Diclofenac): मवेशियों को दी जाने वाली दर्द निवारक दवा; गिद्धों में गुर्दे की विफलता का कारण बनती है", "type": "leaf"},
                {"label": "1990 और 2000 के दशक के बीच भारत में गिद्धों की आबादी में 99% से अधिक की गिरावट आई", "type": "leaf"}
            ]},
            {"label": "गिद्ध संरक्षण कार्य योजना 2020-2025", "type": "branch", "date": "कार्य योजना", "children": [
                {"label": "दवाओं का नियमन: डाइक्लोफेनाक, एसेक्लोफेनाक, कीटोप्रोफेन और निमेसुलाइड के पशु चिकित्सा उपयोग पर प्रतिबंध", "type": "leaf"},
                {"label": "गिद्ध संरक्षण प्रजनन केंद्र (VCBC): भारत में 8 VCBC कार्यरत हैं (जैसे पिंजौर, राजाभटखावा)", "type": "leaf"},
                {"label": "गिद्ध सुरक्षित क्षेत्र (Vulture Safe Zones): गिद्धों के घोंसलों के 100 किमी के दायरे में शून्य डाइक्लोफेनाक उपयोग सुनिश्चित करना", "type": "leaf"}
            ]},
            {"label": "भारत में गिद्धों की प्रजातियां", "type": "branch", "date": "प्रजातियां", "children": [
                {"label": "अति संकटग्रस्त (CR): बंगाल गिद्ध (White-rumped), भारतीय गिद्ध (Gyps indicus), लंबी चोंच वाला गिद्ध, लाल सिर वाला गिद्ध", "type": "leaf"},
                {"label": "प्रवासी गिद्ध: यूरेशियन ग्रिफॉन, हिमालयन ग्रिफॉन और सिनेरियस गिद्ध सर्दियों में भारत आते हैं", "type": "leaf"}
            ]},
            {"label": "यूपीएससी परीक्षा दृष्टिकोण", "type": "branch", "date": "परीक्षा", "children": [
                {"label": "मेलोक्सिकैम और टोल्फेनामिक एसिड: जहरीले एनएसएआईडी को बदलने के लिए सुरक्षित वैकल्पिक दवाएं घोषित", "type": "leaf"},
                {"label": "सफाई सेवाएँ: गिद्ध शवों के सड़ने को रोकते हैं और आवारा कुत्तों की आबादी को नियंत्रित कर रेबीज को रोकते हैं", "type": "leaf"}
            ]}
        ]
    },
    {
        "keys": ["aichi-biodiversity"],
        "en": [
            {"label": "Aichi Targets Origin", "type": "branch", "date": "Origin", "children": [
                {"label": "Adopted at CBD COP-10 in Nagoya, Aichi Prefecture, Japan (2010) as part of the Strategic Plan for Biodiversity 2011-2020", "type": "leaf"},
                {"label": "Set 20 global targets organized under 5 Strategic Goals (A to E) to halt global biodiversity loss", "type": "leaf"}
            ]},
            {"label": "Five Strategic Goals", "type": "branch", "date": "Goals", "children": [
                {"label": "Goal A: Address underlying causes of biodiversity loss by mainstreaming it across government and society", "type": "leaf"},
                {"label": "Goal B: Reduce direct pressures on biodiversity and promote sustainable use", "type": "leaf"},
                {"label": "Goal C: Improve status of biodiversity by safeguarding ecosystems, species, and genetic diversity", "type": "leaf"},
                {"label": "Goal D & E: Enhance benefits to all and implement biodiversity planning through participatory management", "type": "leaf"}
            ]},
            {"label": "Key Specific Targets", "type": "branch", "date": "Key Targets", "children": [
                {"label": "Target 11: Protecting 17% of terrestrial and inland water areas, and 10% of coastal and marine areas by 2020", "type": "leaf"},
                {"label": "Target 16: Nagoya Protocol on ABS to enter into force and be operational by 2015", "type": "leaf"}
            ]},
            {"label": "UPSC Exam Focus", "type": "branch", "date": "UPSC Focus", "children": [
                {"label": "Outcome: Global assessment showed that none of the 20 Aichi targets were fully met by 2020", "type": "leaf"},
                {"label": "Successor: Replaced by the Kunming-Montreal Global Biodiversity Framework (COP-15 in 2022) with the '30x30' goal", "type": "leaf"}
            ]}
        ],
        "hi": [
            {"label": "आइची लक्ष्यों की उत्पत्ति", "type": "branch", "date": "उत्पत्ति", "children": [
                {"label": "जैव विविधता पर रणनीतिक योजना 2011-2020 के हिस्से के रूप में नागोया, आइची प्रान्त, जापान (2010) में CBD COP-10 में अपनाया गया", "type": "leaf"},
                {"label": "वैश्विक जैव विविधता हानि को रोकने के लिए 5 रणनीतिक लक्ष्यों (A से E) के तहत संगठित 20 वैश्विक लक्ष्य निर्धारित किए गए", "type": "leaf"}
            ]},
            {"label": "पांच रणनीतिक लक्ष्य", "type": "branch", "date": "लक्ष्य", "children": [
                {"label": "लक्ष्य A: सरकार और समाज में जैव विविधता को शामिल करके इसके नुकसान के अंतर्निहित कारणों को संबोधित करना", "type": "leaf"},
                {"label": "लक्ष्य B: जैव विविधता पर प्रत्यक्ष दबाव को कम करना और सतत उपयोग को बढ़ावा देना", "type": "leaf"},
                {"label": "लक्ष्य C: पारिस्थितिक तंत्र, प्रजातियों और आनुवंशिक विविधता की रक्षा करके जैव विविधता की स्थिति में सुधार करना", "type": "leaf"},
                {"label": "लक्ष्य D और E: जैव विविधता से सभी को मिलने वाले लाभ बढ़ाना और सहभागी प्रबंधन के माध्यम से योजनाएं लागू करना", "type": "leaf"}
            ]},
            {"label": "प्रमुख विशिष्ट लक्ष्य", "type": "branch", "date": "मुख्य लक्ष्य", "children": [
                {"label": "लक्ष्य 11: 2020 तक 17% स्थलीय और आंतरिक जल क्षेत्रों तथा 10% तटीय और समुद्री क्षेत्रों का संरक्षण सुनिश्चित करना", "type": "leaf"},
                {"label": "लक्ष्य 16: ABS पर नागोया प्रोटोकॉल को 2015 तक पूरी तरह से लागू और संचालित करना", "type": "leaf"}
            ]},
            {"label": "यूपीएससी परीक्षा दृष्टिकोण", "type": "branch", "date": "परीक्षा", "children": [
                {"label": "परिणाम: वैश्विक मूल्यांकन से पता चला कि 2020 तक 20 आइची लक्ष्यों में से कोई भी पूरी तरह से प्राप्त नहीं हुआ था", "type": "leaf"},
                {"label": "उत्तराधिकारी: COP-15 (2022) में कुनमिंग-मॉन्ट्रियल वैश्विक जैव विविधता ढांचे द्वारा प्रतिस्थापित, जिसमें '30x30' लक्ष्य शामिल है", "type": "leaf"}
            ]}
        ]
    },
    {
        "keys": ["biodiversity-hotspots"],
        "en": [
            {"label": "Hotspots Definition Criteria", "type": "branch", "date": "Criteria", "children": [
                {"label": "Conceived by Norman Myers (1988); represents areas of high species richness and extreme threat", "type": "leaf"},
                {"label": "Criteria 1: Must contain at least 1,500 species of vascular plants as endemics (>0.5% of world's total)", "type": "leaf"},
                {"label": "Criteria 2: Must have lost at least 70% of its original primary native vegetation", "type": "leaf"}
            ]},
            {"label": "Biodiversity Hotspots in India", "type": "branch", "date": "India Hotspots", "children": [
                {"label": "Himalayas: Spans entire Indian Himalayan region; high altitudinal plant diversity and endemism", "type": "leaf"},
                {"label": "Western Ghats: High rainfall region; features endangered species like Lion-tailed Macaque and Nilgiri Tahr", "type": "leaf"},
                {"label": "Indo-Burma: Spans Northeast India (excluding Assam valley) down to Southeast Asia", "type": "leaf"},
                {"label": "Sundaland: Spans Nicobar Islands, Indonesia, Malaysia, and Singapore; rich tropical rainforest biome", "type": "leaf"}
            ]},
            {"label": "Global Hotspots Status", "type": "branch", "date": "Global", "children": [
                {"label": "Currently 36 biodiversity hotspots recognized globally, covering 2.3% of Earth's land surface but hosting >50% of endemic plants", "type": "leaf"},
                {"label": "Managed and funded internationally through Conservation International (CI) and Critical Ecosystem Partnership Fund", "type": "leaf"}
            ]},
            {"label": "UPSC Exam Focus", "type": "branch", "date": "UPSC Focus", "children": [
                {"label": "Hottest Hotspots: Western Ghats and Indo-Burma are identified among the 8 global 'hottest hotspots'", "type": "leaf"},
                {"label": "Hope Spots: Marine equivalents of biodiversity hotspots, designated by Mission Blue (e.g. Andaman & Nicobar, Lakshadweep)", "type": "leaf"}
            ]}
        ],
        "hi": [
            {"label": "हॉटस्पॉट परिभाषा के मानदंड", "type": "branch", "date": "मानदंड", "children": [
                {"label": "नॉर्मन मायर्स (1988) द्वारा संकल्पित; उच्च प्रजाति समृद्धि और अत्यधिक खतरे वाले क्षेत्रों का प्रतिनिधित्व", "type": "leaf"},
                {"label": "मानदंड 1: कम से कम 1,500 संवहनी पौधों (Vascular plants) की स्थानिक प्रजातियां होनी चाहिए", "type": "leaf"},
                {"label": "मानदंड 2: अपने मूल प्राथमिक प्राकृतिक आवास का कम से कम 70% हिस्सा खो चुका होना चाहिए", "type": "leaf"}
            ]},
            {"label": "भारत में जैव विविधता हॉटस्पॉट", "type": "branch", "date": "भारत के हॉटस्पॉट", "children": [
                {"label": "हिमालय: संपूर्ण भारतीय हिमालयी क्षेत्र; उच्च अल्पाइन वनस्पति और स्थानिकता", "type": "leaf"},
                {"label": "पश्चिमी घाट: उच्च वर्षा क्षेत्र; लायन-टेल्ड मकाक और नीलगिरी तहर जैसी लुप्तप्राय प्रजातियों का घर", "type": "leaf"},
                {"label": "इंडो-बर्मा: पूर्वोत्तर भारत (असम घाटी को छोड़कर) से लेकर दक्षिण-पूर्व एशिया तक फैला क्षेत्र", "type": "leaf"},
                {"label": "सुंडालैंड: निकोबार द्वीप समूह, इंडोनेशिया, मलेशिया को कवर करने वाला समृद्ध उष्णकटिबंधीय वर्षावन बायोम", "type": "leaf"}
            ]},
            {"label": "वैश्विक हॉटस्पॉट स्थिति", "type": "branch", "date": "वैश्विक", "children": [
                {"label": "वर्तमान में वैश्विक स्तर पर 36 जैव विविधता हॉटस्पॉट मान्यता प्राप्त हैं, जो पृथ्वी की भूमि का केवल 2.3% हैं", "type": "leaf"},
                {"label": "कंजर्वेशन इंटरनेशनल (CI) और क्रिटिकल इकोसिस्टम पार्टनरशिप फंड के माध्यम से अंतरराष्ट्रीय वित्त पोषण प्राप्त होता है", "type": "leaf"}
            ]},
            {"label": "यूपीएससी परीक्षा दृष्टिकोण", "type": "branch", "date": "परीक्षा", "children": [
                {"label": "हॉटेस्ट हॉटस्पॉट: पश्चिमी घाट और इंडो-बर्मा को वैश्विक स्तर पर 8 'सबसे गर्म हॉटस्पॉट' में स्थान प्राप्त है", "type": "leaf"},
                {"label": "होप स्पॉट्स (Hope Spots): जैव विविधता हॉटस्पॉट के समुद्री समकक्ष, मिशन ब्लू द्वारा नामित (जैसे अंडमान और निकोबार, लक्षद्वीप)", "type": "leaf"}
            ]}
        ]
    },
    {
        "keys": ["cartagena-protocol"],
        "en": [
            {"label": "Cartagena Protocol Origin", "type": "branch", "date": "Overview", "children": [
                {"label": "Adopted in January 2000 as a supplementary agreement to the CBD; entered into force in September 2003", "type": "leaf"},
                {"label": "Governs the biosafety of Living Modified Organisms (LMOs) resulting from modern biotechnology", "type": "leaf"}
            ]},
            {"label": "Core Objectives", "type": "branch", "date": "Objectives", "children": [
                {"label": "Safe handling, transfer, and use of LMOs to protect biodiversity and human health from potential risks", "type": "leaf"},
                {"label": "Establishes a binding regulatory framework to ensure exporting countries notify and get consent from importing countries", "type": "leaf"}
            ]},
            {"label": "Key Mechanisms", "type": "branch", "date": "Mechanisms", "children": [
                {"label": "Advance Informed Agreement (AIA): Prior consent procedure required before first transboundary movement of LMOs for environment release", "type": "leaf"},
                {"label": "Biosafety Clearing-House (BCH): Online portal facilitating sharing of scientific, technical, and regulatory LMO information", "type": "leaf"}
            ]},
            {"label": "UPSC Exam Focus", "type": "branch", "date": "UPSC Focus", "children": [
                {"label": "Precautionary Principle: Key driver allowing importing nations to restrict LMO imports even in absence of full scientific certainty of risk", "type": "leaf"},
                {"label": "Nodal agency in India: Ministry of Environment, Forest and Climate Change (MoEFCC) operates as the national focal point", "type": "leaf"}
            ]}
        ],
        "hi": [
            {"label": "कार्टाजेना प्रोटोकॉल की उत्पत्ति", "type": "branch", "date": "परिचय", "children": [
                {"label": "जनवरी 2000 में CBD के पूरक समझौते के रूप में अपनाया गया; सितंबर 2003 में लागू हुआ", "type": "leaf"},
                {"label": "आधुनिक जैव प्रौद्योगिकी से उत्पन्न जीवित संशोधित जीवों (LMOs) की जैव सुरक्षा को नियंत्रित करता है", "type": "leaf"}
            ]},
            {"label": "मुख्य उद्देश्य", "type": "branch", "date": "उद्देश्य", "children": [
                {"label": "संभावित जोखिमों से जैव विविधता और मानव स्वास्थ्य की रक्षा के लिए LMOs का सुरक्षित संचालन, हस्तांतरण और उपयोग", "type": "leaf"},
                {"label": "यह सुनिश्चित करने के लिए एक बाध्यकारी ढांचा कि निर्यातक देश आयातक देश को पूर्व सूचना और सहमति प्रदान करें", "type": "leaf"}
            ]},
            {"label": "प्रमुख तंत्र (Mechanisms)", "type": "branch", "date": "तंत्र", "children": [
                {"label": "अग्रिम सूचित समझौता (AIA): पर्यावरण में LMOs की पहली सीमा पार आवाजाही से पहले पूर्व सहमति प्रक्रिया आवश्यक", "type": "leaf"},
                {"label": "बायोसेफ्टी क्लियरिंग-हाउस (BCH): LMO की वैज्ञानिक, तकनीकी और विनियामक जानकारी साझा करने के लिए ऑनलाइन पोर्टल", "type": "leaf"}
            ]},
            {"label": "यूपीएससी परीक्षा दृष्टिकोण", "type": "branch", "date": "परीक्षा", "children": [
                {"label": "एहतियाती सिद्धांत (Precautionary Principle): आयातक देशों को वैज्ञानिक निश्चितता की कमी में भी LMO आयात को रोकने की अनुमति देता है", "type": "leaf"},
                {"label": "भारत में नोडल एजेंसी: पर्यावरण, वन और जलवायु परिवर्तन मंत्रालय (MoEFCC) राष्ट्रीय फोकल प्वाइंट के रूप में कार्य करता है", "type": "leaf"}
            ]}
        ]
    },
    {
        "keys": ["cbd-convention"],
        "en": [
            {"label": "CBD Origin & Treaty", "type": "branch", "date": "Treaty", "children": [
                {"label": "Opened for signature at Rio Earth Summit in June 1992; entered into force in December 1993", "type": "leaf"},
                {"label": "Legally binding international treaty; ratified by 196 countries (US has signed but not ratified)", "type": "leaf"}
            ]},
            {"label": "Three Main Objectives", "type": "branch", "date": "Objectives", "children": [
                {"label": "Conservation of Biological Diversity: Protecting species, habitats, and ecosystems globally", "type": "leaf"},
                {"label": "Sustainable Use: Ensuring biological components are utilized without long-term depletion", "type": "leaf"},
                {"label": "Access & Benefit Sharing (ABS): Fair sharing of benefits arising from the utilization of genetic resources", "type": "leaf"}
            ]},
            {"label": "Protocols Under CBD", "type": "branch", "date": "Protocols", "children": [
                {"label": "Cartagena Protocol (2000): Biosafety regulations regarding Living Modified Organisms (LMOs)", "type": "leaf"},
                {"label": "Nagoya Protocol (2010): Establishes legally binding regulations for Access and Benefit Sharing of genetic resources", "type": "leaf"}
            ]},
            {"label": "UPSC Exam Focus", "type": "branch", "date": "UPSC Focus", "children": [
                {"label": "Kunming-Montreal Global Biodiversity Framework (COP-15, 2022): Sets 4 goals and 23 targets for 2030, including the 30x30 target", "type": "leaf"},
                {"label": "Biological Diversity Act 2002: Enacted by India to fulfill CBD mandates, establishing the NBA in Chennai", "type": "leaf"}
            ]}
        ],
        "hi": [
            {"label": "CBD की उत्पत्ति और संधि", "type": "branch", "date": "इतिहास", "children": [
                {"label": "जून 1992 में रियो अर्थ समिट में हस्ताक्षर के लिए खोला गया; दिसंबर 1993 में लागू हुआ", "type": "leaf"},
                {"label": "कानूनी रूप से बाध्यकारी अंतरराष्ट्रीय संधि; 196 देशों द्वारा अनुसमर्थित (अमेरिका ने हस्ताक्षर किए हैं लेकिन अनुसमर्थन नहीं)", "type": "leaf"}
            ]},
            {"label": "तीन मुख्य उद्देश्य", "type": "branch", "date": "उद्देश्य", "children": [
                {"label": "जैव विविधता का संरक्षण: वैश्विक स्तर पर प्रजातियों, आवासों और पारिस्थितिक तंत्रों का संरक्षण", "type": "leaf"},
                {"label": "सतत उपयोग: यह सुनिश्चित करना कि जैविक संसाधनों का उपयोग उनकी दीर्घकालिक कमी के बिना किया जाए", "type": "leaf"},
                {"label": "एक्सेस और बेनिफिट शेयरिंग (ABS): आनुवंशिक संसाधनों के उपयोग से प्राप्त लाभों का उचित और न्यायसंगत साझाकरण", "type": "leaf"}
            ]},
            {"label": "CBD के तहत प्रोटोकॉल", "type": "branch", "date": "प्रोटोकॉल", "children": [
                {"label": "कार्टाजेना प्रोटोकॉल (2000): जीवित संशोधित जीवों (LMOs) के संबंध में जैव सुरक्षा नियम", "type": "leaf"},
                {"label": "नागोया प्रोटोकॉल (2010): आनुवंशिक संसाधनों के एक्सेस और बेनिफिट शेयरिंग के लिए कानूनी रूप से बाध्यकारी नियम", "type": "leaf"}
            ]},
            {"label": "यूपीएससी परीक्षा दृष्टिकोण", "type": "branch", "date": "परीक्षा", "children": [
                {"label": "कुनमिंग-मॉन्ट्रियल वैश्विक जैव विविधता ढांचा (COP-15, 2022): 2030 के लिए 4 लक्ष्य और 23 कार्य निर्धारित, जिसमें 30x30 लक्ष्य शामिल है", "type": "leaf"},
                {"label": "जैव विविधता अधिनियम 2002: भारत द्वारा CBD के उद्देश्यों को पूरा करने के लिए अधिनियमित, चेन्नई में NBA की स्थापना की गई", "type": "leaf"}
            ]}
        ]
    },
    {
        "keys": ["charismatic-species"],
        "en": [
            {"label": "Definition & Appeal", "type": "branch", "date": "Concept", "children": [
                {"label": "Species with widespread popular appeal, used by environmental groups to raise conservation funds", "type": "leaf"},
                {"label": "Typically large, visually appealing mammals (e.g. Giant Panda, Bengal Tiger, African Elephant)", "type": "leaf"}
            ]},
            {"label": "Conservation Utility", "type": "branch", "date": "Value", "children": [
                {"label": "Flagship role: Symbolizes conservation campaigns, driving public donations and political support", "type": "leaf"},
                {"label": "Umbrella effect: Funding generated to protect charismatic species covers their entire habitat and co-occurring species", "type": "leaf"}
            ]},
            {"label": "Ecological Bias Critiques", "type": "branch", "date": "Critiques", "children": [
                {"label": "Taxonomic Bias: Conservation funds disproportionately favor birds and mammals over insects, fungi, and plants", "type": "leaf"},
                {"label": "Neglects less appealing but ecologically vital species (e.g., decomposers, soil microbes)", "type": "leaf"}
            ]},
            {"label": "UPSC Exam Focus", "type": "branch", "date": "UPSC Focus", "children": [
                {"label": "WWF logo: The Giant Panda (Ailuropoda melanoleuca) has been the global symbol of WWF since 1961", "type": "leaf"},
                {"label": "Contrast with Keystone: Keystones are defined by ecological impact; charismatic species by public perception", "type": "leaf"}
            ]}
        ],
        "hi": [
            {"label": "परिभाषा और अपील", "type": "branch", "date": "अवधारणा", "children": [
                {"label": "व्यापक लोकप्रिय अपील वाली प्रजातियाँ, जिनका उपयोग संरक्षण निधि जुटाने के लिए प्रतीक के रूप में किया जाता है", "type": "leaf"},
                {"label": "आम तौर पर बड़े, दिखने में आकर्षक स्तनधारी (जैसे विशाल पांडा, बंगाल टाइगर, अफ्रीकी हाथी)", "type": "leaf"}
            ]},
            {"label": "संरक्षण में उपयोगिता", "type": "branch", "date": "मूल्य", "children": [
                {"label": "फ्लैगशिप भूमिका: संरक्षण अभियानों का प्रतीक, जो सार्वजनिक दान और राजनीतिक समर्थन जुटाता है", "type": "leaf"},
                {"label": "अम्ब्रेला प्रभाव: करिश्माई प्रजातियों की रक्षा के लिए जुटाया गया धन उनके पूरे आवास और सह-प्रजातियों को सुरक्षित करता है", "type": "leaf"}
            ]},
            {"label": "पारिस्थितिक पूर्वाग्रह की आलोचना", "type": "branch", "date": "आलोचना", "children": [
                {"label": "वर्गीकरण पूर्वाग्रह (Taxonomic Bias): कीटों, कवक और पौधों की तुलना में पक्षियों और स्तनधारियों को अधिक वित्तीय प्राथमिकता", "type": "leaf"},
                {"label": "कम आकर्षक लेकिन पारिस्थितिक रूप से आवश्यक प्रजातियों (जैसे अपघटक, मिट्टी के रोगाणु) की उपेक्षा का खतरा", "type": "leaf"}
            ]},
            {"label": "यूपीएससी परीक्षा दृष्टिकोण", "type": "branch", "date": "परीक्षा", "children": [
                {"label": "WWF लोगो: विशाल पांडा (Giant Panda) 1961 से WWF का वैश्विक प्रतीक रहा है", "type": "leaf"},
                {"label": "कीस्टोन के साथ तुलना: कीस्टोन पारिस्थितिक प्रभाव से परिभाषित होते हैं; करिश्माई प्रजातियां मानवीय पसंद से", "type": "leaf"}
            ]}
        ]
    },
    {
        "keys": ["conservation-assured", "tiger-standards"],
        "en": [
            {"label": "CA|TS Overview", "type": "branch", "date": "Overview", "children": [
                {"label": "Conservation Assured Tiger Standards: Global accreditation tool developed by WWF and Tiger Range Countries", "type": "leaf"},
                {"label": "Defines minimum standards for effective management of wild tiger sites, facilitating audit and assessment", "type": "leaf"}
            ]},
            {"label": "Accreditation in India", "type": "branch", "date": "India Status", "children": [
                {"label": "14 Tiger Reserves in India achieved CA|TS accreditation in July 2021 (e.g. Manas, Kaziranga, Kanha, Pench, Sundarbans)", "type": "leaf"},
                {"label": "Administered nationally by the National Tiger Conservation Authority (NTCA) to monitor reserve standards", "type": "leaf"}
            ]},
            {"label": "Core Objectives", "type": "branch", "date": "Objectives", "children": [
                {"label": "Standardize protection, community engagement, habitat management, and tiger population monitoring across range countries", "type": "leaf"},
                {"label": "Reduces poaching pressures and strengthens local support through structured benefit sharing", "type": "leaf"}
            ]},
            {"label": "UPSC Exam Focus", "type": "branch", "date": "UPSC Focus", "children": [
                {"label": "Tx2 Target: Global commitment made in 2010 to double wild tiger populations; CA|TS serves as the key audit tool", "type": "leaf"},
                {"label": "Global Tiger Forum (GTF) acts as the coordinating international body promoting CA|TS implementation", "type": "leaf"}
            ]}
        ],
        "hi": [
            {"label": "CA|TS का अवलोकन", "type": "branch", "date": "अवलोकन", "children": [
                {"label": "कंजर्वेशन एश्योर्ड टाइगर स्टैंडर्ड्स: WWF और टाइगर रेंज देशों द्वारा विकसित एक वैश्विक मान्यता उपकरण", "type": "leaf"},
                {"label": "बाघ क्षेत्रों के प्रभावी प्रबंधन के लिए न्यूनतम मानदंड निर्धारित करता है, जिससे ऑडिट और मूल्यांकन आसान होता है", "type": "leaf"}
            ]},
            {"label": "भारत में मान्यता", "type": "branch", "date": "भारत में स्थिति", "children": [
                {"label": "जुलाई 2021 में भारत के 14 बाघ अभयारण्यों को CA|TS मान्यता मिली (जैसे मानस, काजीरंगा, कान्हा, पेंच, सुंदरवन)", "type": "leaf"},
                {"label": "टाइगर रिजर्व मानकों की निगरानी के लिए राष्ट्रीय स्तर पर राष्ट्रीय बाघ संरक्षण प्राधिकरण (NTCA) द्वारा संचालित", "type": "leaf"}
            ]},
            {"label": "मुख्य उद्देश्य", "type": "branch", "date": "उद्देश्य", "children": [
                {"label": "सुरक्षा, सामुदायिक जुड़ाव, आवास प्रबंधन और बाघों की संख्या की निगरानी को सभी रेंज देशों में मानकीकृत करना", "type": "leaf"},
                {"label": "अवैध शिकार के दबाव को कम करना और स्थानीय लोगों में संरक्षण के प्रति विश्वास मजबूत करना", "type": "leaf"}
            ]},
            {"label": "यूपीएससी परीक्षा दृष्टिकोण", "type": "branch", "date": "परीक्षा", "children": [
                {"label": "Tx2 लक्ष्य: 2010 में जंगली बाघों की आबादी को दोगुना करने की वैश्विक प्रतिबद्धता; CA|TS प्रमुख ऑडिट उपकरण है", "type": "leaf"},
                {"label": "ग्लोबल टाइगर फोरम (GTF) CA|TS कार्यान्वयन को बढ़ावा देने वाले अंतरराष्ट्रीय समन्वय निकाय के रूप में कार्य करता है", "type": "leaf"}
            ]}
        ]
    },
    {
        "keys": ["crocodile-conservation", "project-crocodile", "project-crocod"],
        "en": [
            {"label": "Project Crocodile Launch", "type": "branch", "date": "Overview", "children": [
                {"label": "Launched in 1975 in Odisha (Tikarpada and Bhitarkanika) with financial assistance from FAO and UNDP", "type": "leaf"},
                {"label": "Addressed extreme depletion of crocodilian species in India due to hunting and habitat loss", "type": "leaf"}
            ]},
            {"label": "Three Target Species", "type": "branch", "date": "Species", "children": [
                {"label": "Gharial (Gavialis gangeticus): Critically Endangered; fish-eating crocodile with long narrow snout, endemic to Indian subcontinent", "type": "leaf"},
                {"label": "Mugger (Crocodylus palustris): Vulnerable; marsh crocodile inhabiting freshwater lakes and rivers in India", "type": "leaf"},
                {"label": "Saltwater Crocodile (Crocodylus porosus): Least Concern; largest living reptile, found in Bhitarkanika (Odisha) and Sunderbans", "type": "leaf"}
            ]},
            {"label": "Conservation Strategy", "type": "branch", "date": "Strategy", "children": [
                {"label": "Rear and Release: Collecting wild eggs, hatching them in captivity, rearing juveniles, and reintroducing them into wild", "type": "leaf"},
                {"label": "National Chambal Sanctuary: Created on Chambal River spanning MP, UP, and Rajasthan specifically for Gharials", "type": "leaf"}
            ]},
            {"label": "UPSC Exam Focus", "type": "branch", "date": "UPSC Focus", "children": [
                {"label": "Gharial Habitat: Restricted primarily to clean, fast-flowing rivers; Chambal holds the largest wild population", "type": "leaf"},
                {"label": "Bhitarkanika Sanctuary (Odisha) holds the highest density of saltwater crocodiles in India", "type": "leaf"}
            ]}
        ],
        "hi": [
            {"label": "परियोजना मगरमच्छ की शुरुआत", "type": "branch", "date": "इतिहास", "children": [
                {"label": "1975 में ओडिशा (टीकरपाड़ा और भितरकनिका) में FAO और UNDP की वित्तीय सहायता से शुरू की गई", "type": "leaf"},
                {"label": "शिकार और आवास के नुकसान के कारण भारत में मगरमच्छ प्रजातियों की अत्यधिक गिरावट को रोकना", "type": "leaf"}
            ]},
            {"label": "तीन लक्षित प्रजातियां", "type": "branch", "date": "प्रजातियां", "children": [
                {"label": "घड़ियाल (Gavialis gangeticus): अति संकटग्रस्त (CR); लंबी पतली थूथन वाला मछली खाने वाला मगरमच्छ", "type": "leaf"},
                {"label": "मगर (Mugger): संवेदनशील (VU); मीठे पानी की झीलों और नदियों में रहने वाला दलदली मगरमच्छ", "type": "leaf"},
                {"label": "खारे पानी का मगरमच्छ (Saltwater): सबसे बड़ा जीवित सरीसृप, भितरकनिका (ओडिशा) और सुंदरवन में पाया जाता है", "type": "leaf"}
            ]},
            {"label": "संरक्षण की रणनीति", "type": "branch", "date": "रणनीति", "children": [
                {"label": "पालन और विमुक्ति (Rear and Release): जंगली अंडे एकत्र करना, कृत्रिम रूप से सेना, बच्चों को बड़ा कर पुनः विमुक्त करना", "type": "leaf"},
                {"label": "राष्ट्रीय चंबल अभयारण्य: मुख्य रूप से घड़ियालों की रक्षा के लिए चंबल नदी (MP, UP, राजस्थान) पर निर्मित", "type": "leaf"}
            ]},
            {"label": "यूपीएससी परीक्षा दृष्टिकोण", "type": "branch", "date": "परीक्षा", "children": [
                {"label": "घड़ियाल आवास: मुख्य रूप से स्वच्छ, तीव्र बहने वाली नदियों तक सीमित; चंबल में सबसे बड़ी आबादी है", "type": "leaf"},
                {"label": "ओडिशा का भितरकनिका अभयारण्य भारत में खारे पानी के मगरमच्छों का सबसे बड़ा निवास स्थान है", "type": "leaf"}
            ]}
        ]
    },
    {
        "keys": ["dolphin-conservation", "ganges-dolphin", "dolphin"],
        "en": [
            {"label": "Ganges River Dolphin Status", "type": "branch", "date": "Ganges Dolphin", "children": [
                {"label": "Ganges Dolphin (Platanista gangetica): Endangered; declared National Aquatic Animal of India in 2009", "type": "leaf"},
                {"label": "Blind Mammal: Effectively blind; utilizes sonar/echolocation (producing click sounds, locally called 'Susu') to hunt in turbid waters", "type": "leaf"}
            ]},
            {"label": "Habitat & Range", "type": "branch", "date": "Habitat", "children": [
                {"label": "Endemic to Ganges-Brahmaputra-Meghna and Karnaphuli-Sangu river systems of India, Nepal, and Bangladesh", "type": "leaf"},
                {"label": "Requires deep pool habitats with slow currents; cannot survive in saline marine environments", "type": "leaf"}
            ]},
            {"label": "Project Dolphin", "type": "branch", "date": "Project Dolphin", "children": [
                {"label": "Announced on Independence Day 2020 by Prime Minister; models Project Tiger style protection", "type": "leaf"},
                {"label": "Focuses on modern river patrolling, monitoring, and reducing threats from gillnets and river pollution", "type": "leaf"}
            ]},
            {"label": "UPSC Exam Focus", "type": "branch", "date": "UPSC Focus", "children": [
                {"label": "Vikramshila Gangetic Dolphin Sanctuary (Bihar): India's only dedicated sanctuary for Gangetic dolphins", "type": "leaf"},
                {"label": "Threats: Siltation, dam construction fragmenting populations, and heavy organic pesticide pollution (bioaccumulation)", "type": "leaf"}
            ]}
        ],
        "hi": [
            {"label": "गंगा नदी डॉल्फ़िन की स्थिति", "type": "branch", "date": "गंगा डॉल्फ़िन", "children": [
                {"label": "गंगा डॉल्फ़िन (Platanista gangetica): लुप्तप्राय (EN); 2009 में भारत का राष्ट्रीय जलीय जीव घोषित किया गया", "type": "leaf"},
                {"label": "दृष्टिहीन स्तनधारी: पूर्णतः अंधी होती है; शिकार के लिए प्रतिध्वनि निर्धारण (Echolocation - सूँस/Susu) का उपयोग करती है", "type": "leaf"}
            ]},
            {"label": "आवास और क्षेत्र", "type": "branch", "date": "आवास", "children": [
                {"label": "भारत, नेपाल और बांग्लादेश की गंगा-ब्रह्मपुत्र-मेघना और कर्णफुली-सांगू नदी प्रणालियों की स्थानिक प्रजाति", "type": "leaf"},
                {"label": "धीमी गति वाले गहरे पानी के गर्तों की आवश्यकता होती है; खारे पानी के समुद्री वातावरण में जीवित नहीं रह सकती", "type": "leaf"}
            ]},
            {"label": "प्रोजेक्ट डॉल्फ़िन", "type": "branch", "date": "परियोजना", "children": [
                {"label": "प्रधानमंत्री द्वारा स्वतंत्रता दिवस 2020 पर घोषित; प्रोजेक्ट टाइगर की तर्ज पर संरक्षण रणनीतियां लागू करना", "type": "leaf"},
                {"label": "नदी गश्त, आधुनिक निगरानी उपकरणों के उपयोग और नदी प्रदूषण तथा जाल में फंसने के खतरों को कम करने पर केंद्रित", "type": "leaf"}
            ]},
            {"label": "यूपीएससी परीक्षा दृष्टिकोण", "type": "branch", "date": "परीक्षा", "children": [
                {"label": "विक्रमशिला गंगा डॉल्फ़िन अभयारण्य (बिहार): गंगा डॉल्फ़िन के लिए भारत का एकमात्र समर्पित वन्यजीव अभयारण्य", "type": "leaf"},
                {"label": "प्रमुख खतरे: गाद जमा होना, बांध निर्माण से आबादी का विखंडन और रासायनिक कीटनाशकों का जैव-संचय", "type": "leaf"}
            ]}
        ]
    },
    {
        "keys": ["elephant-corridors"],
        "en": [
            {"label": "Definition & Purpose", "type": "branch", "date": "Concept", "children": [
                {"label": "Narrow strips of land linking two larger habitats, allowing elephants to migrate safely without human contact", "type": "leaf"},
                {"label": "Essential to maintain genetic flow, prevent inbreeding, and reduce human-wildlife conflict", "type": "leaf"}
            ]},
            {"label": "Status in India", "type": "branch", "date": "India Corridor", "children": [
                {"label": "Over 100 elephant corridors identified in India (highest number in West Bengal and South India)", "type": "leaf"},
                {"label": "Threatened by infrastructure expansion (highways, railways, canals, coal mining) dissecting migratory paths", "type": "leaf"}
            ]},
            {"label": "Right of Passage Initiative", "type": "branch", "date": "Initiatives", "children": [
                {"label": "Campaign by Wildlife Trust of India (WTI) to secure and legalise identified corridors through land acquisition", "type": "leaf"},
                {"label": "Focuses on voluntary relocation of villages situated inside critical bottleneck zones", "type": "leaf"}
            ]},
            {"label": "UPSC Exam Focus", "type": "branch", "date": "UPSC Focus", "children": [
                {"label": "Legal Status: Elephant corridors have no formal statutory protection under WPA, unlike Tiger Reserves", "type": "leaf"},
                {"label": "Conflict mitigation: Implementation of elephant underpasses, railway speed limits, and honeybee barriers (Project RE-HAB)", "type": "leaf"}
            ]}
        ],
        "hi": [
            {"label": "परिभाषा और उद्देश्य", "type": "branch", "date": "अवधारणा", "children": [
                {"label": "दो बड़े आवासों को जोड़ने वाली भूमि की संकीर्ण पट्टियां, जो हाथियों को सुरक्षित प्रवास की अनुमति देती हैं", "type": "leaf"},
                {"label": "आनुवंशिक प्रवाह बनाए रखने, इनब्रीडिंग रोकने और मानव-हाथी संघर्ष को कम करने के लिए आवश्यक", "type": "leaf"}
            ]},
            {"label": "भारत में गलियारों की स्थिति", "type": "branch", "date": "गलियारे", "children": [
                {"label": "भारत में 100 से अधिक हाथी गलियारों की पहचान की गई है (सर्वाधिक पश्चिम बंगाल और दक्षिण भारत में)", "type": "leaf"},
                {"label": "बुनियादी ढांचा विस्तार (राजमार्ग, रेलवे, कोयला खनन) के कारण प्रवासी मार्ग गंभीर रूप से प्रभावित हैं", "type": "leaf"}
            ]},
            {"label": "राइट ऑफ पैसेज पहल", "type": "branch", "date": "पहल", "children": [
                {"label": "वाइल्डलाइफ ट्रस्ट ऑफ इंडिया (WTI) द्वारा भूमि अधिग्रहण के माध्यम से इन गलियारों को कानूनी रूप से सुरक्षित करने का अभियान", "type": "leaf"},
                {"label": "हाथी गलियारे के संवेदनशील क्षेत्रों में स्थित गांवों के स्वैच्छिक पुनर्वास पर केंद्रित", "type": "leaf"}
            ]},
            {"label": "यूपीएससी परीक्षा दृष्टिकोण", "type": "branch", "date": "परीक्षा", "children": [
                {"label": "कानूनी स्थिति: टाइगर रिजर्व के विपरीत, हाथी गलियारों को WPA के तहत कोई औपचारिक वैधानिक सुरक्षा प्राप्त नहीं है", "type": "leaf"},
                {"label": "संघर्ष शमन: हाथी अंडरपास का निर्माण, रेल गति सीमा और मधुमक्खी बाधाओं का उपयोग (प्रोजेक्ट RE-HAB)", "type": "leaf"}
            ]}
        ]
    },
    {
        "keys": ["flagship-species"],
        "en": [
            {"label": "Definition & Role", "type": "branch", "date": "Concept", "children": [
                {"label": "Species chosen to represent an environmental cause, serving as an ambassador or symbol for a campaign", "type": "leaf"},
                {"label": "Leverages human empathy and aesthetic appeal to secure public support and conservation funding", "type": "leaf"}
            ]},
            {"label": "Examples of Flagship Species", "type": "branch", "date": "Examples", "children": [
                {"label": "Giant Panda: The global ambassador for WWF, driving millions in conservation funding since 1961", "type": "leaf"},
                {"label": "Bengal Tiger: In India, symbolizes forest health and draws massive ecotourism and government protection", "type": "leaf"},
                {"label": "African Elephant: Represents savannah preservation and the global fight against illegal ivory trade", "type": "leaf"}
            ]},
            {"label": "Conservation Benefits", "type": "branch", "date": "Benefits", "children": [
                {"label": "Raises awareness and funding that supports broader ecosystem preservation", "type": "leaf"},
                {"label": "Protects other less popular species within the same habitat (acts as an umbrella)", "type": "leaf"}
            ]},
            {"label": "UPSC Exam Focus", "type": "branch", "date": "UPSC Focus", "children": [
                {"label": "Difference from Keystone: Flagship is a sociological designation; Keystone is strictly ecological", "type": "leaf"},
                {"label": "Project Dolphin and Project Tiger represent flagship-species driven conservation policy frameworks in India", "type": "leaf"}
            ]}
        ],
        "hi": [
            {"label": "परिभाषा और भूमिका", "type": "branch", "date": "अवधारणा", "children": [
                {"label": "वह प्रजाति जिसे पर्यावरण संरक्षण के लिए राजदूत या प्रतीक के रूप में चुना जाता है", "type": "leaf"},
                {"label": "जनता का ध्यान और संरक्षण निधि आकर्षित करने के लिए मानवीय संवेदना और सौंदर्य अपील का लाभ उठाती है", "type": "leaf"}
            ]},
            {"label": "फ्लैगशिप प्रजातियों के उदाहरण", "type": "branch", "date": "उदाहरण", "children": [
                {"label": "विशाल पांडा: WWF का वैश्विक राजदूत, जो 1961 से पर्यावरण अभियानों को निर्देशित कर रहा है", "type": "leaf"},
                {"label": "बंगाल टाइगर: भारत में, वन स्वास्थ्य का प्रतीक और सरकारी संरक्षण नीतियों का मुख्य केंद्र", "type": "leaf"},
                {"label": "अफ्रीकी हाथी: सवाना संरक्षण और हाथी दांत के अवैध व्यापार के खिलाफ वैश्विक लड़ाई का प्रतीक", "type": "leaf"}
            ]},
            {"label": "संरक्षण लाभ", "type": "branch", "date": "लाभ", "children": [
                {"label": "जागरूकता और धन जुटाता है जो अंततः पूरे पारिस्थितिकी तंत्र के संरक्षण का समर्थन करता है", "type": "leaf"},
                {"label": "उसी आवास में रहने वाली अन्य कम लोकप्रिय प्रजातियों की रक्षा करता है (अम्ब्रेला प्रभाव)", "type": "leaf"}
            ]},
            {"label": "यूपीएससी परीक्षा दृष्टिकोण", "type": "branch", "date": "परीक्षा", "children": [
                {"label": "कीस्टोन से अंतर: फ्लैगशिप एक सामाजिक/नीतिगत वर्गीकरण है; कीस्टोन विशुद्ध रूप से पारिस्थितिक है", "type": "leaf"},
                {"label": "भारत में प्रोजेक्ट डॉल्फ़िन और प्रोजेक्ट टाइगर फ्लैगशिप प्रजाति संरक्षण नीतियों के सर्वोत्तम उदाहरण हैं", "type": "leaf"}
            ]}
        ]
    },
    {
        "keys": ["foundation-species"],
        "en": [
            {"label": "Definition & Influence", "type": "branch", "date": "Concept", "children": [
                {"label": "Autogenic ecosystem engineers that create, modify, and maintain physical habitats for other species", "type": "leaf"},
                {"label": "Typically dominate the ecosystem in terms of huge biomass and structural presence", "type": "leaf"}
            ]},
            {"label": "Classic Examples", "type": "branch", "date": "Examples", "children": [
                {"label": "Kelp Forests: Giant brown algae form underwater marine forests that provide shelter for fish and otters", "type": "leaf"},
                {"label": "Stony Corals: Build the calcium carbonate skeleton structures of coral reefs, hosting 25% of marine life", "type": "leaf"},
                {"label": "Sphagnum Moss: Modifies northern peatland soil chemistry, creating acidic wetland habitats", "type": "leaf"}
            ]},
            {"label": "Ecological Function", "type": "branch", "date": "Ecological Role", "children": [
                {"label": "Modulates climate, water cycles, and nutrient flows within their physical structure", "type": "leaf"},
                {"label": "Provides primary food energy and complex 3D shelters to prevent predation", "type": "leaf"}
            ]},
            {"label": "UPSC Exam Focus", "type": "branch", "date": "UPSC Focus", "children": [
                {"label": "Difference from Keystone: Foundation species have high abundance/biomass; Keystone species have low abundance but high impact", "type": "leaf"},
                {"label": "Loss of foundation species (e.g. coral bleaching) leads to rapid collapse of associated community biodiversity", "type": "leaf"}
            ]}
        ],
        "hi": [
            {"label": "परिभाषा और प्रभाव", "type": "branch", "date": "अवधारणा", "children": [
                {"label": "वे जीव जो अन्य प्रजातियों के लिए भौतिक आवासों का निर्माण, संशोधन और रखरखाव करते हैं", "type": "leaf"},
                {"label": "आमतौर पर जैवभार (Biomass) और संरचनात्मक उपस्थिति के संदर्भ में पारिस्थितिकी तंत्र पर हावी होते हैं", "type": "leaf"}
            ]},
            {"label": "क्लासिक उदाहरण", "type": "branch", "date": "उदाहरण", "children": [
                {"label": "केल्प वन (Kelp Forests): विशाल भूरे शैवाल जो मछलियों और ऊदबिलाव को आश्रय देने वाले जलीय वनों का निर्माण करते हैं", "type": "leaf"},
                {"label": "प्रवाल (Corals): रीफ की कैल्शियम कार्बोनेट संरचनाएं बनाते हैं, जो 25% समुद्री जीवन की रक्षा करती हैं", "type": "leaf"},
                {"label": "स्फैगनम मॉस (Sphagnum): उत्तरी पीट भूमि की मिट्टी के रसायन को संशोधित कर अम्लीय आर्द्रभूमि आवास बनाता है", "type": "leaf"}
            ]},
            {"label": "पारिस्थितिक कार्य", "type": "branch", "date": "भूमिका", "children": [
                {"label": "अपनी भौतिक संरचना के भीतर जलवायु, जल चक्र और पोषक तत्वों के प्रवाह को नियंत्रित करते हैं", "type": "leaf"},
                {"label": "प्राथमिक खाद्य ऊर्जा और शिकारियों से बचने के लिए जटिल त्रि-आयामी आश्रय प्रदान करते हैं", "type": "leaf"}
            ]},
            {"label": "यूपीएससी परीक्षा दृष्टिकोण", "type": "branch", "date": "परीक्षा", "children": [
                {"label": "कीस्टोन से अंतर: फाउंडेशन प्रजातियों की प्रचुरता अधिक होती है; कीस्टोन की प्रचुरता कम पर प्रभाव अत्यधिक होता है", "type": "leaf"},
                {"label": "फाउंडेशन प्रजातियों के नुकसान (जैसे प्रवाल विरंजन) से संबद्ध जैव विविधता का तेजी से पतन होता है", "type": "leaf"}
            ]}
        ]
    },
    {
        "keys": ["sawen"],
        "en": [
            {"label": "SAWEN Overview", "type": "branch", "date": "Overview", "children": [
                {"label": "South Asia Wildlife Enforcement Network: Inter-governmental wildlife law enforcement support body", "type": "leaf"},
                {"label": "Launched in January 2011 in Paro, Bhutan; Secretariat is based in Kathmandu, Nepal", "type": "leaf"}
            ]},
            {"label": "Member Countries", "type": "branch", "date": "Members", "children": [
                {"label": "Comprises 8 South Asian nations: Afghanistan, Bangladesh, Bhutan, India, Maldives, Nepal, Pakistan, Sri Lanka", "type": "leaf"},
                {"label": "Aims to coordinate regional efforts against illegal cross-border wildlife trade and poaching", "type": "leaf"}
            ]},
            {"label": "Key Objectives", "type": "branch", "date": "Objectives", "children": [
                {"label": "Harmonize wildlife laws, share intelligence on trade routes, and build capacity of forest and customs officials", "type": "leaf"},
                {"label": "Combats smuggling of high-value items like Tiger parts, Rhino horns, Red Sandalwood, and Shahtoosh wool", "type": "leaf"}
            ]},
            {"label": "UPSC Exam Focus", "type": "branch", "date": "UPSC Focus", "children": [
                {"label": "India joined SAWEN formally in April 2016, designating WCCB (Wildlife Crime Control Bureau) as its national focal point", "type": "leaf"},
                {"label": "SAWEN facilitates transboundary cooperation in joint border patrolling along porous borders (e.g. India-Nepal, India-Bhutan)", "type": "leaf"}
            ]}
        ],
        "hi": [
            {"label": "SAWEN का अवलोकन", "type": "branch", "date": "अवलोकन", "children": [
                {"label": "दक्षिण एशिया वन्यजीव प्रवर्तन नेटवर्क (SAWEN): वन्यजीव कानूनों को लागू करने वाला अंतर-सरकारी सहायता निकाय", "type": "leaf"},
                {"label": "जनवरी 2011 में पारो, भूटान में शुरू किया गया; सचिवालय काठमांडू, नेपाल में स्थित है", "type": "leaf"}
            ]},
            {"label": "सदस्य देश", "type": "branch", "date": "सदस्य", "children": [
                {"label": "8 दक्षिण एशियाई देश शामिल हैं: अफगानिस्तान, बांग्लादेश, भूटान, भारत, मालदीव, नेपाल, पाकिस्तान, श्रीलंका", "type": "leaf"},
                {"label": "सीमा पार अवैध वन्यजीव व्यापार और अवैध शिकार के खिलाफ क्षेत्रीय प्रयासों के समन्वय का लक्ष्य", "type": "leaf"}
            ]},
            {"label": "मुख्य उद्देश्य", "type": "branch", "date": "उद्देश्य", "children": [
                {"label": "वन्यजीव कानूनों में सामंजस्य स्थापित करना, तस्कर मार्गों पर खुफिया जानकारी साझा करना और अधिकारियों की क्षमता निर्माण", "type": "leaf"},
                {"label": "बाघ के अंगों, गैंडे के सींग, लाल चंदन और शहतूश ऊन जैसी उच्च मूल्य वाली वस्तुओं की तस्करी रोकना", "type": "leaf"}
            ]},
            {"label": "यूपीएससी परीक्षा दृष्टिकोण", "type": "branch", "date": "परीक्षा", "children": [
                {"label": "भारत औपचारिक रूप से अप्रैल 2016 में SAWEN में शामिल हुआ; WCCB को राष्ट्रीय नोडल एजेंसी नामित किया गया", "type": "leaf"},
                {"label": "SAWEN खुली सीमाओं (जैसे भारत-नेपाल, भारत-भूटान) पर संयुक्त सीमा गश्त में सीमा पार सहयोग की सुविधा प्रदान करता है", "type": "leaf"}
            ]}
        ]
    },
    {
        "keys": ["rhino-vision", "one-horn-rhino"],
        "en": [
            {"label": "Indian Rhino Vision 2020", "type": "branch", "date": "IRV 2020", "children": [
                {"label": "Launched in 2005 by Assam Forest Dept, WWF-India, and International Rhino Foundation (IRF)", "type": "leaf"},
                {"label": "Target: Attain a wild population of at least 3,000 Greater One-Horned Rhinos in Assam by 2020", "type": "leaf"}
            ]},
            {"label": "Seven Protected Areas", "type": "branch", "date": "PA Network", "children": [
                {"label": "Aims to distribute rhinos across 7 PAs in Assam (Kaziranga, Pobitora, Orang, Manas, Laokhowa, Burachapori, Dibru-Saikhowa)", "type": "leaf"},
                {"label": "Reduces vulnerability of the species to epidemics/natural disasters by dispersing the population from Kaziranga", "type": "leaf"}
            ]},
            {"label": "Translocation Program", "type": "branch", "date": "Translocations", "children": [
                {"label": "Wild-to-wild translocations: Moving rhinos from overpopulated areas (Pobitora and Kaziranga) to Manas National Park", "type": "leaf"},
                {"label": "Successfully re-established a breeding population of rhinos in Manas, which had lost all rhinos due to past civil unrest", "type": "leaf"}
            ]},
            {"label": "UPSC Exam Focus", "type": "branch", "date": "UPSC Focus", "children": [
                {"label": "Greater One-Horned Rhino (Rhinoceros unicornis): IUCN Vulnerable (VU); listed under Schedule I of WPA 1972", "type": "leaf"},
                {"label": "Kaziranga National Park holds the world's largest population of the Greater One-Horned Rhino (>70%)", "type": "leaf"}
            ]}
        ],
        "hi": [
            {"label": "भारतीय गैंडा विज़न 2020", "type": "branch", "date": "IRV 2020", "children": [
                {"label": "2005 में असम वन विभाग, WWF-भारत और इंटरनेशनल राइनो फाउंडेशन (IRF) द्वारा शुरू किया गया", "type": "leaf"},
                {"label": "लक्ष्य: 2020 तक असम में एक सींग वाले गैंडों की संख्या को कम से कम 3,000 तक पहुंचाना", "type": "leaf"}
            ]},
            {"label": "सात संरक्षित क्षेत्र", "type": "branch", "date": "नेटवर्क", "children": [
                {"label": "असम के 7 क्षेत्रों में गैंडों को वितरित करना (काजीरंगा, पोबितोरा, ओरांग, मानस, लाओखोवा, बुराचपोरी, डिब्रू-सैखोवा)", "type": "leaf"},
                {"label": "काजीरंगा से आबादी को फैलाकर महामारी/बाढ़ के खतरों के प्रति प्रजातियों की संवेदनशीलता को कम करना", "type": "leaf"}
            ]},
            {"label": "स्थानांतरण कार्यक्रम (Translocation)", "type": "branch", "date": "स्थानांतरण", "children": [
                {"label": "जंगली-से-जंगली स्थानांतरण: पोबितोरा और काजीरंगा से गैंडों को मानस राष्ट्रीय उद्यान में स्थानांतरित करना", "type": "leaf"},
                {"label": "मानस में गैंडों की प्रजनन आबादी को सफलतापूर्वक स्थापित किया, जहां नागरिक अशांति के कारण सभी गैंडे नष्ट हो गए थे", "type": "leaf"}
            ]},
            {"label": "यूपीएससी परीक्षा दृष्टिकोण", "type": "branch", "date": "परीक्षा", "children": [
                {"label": "एक सींग वाला गैंडा (Rhinoceros unicornis): IUCN संवेदनशील (VU); WPA 1972 की अनुसूची I के तहत सूचीबद्ध", "type": "leaf"},
                {"label": "काजीरंगा राष्ट्रीय उद्यान में एक सींग वाले गैंडों की दुनिया की सबसे बड़ी आबादी (>70%) निवास करती है", "type": "leaf"}
            ]}
        ]
    },
    {
        "keys": ["indicator-species"],
        "en": [
            {"label": "Definition & Environmental Role", "type": "branch", "date": "Concept", "children": [
                {"label": "Species whose presence, absence, or health directly reflects specific environmental conditions or pollution levels", "type": "leaf"},
                {"label": "Acts as an early warning system for ecological changes, showing sensitivity to habitat degradation", "type": "leaf"}
            ]},
            {"label": "Classic Indicator Examples", "type": "branch", "date": "Examples", "children": [
                {"label": "Lichens: Sensitive to sulfur dioxide (SO2); absent in urban or heavily polluted industrial zones", "type": "leaf"},
                {"label": "Amphibians: Permeable skin absorbs chemical toxins; reflects wetland health and chemical contamination", "type": "leaf"},
                {"label": "River Otters: Indicate clean, unpolluted freshwater river systems and healthy fish populations", "type": "leaf"}
            ]},
            {"label": "Biological Monitoring", "type": "branch", "date": "Methods", "children": [
                {"label": "Biomonitoring is cheaper and more representative of long-term health than discrete chemical testing", "type": "leaf"},
                {"label": "Assesses bioaccumulation of toxins in lower trophic levels before it impacts apex predators", "type": "leaf"}
            ]},
            {"label": "UPSC Exam Focus", "type": "branch", "date": "UPSC Focus", "children": [
                {"label": "Benthic macroinvertebrates (mayfly/stonefly larvae): Used to calculate River Biotic Indices and water quality", "type": "leaf"},
                {"label": "Mosses are excellent bio-indicators for airborne heavy metal deposition (e.g. Lead, Cadmium)", "type": "leaf"}
            ]}
        ],
        "hi": [
            {"label": "परिभाषा और पारिस्थितिक भूमिका", "type": "branch", "date": "अवधारणा", "children": [
                {"label": "वह प्रजाति जिसकी उपस्थिति या स्वास्थ्य विशिष्ट पर्यावरणीय परिस्थितियों या प्रदूषण के स्तर को दर्शाता है", "type": "leaf"},
                {"label": "पारिस्थितिक परिवर्तनों के लिए शुरुआती चेतावनी प्रणाली के रूप में कार्य करती है, जो आवास क्षरण के प्रति संवेदनशीलता दिखाती है", "type": "leaf"}
            ]},
            {"label": "क्लासिक उदाहरण", "type": "branch", "date": "उदाहरण", "children": [
                {"label": "लाइकेन: सल्फर डाइऑक्साइड (SO2) के प्रति संवेदनशील; प्रदूषित या औद्योगिक क्षेत्रों में अनुपस्थित रहते हैं", "type": "leaf"},
                {"label": "उभयचर (मेंढक): पारगम्य त्वचा रसायनों को अवशोषित करती है; आर्द्रभूमि के स्वास्थ्य को दर्शाती है", "type": "leaf"},
                {"label": "नदी के ऊदबिलाव (River Otters): स्वच्छ, प्रदूषण मुक्त जल और स्वस्थ मछली आबादी का संकेत देते हैं", "type": "leaf"}
            ]},
            {"label": "जैविक निगरानी (Biomonitoring)", "type": "branch", "date": "विधियां", "children": [
                {"label": "अलग-अलग रासायनिक परीक्षणों की तुलना में जैव-निगरानी दीर्घकालिक पारिस्थितिक स्वास्थ्य की बेहतर पहचान करती है", "type": "leaf"},
                {"label": "शीर्ष शिकारियों को प्रभावित करने से पहले निचले ट्रॉफिक स्तरों में विषाक्त पदार्थों के जैव-संचय का आकलन करती है", "type": "leaf"}
            ]},
            {"label": "यूपीएससी परीक्षा दृष्टिकोण", "type": "branch", "date": "परीक्षा", "children": [
                {"label": "बेंथिक मैक्रोइनवर्टेब्रेट्स (मेफ्लाई लार्वा): नदी जैविक सूचकांक और पानी की गुणवत्ता की गणना करने के लिए उपयोग", "type": "leaf"},
                {"label": "काई (Mosses) हवा में भारी धातु जमाव (जैसे सीसा, कैडमियम) के लिए उत्कृष्ट जैव-संकेतक हैं", "type": "leaf"}
            ]}
        ]
    },
    {
        "keys": ["invasivealien-species", "invasive-alien", "invasive"],
        "en": [
            {"label": "Definition & Impacts", "type": "branch", "date": "Concept", "children": [
                {"label": "Non-native species introduced outside their natural range, spreading rapidly and displacing native flora/fauna", "type": "leaf"},
                {"label": "Disrupts ecological balance, outcompetes native species for nutrients, and causes major economic losses", "type": "leaf"}
            ]},
            {"label": "Major Plant Invasives in India", "type": "branch", "date": "Plants", "children": [
                {"label": "Lantana camara: Shrub from tropical America; releases allelopathic chemicals, choking native forest undergrowth", "type": "leaf"},
                {"label": "Water Hyacinth (Eichhornia crassipes): 'Terror of Bengal'; drains dissolved oxygen, killing aquatic life", "type": "leaf"},
                {"label": "Parthenium hysterophorus (Congress Grass): Toxic weed causing allergies in humans and livestock", "type": "leaf"}
            ]},
            {"label": "Major Animal Invasives", "type": "branch", "date": "Animals", "children": [
                {"label": "Giant African Snail: Destroys crops; acts as a vector for human pathogens", "type": "leaf"},
                {"label": "Largetooth Sawfish / African Sharptooth Catfish: Outcompetes native river fish in Indian inland waters", "type": "leaf"}
            ]},
            {"label": "UPSC Exam Focus", "type": "branch", "date": "UPSC Focus", "children": [
                {"label": "IUCN Database: Managed by the Invasive Species Specialist Group (ISSG); tracks global invasive database", "type": "leaf"},
                {"label": "WPA 2022 Amendment: Empowers the Central Government to regulate or ban import and trade of invasive alien species", "type": "leaf"}
            ]}
        ],
        "hi": [
            {"label": "परिभाषा और प्रभाव", "type": "branch", "date": "अवधारणा", "children": [
                {"label": "गैर-मूल प्रजातियां जो अपने प्राकृतिक आवास से बाहर आकर तेजी से फैलती हैं और मूल प्रजातियों को विस्थापित करती हैं", "type": "leaf"},
                {"label": "पारिस्थितिक संतुलन बिगाड़ती हैं, पोषक तत्वों के लिए प्रतिस्पर्धा करती हैं और बड़े आर्थिक नुकसान का कारण बनती हैं", "type": "leaf"}
            ]},
            {"label": "भारत में प्रमुख आक्रामक पौधे", "type": "branch", "date": "पौधे", "children": [
                {"label": "लैंटाना कैमारा (Lantana camara): उष्णकटिबंधीय अमेरिका की झाड़ी; एलीलोपैथिक रसायनों को छोड़ती है जो वनों को नष्ट करते हैं", "type": "leaf"},
                {"label": "जलकुंभी (Water Hyacinth): 'बंगाल का आतंक'; घुलित ऑक्सीजन को सोख लेती है जिससे जलीय जीवन मर जाता है", "type": "leaf"},
                {"label": "पार्थेनियम (गाजर घास): मनुष्यों और मवेशियों में एलर्जी पैदा करने वाला विषैला खरपतवार", "type": "leaf"}
            ]},
            {"label": "प्रमुख आक्रामक जंतु", "type": "branch", "date": "जंतु", "children": [
                {"label": "विशाल अफ्रीकी घोंघा (Giant African Snail): फसलों को नष्ट करता है और मानव रोगजनकों के वाहक के रूप में कार्य करता है", "type": "leaf"},
                {"label": "अफ्रीकी कैटफिश (Clarias gariepinus): भारत के अंतर्देशीय जलमार्गों में मूल मछली प्रजातियों को विस्थापित करती है", "type": "leaf"}
            ]},
            {"label": "यूपीएससी परीक्षा दृष्टिकोण", "type": "branch", "date": "परीक्षा", "children": [
                {"label": "IUCN डेटाबेस: आक्रामक प्रजाति विशेषज्ञ समूह (ISSG) द्वारा प्रबंधित; आक्रामक डेटा को ट्रैक करता है", "type": "leaf"},
                {"label": "WPA 2022 संशोधन: केंद्र सरकार को आक्रामक विदेशी प्रजातियों के आयात और व्यापार को विनियमित करने का अधिकार प्रदान करता है", "type": "leaf"}
            ]}
        ]
    },
    {
        "keys": ["keystone-species"],
        "en": [
            {"label": "Definition & Ecological Impact", "type": "branch", "date": "Concept", "children": [
                {"label": "Species with disproportionately large ecological impact relative to its low abundance or biomass", "type": "leaf"},
                {"label": "Removal triggers a trophic cascade, causing secondary extinctions and restructuring the entire food web", "type": "leaf"}
            ]},
            {"label": "Functional Categories", "type": "branch", "date": "Categories", "children": [
                {"label": "Keystone Predators: Sea Otters control sea urchins to protect kelp forests; Gray Wolves in Yellowstone control elk populations", "type": "leaf"},
                {"label": "Ecosystem Engineers: Beavers construct wetlands; African Elephants suppress woody vegetation to maintain savanna grasslands", "type": "leaf"},
                {"label": "Mutualists: Fig trees provide critical year-round food resources (keystone food resource) for tropical frugivores during dry seasons", "type": "leaf"}
            ]},
            {"label": "Conservation Significance", "type": "branch", "date": "Conservation", "children": [
                {"label": "Focusing conservation on keystones protects hundreds of dependent species simultaneously", "type": "leaf"},
                {"label": "Optimizes limited funding by prioritizing ecologically high-value species", "type": "leaf"}
            ]},
            {"label": "UPSC Exam Focus", "type": "branch", "date": "UPSC Focus", "children": [
                {"label": "Keystone vs Dominant: Dominant species have high abundance/biomass (e.g. Kelp, Corals); Keystones have low biomass but high impact", "type": "leaf"},
                {"label": "Trophic Cascade: Ecological process starting at the top of the food chain and tumbling down to the bottom", "type": "leaf"}
            ]}
        ],
        "hi": [
            {"label": "परिभाषा और पारिस्थितिक प्रभाव", "type": "branch", "date": "अवधारणा", "children": [
                {"label": "वह प्रजाति जिसका अपनी कम प्रचुरता या जैवभार के बावजूद पारिस्थितिकी तंत्र पर अत्यधिक प्रभाव होता है", "type": "leaf"},
                {"label": "इसे हटाने से ट्रॉफिक कैस्केड शुरू होता है, जिससे द्वितीयक विलुप्ति होती है और पूरा खाद्य जाल बदल जाता है", "type": "leaf"}
            ]},
            {"label": "कार्यात्मक श्रेणियां", "type": "branch", "date": "श्रेणियां", "children": [
                {"label": "कीस्टोन शिकारी: समुद्री ऊदबिलाव समुद्री अर्चिन को नियंत्रित करते हैं; ग्रे भेड़िये एल्क आबादी को नियंत्रित करते हैं", "type": "leaf"},
                {"label": "पारिस्थितिकी तंत्र इंजीनियर: बीवर आर्द्रभूमि बनाते हैं; अफ्रीकी हाथी सवाना घास के मैदानों को बनाए रखते हैं", "type": "leaf"},
                {"label": "पारस्परिक सहयोगी (Mutualists): अंजीर के पेड़ शुष्क मौसम में उष्णकटिबंधीय फल खाने वाले जीवों को भोजन प्रदान करते हैं", "type": "leaf"}
            ]},
            {"label": "संरक्षण का महत्व", "type": "branch", "date": "संरक्षण", "children": [
                {"label": "कीस्टोन प्रजातियों पर ध्यान केंद्रित करने से एक साथ सैकड़ों निर्भर प्रजातियों की रक्षा होती है", "type": "leaf"},
                {"label": "पारिस्थितिक रूप से उच्च मूल्य वाली प्रजातियों को प्राथमिकता देकर सीमित धन का इष्टतम उपयोग सुनिश्चित करता है", "type": "leaf"}
            ]},
            {"label": "यूपीएससी परीक्षा दृष्टिकोण", "type": "branch", "date": "परीक्षा", "children": [
                {"label": "कीस्टोन बनाम प्रमुख: प्रमुख प्रजातियों की प्रचुरता अधिक होती है; कीस्टोन की प्रचुरता कम लेकिन प्रभाव अत्यधिक होता है", "type": "leaf"},
                {"label": "ट्रॉफिक कैस्केड: पारिस्थितिक प्रक्रिया जो खाद्य श्रृंखला के शीर्ष से शुरू होती है और नीचे तक प्रवाहित होती है", "type": "leaf"}
            ]}
        ]
    },
    {
        "keys": ["mab-man", "world-network", "biosphere-reserves"],
        "en": [
            {"label": "MAB Programme Origin", "type": "branch", "date": "Overview", "children": [
                {"label": "Man and the Biosphere Programme: Launched by UNESCO in 1971; intergovernmental scientific program", "type": "leaf"},
                {"label": "Aims to establish scientific basis for improving relationship between people and their environments", "type": "leaf"}
            ]},
            {"label": "Biosphere Reserve Zoning", "type": "branch", "date": "Zoning", "children": [
                {"label": "Core Area: Strictly protected ecosystem; no human interference except non-destructive research", "type": "leaf"},
                {"label": "Buffer Zone: Surrounds core; used for cooperative activities, environmental education, and ecotourism", "type": "leaf"},
                {"label": "Transition Area: Outer zone where local communities run sustainable resource management activities", "type": "leaf"}
            ]},
            {"label": "World Network of Biosphere Reserves", "type": "branch", "date": "WNBR Network", "children": [
                {"label": "WNBR coordinates global exchange of conservation methods and biodiversity research across reserves", "type": "leaf"},
                {"label": "India has 18 Biosphere Reserves; 12 are designated under the UNESCO WNBR (e.g. Panna added in 2020)", "type": "leaf"}
            ]},
            {"label": "UPSC Exam Focus", "type": "branch", "date": "UPSC Focus", "children": [
                {"label": "First Biosphere Reserve in India: Nilgiri Biosphere Reserve (established 1986, spans TN, Kerala, Karnataka)", "type": "leaf"},
                {"label": "Legal Status: Biosphere reserves are recognized internationally but implemented through national legislation (WPA 1972)", "type": "leaf"}
            ]}
        ],
        "hi": [
            {"label": "MAB कार्यक्रम की उत्पत्ति", "type": "branch", "date": "अवलोकन", "children": [
                {"label": "मैन एंड द बायोस्फीयर कार्यक्रम: 1971 में यूनेस्को द्वारा शुरू किया गया; अंतर-सरकारी वैज्ञानिक कार्यक्रम", "type": "leaf"},
                {"label": "लोगों और उनके पर्यावरण के बीच संबंधों को बेहतर बनाने के लिए वैज्ञानिक आधार स्थापित करना", "type": "leaf"}
            ]},
            {"label": "बायोस्फीयर रिजर्व का ज़ोनिंग", "type": "branch", "date": "ज़ोनिंग", "children": [
                {"label": "कोर क्षेत्र: पूरी तरह से संरक्षित पारिस्थितिकी तंत्र; अनुसंधान को छोड़कर किसी भी मानवीय हस्तक्षेप की अनुमति नहीं", "type": "leaf"},
                {"label": "बफर क्षेत्र: कोर को घेरता है; इसका उपयोग सहकारी गतिविधियों, पर्यावरण शिक्षा और पर्यावरण-पर्यटन के लिए होता है", "type": "leaf"},
                {"label": "संक्रमण क्षेत्र: सबसे बाहरी क्षेत्र जहां स्थानीय समुदाय टिकाऊ संसाधन प्रबंधन गतिविधियों का संचालन करते हैं", "type": "leaf"}
            ]},
            {"label": "बायोस्फीयर रिजर्व का वैश्विक नेटवर्क (WNBR)", "type": "branch", "date": "नेटवर्क", "children": [
                {"label": "WNBR विभिन्न रिजर्वों के बीच संरक्षण विधियों और जैव विविधता अनुसंधान के वैश्विक आदान-प्रदान का समन्वय करता है", "type": "leaf"},
                {"label": "भारत में 18 बायोस्फीयर रिजर्व हैं; 12 यूनेस्को WNBR के तहत नामित हैं (जैसे 2020 में पन्ना को शामिल किया गया)", "type": "leaf"}
            ]},
            {"label": "यूपीएससी परीक्षा दृष्टिकोण", "type": "branch", "date": "परीक्षा", "children": [
                {"label": "भारत का पहला बायोस्फीयर रिजर्व: नीलगिरि बायोस्फीयर रिजर्व (1986 में स्थापित, TN, केरल, कर्नाटक में फैला है)", "type": "leaf"},
                {"label": "कानूनी स्थिति: बायोस्फीयर रिजर्व अंतरराष्ट्रीय स्तर पर मान्यता प्राप्त हैं लेकिन राष्ट्रीय कानून (WPA 1972) के तहत लागू होते हैं", "type": "leaf"}
            ]}
        ]
    },
    {
        "keys": ["nagoya-protocol"],
        "en": [
            {"label": "Nagoya Protocol Origin", "type": "branch", "date": "Overview", "children": [
                {"label": "Adopted in October 2010 in Nagoya, Japan; entered into force in October 2014", "type": "leaf"},
                {"label": "Supplementary agreement to the CBD, focusing specifically on the third objective of the convention", "type": "leaf"}
            ]},
            {"label": "Access and Benefit Sharing (ABS)", "type": "branch", "date": "ABS Core", "children": [
                {"label": "Regulates access to genetic resources and ensures fair sharing of benefits with provider countries", "type": "leaf"},
                {"label": "Prior Informed Consent (PIC): Required from host nation prior to accessing genetic resources", "type": "leaf"},
                {"label": "Mutually Agreed Terms (MAT): Establishes contracts between user and provider on benefits, transfer, and usage", "type": "leaf"}
            ]},
            {"label": "Traditional Knowledge Integration", "type": "branch", "date": "Indigenous Rights", "children": [
                {"label": "Covers traditional knowledge associated with genetic resources held by indigenous and local communities", "type": "leaf"},
                {"label": "Mandates benefit sharing with local communities who hold the historical knowledge of medicinal flora", "type": "leaf"}
            ]},
            {"label": "UPSC Exam Focus", "type": "branch", "date": "UPSC Focus", "children": [
                {"label": "India's Compliance: Complies through Biological Diversity Act 2002; NBA Chennai monitors ABS applications", "type": "leaf"},
                {"label": "ABS Clearing-House: Online platform facilitating exchange of information on access and benefit-sharing", "type": "leaf"}
            ]}
        ],
        "hi": [
            {"label": "नागोया प्रोटोकॉल की उत्पत्ति", "type": "branch", "date": "परिचय", "children": [
                {"label": "अक्टूबर 2010 में नागोया, जापान में अपनाया गया; अक्टूबर 2014 में लागू हुआ", "type": "leaf"},
                {"label": "CBD का पूरक समझौता, जो विशेष रूप से कन्वेंशन के तीसरे उद्देश्य पर ध्यान केंद्रित करता है", "type": "leaf"}
            ]},
            {"label": "एक्सेस और बेनिफिट शेयरिंग (ABS)", "type": "branch", "date": "ABS कोर", "children": [
                {"label": "आनुवंशिक संसाधनों तक पहुंच को नियंत्रित करता है और प्रदाता देशों के साथ लाभों का उचित साझाकरण सुनिश्चित करता", "type": "leaf"},
                {"label": "पूर्व सूचित सहमति (PIC): आनुवंशिक संसाधनों तक पहुंच से पहले मेजबान देश से अनुमति आवश्यक", "type": "leaf"},
                {"label": "पारस्परिक रूप से सहमत शर्तें (MAT): लाभ, हस्तांतरण और उपयोग पर उपयोगकर्ता और प्रदाता के बीच अनुबंध स्थापित करता है", "type": "leaf"}
            ]},
            {"label": "पारंपरिक ज्ञान का एकीकरण", "type": "branch", "date": "स्थानीय अधिकार", "children": [
                {"label": "स्थानीय समुदायों के पास मौजूद आनुवंशिक संसाधनों से जुड़े पारंपरिक ज्ञान को कवर करता है", "type": "leaf"},
                {"label": "उन स्थानीय समुदायों के साथ लाभ साझा करना अनिवार्य करता है जिनके पास औषधीय वनस्पतियों का ऐतिहासिक ज्ञान है", "type": "leaf"}
            ]},
            {"label": "यूपीएससी परीक्षा दृष्टिकोण", "type": "branch", "date": "परीक्षा", "children": [
                {"label": "भारत का अनुपालन: जैव विविधता अधिनियम 2002 के माध्यम से लागू; चेन्नई स्थित NBA आवेदनों की निगरानी करता है", "type": "leaf"},
                {"label": "ABS क्लियरिंग-हाउस: पहुंच और लाभ-साझाकरण पर जानकारी के आदान-प्रदान की सुविधा प्रदान करने वाला ऑनलाइन मंच", "type": "leaf"}
            ]}
        ]
    },
    {
        "keys": ["petersburg-tiger"],
        "en": [
            {"label": "St. Petersburg Summit 2010", "type": "branch", "date": "History", "children": [
                {"label": "Hosted in 2010 in Russia; attended by all 13 Tiger Range Countries (TRCs)", "type": "leaf"},
                {"label": "Addressed the catastrophic decline of wild tigers to an all-time low of ~3,200 individuals globally", "type": "leaf"}
            ]},
            {"label": "Tx2 Target & Global Tiger Recovery Program", "type": "branch", "date": "Tx2 Target", "children": [
                {"label": "Tx2: Global commitment to double the number of wild tigers by the year 2022", "type": "leaf"},
                {"label": "GTRP: Framework detailing national recovery actions, poaching control, and reserve corridor management", "type": "leaf"}
            ]},
            {"label": "13 Tiger Range Countries", "type": "branch", "date": "TRCs", "children": [
                {"label": "India, Nepal, Bangladesh, Bhutan, Russia, China, Myanmar, Thailand, Cambodia, Laos, Vietnam, Malaysia, Indonesia", "type": "leaf"},
                {"label": "Tigers are extinct in Cambodia, Laos, and Vietnam; populations are declining in Southeast Asia", "type": "leaf"}
            ]},
            {"label": "UPSC Exam Focus", "type": "branch", "date": "UPSC Focus", "children": [
                {"label": "Nepal Success: First country to double its wild tiger population under the Tx2 target", "type": "leaf"},
                {"label": "India Success: Tiger numbers doubled from 1,411 (2006) to 3,167+ (2022), hitting targets ahead of schedule", "type": "leaf"}
            ]}
        ],
        "hi": [
            {"label": "सेंट पीटर्सबर्ग शिखर सम्मेलन 2010", "type": "branch", "date": "इतिहास", "children": [
                {"label": "2010 में रूस में आयोजित; सभी 13 टाइगर रेंज देशों (TRCs) ने भाग लिया", "type": "leaf"},
                {"label": "वैश्विक स्तर पर जंगली बाघों की संख्या घटकर ~3,200 रह जाने के संकट को रोकने के लिए आयोजित", "type": "leaf"}
            ]},
            {"label": "Tx2 लक्ष्य और ग्लोबल टाइगर रिकवरी प्रोग्राम", "type": "branch", "date": "Tx2 लक्ष्य", "children": [
                {"label": "Tx2: वर्ष 2022 तक जंगली बाघों की संख्या को दोगुना करने की वैश्विक प्रतिबद्धता", "type": "leaf"},
                {"label": "GTRP: राष्ट्रीय स्तर पर बाघ बहाली कार्यों, अवैध शिकार विरोधी नीतियों और बफर कॉरिडोर का विवरण प्रदान करता है", "type": "leaf"}
            ]},
            {"label": "13 टाइगर रेंज देश", "type": "branch", "date": "रेंज देश", "children": [
                {"label": "भारत, नेपाल, बांग्लादेश, भूटान, रूस, चीन, म्यांमार, थाईलैंड, कंबोडिया, लाओस, वियतनाम, मलेशिया, इंडोनेशिया", "type": "leaf"},
                {"label": "कंबोडिया, लाओस और वियतनाम में बाघ विलुप्त हो चुके हैं; दक्षिण-पूर्व एशिया में आबादी घट रही है", "type": "leaf"}
            ]},
            {"label": "यूपीएससी परीक्षा दृष्टिकोण", "type": "branch", "date": "परीक्षा", "children": [
                {"label": "नेपाल की सफलता: Tx2 लक्ष्य के तहत अपने जंगली बाघों की आबादी को दोगुना करने वाला पहला देश बना", "type": "leaf"},
                {"label": "भारत की सफलता: बाघों की संख्या 1,411 (2006) से बढ़कर 3,167+ (2022) हो गई, जिससे समय से पहले लक्ष्य पूरा हुआ", "type": "leaf"}
            ]}
        ]
    },
    {
        "keys": ["priority-species"],
        "en": [
            {"label": "WWF Definition & Criteria", "type": "branch", "date": "Concept", "children": [
                {"label": "Species identified by WWF as having high ecological, economic, or cultural significance globally", "type": "leaf"},
                {"label": "Prioritized because their protection benefits the wider ecosystem and associated biodiversity", "type": "leaf"}
            ]},
            {"label": "Key Priority Species", "type": "branch", "date": "Examples", "children": [
                {"label": "Tigers and Elephants: Act as umbrella and flagship species; require large forest corridors", "type": "leaf"},
                {"label": "Giant Pandas: Symbolize global wildlife protection; require conservation of bamboo forests", "type": "leaf"},
                {"label": "Rhinos: Threat from poaching for horns; critical for maintaining grasslands", "type": "leaf"}
            ]},
            {"label": "Conservation Approach", "type": "branch", "date": "Conservation", "children": [
                {"label": "Directs resources towards species under immediate threat of extinction or habitat loss", "type": "leaf"},
                {"label": "Promotes local community benefit sharing to curb poaching and illegal wildlife trade", "type": "leaf"}
            ]},
            {"label": "UPSC Exam Focus", "type": "branch", "date": "UPSC Focus", "children": [
                {"label": "Difference from Keystone: Priority species are determined by WWF criteria; Keystone species are defined by ecological impact", "type": "leaf"},
                {"label": "Schedule I of WPA 1972 aligns closely with priority conservation species in India", "type": "leaf"}
            ]}
        ],
        "hi": [
            {"label": "WWF की परिभाषा और मानदंड", "type": "branch", "date": "अवधारणा", "children": [
                {"label": "वैश्विक स्तर पर उच्च पारिस्थितिक, आर्थिक या सांस्कृतिक महत्व रखने वाली प्रजातियाँ", "type": "leaf"},
                {"label": "इन्हें इसलिए प्राथमिकता दी जाती है क्योंकि इनका संरक्षण व्यापक पारिस्थितिकी तंत्र को लाभ पहुंचाता है", "type": "leaf"}
            ]},
            {"label": "प्रमुख प्राथमिकता वाली प्रजातियाँ", "type": "branch", "date": "उदाहरण", "children": [
                {"label": "बाघ और हाथी: अम्ब्रेला और फ्लैगशिप प्रजातियों के रूप में कार्य करते हैं; विशाल वन गलियारों की आवश्यकता होती है", "type": "leaf"},
                {"label": "विशाल पांडा: वैश्विक वन्यजीव संरक्षण का प्रतीक; बांस के जंगलों के संरक्षण की आवश्यकता होती है", "type": "leaf"},
                {"label": "गैंडे: सींग के लिए अवैध शिकार का खतरा; घास के मैदानों को बनाए रखने के लिए महत्वपूर्ण", "type": "leaf"}
            ]},
            {"label": "संरक्षण दृष्टिकोण", "type": "branch", "date": "संरक्षण", "children": [
                {"label": "संसाधनों को उन प्रजातियों की ओर निर्देशित करता है जो विलुप्ति या आवास के नुकसान के तत्काल खतरे में हैं", "type": "leaf"},
                {"label": "अवैध शिकार और वन्यजीव व्यापार को रोकने के लिए स्थानीय सामुदायिक लाभ साझाकरण को बढ़ावा देता है", "type": "leaf"}
            ]},
            {"label": "यूपीएससी परीक्षा दृष्टिकोण", "type": "branch", "date": "परीक्षा", "children": [
                {"label": "कीस्टोन से अंतर: प्राथमिकता वाली प्रजातियाँ WWF के संरक्षण प्राथमिकताओं पर आधारित हैं; कीस्टोन पारिस्थितिक प्रभाव पर", "type": "leaf"},
                {"label": "WPA 1972 की अनुसूची I भारत में संरक्षण प्राथमिकताओं वाली प्रजातियों से गहराई से मेल खाती है", "type": "leaf"}
            ]}
        ]
    },
    {
        "keys": ["project-elephant", "elephant-census", "elephant"],
        "en": [
            {"label": "Project Elephant Launch", "type": "branch", "date": "Launch", "children": [
                {"label": "Launched in February 1992 by MoEFCC to protect elephants, their habitats, and migratory corridors", "type": "leaf"},
                {"label": "Provides financial and technical support to major elephant-bearing states in India", "type": "leaf"}
            ]},
            {"label": "Elephant Census", "type": "branch", "date": "Census", "children": [
                {"label": "Conducted every 5 years using direct count and dung decay density estimation methods", "type": "leaf"},
                {"label": "Latest census estimates India's wild elephant population at ~27,312; Karnataka holds the highest number", "type": "leaf"}
            ]},
            {"label": "Key Protection Initiatives", "type": "branch", "date": "Initiatives", "children": [
                {"label": "Elephant Reserves: Currently 33 declared reserves in India (e.g. Terai ER, Lemru ER, Agasthyamalai ER)", "type": "leaf"},
                {"label": "MIKE Programme: Monitoring the Illegal Killing of Elephants; 10 sites in India (e.g. Shivalik, Deomali)", "type": "leaf"}
            ]},
            {"label": "UPSC Exam Focus", "type": "branch", "date": "UPSC Focus", "children": [
                {"label": "Asian Elephant (Elephas maximus): IUCN Endangered (EN); listed under Schedule I of WPA 1972 and Appendix I of CITES", "type": "leaf"},
                {"label": "National Heritage Animal: Declared as India's National Heritage Animal in 2010 to strengthen its protection", "type": "leaf"}
            ]}
        ],
        "hi": [
            {"label": "प्रोजेक्ट एलीफेंट की शुरुआत", "type": "branch", "date": "शुरुआत", "children": [
                {"label": "हाथियों, उनके आवासों और प्रवासी मार्गों की सुरक्षा के लिए MoEFCC द्वारा फरवरी 1992 में शुरू किया गया", "type": "leaf"},
                {"label": "भारत में हाथियों की आबादी वाले प्रमुख राज्यों को वित्तीय और तकनीकी सहायता प्रदान करता है", "type": "leaf"}
            ]},
            {"label": "हाथी जनगणना", "type": "branch", "date": "जनगणना", "children": [
                {"label": "प्रत्येक 5 वर्ष में प्रत्यक्ष गणना और गोबर अपघटन घनत्व आकलन विधियों का उपयोग करके आयोजित की जाती है", "type": "leaf"},
                {"label": "नवीनतम जनगणना के अनुसार भारत में हाथियों की संख्या ~27,312 है; कर्नाटक में सर्वाधिक हाथी हैं", "type": "leaf"}
            ]},
            {"label": "प्रमुख संरक्षण पहलें", "type": "branch", "date": "पहलें", "children": [
                {"label": "हाथी अभयारण्य: भारत में वर्तमान में 33 हाथी रिजर्व घोषित हैं (जैसे तराई ER, लेमरू ER, अगस्त्यमलाई ER)", "type": "leaf"},
                {"label": "MIKE कार्यक्रम: हाथियों की अवैध हत्या की निगरानी; भारत में 10 MIKE साइटें हैं (जैसे शिवालिक, देवमाली)", "type": "leaf"}
            ]},
            {"label": "यूपीएससी परीक्षा दृष्टिकोण", "type": "branch", "date": "परीक्षा", "children": [
                {"label": "एशियाई हाथी (Elephas maximus): IUCN लुप्तप्राय (EN); WPA 1972 की अनुसूची I और CITES की परिशिष्ट I में सूचीबद्ध", "type": "leaf"},
                {"label": "राष्ट्रीय विरासत पशु: हाथियों के संरक्षण को मजबूत करने के लिए 2010 में भारत का राष्ट्रीय विरासत पशु घोषित", "type": "leaf"}
            ]}
        ]
    },
    {
        "keys": ["project-hangul", "kashmir-stag"],
        "en": [
            {"label": "Project Hangul Origin", "type": "branch", "date": "Overview", "children": [
                {"label": "Launched in the 1970s by the Jammu and Kashmir Government with assistance from WWF and IUCN", "type": "leaf"},
                {"label": "Aimed to save the critically endangered Kashmir Stag (Hangul) from imminent extinction", "type": "leaf"}
            ]},
            {"label": "Hangul Characteristics", "type": "branch", "date": "Species", "children": [
                {"label": "Kashmir Stag (Cervus elaphus hanglu): A subspecies of Red Deer; known for its magnificent antlers", "type": "leaf"},
                {"label": "Critically Endangered (CR): Listed under Schedule I of WPA 1972; population has shrunk to under 300 individuals", "type": "leaf"}
            ]},
            {"label": "Habitat Restriction", "type": "branch", "date": "Habitat", "children": [
                {"label": "Dachigam National Park: Located near Srinagar, holds the last viable wild population of Hangul", "type": "leaf"},
                {"label": "Requires temperate coniferous forests and alpine pastures for seasonal migration", "type": "leaf"}
            ]},
            {"label": "UPSC Exam Focus", "type": "branch", "date": "UPSC Focus", "children": [
                {"label": "Threats: Habitat fragmentation due to sheep grazing, wood cutting, and military deployments in boundary areas", "type": "leaf"},
                {"label": "State Animal: Hangul is the state animal of Jammu and Kashmir", "type": "leaf"}
            ]}
        ],
        "hi": [
            {"label": "प्रोजेक्ट हंगुल की उत्पत्ति", "type": "branch", "date": "अवलोकन", "children": [
                {"label": "1970 के दशक में जम्मू-कश्मीर सरकार द्वारा WWF और IUCN की सहायता से शुरू किया गया था", "type": "leaf"},
                {"label": "अति संकटग्रस्त कश्मीर स्टैग (हंगुल) को विलुप्त होने से बचाना मुख्य लक्ष्य था", "type": "leaf"}
            ]},
            {"label": "हंगुल की विशेषताएं", "type": "branch", "date": "प्रजाति", "children": [
                {"label": "कश्मीर स्टैग (Cervus elaphus hanglu): लाल हिरण (Red Deer) की एक उपप्रजाति; सींगों के लिए प्रसिद्ध", "type": "leaf"},
                {"label": "अति संकटग्रस्त (CR): WPA 1972 की अनुसूची I के तहत सूचीबद्ध; आबादी घटकर 300 से भी कम रह गई है", "type": "leaf"}
            ]},
            {"label": "आवास प्रतिबंध", "type": "branch", "date": "आवास", "children": [
                {"label": "दाचीगाम राष्ट्रीय उद्यान: श्रीनगर के पास स्थित, हंगुल की अंतिम व्यवहार्य जंगली आबादी का घर", "type": "leaf"},
                {"label": "मौसमी प्रवास के लिए समशीतोष्ण शंकुधारी वनों और अल्पाइन घास के मैदानों की आवश्यकता होती है", "type": "leaf"}
            ]},
            {"label": "यूपीएससी परीक्षा दृष्टिकोण", "type": "branch", "date": "परीक्षा", "children": [
                {"label": "प्रमुख खतरे: भेड़ चराई, वन कटाई और सीमा क्षेत्रों में सेना की तैनाती से आवास का विखंडन", "type": "leaf"},
                {"label": "राजकीय पशु: हंगुल जम्मू और कश्मीर का राजकीय पशु है", "type": "leaf"}
            ]}
        ]
    },
    {
        "keys": ["project-sea-turtle"],
        "en": [
            {"label": "Project Sea Turtle Launch", "type": "branch", "date": "Overview", "children": [
                {"label": "Launched in November 1999 by MoEFCC in collaboration with Wildlife Institute of India (WII)", "type": "leaf"},
                {"label": "Aims to protect sea turtles in coastal waters, focusing heavily on Odisha's nesting beaches", "type": "leaf"}
            ]},
            {"label": "Olive Ridley Turtles", "type": "branch", "date": "Species", "children": [
                {"label": "Olive Ridley (Lepidochelys olivacea): Vulnerable (VU); smallest and most abundant of all sea turtles", "type": "leaf"},
                {"label": "Arribada: Mass nesting behavior where thousands of females gather on beaches to lay eggs simultaneously", "type": "leaf"}
            ]},
            {"label": "Nesting Sites in India", "type": "branch", "date": "Nesting Sites", "children": [
                {"label": "Gahirmatha Marine Sanctuary (Odisha): World's largest nesting beach for Olive Ridley turtles", "type": "leaf"},
                {"label": "Rushikulya and Devi River Mouths: Other major arribada sites along the Odisha coast", "type": "leaf"}
            ]},
            {"label": "UPSC Exam Focus", "type": "branch", "date": "UPSC Focus", "children": [
                {"label": "Turtle Excluder Devices (TED): Special grids in trawl nets allowing turtles to escape, mandated for trawlers", "type": "leaf"},
                {"label": "Operation Olivia: Annual coastal security exercise conducted by Indian Coast Guard to protect nesting turtles", "type": "leaf"}
            ]}
        ],
        "hi": [
            {"label": "प्रोजेक्ट सी टर्टल की शुरुआत", "type": "branch", "date": "अवलोकन", "children": [
                {"label": "नवंबर 1999 में MoEFCC द्वारा भारतीय वन्यजीव संस्थान (WII) के सहयोग से शुरू किया गया था", "type": "leaf"},
                {"label": "तटीय जल में समुद्री कछुओं की रक्षा करना, विशेष रूप से ओडिशा के घोंसला बनाने वाले समुद्र तटों पर ध्यान केंद्रित करना", "type": "leaf"}
            ]},
            {"label": "ओलिव रिडले कछुए", "type": "branch", "date": "प्रजाति", "children": [
                {"label": "ओलिव रिडले (Lepidochelys olivacea): संवेदनशील (VU); सभी समुद्री कछुओं में सबसे छोटा और सबसे प्रचुर", "type": "leaf"},
                {"label": "अरीबाडा (Arribada): सामूहिक घोंसला बनाने का व्यवहार जहां हजारों मादाएं अंडे देने के लिए समुद्र तटों पर एकत्र होती हैं", "type": "leaf"}
            ]},
            {"label": "भारत में घोंसला बनाने के स्थल", "type": "branch", "date": "स्थल", "children": [
                {"label": "गहिरमाथा समुद्री अभयारण्य (ओडिशा): ओलिव रिडले कछुओं के लिए दुनिया का सबसे बड़ा सामूहिक घोंसला स्थल", "type": "leaf"},
                {"label": "ऋषिकुल्या और देवी नदी मुहाना: ओडिशा तट पर अन्य प्रमुख अरीबाडा स्थल", "type": "leaf"}
            ]},
            {"label": "यूपीएससी परीक्षा दृष्टिकोण", "type": "branch", "date": "परीक्षा", "children": [
                {"label": "टर्टल एक्सक्लूडर डिवाइसेस (TED): मछली पकड़ने वाले जालों में विशेष ग्रिड जो कछुओं को बाहर निकलने की अनुमति देते हैं", "type": "leaf"},
                {"label": "ऑपरेशन ओलिविया: ओलिव रिडले कछुओं की सुरक्षा के लिए भारतीय तटरक्षक बल द्वारा संचालित वार्षिक अभ्यास", "type": "leaf"}
            ]}
        ]
    },
    {
        "keys": ["project-secure-himalaya", "secure-himalaya"],
        "en": [
            {"label": "SECURE Himalaya Launch", "type": "branch", "date": "Overview", "children": [
                {"label": "Launched in 2017 by MoEFCC in partnership with UNDP and Global Environment Facility (GEF)", "type": "leaf"},
                {"label": "Aims to ensure conservation of high-altitude Himalayan ecosystems and secure sustainable livelihoods", "type": "leaf"}
            ]},
            {"label": "Key Landscapes Covered", "type": "branch", "date": "Landscapes", "children": [
                {"label": "Spans 4 states/UTs: Himachal Pradesh (Lahaul-Spiti), Uttarakhand (Gangotri-Govind), Sikkim (Khangchendzonga), Ladakh (Changthang)", "type": "leaf"},
                {"label": "Focuses on high-altitude alpine zones and snow leopard habitats above the tree line", "type": "leaf"}
            ]},
            {"label": "Project Goals", "type": "branch", "date": "Goals", "children": [
                {"label": "Promote sustainable land management, reduce human-wildlife conflict, and check illegal wildlife trade", "type": "leaf"},
                {"label": "Strengthen local community participation in conservation and develop eco-tourism options", "type": "leaf"}
            ]},
            {"label": "UPSC Exam Focus", "type": "branch", "date": "UPSC Focus", "children": [
                {"label": "Snow Leopard (Panthera uncia): Vulnerable (VU); listed under Schedule I of WPA 1972; flagship species of high Himalayas", "type": "leaf"},
                {"label": "GEF Funding: Global Environment Facility provides financial support to meet objectives of Rio Conventions", "type": "leaf"}
            ]}
        ],
        "hi": [
            {"label": "सिक्योर हिमालय की शुरुआत", "type": "branch", "date": "अवलोकन", "children": [
                {"label": "2017 में MoEFCC द्वारा UNDP और वैश्विक पर्यावरण सुविधा (GEF) के सहयोग से शुरू किया गया था", "type": "leaf"},
                {"label": "उच्च ऊंचाई वाले हिमालयी पारिस्थितिक तंत्र के संरक्षण और सतत आजीविका सुनिश्चित करने का लक्ष्य", "type": "leaf"}
            ]},
            {"label": "कवर किए गए प्रमुख क्षेत्र", "type": "branch", "date": "क्षेत्र", "children": [
                {"label": "4 राज्यों/केंद्रशासित प्रदेशों में विस्तृत: हिमाचल (लाहौल-स्पीति), उत्तराखंड (गंगोत्री-गोविंद), सिक्किम (कंचनजंगा), लद्दाख (चांगथांग)", "type": "leaf"},
                {"label": "पेड़ की रेखा (Tree line) से ऊपर उच्च ऊंचाई वाले अल्पाइन क्षेत्रों और हिम तेंदुआ आवासों पर केंद्रित", "type": "leaf"}
            ]},
            {"label": "परियोजना के लक्ष्य", "type": "branch", "date": "लक्ष्य", "children": [
                {"label": "टिकाऊ भूमि प्रबंधन को बढ़ावा देना, मानव-वन्यजीव संघर्ष को कम करना और अवैध वन्यजीव व्यापार को रोकना", "type": "leaf"},
                {"label": "संरक्षण में स्थानीय समुदायों की भागीदारी को मजबूत करना और पर्यावरण-पर्यटन के विकल्प विकसित करना", "type": "leaf"}
            ]},
            {"label": "यूपीएससी परीक्षा दृष्टिकोण", "type": "branch", "date": "परीक्षा", "children": [
                {"label": "हिम तेंदुआ (Panthera uncia): संवेदनशील (VU); WPA 1972 की अनुसूची I के तहत सूचीबद्ध; हिमालय का फ्लैगशिप जीव", "type": "leaf"},
                {"label": "GEF फंडिंग: वैश्विक पर्यावरण सुविधा रियो सम्मेलनों के लक्ष्यों को पूरा करने के लिए वित्तीय सहायता प्रदान करती है", "type": "leaf"}
            ]}
        ]
    },
    {
        "keys": ["project-snow-leopard"],
        "en": [
            {"label": "Project Snow Leopard Launch", "type": "branch", "date": "Overview", "children": [
                {"label": "Launched in 2009 by MoEFCC to safeguard snow leopard populations and high-altitude habitats in India", "type": "leaf"},
                {"label": "Promotes a landscape-based conservation approach with active community participation", "type": "leaf"}
            ]},
            {"label": "Snow Leopard Characteristics", "type": "branch", "date": "Species", "children": [
                {"label": "Snow Leopard (Panthera uncia): 'Ghost of the Mountains'; adapted to extreme cold and steep rocky terrain", "type": "leaf"},
                {"label": "IUCN Status: Vulnerable (VU) since 2017 (previously Endangered); listed under Schedule I of WPA 1972", "type": "leaf"}
            ]},
            {"label": "Key Habitats in India", "type": "branch", "date": "Habitats", "children": [
                {"label": "Hemis National Park (Ladakh): Largest national park in India, holds the highest density of snow leopards", "type": "leaf"},
                {"label": "Great Himalayan NP (HP), Gangotri NP (Uttarakhand), Khangchendzonga NP (Sikkim), Namdapha NP (Arunachal)", "type": "leaf"}
            ]},
            {"label": "UPSC Exam Focus", "type": "branch", "date": "UPSC Focus", "children": [
                {"label": "Threats: Retaliatory killing by herders, decline in natural prey (blue sheep, ibex), and illegal trade in pelts", "type": "leaf"},
                {"label": "Global Snow Leopard and Ecosystem Protection Program (GSLEPP): Intergovernmental alliance to protect landscapes", "type": "leaf"}
            ]}
        ],
        "hi": [
            {"label": "प्रोजेक्ट हिम तेंदुआ की शुरुआत", "type": "branch", "date": "अवलोकन", "children": [
                {"label": "भारत में हिम तेंदुए की आबादी और उच्च ऊंचाई वाले आवासों की सुरक्षा के लिए MoEFCC द्वारा 2009 में शुरू किया गया", "type": "leaf"},
                {"label": "सक्रिय सामुदायिक भागीदारी के साथ परिदृश्य-आधारित (Landscape-based) संरक्षण दृष्टिकोण को बढ़ावा देता है", "type": "leaf"}
            ]},
            {"label": "हिम तेंदुए की विशेषताएं", "type": "branch", "date": "प्रजाति", "children": [
                {"label": "हिम तेंदुआ (Panthera uncia): 'पहाड़ों का भूत'; अत्यधिक ठंड और खड़ी चट्टानी इलाकों के लिए अनुकूलित", "type": "leaf"},
                {"label": "IUCN स्थिति: 2017 से संवेदनशील (VU) (पहले लुप्तप्राय); WPA 1972 की अनुसूची I के तहत सूचीबद्ध", "type": "leaf"}
            ]},
            {"label": "भारत में प्रमुख आवास", "type": "branch", "date": "आवास", "children": [
                {"label": "हेमिस राष्ट्रीय उद्यान (लद्दाख): भारत का सबसे बड़ा राष्ट्रीय उद्यान, हिम तेंदुओं का प्रमुख निवास स्थान", "type": "leaf"},
                {"label": "महान हिमालयी NP (HP), गंगोत्री NP (उत्तराखंड), कंचनजंगा NP (सिक्किम), नामदफा NP (अरुणाचल)", "type": "leaf"}
            ]},
            {"label": "यूपीएससी परीक्षा दृष्टिकोण", "type": "branch", "date": "परीक्षा", "children": [
                {"label": "प्रमुख खतरे: चरवाहों द्वारा प्रतिशोधात्मक हत्या, प्राकृतिक शिकार (नीली भेड़, आइबेक्स) की कमी और फर की तस्करी", "type": "leaf"},
                {"label": "ग्लोबल स्नो लेपर्ड एंड इकोसिस्टम प्रोटेक्शन प्रोग्राम (GSLEPP): उच्च पर्वतीय क्षेत्रों के संरक्षण के लिए वैश्विक गठबंधन", "type": "leaf"}
            ]}
        ]
    },
    {
        "keys": ["project-tiger"],
        "en": [
            {"label": "Introduction & Milestones", "type": "branch", "date": "History", "children": [
                {"label": "Launched on April 1, 1973 from Jim Corbett National Park by Indira Gandhi government", "type": "leaf"},
                {"label": "Administered by the National Tiger Conservation Authority (NTCA), a statutory body under MoEFCC", "type": "leaf"}
            ]},
            {"label": "Conservation Model", "type": "branch", "date": "Zonation", "children": [
                {"label": "Core-Buffer Strategy: Core areas are inviolate National Parks; buffer areas allow co-existence", "type": "leaf"},
                {"label": "M-STrIPES: Android-based GPS app used for ecological monitoring and patrol tracking by guards", "type": "leaf"}
            ]},
            {"label": "Tiger Census", "type": "branch", "date": "Census", "children": [
                {"label": "Conducted every 4 years using camera traps and double sampling methodology", "type": "leaf"},
                {"label": "Latest 2022 Census shows India's wild tiger population has grown to 3,682, representing 75% of global tigers", "type": "leaf"}
            ]},
            {"label": "UPSC Exam Focus", "type": "branch", "date": "UPSC Focus", "children": [
                {"label": "Tiger Reserves: Currently 54 reserves in India (e.g., Guru Ghasidas, Ranipur added recently)", "type": "leaf"},
                {"label": "Global Tiger Forum (GTF): Only inter-governmental international body established to save tigers", "type": "leaf"}
            ]}
        ],
        "hi": [
            {"label": "परिचय और मील के पत्थर", "type": "branch", "date": "इतिहास", "children": [
                {"label": "1 अप्रैल 1973 को इंदिरा गांधी सरकार द्वारा जिम कॉर्बेट राष्ट्रीय उद्यान से शुरू किया गया था", "type": "leaf"},
                {"label": "राष्ट्रीय बाघ संरक्षण प्राधिकरण (NTCA) द्वारा प्रशासित, जो MoEFCC के तहत एक वैधानिक निकाय है", "type": "leaf"}
            ]},
            {"label": "संरक्षण मॉडल", "type": "branch", "date": "रणनीति", "children": [
                {"label": "कोर-बफर रणनीति: कोर क्षेत्र पूरी तरह से राष्ट्रीय उद्यान हैं; बफर क्षेत्रों में सह-अस्तित्व की अनुमति है", "type": "leaf"},
                {"label": "M-STrIPES: वन रक्षकों द्वारा गश्त ट्रैकिंग और बाघों की निगरानी के लिए उपयोग किया जाने वाला जीपीएस-आधारित ऐप", "type": "leaf"}
            ]},
            {"label": "बाघ जनगणना (Tiger Census)", "type": "branch", "date": "जनगणना", "children": [
                {"label": "कैमरा ट्रैप और डबल सैंपलिंग पद्धति का उपयोग करके प्रत्येक 4 वर्ष में आयोजित की जाती है", "type": "leaf"},
                {"label": "2022 की जनगणना के अनुसार भारत में बाघों की संख्या 3,682 हो गई है, जो वैश्विक बाघों का 75% है", "type": "leaf"}
            ]},
            {"label": "यूपीएससी परीक्षा दृष्टिकोण", "type": "branch", "date": "यूपीएससी", "children": [
                {"label": "बाघ अभयारण्य: वर्तमान में भारत में 54 टाइगर रिजर्व घोषित हैं (जैसे रानीपुर, धौलपुर-करौली)", "type": "leaf"},
                {"label": "ग्लोबल टाइगर फोरम (GTF): बाघों को बचाने के लिए स्थापित एकमात्र अंतर-सरकारी अंतर्राष्ट्रीय निकाय", "type": "leaf"}
            ]}
        ]
    },
    {
        "keys": ["state-of-protected-areas", "protected-areas-in-the-world"],
        "en": [
            {"label": "Global Protected Areas Status", "type": "branch", "date": "Global", "children": [
                {"label": "Managed under the UNEP World Conservation Monitoring Centre (UNEP-WCMC) and IUCN World Commission on Protected Areas", "type": "leaf"},
                {"label": "Protected Planet: Online database tracking global progress on terrestrial and marine protected areas", "type": "leaf"}
            ]},
            {"label": "International Frameworks", "type": "branch", "date": "Frameworks", "children": [
                {"label": "Aichi Target 11: Set target of protecting 17% land and 10% marine areas globally by 2020", "type": "leaf"},
                {"label": "Kunming-Montreal target (30x30): Replaced Aichi; aims to protect 30% of global land and oceans by 2030", "type": "leaf"}
            ]},
            {"label": "Key Protection Categories", "type": "branch", "date": "IUCN Categories", "children": [
                {"label": "Category Ia & Ib: Strict Nature Reserves and Wilderness Areas; highest protection with no human presence", "type": "leaf"},
                {"label": "Category II: National Parks; protects ecological integrity while permitting managed public visitation", "type": "leaf"},
                {"label": "Category IV: Habitat/Species Management Areas; managed for active conservation of specific species", "type": "leaf"}
            ]},
            {"label": "UPSC Exam Focus", "type": "branch", "date": "UPSC Focus", "children": [
                {"label": "Underrepresented Biomes: Marine ecosystems and temperate grasslands remain underrepresented in global PAs", "type": "leaf"},
                {"label": "OECMs: Other Effective Area-based Conservation Measures; recognizes community-managed conservation zones outside formal parks", "type": "leaf"}
            ]}
        ],
        "hi": [
            {"label": "वैश्विक संरक्षित क्षेत्रों की स्थिति", "type": "branch", "date": "वैश्विक", "children": [
                {"label": "UNEP विश्व संरक्षण निगरानी केंद्र (UNEP-WCMC) और IUCN विश्व संरक्षित क्षेत्र आयोग द्वारा प्रबंधित", "type": "leaf"},
                {"label": "प्रोटेक्टेड प्लैनेट: वैश्विक स्थलीय और समुद्री संरक्षित क्षेत्रों की प्रगति को ट्रैक करने वाला ऑनलाइन डेटाबेस", "type": "leaf"}
            ]},
            {"label": "अंतरराष्ट्रीय नीतियां", "type": "branch", "date": "नीतियां", "children": [
                {"label": "आइची लक्ष्य 11: 2020 तक वैश्विक स्तर पर 17% भूमि और 10% समुद्री क्षेत्रों के संरक्षण का लक्ष्य निर्धारित किया था", "type": "leaf"},
                {"label": "कुनमिंग-मॉन्ट्रियल (30x30): आइची को प्रतिस्थापित किया; 2030 तक वैश्विक स्तर पर 30% भूमि और महासागरों के संरक्षण का लक्ष्य", "type": "leaf"}
            ]},
            {"label": "प्रमुख संरक्षण श्रेणियां", "type": "branch", "date": "श्रेणियां", "children": [
                {"label": "श्रेणी Ia और Ib: सख्त प्रकृति रिजर्व और वन्यजीव क्षेत्र; मानवीय गतिविधियों से पूरी तरह मुक्त", "type": "leaf"},
                {"label": "श्रेणी II: राष्ट्रीय उद्यान; पर्यटकों को अनुमति देते हुए पारिस्थितिक अखंडता की रक्षा करना", "type": "leaf"},
                {"label": "श्रेणी IV: आवास/प्रजाति प्रबंधन क्षेत्र; विशिष्ट प्रजातियों के संरक्षण के लिए सक्रिय प्रबंधन", "type": "leaf"}
            ]},
            {"label": "यूपीएससी परीक्षा दृष्टिकोण", "type": "branch", "date": "परीक्षा", "children": [
                {"label": "अल्प-प्रतिनिधित्व वाले बायोम: वैश्विक संरक्षित क्षेत्रों में समुद्री पारिस्थितिक तंत्र और समशीतोष्ण घास के मैदान कम हैं", "type": "leaf"},
                {"label": "OECMs: अन्य प्रभावी क्षेत्र-आधारित संरक्षण उपाय; औपचारिक पार्कों के बाहर सामुदायिक संरक्षण क्षेत्रों को मान्यता देना", "type": "leaf"}
            ]}
        ]
    },
    {
        "keys": ["umbrella-species"],
        "en": [
            {"label": "Definition & Criteria", "type": "branch", "date": "Concept", "children": [
                {"label": "Species with large habitat needs or home ranges; protecting them automatically protects co-occurring species", "type": "leaf"},
                {"label": "Serves as an umbrella under which the entire ecological community is conserved in the same landscape", "type": "leaf"}
            ]},
            {"label": "Representative Examples", "type": "branch", "date": "Examples", "children": [
                {"label": "Bengal Tiger: Requires vast tracts of intact forest; saving tigers protects deer, leopards, monkeys, and plants in same habitat", "type": "leaf"},
                {"label": "Grizzly Bear: Requires large, undisturbed wilderness areas; protects alpine vegetation, fish, and birds", "type": "leaf"},
                {"label": "Ganges River Dolphin: Requires clean river systems; protects river fish, turtles, and wetland flora", "type": "leaf"}
            ]},
            {"label": "Conservation Merits", "type": "branch", "date": "Merits", "children": [
                {"label": "Allows conservation planning on a landscape-wide scale rather than focusing on individual species", "type": "leaf"},
                {"label": "Simplifies policy decisions and optimizes biodiversity budget allocations", "type": "leaf"}
            ]},
            {"label": "UPSC Exam Focus", "type": "branch", "date": "UPSC Focus", "children": [
                {"label": "Keystone vs Umbrella: Keystone species have disproportionate impact relative to low biomass; Umbrella species simply require large habitats", "type": "leaf"},
                {"label": "Protected Area Net: Designing national parks based on umbrella species requirements captures regional biodiversity", "type": "leaf"}
            ]}
        ],
        "hi": [
            {"label": "परिभाषा और मानदंड", "type": "branch", "date": "अवधारणा", "children": [
                {"label": "विशाल प्राकृतिक आवास की आवश्यकता वाली प्रजाति; इसकी रक्षा करने से उसी क्षेत्र की अन्य प्रजातियों का संरक्षण स्वतः हो जाता है", "type": "leaf"},
                {"label": "एक छत्र (छतरी) के रूप में कार्य करती है जिसके तहत संपूर्ण पारिस्थितिक समुदाय को एक ही परिदृश्य में संरक्षित किया जाता है", "type": "leaf"}
            ]},
            {"label": "प्रमुख उदाहरण", "type": "branch", "date": "उदाहरण", "children": [
                {"label": "बंगाल टाइगर: विस्तृत वनों की आवश्यकता; बाघों को बचाने से हिरण, तेंदुओं, पक्षियों और वनस्पतियों की रक्षा स्वतः होती है", "type": "leaf"},
                {"label": "ग्रिजली भालू (Grizzly Bear): विशाल जंगली क्षेत्रों की आवश्यकता; अल्पाइन वनस्पतियों, जलीय जीवों और पक्षियों की रक्षा करता है", "type": "leaf"},
                {"label": "गंगा डॉल्फ़िन: स्वच्छ जलमार्गों की आवश्यकता; नदी के पर्यावरण, मछलियों और कछुओं की रक्षा करती है", "type": "leaf"}
            ]},
            {"label": "संरक्षण के लाभ", "type": "branch", "date": "लाभ", "children": [
                {"label": "व्यक्तिगत प्रजातियों पर ध्यान केंद्रित करने के बजाय बड़े स्तर पर आवास संरक्षण की अनुमति देता है", "type": "leaf"},
                {"label": "नीतिगत निर्णयों को सरल बनाता है और जैव विविधता बजट के उपयोग को इष्टतम बनाता है", "type": "leaf"}
            ]},
            {"label": "यूपीएससी परीक्षा दृष्टिकोण", "type": "branch", "date": "परीक्षा", "children": [
                {"label": "कीस्टोन बनाम अम्ब्रेला: कीस्टोन कम संख्या/जैवभार के बावजूद बड़ा प्रभाव रखते हैं; अम्ब्रेला प्रजातियों को बड़े क्षेत्र की आवश्यकता होती है", "type": "leaf"},
                {"label": "संरक्षित क्षेत्र जाल: राष्ट्रीय उद्यानों का आकार अम्ब्रेला प्रजातियों की आवश्यकताओं के आधार पर तय करने से जैव विविधता सुरक्षित होती है", "type": "leaf"}
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
    "species": "प्रजाति",
    "related": "संबंधित",
    "terminologies": "शब्दावली",
    "programs": "कार्यक्रम",
    "action": "कार्य",
    "plan": "योजना",
    "vulture": "गिद्ध",
    "aichi": "आइची",
    "targets": "लक्ष्य",
    "hotspots": "हॉटस्पॉट",
    "international": "अंतर्राष्ट्रीय",
    "cartagena": "कार्टाजेना",
    "protocol": "प्रोटोकॉल",
    "charismatic": "करिश्माई (Charismatic)",
    "crocodile": "मगरमच्छ",
    "dolphin": "डॉल्फ़िन",
    "elephant": "हाथी",
    "corridors": "गलियारे",
    "flagship": "फ्लैगशिप",
    "foundation": "फाउंडेशन",
    "ganges": "गंगा",
    "project": "परियोजना",
    "one-horn": "एक सींग वाला",
    "rhino": "गैंडा",
    "vision": "विज़न",
    "indicator": "संकेतक (Indicator)",
    "invasive": "आक्रामक",
    "alien": "विदेशी (Alien)",
    "keystone": "कीस्टोन (Keystone)",
    "nagoya": "नागोया",
    "summit": "शिखर सम्मेलन",
    "priority": "प्राथमिकता",
    "turtle": "कछुआ",
    "secure": "सिक्योर (Secure)",
    "himalaya": "हिमालय",
    "snow": "हिम",
    "leopard": "तेंदुआ",
    "tiger": "बाघ",
    "state": "स्थिति",
    "protected": "संरक्षित",
    "areas": "क्षेत्र",
    "umbrella": "अम्ब्रेला (Umbrella)",
    "network": "नेटवर्क",
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
                {"label": f"Scientific Framework: Analyzing how {t} operates as a species terminology/conservation program", "type": "leaf"}
            ]
        },
        {
            "label": f"Processes & Mechanisms",
            "type": "branch",
            "date": "Mechanisms",
            "children": [
                {"label": f"Primary Drivers: Factors regulating the development, intensity, and progression of {t}", "type": "leaf"},
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
                {"label": f"वैज्ञानिक ढांचा: {t} जैविक और पारिस्थितिक प्रणालियों के भीतर कैसे कार्य करता है", "type": "leaf"}
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
                {"label": f"मुख्य परीक्षा उत्तर लेखन: {t} को समकालीन पर्यावरण नीतियों और जैव संरक्षण लक्ष्यों से जोड़ना", "type": "leaf"}
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
