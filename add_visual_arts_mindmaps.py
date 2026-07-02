#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import re
import json

BASE = r"upsc/art_and_culture/Visual-Arts"

def get_clean_title(folder_name):
    title = folder_name.replace('-', ' ')
    words = []
    acronyms = {'upsc', 'ad', 'bc', 'ii', 'iii', 'nbpw'}
    for w in title.split():
        if w.lower() in acronyms:
            words.append(w.upper())
        elif w.lower() in ['of', 'and', 'the', 'for', 'in', 'with', 'against', 'to', 'on', 'some', 'by', 'between', 'or']:
            words.append(w.lower())
        else:
            words.append(w.capitalize())
    return ' '.join(words)

def get_custom_branches(folder_name, is_hindi):
    fl = folder_name.lower()

    # 1. Buddhist and Jaina Influence
    if fl == 'buddhist-and-jaina-influence':
        if is_hindi:
            return [
                {"label": "बौद्ध कलात्मक विरासत", "type": "branch", "date": "बौद्ध", "children": [
                    {"label": "प्रतीकात्मक रूप: प्रारंभिक हीनयान चरण में बुद्ध का चरणों, छतरी और खाली सिंहासन द्वारा प्रतीक प्रदर्शन", "type": "leaf"},
                    {"label": "मानव रूप: महायान चरण में गांधार और मथुरा शैलियों में बुद्ध की विशाल मानव मूर्तियों का निर्माण", "type": "leaf"},
                    {"label": "जातक कथाएँ: अमरावती और सांची स्तूपों पर बुद्ध के पूर्व जन्मों की कहानियों का सजीव उभारदार अंकन", "type": "leaf"}
                ]},
                {"label": "जैन कलात्मक विरासत", "type": "branch", "date": "जैन", "children": [
                    {"label": "अयागपट: मथुरा से प्राप्त जैन मन्नत पट्टिकाएं, जिन पर स्वस्तिक और अष्टमांगलिक चिन्ह उत्कीर्ण हैं", "type": "leaf"},
                    {"label": "एकाश्म मूर्तियाँ: श्रवणबेलगोला (कर्नाटक) में बाहुबली की 57 फीट ऊंची गोमतेश्वर मूर्ति (विश्व की सबसे बड़ी)", "type": "leaf"},
                    {"label": "मंदिर वास्तुकला: माउंट आबू का दिलवाड़ा जैन मंदिर (सफेद संगमरमर की बारीक नक्काशी और सुंदर छतें)", "type": "leaf"}
                ]}
            ]
        else:
            return [
                {"label": "Buddhist Artistic Influence", "type": "branch", "date": "Buddhist", "children": [
                    {"label": "Theravada Symbols: Early symbolic representation of Buddha via footprints, empty throne, and umbrellas", "type": "leaf"},
                    {"label": "Mahayana Iconography: Anthropomorphic representations of Buddha appearing first in Gandhara and Mathura schools", "type": "leaf"},
                    {"label": "Relief Panels: Vivid representations of Jataka tales carved on the railings of Sanchi and Amaravati stupas", "type": "leaf"}
                ]},
                {"label": "Jaina Artistic Legacy", "type": "branch", "date": "Jaina", "children": [
                    {"label": "Ayagapatas: Devotional tablet carvings from Mathura featuring auspicious symbols like Swastikas", "type": "leaf"},
                    {"label": "Colossal Monoliths: 57-foot-high Gommateshwara statue of Lord Bahubali at Shravanabelagola", "type": "leaf"},
                    {"label": "Marble Temple Carvings: Ornate ceiling and pillar carvings at Dilwara Jain Temples in Mount Abu", "type": "leaf"}
                ]}
            ]

    # 2. Gupta Cave Architecture
    elif fl == 'gupta-cave-architecture':
        if is_hindi:
            return [
                {"label": "अजंता गुफा वास्तुकला", "type": "branch", "date": "अजंता", "children": [
                    {"label": "संरचना: 29 बौद्ध शैलकृत गुफाएं; चैत्य (प्रार्थना कक्ष) और विहार (मठ) का उत्कृष्ट रूप", "type": "leaf"},
                    {"label": "विशेषताएँ: प्रवेश द्वारों पर यक्ष-यक्षिणी आकृतियां और आंतरिक खंभों पर बारीक नक्काशीदार कोष्ठक", "type": "leaf"}
                ]},
                {"label": "उदयगिरि व एलोरा की गुप्त कालीन गुफाएं", "type": "branch", "date": "गुप्त-वाकाटक", "children": [
                    {"label": "उदयगिरि (MP): चंद्रगुप्त द्वितीय के काल में निर्मित; प्रसिद्ध वराह (विष्णु अवतार) गुफा, सपाट छत वाले प्रारंभिक मंदिर", "type": "leaf"},
                    {"label": "एलोरा प्रारंभिक चरण: गुप्त-वाकाटक संक्रमण काल की शुरुआत; ठोस चट्टान काटकर बनाए गए शुरुआती वैष्णव कक्ष", "type": "leaf"}
                ]}
            ]
        else:
            return [
                {"label": "Ajanta Rock-Cut Structures", "type": "branch", "date": "Ajanta", "children": [
                    {"label": "Layout: 29 horseshoe-aligned Buddhist caves; distinct layout for Chaitya halls and square Viharas", "type": "leaf"},
                    {"label": "Façades: Highly decorated porch columns, arched rock windows, and carved door guardians", "type": "leaf"}
                ]},
                {"label": "Udayagiri & Early Ellora Caves", "type": "branch", "date": "Gupta Era", "children": [
                    {"label": "Udayagiri (MP): Royal patronage of Chandragupta II; features Varaha cave relief and early flat-roofed temples", "type": "leaf"},
                    {"label": "Transition Phase: Early caves of Ellora showcasing the shift from Buddhist designs to early Brahmanical shrines", "type": "leaf"}
                ]}
            ]

    # 3. Harappan Architecture & Town Planning
    elif 'harappan-architecture-town-planning' in fl:
        if is_hindi:
            return [
                {"label": "नियोजन और ग्रिड प्रणाली", "type": "branch", "date": "ग्रिड", "children": [
                    {"label": "शहरी ग्रिड: सड़कें एक दूसरे को समकोण पर काटती हुई शतरंज के बोर्ड जैसी ग्रिड व्यवस्था बनाती थीं", "type": "leaf"},
                    {"label": "विभाजन: पश्चिमी हिस्से में किला/गढ़ ( Citadel - प्रशासनिक भवन) और पूर्वी हिस्से में निचला शहर (आवासीय क्षेत्र)", "type": "leaf"}
                ]},
                {"label": "उन्नत नागरिक सुविधाएं", "type": "branch", "date": "नागरिक", "children": [
                    {"label": "जल निकासी व्यवस्था: पकी ईंटों से ढकी नालियां; कचरा छानने के लिए गड्ढे (cesspools) और साफ-सफाई के मार्ग", "type": "leaf"},
                    {"label": "विशाल सार्वजनिक भवन: मोहनजोदड़ो का विशाल स्नानागार (Great Bath - डामर का वाटरप्रूफ लेप) और बड़े अन्नागार", "type": "leaf"}
                ]}
            ]
        else:
            return [
                {"label": "Urban Grid & Layout", "type": "branch", "date": "Grid", "children": [
                    {"label": "Street Grid: Planned layout where wide main avenues intersected at clean right angles, creating block grids", "type": "leaf"},
                    {"label": "Dual Division: City divided into a fortified Western Citadel (administrative) and an Eastern Lower Town (residential)", "type": "leaf"}
                ]},
                {"label": "Advanced Civic Infrastructure", "type": "branch", "date": "Civic", "children": [
                    {"label": "Sanitary Drainage: Brick-lined covered street sewers with inspection manholes and residential link drains", "type": "leaf"},
                    {"label": "Monumental structures: The Great Bath of Mohenjo-daro (bitumen waterproofed) and ventilated granary vaults", "type": "leaf"}
                ]}
            ]

    # 4. Mauryan Cave Architecture
    elif fl == 'mauryan-cave-architecture':
        if is_hindi:
            return [
                {"label": "बराबर और नागार्जुन पहाड़ियाँ", "type": "branch", "date": "बराबर", "children": [
                    {"label": "संरचना: आजीवक संप्रदाय के भिक्षुओं के लिए सम्राट अशोक और दशरथ द्वारा ग्रेनाइट की कठोर पहाड़ियों को काटकर निर्मित", "type": "leaf"},
                    {"label": "पॉलिश: गुफाओं की आंतरिक दीवारों पर शीशे जैसी अत्यंत चमकदार पॉलिश की गई है (मौर्य लाट जैसी)", "type": "leaf"}
                ]},
                {"label": "लोमस ऋषि व सुदामा गुफाएं", "type": "branch", "date": "गुफाएँ", "children": [
                    {"label": "लोमस ऋषि गुफा: प्रवेश द्वार पर लकड़ी के मेहराब की नकल करते हुए पत्थर पर नक्काशीदार तोरण; हाथियों का जुलूस उत्कीर्ण", "type": "leaf"},
                    {"label": "स्थापत्य प्रारूप: एक आयताकार बाहरी कक्ष जो अंदर एक गोलाकार गुंबददार कक्ष ( चैत्य गृह ) से जुड़ता है", "type": "leaf"}
                ]}
            ]
        else:
            return [
                {"label": "Barabar & Nagarjuni Hill Shrines", "type": "branch", "date": "Barabar", "children": [
                    {"label": "Ajivika Patronage: Built by Ashoka and Dasharatha for Ajivika ascetics, carved out of hard granite faces", "type": "leaf"},
                    {"label": "Mirror polish: Interior cave walls features the characteristic highly reflective Mauryan burnished glaze", "type": "leaf"}
                ]},
                {"label": "Lomas Rishi & Sudama Caves", "type": "branch", "date": "Architectural", "children": [
                    {"label": "Lomas Rishi façade: Ornamental arched gateway replicating wooden thatch roofs with carved elephants", "type": "leaf"},
                    {"label": "Internal design: A rectangular congregational outer hall leading to a circular dome-vaulted inner cell", "type": "leaf"}
                ]}
            ]

    # 5. Harappan Sculptures
    elif fl == 'harappan-sculptures':
        if is_hindi:
            return [
                {"label": "कांस्य ढलाई (धातु कला)", "type": "branch", "date": "लुप्त-मोम", "children": [
                    {"label": "नृत्यांगना (मोहनजोदड़ो): लुप्त-मोम (Lost-Wax) तकनीक से निर्मित; त्रिभंग मुद्रा, हार और चूड़ियों से सजी", "type": "leaf"},
                    {"label": "कांस्य पशु मूर्तियाँ: कालीबंगन से प्राप्त कांस्य बैल और लोथल से प्राप्त तांबे का कुत्ता", "type": "leaf"}
                ]},
                {"label": "पाषाण और मृण्मूर्तियाँ (टेराकोटा)", "type": "branch", "date": "सामग्री", "children": [
                    {"label": "दाढ़ी वाले पुजारी (सेलखड़ी): तिपतिया (Trefoil) शॉल, अर्ध-खुली ध्यानमग्न आँखें और बाजूबंद", "type": "leaf"},
                    {"label": "पुरुष धड़ (लाल बलुआ पत्थर): हड़प्पा से प्राप्त; अत्यधिक यथार्थवादी मांसपेशियां और अंगों के सॉकेट", "type": "leaf"},
                    {"label": "मातृदेवी (मिट्टी): पंखे जैसी टोपी, आभूषणों से लदी; घरेलू पूजा और खिलौना गाड़ियों का निर्माण", "type": "leaf"}
                ]}
            ]
        else:
            return [
                {"label": "Bronze Casting (Metallurgy)", "type": "branch", "date": "Lost-Wax", "children": [
                    {"label": "Dancing Girl (Mohenjo-daro): Cast using lost-wax method; stands in tribhanga posture with bangles", "type": "leaf"},
                    {"label": "Animal figurines: Kalibangan bronze bull and Lothal copper dog demonstrating early metallurgy", "type": "leaf"}
                ]},
                {"label": "Stone & Terracotta Art", "type": "branch", "date": "Media", "children": [
                    {"label": "Bearded Priest (Steatite): Wears a trefoil-patterned shawl; depicted with meditative half-closed eyes", "type": "leaf"},
                    {"label": "Male Torso (Red Sandstone): Realistic anatomical details with socket holes for head and arms", "type": "leaf"},
                    {"label": "Mother Goddess (Terracotta): Crude hand-modeled clay figure with a fan-shaped headdress and chokers", "type": "leaf"}
                ]}
            ]

    # 6. Harappan Seals
    elif fl == 'harappan-seals':
        if is_hindi:
            return [
                {"label": "वर्गीकरण और विशेषताएँ", "type": "branch", "date": "सेलखड़ी", "children": [
                    {"label": "सामग्री: अधिकांशतः वर्गाकार सेलखड़ी (Steatite) की सीलें; अगेट, चर्ट और तांबे का भी प्रयोग", "type": "leaf"},
                    {"label": "लिपि: भावचित्रात्मक (Pictographic) लिपि; बाएँ से दाएँ और दाएँ से बाएँ (Boustrophedon) लिखी गई", "type": "leaf"}
                ]},
                {"label": "प्रमुख सीलें और महत्व", "type": "branch", "date": "उपयोग", "children": [
                    {"label": "पशुपति सील: तीन मुख वाले देवता (शिव का आदि रूप); हाथी, बाघ, गैंडा, भैंसा और पैरों के पास दो हिरण", "type": "leaf"},
                    {"label": "एकश्रृंगी (यूनिकॉर्न) सील: सबसे लोकप्रिय सील; अनुष्ठानिक धूपदान के सामने एक काल्पनिक एक सींग वाला जानवर", "type": "leaf"},
                    {"label": "व्यापार और पहचान: सीलों का उपयोग माल की सुरक्षा (मुहरबंदी) और व्यापारियों की पहचान के लिए किया जाता था", "type": "leaf"}
                ]}
            ]
        else:
            return [
                {"label": "Material & Paleography", "type": "branch", "date": "Steatite", "children": [
                    {"label": "Medium: Mostly square steatite plates; also made of agate, chert, copper, and terracotta", "type": "leaf"},
                    {"label": "Script: Pictographic writing system, read in boustrophedon style (alternating directions)", "type": "leaf"}
                ]},
                {"label": "Iconography & Utility", "type": "branch", "date": "Seals", "children": [
                    {"label": "Pashupati Seal: Seated yogic figure (Proto-Shiva) surrounded by elephant, tiger, rhino, buffalo, and two deer", "type": "leaf"},
                    {"label": "Unicorn Seal: Most common seal, depicting a mythical one-horned beast next to a ceremonial fire altar", "type": "leaf"},
                    {"label": "Commercial use: Employed as clay tags on cargo bags to verify ownership and prevent tampering", "type": "leaf"}
                ]}
            ]

    # 7. Harappan Pottery
    elif fl == 'harappan-pottery':
        if is_hindi:
            return [
                {"label": "प्रकार और तकनीक", "type": "branch", "date": "चाक निर्मित", "children": [
                    {"label": "सादे मृदभांड: अधिक सामान्य प्रकार; मुख्य रूप से लाल मिट्टी से अनाज और पानी के भंडारण के लिए बने", "type": "leaf"},
                    {"label": "चित्रित मृदभांड (लाल व काले): बर्तनों पर लाल लेप लगाकर काले रंग से ज्यामितीय आकृतियां और पेड़ बनाए गए", "type": "leaf"}
                ]},
                {"label": "विशेष आकृतियां और उपयोग", "type": "branch", "date": "प्रयोग", "children": [
                    {"label": "छिद्रित बर्तन: तल में छेद वाले बर्तन, जिनका उपयोग संभवतः मदिरा या पेय पदार्थों को छानने के लिए होता था", "type": "leaf"},
                    {"label": "अलंकरण: बर्तनों पर प्रतिच्छेदित वृत्त (Intersecting Circles), मछली के शल्क और पक्षियों के चित्र बने हैं", "type": "leaf"}
                ]}
            ]
        else:
            return [
                {"label": "Types & Construction", "type": "branch", "date": "Wheel-made", "children": [
                    {"label": "Plain Ware: Highly utilitarian red clay pottery, used for daily domestic storage and cooking", "type": "leaf"},
                    {"label": "Painted Ware (Black-on-Red): Coated with red slip, decorated with black paint designs", "type": "leaf"}
                ]},
                {"label": "Forms & Decoration", "type": "branch", "date": "Utility", "children": [
                    {"label": "Perforated Pots: Feature small holes along the body, likely used for brewing or straining beverages", "type": "leaf"},
                    {"label": "Designs: Dominated by geometric shapes, intersecting circles, pipal leaves, fish scales, and birds", "type": "leaf"}
                ]}
            ]

    # 8. Mauryan Pillars
    elif fl == 'mauryan-pillars':
        if is_hindi:
            return [
                {"label": "वास्तुकला और पॉलिश", "type": "branch", "date": "एकाश्म", "children": [
                    {"label": "एकाश्म लाट: चुनार बलुआ पत्थर के एकल शिलाखंड से निर्मित; शीशे जैसी चमकदार पॉलिश की गई", "type": "leaf"},
                    {"label": "स्वतंत्र स्तंभ: राजकीय घोषणाओं और बौद्ध धम्म के प्रसार के लिए खुले स्थानों पर स्थापित", "type": "leaf"}
                ]},
                {"label": "शीर्ष भाग की वास्तुकला", "type": "branch", "date": "शीर्ष", "children": [
                    {"label": "घंटी/कमल: उल्टा कमल (घंटी) का आधार; इसके ऊपर एक गोलाकार या चौकोर फलक (Abacus) बना है", "type": "leaf"},
                    {"label": "पशु शीर्ष: शीर्ष पर सिंह, बैल या हाथी की जीवंत मूर्ति (जैसे सारनाथ का सिंह शीर्ष, रामपुरवा बैल)", "type": "leaf"},
                    {"label": "अकेमेनियन तुलना: फारसी स्तंभ महलों का हिस्सा थे और पत्थरों को जोड़कर बने थे; मौर्य स्तंभ एकाश्म और स्वतंत्र थे", "type": "leaf"}
                ]}
            ]
        else:
            return [
                {"label": "Monolithic Architecture", "type": "branch", "date": "Polish", "children": [
                    {"label": "Monoliths: Carved from single blocks of Chunar sandstone; features a brilliant, mirror-like glaze", "type": "leaf"},
                    {"label": "State Declarations: Erected independently in public spaces to propagate Ashoka's Dhamma decrees", "type": "leaf"}
                ]},
                {"label": "Capital Components & Contrast", "type": "branch", "date": "Capital", "children": [
                    {"label": "Capital assembly: Consists of an inverted lotus base, an abacus with relief wheels/animals, and crowning beast", "type": "leaf"},
                    {"label": "Examples: Sarnath Lion Capital (adopted as National Emblem) and the Rampurwa Bull Capital", "type": "leaf"},
                    {"label": "Achaemenian contrast: Persian shafts were fluted, built in drums, and supported roofs; Mauryan shafts were smooth and standalone", "type": "leaf"}
                ]}
            ]

    # 9. Mauryan Stupas
    elif fl == 'mauryan-stupas':
        if is_hindi:
            return [
                {"label": "स्तूप की वास्तुकला", "type": "branch", "date": "संरचना", "children": [
                    {"label": "अंड: बुद्ध के अवशेषों (दाँत, भस्म) के ऊपर मिट्टी और पकी ईंटों से बना अर्धगोलाकार गुंबद", "type": "leaf"},
                    {"label": "हर्मिका व छतरी: गुंबद के शीर्ष पर देवताओं के निवास का प्रतीक हर्मिका और उसके ऊपर तीन छतरियां", "type": "leaf"}
                ]},
                {"label": "सांची स्तूप और तोरण", "type": "branch", "date": "सांची", "children": [
                    {"label": "विकास: अशोक द्वारा ईंटों से निर्मित; बाद में शुंग काल में पत्थर से मढ़ा गया और सातवाहनों ने तोरण जोड़े", "type": "leaf"},
                    {"label": "तोरण (द्वार): चारों दिशाओं में नक्काशीदार प्रवेश द्वार, जिन पर बुद्ध के जीवन की जातक कथाएँ अंकित हैं", "type": "leaf"}
                ]}
            ]
        else:
            return [
                {"label": "Stupa Architecture", "type": "branch", "date": "Structure", "children": [
                    {"label": "Anda: Hemispherical brick and mud dome built over relic caskets containing Buddha's remains", "type": "leaf"},
                    {"label": "Harmika & Chhatra: Square balcony on top of the dome (Harmika) representing the abode of gods, with three umbrellas", "type": "leaf"}
                ]},
                {"label": "Evolution of Sanchi", "type": "branch", "date": "Sanchi", "children": [
                    {"label": "Reconstruction: Originally built of brick by Ashoka; encased in stone by Shungas; toranas added by Satavahanas", "type": "leaf"},
                    {"label": "Toranas (Gateways): Richly carved gateways depicting Jataka tales, yakshis, and symbolic representations of Buddha", "type": "leaf"}
                ]}
            ]

    # 10. Mauryan Pottery (Common Wares)
    elif fl == 'mauryan-pottery':
        if is_hindi:
            return [
                {"label": "सामान्य घरेलू उपयोग के बर्तन", "type": "branch", "date": "सामान्य बर्तन", "children": [
                    {"label": "प्रकार: साधारण लाल और धूसर (grey) मृदभांड; अनाज, तेल और पानी के भंडारण के लिए बड़े जार", "type": "leaf"},
                    {"label": "निर्माण: सामान्य चाक पर निर्मित, कम तापमान पर पकाए गए; सजावट का अभाव, उपयोगिता पर बल", "type": "leaf"}
                ]}
            ]
        else:
            return [
                {"label": "Daily Utilitarian Wares", "type": "branch", "date": "Common Ware", "children": [
                    {"label": "Types: Plain red and grey pottery types used in domestic kitchens of common citizens", "type": "leaf"},
                    {"label": "Utility: Large coarse storage jars, bowls, and simple cooking vessels with minimal decoration", "type": "leaf"}
                ]}
            ]

    # 11. Mauryan Pottery NBPW (Luxury Wares)
    elif fl == 'mauryan-pottery-nbpw':
        if is_hindi:
            return [
                {"label": "उत्तरी काली चमकीली मृदभांड (NBPW)", "type": "branch", "date": "NBPW", "children": [
                    {"label": "विशेषताएँ: दर्पण जैसी चमकदार, काली और चिकनी सतह; बहुत पतली मिटटी से बने उत्कृष्ट विलासी बर्तन", "type": "leaf"},
                    {"label": "तकनीक: उच्च तापमान वाली भट्टियों में पकाए गए; लौह अयस्क के लेप के कारण धातु जैसी चमक आती है", "type": "leaf"}
                ]},
                {"label": "शहरीकरण और व्यापार", "type": "branch", "date": "महत्व", "children": [
                    {"label": "द्वितीय नगरीकरण: NBPW का प्रसार गंगा घाटी में द्वितीय नगरीकरण और मौर्य साम्राज्य के उत्कर्ष से जुड़ा है", "type": "leaf"},
                    {"label": "वितरण: उत्तर भारत से लेकर दक्कन (अमरावती) तक पाया गया, जो व्यापक व्यापार नेटवर्क को दर्शाता है", "type": "leaf"}
                ]}
            ]
        else:
            return [
                {"label": "Northern Black Polished Ware", "type": "branch", "date": "NBPW", "children": [
                    {"label": "Characteristics: Features a highly lustrous, mirror-like black glaze with thin, fine clay fabric", "type": "leaf"},
                    {"label": "Technique: Fired in reducing kiln atmosphere at high temperatures; coated with iron-rich slip", "type": "leaf"}
                ]},
                {"label": "Urban Context & Trade", "type": "branch", "date": "Impact", "children": [
                    {"label": "Second Urbanization: Associated with wealthy urban elites of the Mahajanapada and Maurya periods", "type": "leaf"},
                    {"label": "Distribution: Found from Taxila to Bengal and Andhra, proving extensive inland trade routes", "type": "leaf"}
                ]}
            ]

    # 12. Post-Mauryan Stupa
    elif fl == 'post-mauryan-stupa':
        if is_hindi:
            return [
                {"label": "शुंग और सातवाहन काल के बदलाव", "type": "branch", "date": "विकास", "children": [
                    {"label": "वेदिका: लकड़ी की बाड़ के स्थान पर नक्काशीदार पत्थर की वेदिका (बाउंड्री वाल) लगाई गई", "type": "leaf"},
                    {"label": "प्रदक्षिणा पथ: स्तूप के चारों ओर घूमने के लिए दो स्तरों पर पत्थर के मार्ग बनाए गए", "type": "leaf"}
                ]},
                {"label": "भरहुत और अमरावती स्तूप", "type": "branch", "date": "उदाहरण", "children": [
                    {"label": "भरहुत स्तूप (MP): अपनी उभरी हुई जातक कथाओं की नक्काशी और यक्ष-यक्षिणी छवियों के लिए प्रसिद्ध", "type": "leaf"},
                    {"label": "अमरावती स्तूप (AP): सातवाहनों द्वारा संरक्षित; सफेद संगमरमर की पट्टियों से बना विशाल स्तूप", "type": "leaf"}
                ]}
            ]
        else:
            return [
                {"label": "Shunga & Satavahana Upgrades", "type": "branch", "date": "Vedika", "children": [
                    {"label": "Vedika replacement: Replaced original wooden enclosures with stone railings carved with relief sculptures", "type": "leaf"},
                    {"label": "Pradakshina Path: Created elevated and ground-level pathways for circumambulation with stone balustrades", "type": "leaf"}
                ]},
                {"label": "Bharhut & Amaravati Stupas", "type": "branch", "date": "Examples", "children": [
                    {"label": "Bharhut (MP): Renowned for early low-relief narrative medallions representing Jataka tales and guardian Yakshas", "type": "leaf"},
                    {"label": "Amaravati Stupa: Built under Satavahanas using white marble panels, depicting highly dynamic group figures", "type": "leaf"}
                ]}
            ]

    # 13. Post-Mauryan Caves and Their Types
    elif fl == 'post-mauryan-caves-and-their-types':
        if is_hindi:
            return [
                {"label": "चैत्य और विहार", "type": "branch", "date": "वर्गीकरण", "children": [
                    {"label": "चैत्य: अर्धगोलाकार छत वाले प्रार्थना कक्ष, जिसके अंत में एक पूजा स्तूप होता था (जैसे कार्ला चैत्य)", "type": "leaf"},
                    {"label": "विहार: भिक्षुओं के रहने के लिए चट्टानों को काटकर बनाए गए कमरे; इनमें सोने के लिए पत्थर के चबूतरे थे", "type": "leaf"}
                ]},
                {"label": "प्रमुख शैलकर्तित केंद्र", "type": "branch", "date": "स्थान", "children": [
                    {"label": "कार्ला चैत्य (MH): सबसे बड़ा और सुंदर चैत्य; विशाल नक्काशीदार खंभे और लकड़ी की छत की नकल", "type": "leaf"},
                    {"label": "उदयगिरि व खंडगिरि (ओडिशा): खारवेल द्वारा जैन भिक्षुओं के लिए निर्मित गुफाएं (जैसे हाथीगुम्फा गुफा)", "type": "leaf"}
                ]}
            ]
        else:
            return [
                {"label": "Chaityas & Viharas", "type": "branch", "date": "Types", "children": [
                    {"label": "Chaityas: Vaulted congregational halls containing a small stupa at the far end for worship", "type": "leaf"},
                    {"label": "Viharas: Residential rock-cut monasteries with small cells opening into a central common courtyard", "type": "leaf"}
                ]},
                {"label": "Key Caves & Innovations", "type": "branch", "date": "Caves", "children": [
                    {"label": "Karle Chaitya (Maharashtra): Famed for its monumental size, ribbed wooden roof mimics, and lion pillars", "type": "leaf"},
                    {"label": "Udayagiri & Khandagiri (Odisha): Patronized by King Kharavela for Jain monks, featuring Hatigumpha inscriptions", "type": "leaf"}
                ]}
            ]

    # 14. Post-Mauryan Sculpture (General Developments)
    elif fl == 'post-mauryan-sculpture':
        if is_hindi:
            return [
                {"label": "मूर्तिकला का विकास", "type": "branch", "date": "सामान्य विकास", "children": [
                    {"label": "प्रारूप: यक्ष-यक्षिणी छवियों का विशाल स्तर पर निर्माण; पूजा पंथ की छवियों की शुरुआत", "type": "leaf"},
                    {"label": "अलंकरण: तोरण द्वारों पर जातक कथाओं के विस्तृत और जटिल रिलीफ (उभरा हुआ उत्कीर्णन)", "type": "leaf"}
                ]}
            ]
        else:
            return [
                {"label": "Cult Images & Reliefs", "type": "branch", "date": "Reliefs", "children": [
                    {"label": "Cult Icons: Widespread production of freestanding guardian Yaksha and Yakshini figures", "type": "leaf"},
                    {"label": "Decorative Reliefs: Detailed relief panels carved on gateways depicting Siddhartha's departures and symbols", "type": "leaf"}
                ]}
            ]

    # 15. Post-Mauryan Sculpture Gandhara, Mathura, Amaravati
    elif fl == 'post-mauryan-sculpture-gandhara-mathura-amravati-school':
        if is_hindi:
            return [
                {"label": "गांधार और मथुरा शैलियाँ", "type": "branch", "date": "कुषाण काल", "children": [
                    {"label": "गांधार स्कूल: यूनानी-रोमन प्रभाव; नीले-धूसर शिस्ट पत्थर का प्रयोग; बुद्ध के घुंघराले बाल और शॉल में सिलवटें", "type": "leaf"},
                    {"label": "मथुरा स्कूल: पूर्णतः स्वदेशी शैली; चित्तीदार लाल बलुआ पत्थर; बुद्ध की हट्टी-कट्टी काया और अभय मुद्रा", "type": "leaf"}
                ]},
                {"label": "अमरावती शैली", "type": "branch", "date": "सातवाहन", "children": [
                    {"label": "विशेषताएँ: सफेद संगमरमर/चुना पत्थर का प्रयोग; कथात्मक दृश्यों (जातक कथाओं) का सजीव चित्रण", "type": "leaf"},
                    {"label": "त्रिभंग मुद्रा: मूर्तियों में अत्यधिक गतिशीलता और त्रिभंग (शरीर में तीन घुमाव) मुद्रा का बहुतायत प्रयोग", "type": "leaf"}
                ]}
            ]
        else:
            return [
                {"label": "Gandhara vs Mathura Schools", "type": "branch", "date": "Kushan", "children": [
                    {"label": "Gandhara School: Hellenistic-Roman style; uses blue-grey schist; depicts Buddha with halo, curly hair, and drapery folds", "type": "leaf"},
                    {"label": "Mathura School: Indigenous style; uses spotted red sandstone; depicts Buddha as robust, bare-chested in abhaya mudra", "type": "leaf"}
                ]},
                {"label": "Amaravati School", "type": "branch", "date": "Satavahana", "children": [
                    {"label": "Medium: White marble; emphasizes narrative medallions depicting scenes from Jataka tales", "type": "leaf"},
                    {"label": "Group compositions: Characterized by highly dynamic, expressive, and crowded figures in tribhanga posture", "type": "leaf"}
                ]}
            ]

    # 16. Gupta Sculpture (General Schools)
    elif fl == 'gupta-sculpture':
        if is_hindi:
            return [
                {"label": "गुप्त मूर्तिकला के विभिन्न केंद्र", "type": "branch", "date": "स्कूल्स", "children": [
                    {"label": "मथुरा व पाटलिपुत्र स्कूल: मथुरा में लाल बलुआ पत्थर की मूर्तियों पर सिलवटदार वस्त्र (मलमल जैसा प्रभाव)", "type": "leaf"},
                    {"label": "उदयगिरि वराह (MP): गुप्त काल की विशाल वराह (विष्णु अवतार) मूर्ति, जो पृथ्वी को बचाते हुए दिखाई गई है", "type": "leaf"}
                ]}
            ]
        else:
            return [
                {"label": "Gupta Sculptural Schools", "type": "branch", "date": "Centers", "children": [
                    {"label": "Mathura & Pataliputra: Mathura school retained red sandstone with delicate wet-drapery lines", "type": "leaf"},
                    {"label": "Udayagiri Varaha: Monumental rock-cut relief of Varaha (boar incarnation of Vishnu) saving the Earth", "type": "leaf"}
                ]}
            ]

    # 17. Gupta Sarnath Style of Sculpture
    elif fl == 'gupta-sarnath-style-of-sculpture':
        if is_hindi:
            return [
                {"label": "सारनाथ स्कूल की विशेषताएं", "type": "branch", "date": "गुप्त काल", "children": [
                    {"label": "आध्यात्मिक आभा: चेहरे पर गहरा ध्यान और शांत भाव; आभामंडल पर अत्यंत जटिल और सुंदर नक्काशी की गई", "type": "leaf"},
                    {"label": "पारदर्शी वस्त्र: बिना किसी सिलवट (folds) के शरीर से लिपटे पारदर्शी और चिकने वस्त्र", "type": "leaf"},
                    {"label": "सारनाथ बुद्ध: धर्मचक्रप्रवर्तन मुद्रा में बैठे बुद्ध; गुप्त मूर्तिकला का सर्वोत्कृष्ट उदाहरण", "type": "leaf"},
                    {"label": "सुल्तानगंज बुद्ध: 2.3 मीटर ऊंची विशाल तांबे की बुद्ध प्रतिमा, जो धातु ढलाई में गुप्त कला को दर्शाती है", "type": "leaf"}
                ]}
            ]
        else:
            return [
                {"label": "Sarnath Style Sensibility", "type": "branch", "date": "Gupta Zenith", "children": [
                    {"label": "Spiritual calm: meditative half-closed eyes representing introspection; highly ornate, large halo (Prabhamandala)", "type": "leaf"},
                    {"label": "Plain drapery: Smooth transparent robes wrapping the body closely without any fold markings", "type": "leaf"},
                    {"label": "Sarnath Seated Buddha: Shown in Dharmachakra Pravartana Mudra, the pinnacle of Gupta sculpture", "type": "leaf"},
                    {"label": "Sultanganj Buddha: Colossal 2.3-meter-high copper statue demonstrating advanced metallic casting skills", "type": "leaf"}
                ]}
            ]

    # 18. Gupta Fresco Mural Painting
    elif fl == 'gupta-fresco-mural-painting':
        if is_hindi:
            return [
                {"label": "अजंता भित्तिचित्र कला", "type": "branch", "date": "अजंता", "children": [
                    {"label": "तकनीक: टेम्पेरा (Tempera) विधि; चट्टान पर मिट्टी, गोबर और चूने का पलस्तर कर गीली सतह पर चित्र बनाए गए", "type": "leaf"},
                    {"label": "चित्र: बोधिसत्व पद्मपाणि (हाथ में कमल) और वज्रपाणि; जातक कथाओं के विस्तृत दृश्य", "type": "leaf"}
                ]},
                {"label": "बाघ गुफा चित्र", "type": "branch", "date": "बाघ", "children": [
                    {"label": "धर्मनिरपेक्ष चित्र: बौद्ध गुफाएं होने के बावजूद चित्र धर्मनिरपेक्ष हैं, जिनमें संगीत, नृत्य और जुलूस अंकित हैं", "type": "leaf"},
                    {"label": "शैली: अजंता की तुलना में रूपरेखा सरल है लेकिन मानवीय भावनाएं अत्यधिक जीवंत हैं", "type": "leaf"}
                ]}
            ]
        else:
            return [
                {"label": "Ajanta Caves Murals", "type": "branch", "date": "Ajanta", "children": [
                    {"label": "Tempera technique: Rock surface plastered with clay, cow dung, and lime; painted with organic pigments", "type": "leaf"},
                    {"label": "Iconography: Masterpieces like Bodhisattva Padmapani and Vajrapani, depicting compassion and power", "type": "leaf"}
                ]},
                {"label": "Bagh Caves Paintings", "type": "branch", "date": "Bagh", "children": [
                    {"label": "Secular themes: Display music, group dances (Hallisaka), and royal processions despite Buddhist context", "type": "leaf"},
                    {"label": "Aesthetics: Possess simpler outlines than Ajanta but express high vitality and emotional realism", "type": "leaf"}
                ]}
            ]

    # 19. Medieval School of Sculpture
    elif fl == 'medieval-school-of-sculpture':
        if is_hindi:
            return [
                {"label": "पूर्वी भारत: पाल और सेन शैलियाँ", "type": "branch", "date": "बिहार-बंगाल", "children": [
                    {"label": "नालंदा कांस्य: वज्रयान बौद्ध देवी-देवताओं की सुंदर नक्काशीदार कांस्य मूर्तियां; पालों द्वारा संरक्षित", "type": "leaf"},
                    {"label": "काला बेसाल्ट: काले पत्थर (Basalt) को तराशकर बनाई गई चिकनी मूर्तियाँ; मुख्य रूप से मंदिर की दीवारों पर स्थापित", "type": "leaf"}
                ]},
                {"label": "दक्षिणी भारत: चोल और नायक कला", "type": "branch", "date": "कांस्य", "children": [
                    {"label": "चोल नटराज: ब्रह्मांडीय नृत्य मुद्रा (आनंद तांडव) में शिव; अपस्मार (अज्ञानता के राक्षस) को पैरों तले दबाया", "type": "leaf"},
                    {"label": "विजयनगर स्तंभ: मंदिर के खंभों पर अलंकृत नक्काशी, जिसमें घोड़ों (याली) की आकृतियां प्रमुख हैं", "type": "leaf"}
                ]}
            ]
        else:
            return [
                {"label": "Eastern India: Pala & Sena Schools", "type": "branch", "date": "Pala", "children": [
                    {"label": "Nalanda Bronzes: Vajrayana Buddhist icons produced with high casting precision under Pala kings", "type": "leaf"},
                    {"label": "Black Basalt: Lustrous, highly polished stone sculptures carved for temple niches in Bengal/Bihar", "type": "leaf"}
                ]},
                {"label": "Southern India: Chola & Vijayanagar Art", "type": "branch", "date": "Bronzes", "children": [
                    {"label": "Chola Nataraja: Cosmic dance of Shiva in Ananda Tandava pose; treading upon demon Apasmara", "type": "leaf"},
                    {"label": "Vijayanagar Pillars: High-relief sculptures on pillars featuring mythical rearing horses (Yali motifs)", "type": "leaf"}
                ]}
            ]

    # 20. Modern Indian Sculpture
    elif fl == 'modern-indian-sculpture':
        if is_hindi:
            return [
                {"label": "रामकिंकर बैज और आधुनिकता", "type": "branch", "date": "शांतिनिकेतन", "children": [
                    {"label": "कंक्रीट का प्रयोग: रामकिंकर बैज ने आधुनिक कला में पहली बार सीमेंट और कंक्रीट का प्रयोग शुरू किया", "type": "leaf"},
                    {"label": "संथाल परिवार: शांतिनिकेतन में स्थापित संथाल परिवार की मूर्ति; आदिवासी जीवन का यथार्थ चित्रण", "type": "leaf"}
                ]},
                {"label": "स्वतंत्रता के बाद का विकास", "type": "branch", "date": "आधुनिक मूर्तिकार", "children": [
                    {"label": "देवी प्रसाद राय चौधरी: 'श्रम की विजय' (मरीना beach) जैसी विशाल कांस्य मूर्तियों का निर्माण कराया", "type": "leaf"},
                    {"label": "अमूर्त कला: शंक चौधरी और प्रदोष दासगुप्ता ने मूर्तिकला में अमूर्त रूपों (abstract forms) का प्रयोग किया", "type": "leaf"}
                ]}
            ]
        else:
            return [
                {"label": "Ramkinkar Baij & Shantiniketan", "type": "branch", "date": "Baij", "children": [
                    {"label": "Concrete pioneer: Ramkinkar Baij used cement, concrete, and local soil for outdoor sculptures", "type": "leaf"},
                    {"label": "Santhal Family: Celebrated work showing tribal migration, introducing modern expressionism", "type": "leaf"}
                ]},
                {"label": "Post-Independence Modernism", "type": "branch", "date": "Sculptors", "children": [
                    {"label": "DP Roy Chowdhury: Famous for the realistic bronze statue 'Triumph of Labour' at Marina Beach", "type": "leaf"},
                    {"label": "Abstract forms: Shankho Chaudhuri and Prodosh Dasgupta integrated European abstract styling", "type": "leaf"}
                ]}
            ]

    # Fallback
    else:
        if is_hindi:
            return [
                {"label": "दृश्य कला सामान्य", "type": "branch", "date": "ललित कला", "children": [
                    {"label": "हड़प्पा काल से लेकर आधुनिक काल तक की मूर्तिकला, भित्तिचित्र और मृदभांड कला का विकास", "type": "leaf"},
                    {"label": "धार्मिक और धर्मनिरपेक्ष शैलियों का संगम; विभिन्न राजवंशों द्वारा कला को संरक्षण", "type": "leaf"}
                ]}
            ]
        else:
            return [
                {"label": "Visual Arts Overview", "type": "branch", "date": "Fine Arts", "children": [
                    {"label": "Evolution of Indian sculptures, murals, and pottery traditions from Harappa to the modern era", "type": "leaf"},
                    {"label": "Reflects religious pluralism, royal patronage, and synthetic architectural developments", "type": "leaf"}
                ]}
            ]

def process_file(html_path, is_hindi):
    print(f"Processing: {html_path} (is_hindi={is_hindi})")
    
    with open(html_path, 'r', encoding='utf-8') as f:
        html = f.read()

    # Normalize newlines
    html = html.replace('\r\n', '\n')

    # Remove any existing mindmap CSS/container/script tags
    html = html.replace('    <link rel="stylesheet" href="/assets/css/mindmap.min.css?v=2">\n', '')
    html = html.replace('    <link rel="stylesheet" href="/assets/css/mindmap.min.css?v=1">\n', '')
    html = html.replace('    <link rel="stylesheet" href="/assets/css/mindmap.min.css">\n', '')
    
    # Match and clean existing interactive mindmap card
    mindmap_div_pattern = r'\s*<!-- Interactive Mindmap -->.*?<!-- Deep-Dive Study Guide \(Dynamically Rendered\) -->'
    html = re.sub(mindmap_div_pattern, '\n            <!-- Deep-Dive Study Guide (Dynamically Rendered) -->', html, flags=re.DOTALL)
    
    # Match and clean existing mindmap engine script
    script_pattern = r'\s*<!-- Interactive Mindmap -->.*?renderMindmap\(.*?\);\s*</script>'
    html = re.sub(script_pattern, '', html, flags=re.DOTALL)

    # Get topic title from content.json if it exists
    folder_path = os.path.dirname(html_path)
    content_json_path = os.path.join(folder_path, "content.json")
    folder_name = os.path.basename(folder_path)
    if folder_name == 'hi':
        parent_folder = os.path.dirname(folder_path)
        folder_name = os.path.basename(parent_folder)
        content_json_path = os.path.join(parent_folder, "hi", "content.json")
        if not os.path.exists(content_json_path):
            content_json_path = os.path.join(parent_folder, "content.json")

    clean_title = get_clean_title(folder_name)
    
    topic_name = clean_title
    if os.path.exists(content_json_path):
        try:
            with open(content_json_path, 'r', encoding='utf-8') as f:
                c_data = json.load(f)
                topic_name = c_data.get('hero', {}).get('title', topic_name)
        except Exception as e:
            print(f"  Error reading content.json: {e}")

    # Build unique mindmap data using refined keyword matching on the folder_name
    branches = get_custom_branches(folder_name, is_hindi)
    mindmap_data = {
        "label": clean_title,
        "type": "root",
        "children": branches
    }

    # Re-inject CSS link before closing </head>
    css_link = '    <link rel="stylesheet" href="/assets/css/mindmap.min.css?v=2">\n'
    if css_link not in html:
        html = html.replace('</head>', css_link + '</head>')

    # Re-inject Mindmap Div before deep-dive-section
    if is_hindi:
        instr = 'किसी <strong style="color:#a78bfa;">बैंगनी</strong> या <strong style="color:#2ecc71;">हरे</strong> <strong>+</strong> पर क्लिक करें — एक को खोलने पर दूसरे स्वतः बंद हो जाएंगे।'
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
        # Fallback to Tab 1 notes panel
        tab1_marker = '<div class="tab-panel active" id="notes-panel" role="tabpanel" aria-labelledby="notes-panel">'
        if tab1_marker in html:
            html = html.replace(tab1_marker, tab1_marker + '\n' + mindmap_card, 1)

    # Re-inject script before </body>
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

    # Write back
    with open(html_path, 'w', encoding='utf-8') as f:
        f.write(html)
        
    print(f"  Successfully patched {html_path}")

def main():
    total_processed = 0
    for root, dirs, files in os.walk(BASE):
        rel_path = os.path.relpath(root, BASE)
        parts = rel_path.split(os.sep)
        
        is_hindi = False
        if 'hi' in parts:
            is_hindi = True
        
        for file in files:
            if file == "index.html":
                html_path = os.path.join(root, file)
                process_file(html_path, is_hindi)
                total_processed += 1
                
    print(f"\nDone! Patched {total_processed} files successfully.")

if __name__ == '__main__':
    main()
