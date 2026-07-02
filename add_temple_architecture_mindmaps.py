#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import re
import json

BASE = r"upsc/art_and_culture/Temple-Architecture"

def get_clean_title(folder_name):
    title = folder_name.replace('-', ' ')
    words = []
    acronyms = {'upsc', 'ad', 'bc', 'ii', 'iii', 'rcc'}
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

    # 1. Evolution of Temple Architecture
    if 'evolution-of-temple-architecture' in fl:
        if is_hindi:
            return [
                {"label": "उत्तरी भारत (गुप्त काल की शुरुआत)", "type": "branch", "date": "गुप्त काल", "children": [
                    {"label": "प्रारंभिक सपाट छत: सांची का मंदिर 17 (सपाट छत, छोटा मंडप, वर्गाकार गर्भगृह)", "type": "leaf"},
                    {"label": "शिखर का उदय: देवगढ़ का दशावतार मंदिर (प्रारंभिक शिखर, पंचायतन शैली जिसमें चार सहायक मंदिर हैं)", "type": "leaf"}
                ]},
                {"label": "दक्षिणी भारत (पल्लव काल के चरण)", "type": "branch", "date": "पल्लव काल", "children": [
                    {"label": "गुफा मंदिर (महेंद्र समूह): शैलकृत स्तंभों वाले कक्ष (मण्डप); कोई स्वतंत्र मंदिर नहीं", "type": "leaf"},
                    {"label": "रथ मंदिर (मामल्ल समूह): महाबलीपुरम के एकाश्म पंच रथ (जैसे धर्मराज रथ जो द्रविड़ शैली का प्रतीक है)", "type": "leaf"},
                    {"label": "संरचनात्मक मंदिर (राजसिंह समूह): कांचीपुरम का कैलाशनाथ मंदिर; पहली बार ईंत और पत्थर के गारे का प्रयोग", "type": "leaf"}
                ]}
            ]
        else:
            return [
                {"label": "North Indian Evolution (Gupta Beginnings)", "type": "branch", "date": "Gupta", "children": [
                    {"label": "Flat-roofed temples: Sanchi Temple 17 (flat roof, small pillared portico, square sanctum)", "type": "leaf"},
                    {"label": "Introduction of Shikhara: Deogarh Dashavatara Temple (early shikhara, panchayatna style with 4 corner shrines)", "type": "leaf"}
                ]},
                {"label": "South Indian Evolution (Pallava Stages)", "type": "branch", "date": "Pallava", "children": [
                    {"label": "Rock-cut Mandapas (Mahendra group): Pillared caves cut from granite, representing early stages", "type": "leaf"},
                    {"label": "Monolithic Rathas (Mamalla group): Five Pancha Rathas at Mahabalipuram, showcasing Dravidian precursors", "type": "leaf"},
                    {"label": "Structural Temples (Rajasimha group): Shore Temple and Kanchipuram Kailasanatha temple built of sandstone block masonry", "type": "leaf"}
                ]}
            ]

    # 2. Types of Temple Architecture and subtypes (Nagara, Dravida, Vesara)
    elif fl == 'types-of-temple-architecture-and-subtypes':
        if is_hindi:
            return [
                {"label": "नागर और द्रविड़ शैलियाँ", "type": "branch", "date": "मुख्य शैलियाँ", "children": [
                    {"label": "नागर शैली (उत्तर): रेखीय शिखर (लैटिना/फामसाना), गर्भगृह, मंडप; ऊंचे चबूतरे (जगती) पर निर्मित; कोई गोपुरम नहीं", "type": "leaf"},
                    {"label": "द्रविड़ शैली (दक्षिण): पिरामिडनुमा विमान (सीढ़ीदार मीनार), ऊंची चहारदीवारी और विशाल प्रवेश द्वार (गोपुरम)", "type": "leaf"}
                ]},
                {"label": "वेसर शैली (मिश्रित)", "type": "branch", "date": "वेसर", "children": [
                    {"label": "वेसर शैली (चालुक्य): नागर और द्रविड़ का मिश्रण; पट्टदकल और बादामी के मंदिरों में देखा जाता है", "type": "leaf"}
                ]}
            ]
        else:
            return [
                {"label": "Nagara vs Dravida Architecture", "type": "branch", "date": "Core Styles", "children": [
                    {"label": "Nagara (North): Characterized by curvilinear Shikhara, built on raised Jagati platform; lacks boundary walls", "type": "leaf"},
                    {"label": "Dravida (South): Features pyramidal Vimana, open pillared Mandapas, sacred water tank, and tall Gopurams", "type": "leaf"}
                ]},
                {"label": "Vesara Style (Deccan Hybrid)", "type": "branch", "date": "Vesara", "children": [
                    {"label": "Vesara (Chalukyan): Hybrid style combining Nagara shikhara forms with Dravida layouts, seen at Pattadakal", "type": "leaf"}
                ]}
            ]

    # 3. Types of Temple Architecture Nagara Dravida Vesara Hoysala and subtypes
    elif fl == 'types-of-temple-architecture-nagara-dravida-vesara-hoysala-and-subtypes':
        if is_hindi:
            return [
                {"label": "नागर शैली के उप-प्रकार", "type": "branch", "date": "नागर उप-प्रकार", "children": [
                    {"label": "ओडिशा स्कूल: रेखा देउल (शिखर), जगमोहन (मंडप); बाहरी दीवारों पर जटिल नक्काशी; जैसे कोणार्क सूर्य मंदिर", "type": "leaf"},
                    {"label": "खजुराहो स्कूल: चंदेल शासक; आंतरिक और बाहरी दोनों दीवारों पर नक्काशी; कामुक मूर्तियां; पंचायतन शैली", "type": "leaf"},
                    {"label": "सोलंकी स्कूल: गुजरात; सूर्य कुंड (सीढ़ीदार जलाशय), खंभों पर सुंदर तोरण; जैसे मोढेरा सूर्य मंदिर", "type": "leaf"}
                ]},
                {"label": "होयसल और विजयनगर शैलियाँ", "type": "branch", "date": "होयसल-विजयनगर", "children": [
                    {"label": "होयसल शैली: तारकीय (Star-shaped) भू-योजना; सोपस्टोन (नरम पत्थर) का उपयोग और दीवारों पर बारीक नक्काशी", "type": "leaf"},
                    {"label": "कल्याण मंडप: विजयनगर काल की विशेषता; मंदिर परिसरों में देवताओं के विवाह के लिए बने अलंकृत नक्काशीदार स्तंभों वाले कक्ष", "type": "leaf"}
                ]}
            ]
        else:
            return [
                {"label": "Nagara Regional Subtypes", "type": "branch", "date": "Nagara Subtypes", "children": [
                    {"label": "Odisha School: Rekha Deul (shikhara) and Jagamohana (mandapa); highly carved outer walls, e.g. Konark", "type": "leaf"},
                    {"label": "Khajuraho School: Chandela patronage; features both inner and outer wall carvings; elevated plinths", "type": "leaf"},
                    {"label": "Solanki School: Gujarat; features a stepwell (Surya Kund) and decorative gateways (Toranas), e.g. Modhera", "type": "leaf"}
                ]},
                {"label": "Hoysala Stellate Temples", "type": "branch", "date": "Hoysala", "children": [
                    {"label": "Stellate plan: Star-shaped ground plans constructed using soft chloritic schist soapstone", "type": "leaf"},
                    {"label": "Relief friezes: Intricate layered horizontal bands of elephants, horses, and puranic narratives", "type": "leaf"}
                ]}
            ]

    # 4. Indo-Islamic Imperial Style
    elif fl == 'indo-islamic-imperial-style':
        if is_hindi:
            return [
                {"label": "शाही शैली की तकनीकी विशेषताएँ", "type": "branch", "date": "सल्तनत काल", "children": [
                    {"label": "मेहराबदार तकनीक: मेहराब और गुंबद (Arcuate style) का परिचय; सीमेंटिंग एजेंट के रूप में गारे (मोर्टार) का प्रयोग", "type": "leaf"},
                    {"label": "सजावट: मानव/पशु चित्रों पर प्रतिबंध; अरबी (Arabesque), ज्यामितीय आकृतियों और सुलेख (Calligraphy) का उपयोग", "type": "leaf"}
                ]}
            ]
        else:
            return [
                {"label": "Arcuate Technology & Aesthetics", "type": "branch", "date": "Delhi Sultanate", "children": [
                    {"label": "Arcuate Style: Introduced arches, domes, vaults, and plaster mortar, replacing lintel-beam systems", "type": "leaf"},
                    {"label": "Decoration: Prohibited human figures; used geometric arabesques, floral patterns, and Quranic calligraphy", "type": "leaf"}
                ]}
            ]

    # 5. Indo-Islamic Imperial Style Delhi Sultanate
    elif fl == 'indo-islamic-imperial-style-delhi-sultanate':
        if is_hindi:
            return [
                {"label": "राजवंश-वार विकास", "type": "branch", "date": "सल्तनत राजवंश", "children": [
                    {"label": "गुलाम/खिलजी: कुव्वत-उल-इस्लाम मस्जिद, अलाई दरवाजा (अकबर से पहले पहली बार सच्ची मेहराब और लाल बलुआ पत्थर)", "type": "leaf"},
                    {"label": "तुगलक: ढलवां दीवारें (सलामी तकनीक/Batter), गारे का भारी प्रयोग और गयासुद्दीन तुगलक का मकबरा", "type": "leaf"},
                    {"label": "लोधी: दोहरे गुंबद (Double Dome) की शुरुआत और अष्टकोणीय मकबरे (लोधी गार्डन)", "type": "leaf"}
                ]}
            ]
        else:
            return [
                {"label": "Dynastic Monumental Shifts", "type": "branch", "date": "Sultanate", "children": [
                    {"label": "Mamluk & Khalji: Alai Darwaza showing early true dome and red sandstone with marble decorations", "type": "leaf"},
                    {"label": "Tughlaq phase: Introduced sloped walls (batter technique) and grey sandstone for strength", "type": "leaf"},
                    {"label": "Lodhis: Introduced octagonal tomb shapes and the double dome technique to raise dome height", "type": "leaf"}
                ]}
            ]

    # 6. Indo-Islamic Provincial Style
    elif fl == 'indo-islamic-provincial-style':
        if is_hindi:
            return [
                {"label": "जौनपुर और बंगाल शैलियाँ", "type": "branch", "date": "पूर्वी प्रांत", "children": [
                    {"label": "जौनपुर (शर्की शैली): अटाला मस्जिद (विशाल अलंकृत प्रवेश द्वार/Pylon, ऊंचे मेहराबदार अग्रभाग)", "type": "leaf"},
                    {"label": "बंगाल शैली: ईंट वास्तुकला; झुकी हुई बाँस की छतों जैसी छतें (बांग्ला छत, जैसे अदीना मस्जिद)", "type": "leaf"}
                ]}
            ]
        else:
            return [
                {"label": "Eastern Provinces (Jaunpur & Bengal)", "type": "branch", "date": "East", "children": [
                    {"label": "Jaunpur (Sharqi): Atala Mosque (characterized by massive sloping pylon gateways flanking the facade)", "type": "leaf"},
                    {"label": "Bengal: Used brick due to lack of stone; features curved eaves mimicking bamboo roofs (e.g. Adina Mosque)", "type": "leaf"}
                ]}
            ]

    # 7. Indo-Islamic Provincial Style Malwa or Pathan Style
    elif fl == 'indo-islamic-provincial-style-malwa-or-pathan-style':
        if is_hindi:
            return [
                {"label": "मालवा और गुजरात शैलियाँ", "type": "branch", "date": "पश्चिमी प्रांत", "children": [
                    {"label": "मालवा शैली: मांडू का हिंडोला महल, जहाज महल; बड़े जल निकायों का उपयोग, संगमरमर का आयात", "type": "leaf"},
                    {"label": "गुजरात शैली: जामा मस्जिद (अहमदाबाद), सीदी सैयद मस्जिद (सजीव नक्काशीदार पत्थर की जाली), स्थानीय हिंदू रूपांकन", "type": "leaf"}
                ]}
            ]
        else:
            return [
                {"label": "Western Provinces (Malwa & Gujarat)", "type": "branch", "date": "West", "children": [
                    {"label": "Malwa (Mandu): Jahaz Mahal & Hindola Mahal; characterized by massive courtyards and large pools", "type": "leaf"},
                    {"label": "Gujarat: Fused local Hindu stone carving with Islamic domes, e.g. Sidi Saiyyed Mosque lattices", "type": "leaf"}
                ]}
            ]

    # 8. Indo-Islamic Mughal Style
    elif fl == 'indo-islamic-mughal-style':
        if is_hindi:
            return [
                {"label": "अकबर का लाल बलुआ पत्थर काल", "type": "branch", "date": "1556-1605 ई.", "children": [
                    {"label": "Fatehpur Sikri: बुलंद दरवाजा, जोधाबाई महल, पंच महल; लाल बलुआ पत्थर और धरन-बीम (trabeate) का प्रयोग", "type": "leaf"},
                    {"label": "हुमायूँ का मकबरा: दिल्ली में निर्मित; चारबाग उद्यान योजना और दोहरे गुंबद का प्रारंभिक प्रयोग", "type": "leaf"}
                ]},
                {"label": "शाहजहाँ का सफेद संगमरमर काल", "type": "branch", "date": "1628-1658 ई.", "children": [
                    {"label": "पिएत्रा ड्यूरा: संगमरमर की सतहों पर मूल्यवान रत्नों की जड़ावट; जटिल ज्यामितीय समरूपता", "type": "leaf"},
                    {"label": "ताजमहल: दोहरे गुंबद, सफेद मकराना संगमरमर, चार कोनों पर मीनारें और सममित उद्यान", "type": "leaf"}
                ]}
            ]
        else:
            return [
                {"label": "Akbar's Red Sandstone Era", "type": "branch", "date": "1556-1605 AD", "children": [
                    {"label": "Fatehpur Sikri: Buland Darwaza, Panch Mahal; extensively utilized red sandstone and trabeate beams", "type": "leaf"},
                    {"label": "Humayun's Tomb: Early Mughal prototype built in Delhi; features Charbagh garden layouts", "type": "leaf"}
                ]},
                {"label": "Shah Jahan's Marble Zenith", "type": "branch", "date": "1628-1658 AD", "children": [
                    {"label": "Pietra Dura: Inlay of semi-precious stones (lapis lazuli, jasper) into white Makrana marble", "type": "leaf"},
                    {"label": "Taj Mahal: Perfect symmetry, double dome, four flanking minarets, and waterfront Charbagh placement", "type": "leaf"}
                ]}
            ]

    # 9. Indo-Islamic Avadh Style
    elif fl == 'indo-islamic-avadh-style':
        if is_hindi:
            return [
                {"label": "लखनऊ की आसफी वास्तुकला", "type": "branch", "date": "नवाब काल", "children": [
                    {"label": "सामग्री: पत्थरों की कमी के कारण ईंटों और चूने के गारे (Stucco) का उपयोग; नक्काशीदार मेहराबों की भरमार", "type": "leaf"},
                    {"label": "रूमी दरवाजा: तुर्की गेटवे की तर्ज पर बना विशाल प्रवेश द्वार, जिसमें तीन तरफ मेहराबदार रास्ते हैं", "type": "leaf"}
                ]}
            ]
        else:
            return [
                {"label": "Lucknow Nawab School", "type": "branch", "date": "Nawabs", "children": [
                    {"label": "Material: Brick and thick stucco plaster instead of stone; highly decorated arches and parapets", "type": "leaf"},
                    {"label": "Rumi Darwaza: Colossal gateway inspired by Constantinople designs, featuring intricate carvings", "type": "leaf"}
                ]}
            ]

    # 10. Indo-Islamic Avadh Oudh Style
    elif fl == 'indo-islamic-avadh-oudh-style':
        if is_hindi:
            return [
                {"label": "बड़ा इमामबाड़ा", "type": "branch", "date": "इमामबाड़ा", "children": [
                    {"label": "केंद्रीय हॉल: बिना किसी खंभे या गर्डर के सहारे निर्मित दुनिया का सबसे बड़ा मेहराबदार हॉल", "type": "leaf"},
                    {"label": "भूलभुलैया: केंद्रीय हॉल के ऊपर बनी भूलभुलैया (Labyrinth), जो छत का वजन संतुलित करती है", "type": "leaf"}
                ]}
            ]
        else:
            return [
                {"label": "Bara Imambara Engineering", "type": "branch", "date": "Imambara", "children": [
                    {"label": "Central Vault: World's largest vaulted hall constructed without any supporting pillars or iron beams", "type": "leaf"},
                    {"label": "Bhulbhulaiya: Complex labyrinth constructed above the hall to distribute load and prevent collapse", "type": "leaf"}
                ]}
            ]

    # 11. Indo-Islamic Rajput Architecture
    elif fl == 'indo-islamic-rajput-architecture':
        if is_hindi:
            return [
                {"label": "किला व महल वास्तुकला", "type": "branch", "date": "राजपूत", "children": [
                    {"label": "मेहराबदार व धरन मिश्रण: इस्लामी मेहराबों और मुग़ल झरोखों का राजपूत छतरियों के साथ संगम", "type": "leaf"},
                    {"label": "झरोखा व जाली: लटकती हुई बालकनी (झरोखा) और बारीक नक्काशीदार पत्थर की जाली स्क्रीन का व्यापक उपयोग", "type": "leaf"},
                    {"label": "प्रमुख स्मारक: आमेर किला व हवा महल (जयपुर); पहाड़ी पर बने अभेद्य सैन्य किले और बावड़ियों (पानी की बावली)", "type": "leaf"}
                ]}
            ]
        else:
            return [
                {"label": "Fort & Palace Integration", "type": "branch", "date": "Rajput", "children": [
                    {"label": "Structural blend: Integrated Mughal arches and domes with indigenous Jharokhas and stepwells", "type": "leaf"},
                    {"label": "Features: Hanging balconies (Jharokhas), fluted archways, pillared pavilions (Chhatris), and Jaalis", "type": "leaf"},
                    {"label": "Amber Fort & Hawa Mahal: Hawa Mahal (Jaipur) has 953 small windows (Jharokhas) for cooling air currents", "type": "leaf"}
                ]}
            ]

    # 12. Indo-Islamic Sikh Style
    elif fl == 'indo-islamic-sikh-style-of-architecture':
        if is_hindi:
            return [
                {"label": "सिख वास्तुकला की विशेषताएं", "type": "branch", "date": "सिख शैली", "children": [
                    {"label": "संंश्लेषण: मुगलों के प्याज जैसे गुंबदों, मेहराबों और राजपूत छतरियों/झरोखों का अनूठा मिश्रण", "type": "leaf"},
                    {"label": "हरमंदिर साहिब (स्वर्ण मंदिर): चारों दिशाओं में प्रवेश द्वार; संगमरमर की सतहों पर बारीक नक्काशी और सोने की परत", "type": "leaf"}
                ]}
            ]
        else:
            return [
                {"label": "Synthesis of Styles", "type": "branch", "date": "Sikh Style", "children": [
                    {"label": "Eclectic mix: Fused Mughal fluted domes and foliated arches with Rajput chhatris and projections", "type": "leaf"},
                    {"label": "Harmandir Sahib (Golden Temple): Features four entrances; interior decorated with Pietra Dura marble work and gold leaf", "type": "leaf"}
                ]}
            ]

    # 13. European Influence
    elif fl == 'european-influence':
        if is_hindi:
            return [
                {"label": "पुर्तगाली और फ्रांसीसी प्रभाव", "type": "branch", "date": "उपनिवेश", "children": [
                    {"label": "पुर्तगाली: बारोक (Baroque) शैली के चर्च; प्लास्टर की कोटिंग और सफेद धोए गए चर्च (जैसे गोवा के चर्च)", "type": "leaf"},
                    {"label": "फ्रांसीसी: पांडिचेरी में नियोजित ग्रिड सड़कें और हवादार फ्रांसीसी कोठियां", "type": "leaf"}
                ]}
            ]
        else:
            return [
                {"label": "Portuguese & French Influences", "type": "branch", "date": "Colonial", "children": [
                    {"label": "Portuguese Goa: Introduced Baroque architecture, white-washed lime facades, e.g. Basilica of Bom Jesus", "type": "leaf"},
                    {"label": "French Puducherry: Grid layouts with high-walled bungalows and elegant coastal promenades", "type": "leaf"}
                ]}
            ]

    # 14. European Influence Modern Architecture
    elif fl == 'european-influence-modern-architecture':
        if is_hindi:
            return [
                {"label": "प्रारंभिक ब्रिटिश शैली", "type": "branch", "date": "ब्रिटिश काल", "children": [
                    {"label": "नियो-क्लासिकल शैली: प्रारंभिक शास्त्रीय पुनरुद्धार शैली जिसमें विशाल पोर्टिको और खंभों की कतारें शामिल थीं", "type": "leaf"},
                    {"label": "प्रमुख उदाहरण: कोलकाता का विक्टोरिया मेमोरियल (शास्त्रीय पुनरुद्धार और ताजमहल की प्रतिकृति शैली)", "type": "leaf"}
                ]}
            ]
        else:
            return [
                {"label": "Neo-Classical British Style", "type": "branch", "date": "Early British", "children": [
                    {"label": "Colonnades: Features massive porticos, pediments, and colonnades replicating Greek/Roman halls", "type": "leaf"},
                    {"label": "Victoria Memorial: Built in Kolkata, combining classical Renaissance styling with Mughal details", "type": "leaf"}
                ]}
            ]

    # 15. Indo-Gothic Architecture
    elif fl == 'indo-gothic-architecture':
        if is_hindi:
            return [
                {"label": "इंडो-गॉथिक (विक्टोरियन गॉथिक)", "type": "branch", "date": "विक्टोरियन", "children": [
                    {"label": "विशेषताएँ: ऊंची नुकीली मेहराबें, पसलियों वाली छतें (Ribbed Vaults) और रंगीन काँच की खिड़कियां", "type": "leaf"},
                    {"label": "छत्रपति शिवाजी टर्मिनस (CST): मुंबई का प्रसिद्ध रेलवे स्टेशन, जो विक्टोरियन गॉथिक कला का उत्कृष्ट उदाहरण है", "type": "leaf"}
                ]}
            ]
        else:
            return [
                {"label": "Indo-Gothic (Victorian Gothic)", "type": "branch", "date": "Victorian", "children": [
                    {"label": "Features: Tall pointed lancet arches, ribbed stone vaults, stained glass windows, and ironwork", "type": "leaf"},
                    {"label": "CSMT (Mumbai): Famed railway terminal showcasing Gothic revival style integrated with Indian motifs", "type": "leaf"}
                ]}
            ]

    # 16. Neo-Roman Style
    elif fl == 'neo-roman-style':
        if is_hindi:
            return [
                {"label": "लुटियंस दिल्ली की वास्तुकला", "type": "branch", "date": "लुटियंस", "children": [
                    {"label": "विशेषताएँ: विशाल रोमन शास्त्रीय खंभे (columns), शास्त्रीय समरूपता और केंद्रीय गुंबद", "type": "leaf"},
                    {"label": "भारतीय तत्वों का समावेश: छज्जे (सूर्य से बचाव के लिए), जाली स्क्रीन और पत्थर की छतरियों का प्रयोग किया", "type": "leaf"},
                    {"label": "राष्ट्रपति भवन: केंद्रीय गुंबद सांची के बौद्ध स्तूप से प्रेरित है; लाल और सफेद बलुआ पत्थर का उपयोग", "type": "leaf"}
                ]}
            ]
        else:
            return [
                {"label": "Lutyens' Delhi Design", "type": "branch", "date": "Imperial", "children": [
                    {"label": "Classical symmetry: Roman columns, open colonnades, and central dome structures", "type": "leaf"},
                    {"label": "Indian fusion: Integrated traditional stone chajjas (eaves), jaali screens, and chhatris", "type": "leaf"},
                    {"label": "Rashtrapati Bhavan: Features a copper dome inspired directly by the Buddhist Stupa of Sanchi", "type": "leaf"}
                ]}
            ]

    # 17. Modern Architecture
    elif fl == 'modern-architecture':
        if is_hindi:
            return [
                {"label": "ली कोर्बुसिए और चंडीगढ़", "type": "branch", "date": "कोर्बुसिए", "children": [
                    {"label": "ग्रिड प्रणाली: चंडीगढ़ शहर का नियोजित ग्रिड सेक्टोरल लेआउट और प्रशासनिक भवनों का डिजाइन", "type": "leaf"},
                    {"label": "कंक्रीट कला: ब्रुटलिस्ट वास्तुकला (कच्चे कंक्रीट का उपयोग) और प्रसिद्ध ओपन हैंड स्मारक (Open Hand)", "type": "leaf"}
                ]}
            ]
        else:
            return [
                {"label": "Le Corbusier & Chandigarh", "type": "branch", "date": "Corbusier", "children": [
                    {"label": "Brutalist Concrete: Used raw exposed concrete, sun-breakers (brise-soleil), and grid Sector layouts", "type": "leaf"},
                    {"label": "Capitol Complex: Designed the High Court, Secretariat, and Assembly buildings with open vistas", "type": "leaf"}
                ]}
            ]

    # 18. Notable Architects
    elif fl == 'notable-architects':
        if is_hindi:
            return [
                {"label": "आधुनिक भारतीय वास्तुकार", "type": "branch", "date": "वास्तुकार", "children": [
                    {"label": "चार्ल्स कोरिया: जवाहर कला केंद्र (जयपुर) और गांधी स्मारक संग्रहालय; खुली छतों और वास्तु-पुरुष मंडल का प्रयोग", "type": "leaf"},
                    {"label": "लॉरी बेकर: केरल में कम लागत वाली, पर्यावरण-अनुकूल स्थानीय ईंट वास्तुकला की शुरुआत की", "type": "leaf"}
                ]}
            ]
        else:
            return [
                {"label": "Modernist Architects", "type": "branch", "date": "Architects", "children": [
                    {"label": "Charles Correa: Blended cosmic Vaastu diagrams with open courtyards, e.g. Jawahar Kala Kendra", "type": "leaf"},
                    {"label": "Laurie Baker: Famed for cost-effective organic brick masonry, using filler slabs and jali venting", "type": "leaf"}
                ]}
            ]

    # 19. Post-Independence Period
    elif fl == 'post-independence-period':
        if is_hindi:
            return [
                {"label": "स्वतंत्रता के बाद का संक्रमण", "type": "branch", "date": "राष्ट्र निर्माण", "children": [
                    {"label": "राष्ट्र निर्माण: नए प्रशासनिक परिसरों, आईआईटी और भारी उद्योग कारखानों का आधुनिक रूप", "type": "leaf"},
                    {"label": "सामग्री: प्रबलित कंक्रीट (RCC), कांच और स्टील का बढ़ता उपयोग", "type": "leaf"}
                ]}
            ]
        else:
            return [
                {"label": "Nation-Building Modernism", "type": "branch", "date": "Modernism", "children": [
                    {"label": "Industrial buildings: Massive state-funded campuses, IIT complexes, and government offices", "type": "leaf"},
                    {"label": "Materials: Heavy transition to Reinforced Cement Concrete (RCC), glass panellings, and structural steel", "type": "leaf"}
                ]}
            ]

    # 20. Post-Independence Period Architecture
    elif fl == 'post-independence-period-architecture':
        if is_hindi:
            return [
                {"label": "आधुनिक प्रतीकात्मक संरचनाएँ", "type": "branch", "date": "संरचनाएँ", "children": [
                    {"label": "लोटस टेम्पल (दिल्ली): बहाई उपासना स्थल; कमल की पंखुड़ियों के आकार की संरचना; उत्कृष्ट इंजीनियरिंग", "type": "leaf"},
                    {"label": "एलआईसी बिल्डिंग (मुंबई): प्रारंभिक आधुनिक गगनचुंबी संरचना; इस्पात और कांच का अग्रभाग", "type": "leaf"}
                ]}
            ]
        else:
            return [
                {"label": "Iconic Post-Independence Landmarks", "type": "branch", "date": "Landmarks", "children": [
                    {"label": "Lotus Temple (Delhi): Baha'i House of Worship; constructed with white marble flower-petal vaults", "type": "leaf"},
                    {"label": "LIC Building (Mumbai): Early modernist high-rise structure using structural steel grids and curtain walls", "type": "leaf"}
                ]}
            ]

    # Fallback
    else:
        if is_hindi:
            return [
                {"label": "वास्तुकला सामान्य", "type": "branch", "date": "मूर्तिकला व मंदिर", "children": [
                    {"label": "नागर, द्रविड़ और वेसर शैलियों का क्रमिक विकास; दक्कन और सल्तनत स्थापत्य शैलियाँ", "type": "leaf"},
                    {"label": "औपनिवेशिक काल और आधुनिक स्वतंत्र भारत की वास्तुकला प्रवृत्तियां", "type": "leaf"}
                ]}
            ]
        else:
            return [
                {"label": "Architecture Overview", "type": "branch", "date": "Architecture", "children": [
                    {"label": "Evolution of classical temple styles (Nagara/Dravida) and Islamic arcuate constructions", "type": "leaf"},
                    {"label": "Encompasses colonial Gothic revivals, Lutyens' layouts, and post-independence modernist buildings", "type": "leaf"}
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
