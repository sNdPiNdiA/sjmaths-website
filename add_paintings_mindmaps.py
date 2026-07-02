#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import re
import json

BASE = r"upsc/art_and_culture/Paintings"

def get_clean_title(folder_name):
    title = folder_name.replace('-', ' ')
    words = []
    acronyms = {'upsc', 'ad', 'bc', 'ii', 'iii', 'pag'}
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

    # 1. Cave Paintings
    if 'cave-paintings' in fl:
        if is_hindi:
            return [
                {"label": "प्रागैतिहासिक शैलचित्र (भीमबेटका)", "type": "branch", "date": "भीमबेटका", "children": [
                    {"label": "पुरापाषाण व मध्यपाषाण: बड़ी आकृतियां, शिकार के दृश्य; प्राकृतिक खनिज रंगों (गेरू, सफेद, हरा) का प्रयोग", "type": "leaf"},
                    {"label": "भीमबेटका (MP): 700 से अधिक रॉक शेल्टर; वी.एस. वाकणकर द्वारा खोजे गए; दैनिक जीवन, नृत्य और पशु आकृतियों का चित्रण", "type": "leaf"}
                ]},
                {"label": "मध्यपाषाण कालीन लघुचित्र", "type": "branch", "date": "लघुचित्र", "children": [
                    {"label": "आकार में कमी: चित्रों का आकार छोटा हुआ; व्यक्तिगत शिकार के स्थान पर सामूहिक शिकार और जाल बिछाने का चित्रण", "type": "leaf"},
                    {"label": "पारिवारिक जीवन: महिलाओं को अनाज पीसते, भोजन पकाते और बच्चों के साथ खेलते दिखाया गया है", "type": "leaf"}
                ]}
            ]
        else:
            return [
                {"label": "Prehistoric Rock Art (Bhimbetka)", "type": "branch", "date": "Bhimbetka", "children": [
                    {"label": "Upper Paleo & Meso: Depicts animals (bison, tiger), communal hunting, and rituals using green/red ochre (Geru)", "type": "leaf"},
                    {"label": "Discovery: Found by V.S. Wakankar in 1957; displays continuous cultural evolution through layers of paintings", "type": "leaf"}
                ]},
                {"label": "Mesolithic Stylistic Shift", "type": "branch", "date": "Shift", "children": [
                    {"label": "Scale reduction: Paintings became smaller (micros) with dynamic outlines and stylized human stick figures", "type": "leaf"},
                    {"label": "Social Scenes: Portrays family life, gathering wild honey, childbirth, burials, and musical instruments", "type": "leaf"}
                ]}
            ]

    # 2. Tradition of Mural Paintings in India
    elif 'tradition-of-mural-paintings' in fl:
        if is_hindi:
            return [
                {"label": "शास्त्रीय भित्तिचित्र (उत्तर व दक्कन)", "type": "branch", "date": "शास्त्रीय", "children": [
                    {"label": "अजंता (बौद्ध): चूने-गोबर के पलस्तर पर भित्तिचित्र (Tempera); बोधिसत्व पद्मपाणि और वज्रपाणि, मरणासन्न राजकुमारी का चित्र", "type": "leaf"},
                    {"label": "बाघ गुफाएं (MP): अजंता जैसी ही तकनीक, लेकिन चित्र धर्मनिरपेक्ष हैं (शासक, संगीतकार और जुलूस)", "type": "leaf"}
                ]},
                {"label": "दक्षिणी भित्तिचित्र परंपराएं", "type": "branch", "date": "दक्षिण भारत", "children": [
                    {"label": "सित्तनवासन (TN): पल्लव/पांड्य काल की जैन गुफा; कमल तालाब, नृत्य करती अप्सराओं का सजीव चित्रण", "type": "leaf"},
                    {"label": "लेपाक्षी (AP): विजयनगर काल; शिव के विभिन्न रूपों का अंकन, तीखी बाह्य रेखाएं और कोणीय आकृतियां", "type": "leaf"},
                    {"label": "बादामी (KA): चालुक्य काल; वैष्णव विषयों पर आधारित सबसे पुराने हिंदू गुफा भित्तिचित्र", "type": "leaf"}
                ]}
            ]
        else:
            return [
                {"label": "Classical Murals (North & Deccan)", "type": "branch", "date": "Classical", "children": [
                    {"label": "Ajanta (Buddhist): Plaster base painted with tempera; features Bodhisattva Padmapani and the Dying Princess", "type": "leaf"},
                    {"label": "Bagh Caves (MP): Secular lifestyle murals (music, dance, horsemen) despite Buddhist architectural context", "type": "leaf"}
                ]},
                {"label": "Southern Mural Traditions", "type": "branch", "date": "South", "children": [
                    {"label": "Sittanavasal (TN): Jain cave featuring dynamic frescos of lotus ponds, dancing nymphs, and animals", "type": "leaf"},
                    {"label": "Lepakshi (AP): Vijayanagar style, characterized by dark profile outlines, three-quarter profiles, and epic themes", "type": "leaf"},
                    {"label": "Badami (Karnataka): Chalukyan murals inside Cave 3, depicting earliest surviving Hindu cave paintings", "type": "leaf"}
                ]}
            ]

    # 3. Tradition of Miniature Paintings in India
    elif 'tradition-of-miniature-paintings' in fl:
        if is_hindi:
            return [
                {"label": "प्रारंभिक मध्ययुगीन पांडुलिपि कला", "type": "branch", "date": "ताड़पत्र", "children": [
                    {"label": "पाल शैली (बंगाल): 11वीं-12वीं शताब्दी; ताड़ के पत्तों पर वज्रयान बौद्ध देवी-देवताओं के लघुचित्र; कोमल रेखाएं", "type": "leaf"},
                    {"label": "अपभ्रंश/पश्चिमी शैली (गुजरात): जैन ग्रंथ (कल्पसूत्र); उभरी हुई आँखें (protruding eyes), कोणीय चेहरे, सोने-चांदी की स्याही", "type": "leaf"}
                ]},
                {"label": "सल्तनत संक्रमण काल", "type": "branch", "date": "संक्रमण", "children": [
                    {"label": "निअमतनामा: मांडू (मालवा) के सुल्तान के लिए लिखी गई पाक कला की सचित्र पुस्तक; भारत-फारसी शैली का संगम", "type": "leaf"},
                    {"label": "विशेषताएँ: स्वदेशी रंगों और फारसी परिप्रेक्ष्य/मेहराबों का एकीकरण, जिसने मुग़ल शैली का मार्ग प्रशस्त किया", "type": "leaf"}
                ]}
            ]
        else:
            return [
                {"label": "Early Manuscript Miniatures", "type": "branch", "date": "Manuscripts", "children": [
                    {"label": "Pala School: 11th-12th c. palm-leaf paintings illustrating Vajrayana Buddhist texts; features graceful sinuous lines", "type": "leaf"},
                    {"label": "Western Indian School: Jain texts (Kalpasutra); characterized by angular faces, protruding eyes, and gold inks", "type": "leaf"}
                ]},
                {"label": "Sultanate Transition Phase", "type": "branch", "date": "Sultanate", "children": [
                    {"label": "Nimatnama: Illustrated book of recipes at Mandu, fusing Persian shapes with Indian red/saffron colors", "type": "leaf"},
                    {"label": "Pre-Mughal synthesis: Shows integration of Persian landscape borders with indigenous flat figures", "type": "leaf"}
                ]}
            ]

    # 4. Mughal Painting
    elif 'mughal-painting' in fl:
        if is_hindi:
            return [
                {"label": "स्थापना और विस्तार (हुमायूँ व अकबर)", "type": "branch", "date": "शुरुआत", "children": [
                    {"label": "हुमायूँ: फारसी चित्रकारों (मीर सैय्यद अली, ख्वाजा अब्दुस समद) को लाया, जिन्होंने मुगल चित्रशाला की नींव रखी", "type": "leaf"},
                    {"label": "अकबर: तस्वीरखाना (शाही चित्रशाला) की स्थापना की; हमजानामा, महाभारत (रज्मनामा) और अकबरनामा का सचित्र संकलन", "type": "leaf"},
                    {"label": "शैली: सामूहिक काम (एक चित्र पर कई कलाकार); त्रिविमीय प्रभाव (3D effect) और चमकदार रंगों का उपयोग", "type": "leaf"}
                ]},
                {"label": "चरमोत्कर्ष और ह्रास (जहाँगीर व शाहजहाँ)", "type": "branch", "date": "चरमोत्कर्ष", "children": [
                    {"label": "जहाँगीर: व्यक्तिगत चित्र, प्रकृति अध्ययन (उस्ताद मंसूर के साइबेरियन सारस, फूल); यूरोपीय प्रभाव (आभामंडल, छायांकन)", "type": "leaf"},
                    {"label": "शाहजहाँ: औपचारिक दरबारी दृश्य, सुनहरी बॉर्डर (हाशिया), और शाही भव्यता पर बल; पिएत्रा ड्यूरा जैसी सूक्ष्मता", "type": "leaf"},
                    {"label": "औरंगजेब: कला का संरक्षण समाप्त किया; चित्रकार क्षेत्रीय रियासतों (राजस्थान, पहाड़ी राज्यों) में पलायन कर गए", "type": "leaf"}
                ]}
            ]
        else:
            return [
                {"label": "Foundations & Workshops (Akbar)", "type": "branch", "date": "Akbar", "children": [
                    {"label": "Humayun's Return: Brought Persian masters Mir Sayyid Ali and Abdus Samad to Delhi, starting the atelier", "type": "leaf"},
                    {"label": "Akbari Tasvir Khana: Large-scale production; illustrated Hamzanama, Razmnama (Mahabharata), and Baburnama", "type": "leaf"},
                    {"label": "Synthesis: Combined Persian high-horizon vistas with Indian realism, active postures, and local colors", "type": "leaf"}
                ]},
                {"label": "Naturalism & Grandeur (Jahangir & Shah Jahan)", "type": "branch", "date": "Zenith", "children": [
                    {"label": "Jahangir: Shifted to single artist portraits and nature studies (Ustad Mansur's flora/fauna); added European halos", "type": "leaf"},
                    {"label": "Shah Jahan: Focus on formal court durbars, elaborate gold-filled borders (Hashiyas), and luxurious palettes", "type": "leaf"},
                    {"label": "Decline: Aurangzeb's religious orthodoxy led to dispersion of painters to Rajasthan and Pahari hills", "type": "leaf"}
                ]}
            ]

    # 5. Paintings in the Deccan
    elif 'paintings-in-the-deccan' in fl or 'deccan' in fl:
        if is_hindi:
            return [
                {"label": "दक्कनी चित्रकला की विशेषताएं", "type": "branch", "date": "दक्कन शैली", "children": [
                    {"label": "रंग योजना: गहरे, समृद्ध और चमकदार रंगों (नीला, लाल, सोना) का प्रचुर उपयोग; सुनहरी पहाड़ी पृष्ठभूमि", "type": "leaf"},
                    {"label": "मानव आकृति: लंबे, छरहरे शरीर वाले स्त्री-पुरुष; चेहरे पर फारसी और दक्कनी वस्त्रों का प्रभाव", "type": "leaf"}
                ]},
                {"label": "प्रमुख स्कूल और कृतियाँ", "type": "branch", "date": "स्कूल्स", "children": [
                    {"label": "बीजापुर: नजूम-अल-उलूम (खगोल विज्ञान ग्रंथ); इब्राहिम आदिल शाह द्वितीय का चित्रण (संगीत प्रेमी सुल्तान)", "type": "leaf"},
                    {"label": "अहमद नगर व गोलकुंडा: गोलकुंडा के चित्र समृद्ध आभूषणों और हरे-भरे परिदृश्य के लिए प्रसिद्ध हैं", "type": "leaf"}
                ]}
            ]
        else:
            return [
                {"label": "Deccani Aesthetic Features", "type": "branch", "date": "Deccan Style", "children": [
                    {"label": "Palette: Intense rich colors (lapis lazuli blue, gold, deep red) and golden sky backgrounds", "type": "leaf"},
                    {"label": "Slender Figures: Elongated human forms dressed in fine, transparent Deccani garments", "type": "leaf"}
                ]},
                {"label": "Sultanate Ateliers", "type": "branch", "date": "Schools", "children": [
                    {"label": "Bijapur: Najm-al-Ulum (astronomy atlas); patronized by Ibrahim Adil Shah II (portrayed playing veena)", "type": "leaf"},
                    {"label": "Ahmednagar & Golconda: Golconda miniatures show rich jewelry, local flora, and hybrid Persian elements", "type": "leaf"}
                ]}
            ]

    # 6. Miniature Painting in South India
    elif 'miniature-painting-in-south-india' in fl:
        if is_hindi:
            return [
                {"label": "तंजौर चित्रकला शैली", "type": "branch", "date": "तंजौर", "children": [
                    {"label": "विशेषताएँ: लकड़ी के तख्तों (Planks) पर चित्रण; शुद्ध सोने की परतों (Gold Leaf) का उपयोग", "type": "leaf"},
                    {"label": "सजावट: चित्रों में काँच के मोतियों, कीमती रत्नों और अर्ध-कीमती पत्थरों का जड़ाऊ काम; उभरी हुई आकृतियां (Gesso)", "type": "leaf"},
                    {"label": "विषय: मुख्य रूप से हिंदू धार्मिक विषय, विशेषकर बाल कृष्ण (माखन चोर रूप)", "type": "leaf"}
                ]},
                {"label": "मैसूर चित्रकला शैली", "type": "branch", "date": "मैसूर", "children": [
                    {"label": "विशेषताएँ: लकड़ी पर चिपकाए गए कागज पर चित्र; तंजौर की तुलना में शांत रंग और बारीक रेखाएं", "type": "leaf"},
                    {"label": "गेसो पेस्ट: जड़ाऊ काम के स्थान पर लेड व्हाइट और गोंद से बने पतले गेसो पेस्ट का उपयोग, जिस पर हल्की सोने की परत चढ़ती थी", "type": "leaf"}
                ]}
            ]
        else:
            return [
                {"label": "Thanjavur (Tanjore) School", "type": "branch", "date": "Tanjore", "children": [
                    {"label": "Technique: Done on wooden boards; characterized by high relief work using gesso paste (lead white)", "type": "leaf"},
                    {"label": "Embellishments: Incised gold leaf sheets, semi-precious glass beads, and stones decorating deities", "type": "leaf"},
                    {"label": "Subject: Dominated by images of baby Krishna (Balakrishna) in various playful forms", "type": "leaf"}
                ]},
                {"label": "Mysore Miniature School", "type": "branch", "date": "Mysore", "children": [
                    {"label": "Features: Delicate brushwork, muted natural colors, and complex iconographic descriptions on paper", "type": "leaf"},
                    {"label": "Gesso application: Thin gesso relief work with gold foil overlay, creating a flatter, more detailed finish", "type": "leaf"}
                ]}
            ]

    # 7. Regional Paintings (Rajasthani & Pahari)
    elif 'regional-paintings' in fl:
        if is_hindi:
            return [
                {"label": "राजस्थानी शैलियाँ (मेवाड़, किशनगढ़, बूंदी)", "type": "branch", "date": "राजस्थान", "children": [
                    {"label": "मेवाड़ शैली: सबसे पुरानी शैली; चटकीले लाल-पीले रंग; वैष्णव विषय (गीत गोविंद, भागवत पुराण)", "type": "leaf"},
                    {"label": "किशनगढ़ शैली: निहाल चंद द्वारा रचित 'बनी-ठनी' (भारतीय मोनालिसा); लंबी धनुषाकार आँखें, नुकीली ठुड्डी और नाक", "type": "leaf"},
                    {"label": "बूंदी व कोटा: हरे-भरे जंगलों, बादलों और शिकार के दृश्यों (कोटा में महिलाओं द्वारा शेर का शिकार) का सजीव चित्रण", "type": "leaf"}
                ]},
                {"label": "पहाड़ी शैलियाँ (बसोहली व कांगड़ा)", "type": "branch", "date": "पहाड़ी", "children": [
                    {"label": "बसोहली शैली: सबसे पुरानी पहाड़ी शैली; गहरे चटकीले रंग, चित्रों में चमक लाने के लिए बीटल विंग (भृंग पंख) का उपयोग", "type": "leaf"},
                    {"label": "कांगड़ा शैली: अत्यंत काव्यात्मक (Lyrical) शैली; शांत हल्के रंग, जयदेव के गीत गोविंद से प्रभावित राधा-कृष्ण चित्र", "type": "leaf"}
                ]}
            ]
        else:
            return [
                {"label": "Rajasthani Schools", "type": "branch", "date": "Rajasthan", "children": [
                    {"label": "Mewar school: Earliest school; characterized by direct flat coloring, deep red borders, and Ragamala paintings", "type": "leaf"},
                    {"label": "Kishangarh (Bani Thani): Painted by Nihal Chand; features exaggerated bow-like eyes, pointed chin, and high forehead", "type": "leaf"},
                    {"label": "Bundi & Kota: Kota features dramatic hunting scenes (including women hunting tigers); Bundi focuses on lush green trees", "type": "leaf"}
                ]},
                {"label": "Pahari Schools", "type": "branch", "date": "Pahari", "children": [
                    {"label": "Basohli style: Bold monochrome backgrounds, intense expressions, and paste of real beetle wings for jewelry luster", "type": "leaf"},
                    {"label": "Kangra School: Lyrical and delicate; inspired by Vaishnavite Bhakti literature; soft green shades for hills", "type": "leaf"}
                ]}
            ]

    # 8. Modern Paintings
    elif 'modern-paintings' in fl:
        if is_hindi:
            return [
                {"label": "राजा रवि वर्मा और कंपनी शैली", "type": "branch", "date": "कंपनी शैली", "children": [
                    {"label": "कंपनी स्कूल: ब्रिटिश अधिकारियों के लिए स्थानीय भारतीय जनजीवन, डाकिए, सब्जी विक्रेता का यथार्थवादी चित्रण", "type": "leaf"},
                    {"label": "राजा रवि वर्मा: पश्चिमी तेल चित्रण (Oil Painting) और यथार्थवादी अकादमिक शैली का भारतीय हिंदू देवियों (लक्ष्मी, सरस्वती, शकुंतला) के साथ एकीकरण", "type": "leaf"}
                ]},
                {"label": "बंगाल स्कूल और स्वदेशी आंदोलन", "type": "branch", "date": "बंगाल स्कूल", "children": [
                    {"label": "अवनींद्रनाथ टैगोर: पश्चिमी शैली का विरोध; जापानी वाश (Wash) पेंटिंग को अपनाया; प्रसिद्ध 'भारत माता' का चित्र", "type": "leaf"},
                    {"label": "नंदलाल बोस: हरिपुरा कांग्रेस के पोस्टर बनाए (सच्चा ग्रामीण जीवन); अजंता गुफा चित्रों के रेखाचित्र तैयार किए", "type": "leaf"}
                ]}
            ]
        else:
            return [
                {"label": "Colonial Period & Raja Ravi Varma", "type": "branch", "date": "Colonial", "children": [
                    {"label": "Company Paintings: Commissioned by EIC officers; captures Indian professions, flora, fauna with European perspective", "type": "leaf"},
                    {"label": "Raja Ravi Varma: Blended Western oil painting on canvas with Indian mythology (Shakuntala, Harischandra)", "type": "leaf"}
                ]},
                {"label": "Bengal School & Nationalist Revival", "type": "branch", "date": "Bengal", "children": [
                    {"label": "Abanindranath Tagore: Rejected oil; adopted Japanese wash painting techniques; painted iconic 'Bharat Mata'", "type": "leaf"},
                    {"label": "Nandalal Bose: Designed Haripura Congress posters depicting rural artisans; illustrated original Constitution of India", "type": "leaf"}
                ]}
            ]

    # 9. Contemporary Paintings
    elif 'contemporary-paintings' in fl:
        if is_hindi:
            return [
                {"label": "प्रोग्रेसिव आर्टिस्ट्स ग्रुप (PAG)", "type": "branch", "date": "PAG", "children": [
                    {"label": "गठन: 1947 में मुंबई में एफ.एन. सूजा, एस.एच. रजा, एम.एफ. हुसैन द्वारा स्थापित", "type": "leaf"},
                    {"label": "सिद्धांत: बंगाल स्कूल और औपनिवेशिक यथार्थवाद दोनों को खारिज किया; पश्चिमी आधुनिक अमूर्त कला (Cubism) को भारतीय प्रतीकों से मिलाया", "type": "leaf"},
                    {"label": "कलाकार: एम.एफ. हुसैन (दौड़ते घोड़े), एस.एच. रजा (बिंदु चित्र श्रृंखला), एफ.एन. सूजा (तीक्ष्ण अमूर्त चेहरे)", "type": "leaf"}
                ]},
                {"label": "लोक कला का आधुनिक एकीकरण", "type": "branch", "date": "लोक कला", "children": [
                    {"label": "जामिनी राय: बंगाल की कालीघाट पट कला और संथाल लोक कला को अपनाया; सपाट चमकीले रंगों और मोटी रेखाओं का प्रयोग", "type": "leaf"}
                ]}
            ]
        else:
            return [
                {"label": "Progressive Artists' Group", "type": "branch", "date": "Bombay PAG", "children": [
                    {"label": "Formation: Est. in Bombay in 1947 by F.N. Souza, S.H. Raza, M.F. Husain, and K.H. Ara", "type": "leaf"},
                    {"label": "Philosophy: Broke away from Bengal School sentimentality; combined international modernism (Cubism) with Indian ethos", "type": "leaf"},
                    {"label": "Key Artists: Raza (celebrated Bindu series), Husain (powerful dynamic horses), and Souza (distorted figures)", "type": "leaf"}
                ]},
                {"label": "Modern Folk Adaptations", "type": "branch", "date": "Folk", "children": [
                    {"label": "Jamini Roy: Rediscovered Kalighat scroll styles and Santhal tribals; painted with flat earthy tempera lines", "type": "leaf"}
                ]}
            ]

    # Fallback
    else:
        if is_hindi:
            return [
                {"label": "चित्रकला सामान्य", "type": "branch", "date": "चित्रकला", "children": [
                    {"label": "भीमबेटका के प्रागैतिहासिक चित्रों से लेकर शास्त्रीय भित्तिचित्रों (अजंता, लेपाक्षी) का इतिहास", "type": "leaf"},
                    {"label": "मध्यकालीन मुग़ल, दक्कन व राजस्थानी लघुचित्र और आधुनिक राष्ट्रवादी चित्रकला आंदोलन", "type": "leaf"}
                ]}
            ]
        else:
            return [
                {"label": "Paintings Overview", "type": "branch", "date": "Paintings", "children": [
                    {"label": "Traces history from prehistoric cave art (Bhimbetka) to classical temple frescoes", "type": "leaf"},
                    {"label": "Covers medieval Mughal/Deccani miniature developments and post-independence modernist art groups", "type": "leaf"}
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
