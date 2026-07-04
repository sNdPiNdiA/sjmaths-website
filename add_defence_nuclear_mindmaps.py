#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import re
import json

BASE_DIR = r"upsc/science_and_tech/Defence-Nuclear-Technology"

def get_clean_title(folder_name):
    title = re.sub(r'([a-z])([A-Z])', r'\1 \2', folder_name)
    title = title.replace('-', ' ')
    words = []
    acronyms = {'barc', 'igmdp', 'dae', 'uav', 'drdo', 'cern', 'npcil', 'bhavini', 'aerb', 'igcar', 'phwr', 'fbr', 'ahwr', 'atgm', 'srbm', 'icbm', 'sam', 'patna'}
    for w in title.split():
        if w.lower() in acronyms:
            words.append(w.upper())
        elif w.lower() in ['of', 'and', 'the', 'for', 'in', 'with', 'against', 'to', 'on', 'some', 'by', 'their', 'vs']:
            words.append(w.lower())
        else:
            words.append(w.capitalize())
    return ' '.join(words)

# Grouped dataset containing fact-rich mindmaps with colons to support sub-branch restructuring
# Every single directory has its own completely unique dataset.
GROUPS = [
    {
        "keys": ["ballistic-vs-cruise-missile"],
        "en": [
            {"label": "Ballistic Missiles", "type": "branch", "date": "Ballistic", "children": [
                {"label": "Trajectory: Projectile parabolic path; exits the atmosphere during mid-course and re-enters under gravity", "type": "leaf"},
                {"label": "Propulsion: Rocket-powered launch; fuel burns out early, and the warhead follows an unpowered free-fall path", "type": "leaf"},
                {"label": "Examples: Agni series (IRBM/ICBM) and Prithvi (SRBM) missiles in India's inventory", "type": "leaf"}
            ]},
            {"label": "Cruise Missiles", "type": "branch", "date": "Cruise", "children": [
                {"label": "Trajectory: Flat atmospheric flightpath; flies close to the terrain (sea-skimming capability) to evade radar detection", "type": "leaf"},
                {"label": "Propulsion: Powered continuously by jet engines (turbofan/turbojet) throughout its entire flight", "type": "leaf"},
                {"label": "Examples: BrahMos (supersonic joint venture with Russia) and Nirbhay (subsonic cruise)", "type": "leaf"}
            ]}
        ],
        "hi": [
            {"label": "बैलिस्टिक मिसाइलें", "type": "branch", "date": "बैलिस्टिक", "children": [
                {"label": "प्रक्षेपवक्र (Trajectory): परवलयाकार मार्ग; मध्य-मार्ग में वायुमंडल से बाहर निकलती है और गुरुत्वाकर्षण के तहत पुनः प्रवेश करती है", "type": "leaf"},
                {"label": "प्रणोदन: रॉकेट-संचालित लॉन्च; ईंधन शुरुआत में ही समाप्त हो जाता है, और वारहेड मुक्त-पतन मार्ग का अनुसरण करता है", "type": "leaf"},
                {"label": "उदाहरण: भारत की अग्नि श्रृंखला (IRBM/ICBM) और पृथ्वी (SRBM) मिसाइलें", "type": "leaf"}
            ]},
            {"label": "क्रूज मिसाइलें", "type": "branch", "date": "क्रूज", "children": [
                {"label": "प्रक्षेपवक्र: समानांतर वायुमंडलीय उड़ान; रडार से बचने के लिए सतह के करीब (Sea-Skimming) उड़ती है", "type": "leaf"},
                {"label": "प्रणोदन: पूरी उड़ान के दौरान जेट इंजन (टर्बोफैन/टर्बोजेट) द्वारा निरंतर संचालित होती है", "type": "leaf"},
                {"label": "उदाहरण: ब्रह्मोस (रूस के साथ संयुक्त Supersonic मिसाइल) और निर्भय (Subsonic मिसाइल)", "type": "leaf"}
            ]}
        ]
    },
    {
        "keys": ["barc"],
        "en": [
            {"label": "BARC Overview", "type": "branch", "date": "BARC", "children": [
                {"label": "Origins: Bhabha Atomic Research Centre, founded in 1954 at Trombay, Mumbai; premier nuclear research facility named after Homi J. Bhabha", "type": "leaf"},
                {"label": "Research Reactors: Operates historic reactors Apsara (Asia's first, upgraded to Apsara-U), CIRUS, and Dhruva (produces weapons-grade Plutonium)", "type": "leaf"},
                {"label": "Key Mandates: Coordinates R&D in nuclear power engineering, fuel reprocessing, isotopes manufacturing for medicine, and safety monitoring", "type": "leaf"}
            ]}
        ],
        "hi": [
            {"label": "BARC का अवलोकन", "type": "branch", "date": "BARC", "children": [
                {"label": "उत्पत्ति: भाभा परमाणु अनुसंधान केंद्र, 1954 में ट्रॉम्बे, मुंबई में स्थापित; होमी जे. भाभा के नाम पर प्रमुख परमाणु अनुसंधान संस्थान", "type": "leaf"},
                {"label": "अनुसंधान रिएक्टर: ऐतिहासिक रिएक्टर अप्सरा (एशिया का पहला), सायरस (CIRUS), और ध्रुव (हथियार-ग्रेड प्लूटोनियम का मुख्य उत्पादक)", "type": "leaf"},
                {"label": "मुख्य अधिदेश: परमाणु ऊर्जा इंजीनियरिंग, ईंधन पुनर्संसाधन, चिकित्सा के लिए समस्थानिकों (Isotopes) का निर्माण और सुरक्षा अनुसंधान", "type": "leaf"}
            ]}
        ]
    },
    {
        "keys": ["defence-technology-organizations"],
        "en": [
            {"label": "DRDO Ecosystem", "type": "branch", "date": "DRDO", "children": [
                {"label": "Definition: Defence Research and Development Organisation; established in 1958 by merging Technical Development Establishment of Army with Defence Science Organisation", "type": "leaf"},
                {"label": "Key Laboratories: Network of 50+ labs like ADE (Aeronautical Development), DLRL (Electronics), and VRDE (Vehicles)", "type": "leaf"},
                {"label": "Major Projects: Development of Tejas Light Combat Aircraft (LCA), Arjun Main Battle Tank (MBT), Pinaka Multi-Barrel Rocket Launcher, and Netra AEW&CS", "type": "leaf"}
            ]}
        ],
        "hi": [
            {"label": "DRDO पारिस्थितिकी तंत्र", "type": "branch", "date": "DRDO", "children": [
                {"label": "परिभाषा: रक्षा अनुसंधान एवं विकास संगठन; सेना के तकनीकी विकास प्रतिष्ठान और रक्षा विज्ञान संगठन के विलय द्वारा 1958 में स्थापित", "type": "leaf"},
                {"label": "प्रमुख प्रयोगशालाएं: ADE (वैमानिकी विकास), DLRL (इलेक्ट्रॉनिक्स), और VRDE (वाहन) जैसी 50+ प्रयोगशालाओं का नेटवर्क", "type": "leaf"},
                {"label": "प्रमुख परियोजनाएं: तेजस लड़ाकू विमान (LCA), अर्जुन युद्धक टैंक (MBT), पिनाका मल्टी-बैरल रॉकेट लॉन्चर और नेत्रा AEW&CS का विकास", "type": "leaf"}
            ]}
        ]
    },
    {
        "keys": ["department-of-atomic-energy"],
        "en": [
            {"label": "DAE Framework", "type": "branch", "date": "DAE", "children": [
                {"label": "Structure: Department of Atomic Energy, established in 1954, placed directly under the Prime Minister of India", "type": "leaf"},
                {"label": "Apex Authority: Atomic Energy Commission (AEC) sets the policy guidelines for DAE operations", "type": "leaf"},
                {"label": "Public Sector Units: Supervises NPCIL (Nuclear Power Corporation of India) and BHAVINI (Fast Breeder reactor builder)", "type": "leaf"}
            ]}
        ],
        "hi": [
            {"label": "DAE का ढांचा", "type": "branch", "date": "DAE", "children": [
                {"label": "संरचना: परमाणु ऊर्जा विभाग (DAE), 1954 में स्थापित, सीधे भारत के प्रधानमंत्री के अधीन कार्यरत", "type": "leaf"},
                {"label": "शीर्ष प्राधिकरण: परमाणु ऊर्जा आयोग (AEC) DAE के संचालन के लिए नीतिगत दिशा-निर्देश निर्धारित करता है", "type": "leaf"},
                {"label": "सार्वजनिक क्षेत्र के उपक्रम: NPCIL (न्यूक्लियर पावर कॉरपोरेशन) और BHAVINI (फास्ट ब्रीडर रिएक्टर निर्माता) का पर्यवेक्षण करता है", "type": "leaf"}
            ]}
        ]
    },
    {
        "keys": ["integrated-guided-missile-development-programme"],
        "en": [
            {"label": "IGMDP Concept", "type": "branch", "date": "IGMDP", "children": [
                {"label": "Origins: Conceived by Dr. A.P.J. Abdul Kalam; managed by DRDO, sanctioned in 1983 to achieve self-reliance in missile technology", "type": "leaf"},
                {"label": "PATNA Missiles: Developed 5 core missile platforms: Prithvi (SRBM), Agni (IRBM/ICBM), Trishul (SR-SAM), Akash (MR-SAM), Nag (anti-tank)", "type": "leaf"},
                {"label": "Completion: Declared complete in 2008 after successful development of these tactical and strategic weapon systems", "type": "leaf"}
            ]}
        ],
        "hi": [
            {"label": "IGMDP की अवधारणा", "type": "branch", "date": "IGMDP", "children": [
                {"label": "उत्पत्ति: डॉ. ए.पी.जे. अब्दुल कलाम द्वारा परिकल्पित; मिसाइल प्रौद्योगिकी में आत्मनिर्भरता के लिए 1983 में स्वीकृत परियोजना", "type": "leaf"},
                {"label": "PATNA मिसाइलें: 5 मुख्य मिसाइल प्रणालियों का विकास: पृथ्वी (SRBM), अग्नि (IRBM/ICBM), त्रिशूल (SR-SAM), आकाश (MR-SAM), नाग (Anti-Tank)", "type": "leaf"},
                {"label": "समाप्ति: इन सामरिक और रणनीतिक हथियार प्रणालियों के सफल विकास के बाद 2008 में इसे पूर्ण घोषित किया गया", "type": "leaf"}
            ]}
        ]
    },
    {
        "keys": ["missile-system-and-classification"],
        "en": [
            {"label": "Missile Classifications", "type": "branch", "date": "Classification", "children": [
                {"label": "Speed classes: Subsonic (below Mach 0.8), Supersonic (Mach 1.2 to 5.0, e.g. BrahMos), Hypersonic (above Mach 5.0, e.g. Shaurya)", "type": "leaf"},
                {"label": "Launch Modes: Surface-to-Surface (Prithvi), Surface-to-Air (Akash), Air-to-Air (Astra), Anti-Tank Guided Missiles (Helina)", "type": "leaf"},
                {"label": "Guidance Systems: Wire-guided, active radar homing, infrared imaging (fire-and-forget Nag), and GPS-assisted coordinates", "type": "leaf"}
            ]}
        ],
        "hi": [
            {"label": "मिसाइलों का वर्गीकरण", "type": "branch", "date": "वर्गीकरण", "children": [
                {"label": "गति वर्गीकरण: सबसोनिक (माच 0.8 से नीचे), सुपरसोनिक (माच 1.2 से 5.0, जैसे ब्रह्मोस), हाइपरसोनिक (माच 5.0 से ऊपर, जैसे शौर्य)", "type": "leaf"},
                {"label": "लॉन्च मोड: सतह से सतह (पृथ्वी), सतह से हवा (आकाश), हवा से हवा (अस्त्र), एंटी-टैंक गाइडेड मिसाइल (हेलिना)", "type": "leaf"},
                {"label": "निर्देशन प्रणाली: वायर-गाइडेड, सक्रिय रडार होमिंग, इन्फ्रारेड इमेजिंग (दागो और भूल जाओ नाग मिसाइल) और जीपीएस प्रणाली", "type": "leaf"}
            ]}
        ]
    },
    {
        "keys": ["nuclear-energy-and-nuclear-fuels"],
        "en": [
            {"label": "Nuclear Fuels & Physics", "type": "branch", "date": "Fuels", "children": [
                {"label": "Fissile isotopes: Nuclei capable of undergoing fission when hit by low-energy thermal neutrons (Uranium-235, Plutonium-239, Uranium-233)", "type": "leaf"},
                {"label": "Fertile isotopes: Non-fissile materials that can be converted into fissile isotopes via neutron absorption (Uranium-238 to Pu-239; Thorium-232 to U-233)", "type": "leaf"},
                {"label": "Uranium Enrichment: Process increasing concentration of U-235 from natural levels (0.7%) to reactor grade (3-5%) or weapons grade (>90%)", "type": "leaf"}
            ]}
        ],
        "hi": [
            {"label": "परमाणु ईंधन और भौतिकी", "type": "branch", "date": "ईंधन", "children": [
                {"label": "विखंडनीय समस्थानिक (Fissile): तापीय न्यूट्रॉन के टकराने पर विखंडन में जाने वाले नाभिक (यूरेनियम-235, प्लूटोनियम-239, यूरेनियम-233)", "type": "leaf"},
                {"label": "उर्वर समस्थानिक (Fertile): गैर-विखंडनीय पदार्थ जिन्हें न्यूट्रॉन अवशोषण द्वारा विखंडनीय समस्थानिकों में बदला जा सकता है (U-238 से Pu-239, Th-232 से U-233)", "type": "leaf"},
                {"label": "यूरेनियम संवर्धन: यूरेनियम-235 की सांद्रता को प्राकृतिक स्तर (0.7%) से बढ़ाकर रिएक्टर ग्रेड (3-5%) या हथियार ग्रेड (>90%) करना", "type": "leaf"}
            ]}
        ]
    },
    {
        "keys": ["nuclear-organisations-institutions"],
        "en": [
            {"label": "Key Nuclear Institutions", "type": "branch", "date": "Institutions", "children": [
                {"label": "NPCIL: Nuclear Power Corporation of India; designs, constructs, and operates commercial nuclear power reactors in India", "type": "leaf"},
                {"label": "BHAVINI: Bharatiya Nabhikiya Vidyut Nigam Limited; public enterprise constructing India's Prototype Fast Breeder Reactor (PFBR)", "type": "leaf"},
                {"label": "AERB: Atomic Energy Regulatory Board; statutory authority enforcing safety regulations and issuing industrial radiation licenses", "type": "leaf"},
                {"label": "IGCAR: Indira Gandhi Centre for Atomic Research at Kalpakkam; coordinates design of fast breeder reactors and sodium-coolant loops", "type": "leaf"}
            ]}
        ],
        "hi": [
            {"label": "प्रमुख परमाणु संस्थान", "type": "branch", "date": "संस्थान", "children": [
                {"label": "NPCIL: न्यूक्लियर पावर कॉरपोरेशन ऑफ इंडिया; भारत में वाणिज्यिक परमाणु ऊर्जा रिएक्टरों का डिजाइन, निर्माण और संचालन करता है", "type": "leaf"},
                {"label": "BHAVINI: भारतीय नाभिकीय विद्युत निगम लिमिटेड; भारत के प्रोटोटाइप फास्ट ब्रीडर रिएक्टर (PFBR) का निर्माण करने वाला सार्वजनिक उपक्रम", "type": "leaf"},
                {"label": "AERB: परमाणु ऊर्जा नियामक बोर्ड; सुरक्षा नियमों को लागू करने और विकिरण लाइसेंस जारी करने वाला वैधानिक प्राधिकरण", "type": "leaf"},
                {"label": "IGCAR: कल्पक्कम में इंदिरा गांधी परमाणु अनुसंधान केंद्र; फास्ट ब्रीडर रिएक्टरों के डिजाइन का समन्वय करता है", "type": "leaf"}
            ]}
        ]
    },
    {
        "keys": ["nuclear-programme-in-india"],
        "en": [
            {"label": "Three-Stage Nuclear Programme", "type": "branch", "date": "3 Stages", "children": [
                {"label": "Stage 1: Pressurized Heavy Water Reactors (PHWRs) utilizing natural Uranium fuel and Heavy Water moderator, generating power and Plutonium-239", "type": "leaf"},
                {"label": "Stage 2: Fast Breeder Reactors (FBRs) utilizing Plutonium-239 fuel to breed more Plutonium from Uranium-238, or Uranium-233 from Thorium-232", "type": "leaf"},
                {"label": "Stage 3: Advanced Heavy Water Reactors (AHWRs) utilizing Uranium-233 and Thorium-232 fuel cycles to exploit India's massive Thorium reserves", "type": "leaf"}
            ]}
        ],
        "hi": [
            {"label": "तीन-स्तरीय परमाणु कार्यक्रम", "type": "branch", "date": "3 चरण", "children": [
                {"label": "चरण 1: दाबानुकूलित भारी जल रिएक्टर (PHWR); प्राकृतिक यूरेनियम ईंधन और भारी जल मंदक का उपयोग, बिजली और प्लूटोनियम-239 का उत्पादन", "type": "leaf"},
                {"label": "चरण 2: फास्ट ब्रीडर रिएक्टर (FBR); यूरेनियम-238 से अधिक प्लूटोनियम बनाने के लिए प्लूटोनियम-239 ईंधन का उपयोग, थोरियम से U-233 का उत्पादन", "type": "leaf"},
                {"label": "चरण 3: उन्नत भारी जल रिएक्टर (AHWR); भारत के विशाल थोरियम भंडारों का दोहन करने के लिए यूरेनियम-233 और थोरियम-232 ईंधन चक्र", "type": "leaf"}
            ]}
        ]
    },
    {
        "keys": ["other-government-initiatives-in-defence"],
        "en": [
            {"label": "Defence Procurement & R&D", "type": "branch", "date": "Policies", "children": [
                {"label": "DAP 2020: Defence Acquisition Procedure; prioritizes 'Make in India' and sets Indigenous Content (IC) targets in arms procurement", "type": "leaf"},
                {"label": "iDEX initiative: Innovations for Defence Excellence; funds startups and MSMEs to develop indigenous dual-use military technologies", "type": "leaf"},
                {"label": "Defence Corridors: Industrial corridors established in Uttar Pradesh and Tamil Nadu to create manufacturing clusters for private players", "type": "leaf"}
            ]}
        ],
        "hi": [
            {"label": "रक्षा खरीद और R&D नीतियां", "type": "branch", "date": "नीतियां", "children": [
                {"label": "DAP 2020: रक्षा अधिग्रहण प्रक्रिया; 'मेक इन इंडिया' को प्राथमिकता देती है और हथियारों की खरीद में स्वदेशी सामग्री (IC) का लक्ष्य तय करती है", "type": "leaf"},
                {"label": "iDEX पहल: रक्षा उत्कृष्टता के लिए नवाचार; स्वदेशी सैन्य प्रौद्योगिकियों को विकसित करने के लिए स्टार्टअप्स और MSMEs को वित्तीय सहायता", "type": "leaf"},
                {"label": "रक्षा गलियारे (Defence Corridors): निजी कंपनियों के लिए विनिर्माण क्लस्टर बनाने के लिए उत्तर प्रदेश और तमिलनाडु में औद्योगिक गलियारे", "type": "leaf"}
            ]}
        ]
    },
    {
        "keys": ["radiation-and-radioactivity"],
        "en": [
            {"label": "Radioactivity Fundamentals", "type": "branch", "date": "Physics", "children": [
                {"label": "Decay Types: Alpha decay (emits Helium nucleus), Beta decay (emits electron/positron), Gamma decay (emits high-energy photons)", "type": "leaf"},
                {"label": "Half-Life (t1/2): Time required for half of the unstable radioactive nuclei in a sample to undergo decay, unique to each isotope", "type": "leaf"},
                {"label": "Measuring Units: Becquerel (Bq; decay events per second) and Curie; absorbed doses are measured in Grays and Sieverts", "type": "leaf"}
            ]}
        ],
        "hi": [
            {"label": "रेडियोधर्मिता के सिद्धांत", "type": "branch", "date": "भौतिकी", "children": [
                {"label": "क्षय प्रकार (Decay): अल्फा क्षय (हीलियम नाभिक उत्सर्जित करता है), बीटा क्षय (इलेक्ट्रॉन उत्सर्जित करता है), गामा क्षय (ऊर्जावान फोटॉन)", "type": "leaf"},
                {"label": "अर्ध-आयु (Half-Life): किसी नमूने में अस्थिर रेडियोधर्मी नाभिकों के आधे भाग को क्षय होने के लिए आवश्यक समय, प्रत्येक समस्थानिक के लिए विशिष्ट", "type": "leaf"},
                {"label": "मापन इकाइयाँ: बेकरेल (Bq; प्रति सेकंड क्षय घटनाएं) और क्यूरी; अवशोषित खुराक को ग्रे (Grays) और सीवर्ट्स (Sieverts) में मापा जाता है", "type": "leaf"}
            ]}
        ]
    },
    {
        "keys": ["radiation-technologies-and-applications"],
        "en": [
            {"label": "Radiation Applications", "type": "branch", "date": "Uses", "children": [
                {"label": "Medical Uses: Radiotherapy using Cobalt-60 or linear accelerators to destroy cancer cells; radiopharmaceuticals (Iodine-131 for thyroid)", "type": "leaf"},
                {"label": "Food Irradiation: Exposing food to gamma rays or electron beams to eliminate pests, kill bacteria, and extend shelf life", "type": "leaf"},
                {"label": "Archaeology: Carbon-14 radioactive dating to estimate age of organic archaeological artifacts based on carbon decay", "type": "leaf"}
            ]}
        ],
        "hi": [
            {"label": "विकिरण तकनीक के अनुप्रयोग", "type": "branch", "date": "अनुप्रयोग", "children": [
                {"label": "चिकित्सा उपयोग: कैंसर कोशिकाओं को नष्ट करने के लिए कोबाल्ट-60 या त्वरकों का उपयोग करके रेडियोथेरेपी; थायराइड के लिए आयोडीन-131", "type": "leaf"},
                {"label": "खाद्य प्रसंस्करण: कीटों को नष्ट करने, बैक्टीरिया को मारने और शेल्फ जीवन बढ़ाने के लिए भोजन को गामा किरणों से गुजारना", "type": "leaf"},
                {"label": "पुरातत्व: कार्बन क्षय के आधार पर जैविक पुरातात्विक कलाकृतियों की आयु का अनुमान लगाने के लिए कार्बन-14 रेडियोधर्मी डेटिंग", "type": "leaf"}
            ]}
        ]
    },
    {
        "keys": ["radioactive-waste-and-nuclear-waste-management"],
        "en": [
            {"label": "Waste Categories & Processing", "type": "branch", "date": "Waste Management", "children": [
                {"label": "Waste Levels: Low-Level Waste (LLW; contaminated clothing/tools), Intermediate-Level Waste (ILW; chemical sludges), High-Level Waste (HLW; spent fuel)", "type": "leaf"},
                {"label": "Vitrification: Mixing HLW with liquid glass precursor and melting it into solid borosilicate canisters for long-term stabilization", "type": "leaf"},
                {"label": "Geological Repository: Storing processed waste deep underground in stable crystalline geological formations to isolate radiation", "type": "leaf"}
            ]}
        ],
        "hi": [
            {"label": "अपशिष्ट श्रेणियां और प्रसंस्करण", "type": "branch", "date": "अपशिष्ट प्रबंधन", "children": [
                {"label": "अपशिष्ट स्तर: निम्न-स्तरीय अपशिष्ट (LLW; दूषित कपड़े/औजार), मध्यम-स्तरीय (ILW; रासायनिक कीचड़), उच्च-स्तरीय (HLW; खर्च किया हुआ ईंधन)", "type": "leaf"},
                {"label": "कांच बनाना (Vitrification): उच्च-स्तरीय कचरे को तरल कांच के साथ मिलाना और दीर्घकालिक स्थिरता के लिए उसे ठोस बोरोसिलिकेट डिब्बों में ढालना", "type": "leaf"},
                {"label": "भूवैज्ञानिक भंडार: विकिरण को अलग रखने के लिए स्थिर गहरी भूमिगत चट्टान संरचनाओं में प्रसंस्कृत कचरे को संग्रहीत करना", "type": "leaf"}
            ]}
        ]
    },
    {
        "keys": ["types-of-nuclear-reactions-fusion-and-fission"],
        "en": [
            {"label": "Fission vs Fusion Processes", "type": "branch", "date": "Fission & Fusion", "children": [
                {"label": "Nuclear Fission: Splitting of a heavy atomic nucleus (like Uranium-235) into smaller nuclei, releasing energy and neutrons; powers current nuclear plants", "type": "leaf"},
                {"label": "Nuclear Fusion: Combining light nuclei (Deuterium and Tritium) to form helium, releasing massive energy; requires extreme temperatures and pressures", "type": "leaf"},
                {"label": "Tokamak: Toroidal magnetic confinement device designed to contain high-energy hydrogen plasma for controlled fusion (e.g. ITER project)", "type": "leaf"}
            ]}
        ],
        "hi": [
            {"label": "विखंडन बनाम संलयन प्रक्रियाएं", "type": "branch", "date": "विखंडन और संलयन", "children": [
                {"label": "परमाणु विखंडन (Fission): एक भारी परमाणु नाभिक (जैसे यूरेनियम-235) का छोटे नाभिकों में टूटना, ऊर्जा मुक्त करना; वर्तमान रिएक्टरों का आधार", "type": "leaf"},
                {"label": "परमाणु संलयन (Fusion): हीलियम बनाने के लिए हल्के नाभिकों (ड्यूटेरियम और ट्रिटियम) का जुड़ना, विशाल ऊर्जा मुक्त करना; इसके लिए अत्यधिक तापमान आवश्यक", "type": "leaf"},
                {"label": "टोकामक (Tokamak): नियंत्रित संलयन (जैसे ITER परियोजना) के लिए उच्च-ऊर्जा हाइड्रोजन प्लाज्मा को रोकने के लिए डिज़ाइन किया गया चुंबकीय उपकरण", "type": "leaf"}
            ]}
        ]
    },
    {
        "keys": ["types-of-nuclear-reactions"],
        "en": [
            {"label": "Reactions Classifications", "type": "branch", "date": "Reactions", "children": [
                {"label": "Fission: Heavy nucleus split into fragments after neutron capture, releasing kinetic energy and prompt neutrons", "type": "leaf"},
                {"label": "Fusion: Light isotopes fuse together at stellar core temperatures to yield heavier nuclei and energy", "type": "leaf"},
                {"label": "Radioactive Decay: Spontaneous transformation of unstable atomic nuclei into stable states by emitting alpha, beta particles, or gamma rays", "type": "leaf"},
                {"label": "Transmutation: Changing one chemical element or isotope into another via particle bombardment in reactors", "type": "leaf"}
            ]}
        ],
        "hi": [
            {"label": "नाभिकीय प्रतिक्रियाओं का वर्गीकरण", "type": "branch", "date": "प्रतिक्रियाएं", "children": [
                {"label": "विखंडन (Fission): न्यूट्रॉन कैप्चर के बाद भारी नाभिक का टुकड़ों में टूटना, गतिज ऊर्जा और न्यूट्रॉन जारी करना", "type": "leaf"},
                {"label": "संलयन (Fusion): हल्के समस्थानिकों का तारों के कोर तापमान पर फ्यूज होकर भारी नाभिक और ऊर्जा का निर्माण करना", "type": "leaf"},
                {"label": "रेडियोधर्मी क्षय: अल्फा, बीटा कणों या गामा किरणों को उत्सर्जित करके अस्थिर परमाणु नाभिक का स्वतः स्थिर अवस्था में बदलना", "type": "leaf"},
                {"label": "तत्व-परिवर्तन (Transmutation): रिएक्टरों में कण बमबारी के माध्यम से एक रासायनिक तत्व या समस्थानिक को दूसरे में बदलना", "type": "leaf"}
            ]}
        ]
    },
    {
        "keys": ["unmanned-aerial-vehicle"],
        "en": [
            {"label": "UAV Classifications", "type": "branch", "date": "UAV Core", "children": [
                {"label": "Mass limits: Classified by Weight into Nano (<250g), Micro (250g to 2kg), Small (2kg to 25kg), Medium (25kg to 150kg), Large (>150kg) under DGCA guidelines", "type": "leaf"},
                {"label": "Operational Classes: Tactical UAVs, loitering munitions (kamikaze drones), and HALE (High Altitude Long Endurance) intelligence drones", "type": "leaf"}
            ]},
            {"label": "India Indigenous UAVs", "type": "branch", "date": "India UAVs", "children": [
                {"label": "Rustom & Tapas: Medium Altitude Long Endurance (MALE) UAVs developed by DRDO for surveillance and reconnaissance", "type": "leaf"},
                {"label": "Target Drones: Lakshya (pilotless target aircraft) and Abhyas (high-speed expendable aerial target) used for missile training", "type": "leaf"}
            ]}
        ],
        "hi": [
            {"label": "UAV का वर्गीकरण", "type": "branch", "date": "UAV वर्गीकरण", "children": [
                {"label": "वजन सीमा: DGCA दिशानिर्देशों के तहत वजन के आधार पर नैनो (<250 ग्राम), माइक्रो (250 ग्राम से 2 किग्रा), स्मॉल (2 से 25 किग्रा), मीडियम और लार्ज में वर्गीकृत", "type": "leaf"},
                {"label": "ऑपरेशनल श्रेणियां: टैक्टिकल UAVs, लोइटरिंग म्यूनिशन (कामिकेज़ ड्रोन), और HALE (हाई एल्टीट्यूड लॉन्ग एंड्योरेंस) जासूसी ड्रोन", "type": "leaf"}
            ]},
            {"label": "भारत के स्वदेशी UAVs", "type": "branch", "date": "भारत", "children": [
                {"label": "रुस्तम और तापस: निगरानी और टोह लेने के लिए DRDO द्वारा विकसित मीडियम एल्टीट्यूड लॉन्ग एंड्योरेंस (MALE) ड्रोन", "type": "leaf"},
                {"label": "लक्ष्य ड्रोन: मिसाइल प्रशिक्षण के लिए उपयोग किए जाने वाले लक्ष्य (पायलट रहित लक्ष्य विमान) और अभ्यास (Abhyas) हवाई ड्रोन", "type": "leaf"}
            ]}
        ]
    }
]

TRANSLATIONS = {
    "ballistic": "बैलिस्टिक",
    "cruise": "क्रूज",
    "missile": "मिसाइल",
    "barc": "BARC (भाभा परमाणु अनुसंधान केंद्र)",
    "defence": "रक्षा (डिफेंस)",
    "technology": "तकनीक (प्रौद्योगिकी)",
    "organizations": "संगठन",
    "department": "विभाग",
    "atomic": "परमाणु (एटॉमिक)",
    "energy": "ऊर्जा",
    "integrated": "एकीकृत",
    "guided": "निर्देशित (गाइडेड)",
    "development": "विकास",
    "programme": "कार्यक्रम",
    "missile-system": "मिसाइल प्रणाली",
    "classification": "वर्गीकरण",
    "fuels": "ईंधन",
    "organisations": "संगठन",
    "institutions": "संस्थान",
    "other": "अन्य",
    "government": "सरकारी",
    "initiatives": "पहलें",
    "radiation": "विकिरण (रेडिएशन)",
    "radioactivity": "रेडियोधर्मिता",
    "technologies": "तकनीकें",
    "applications": "अनुप्रयोग",
    "radioactive": "रेडियोधर्मी",
    "waste": "अपशिष्ट (कचरा)",
    "nuclear": "परमाणु (न्यूक्लियर)",
    "management": "प्रबंधन",
    "types": "प्रकार",
    "reactions": "प्रतिक्रियाएं",
    "fusion": "संलयन (फ्यूजन)",
    "fission": "विखंडन (फिशन)",
    "unmanned": "मानवरहित",
    "aerial": "हवाई",
    "vehicle": "वाहन (UAV)"
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
                {"label": f"Definition: Understanding the fundamental characteristics, definitions, and scope of {t}", "type": "leaf"},
                {"label": f"Scientific Framework: Analyzing how {t} integrates with defense and nuclear engineering systems", "type": "leaf"}
            ]
        },
        {
            "label": f"Processes & Dynamics",
            "type": "branch",
            "date": "Mechanisms",
            "children": [
                {"label": f"Primary Drivers: Factors regulating the development, design, and implementation of {t}", "type": "leaf"},
                {"label": f"Applied Engineering: Exploring the hardware components, safety protocols, and operations of {t}", "type": "leaf"}
            ]
        },
        {
            "label": f"Socio-Economic & Applied Values",
            "type": "branch",
            "date": "Applications",
            "children": [
                {"label": f"Impacts: How advances in {t} affect national security, energy self-sufficiency, and radiation protection", "type": "leaf"},
                {"label": f"Case Studies: Notable real-world initiatives, technological systems, and research models relating to {t}", "type": "leaf"}
            ]
        },
        {
            "label": f"UPSC Exam Syllabus Relevance",
            "type": "branch",
            "date": "UPSC Core",
            "children": [
                {"label": f"Prelims Prep: Key technical terminologies, regulatory agencies, and institutional bodies associated with {t}", "type": "leaf"},
                {"label": f"Mains Answer Writing: Linking {t} with India's defense modernization, nuclear doctrine, and national missions", "type": "leaf"}
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
                {"label": f"परिभाषा: {t} की बुनियादी विशेषताओं, परिभाषाओं और कार्यक्षेत्र को समझना", "type": "leaf"},
                {"label": f"वैज्ञानिक ढांचा: {t} रक्षा और परमाणु इंजीनियरिंग प्रणालियों के साथ कैसे कार्य करता है", "type": "leaf"}
            ]
        },
        {
            "label": f"प्रक्रियाएं और गतिकी",
            "type": "branch",
            "date": "क्रियाविधि",
            "children": [
                {"label": f"प्राथमिक कारक: {t} के विकास, डिजाइन और कार्यान्वयन को नियंत्रित करने वाले तत्व", "type": "leaf"},
                {"label": f"अनुप्रयुक्त इंजीनियरिंग: {t} के हार्डवेयर घटकों, सुरक्षा नियमों और संचालन का अध्ययन", "type": "leaf"}
            ]
        },
        {
            "label": f"सामाजिक-आर्थिक और व्यावहारिक महत्व",
            "type": "branch",
            "date": "महत्व",
            "children": [
                {"label": f"प्रभाव: {t} में प्रगति राष्ट्रीय सुरक्षा, ऊर्जा आत्मनिर्भरता और विकिरण सुरक्षा को कैसे प्रभावित करती है", "type": "leaf"},
                {"label": f"क्षेत्रीय मामले: {t} से संबंधित उल्लेखनीय वैश्विक उदाहरण और राष्ट्रीय नीति मॉडल", "type": "leaf"}
            ]
        },
        {
            "label": f"यूपीएससी परीक्षा दृष्टिकोण (UPSC Focus)",
            "type": "branch",
            "date": "परीक्षा",
            "children": [
                {"label": f"प्रारंभिक परीक्षा: {t} से जुड़े तकनीकी नियमों, राष्ट्रीय नीतियों और सामान्य परीक्षा भ्रम", "type": "leaf"},
                {"label": f"मुख्य परीक्षा उत्तर लेखन: {t} को रक्षा आधुनिकीकरण, परमाणु सिद्धांत और राष्ट्रीय मिशनों से जोड़ना", "type": "leaf"}
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
