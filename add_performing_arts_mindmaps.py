#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import re
import json

BASE = r"upsc/art_and_culture/Performing-Arts"

def get_clean_title(folder_name):
    title = folder_name.replace('-', ' ')
    words = []
    acronyms = {'upsc', 'ad', 'bc', 'ii', 'iii', 'ipta', 'nsd'}
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

    # 1. Music Classical Indian Music (History & Evolution)
    if fl == 'music-classical-indian-music':
        if is_hindi:
            return [
                {"label": "शास्त्रीय संगीत की उत्पत्ति", "type": "branch", "date": "सामवेद", "children": [
                    {"label": "सामवेद: भारतीय संगीत का मूल स्रोत; संगीतमय मंत्रोच्चार का संकलन", "type": "leaf"},
                    {"label": "भरत का नाट्यशास्त्र: गंधर्व वेद (संगीत) का प्रारंभिक शास्त्रीय पाठ", "type": "leaf"}
                ]}
            ]
        else:
            return [
                {"label": "Origins of Classical Music", "type": "branch", "date": "Roots", "children": [
                    {"label": "Samaveda Chants: Roots of melodic singing and early scale definitions", "type": "leaf"},
                    {"label": "Natya Shastra: Written by Bharata Muni, laying down the grammatical rules of classical Gandharva music", "type": "leaf"}
                ]}
            ]

    # 2. Music Main Pillars of Indian Music (Swara, Raga, Tala)
    elif fl == 'music-main-pillars-of-indian-music':
        if is_hindi:
            return [
                {"label": "भारतीय संगीत के मुख्य स्तंभ", "type": "branch", "date": "संगीत तत्व", "children": [
                    {"label": "स्वर: सात बुनियादी संगीत सुर (स, रे, ग, म, प, ध, नि); श्रुति (22 सूक्ष्म सुर)", "type": "leaf"},
                    {"label": "राग: मधुर ढांचा जो विशिष्ट भावना उत्पन्न करता है; समय सिद्धांत (जैसे भोर में राग भैरव, शाम को राग यमन)", "type": "leaf"},
                    {"label": "ताल: आवर्ती लयबद्ध चक्र (जैसे तीनताल - 16 मात्राएँ, एकताल - 12 मात्राएँ)", "type": "leaf"}
                ]}
            ]
        else:
            return [
                {"label": "Three Pillars of Indian Music", "type": "branch", "date": "Pillars", "children": [
                    {"label": "Swara: Seven basic notes (Sa, Re, Ga, Ma, Pa, Dha, Ni) and 22 microtones (Shrutis)", "type": "leaf"},
                    {"label": "Raga: Melodic framework with specific rules, evoking emotions; bound by time-theory of day/night", "type": "leaf"},
                    {"label": "Tala: Rhythmic cycles measuring musical time, managed by percussion instruments", "type": "leaf"}
                ]}
            ]

    # 3. Hindustani Music
    elif fl == 'music-hindustani-music':
        if is_hindi:
            return [
                {"label": "उत्पत्ति और प्रभाव", "type": "branch", "date": "उत्तर भारत", "children": [
                    {"label": "फारसी प्रभाव: अमीर खुसरो द्वारा दिल्ली सल्तनत काल में फारसी और अरबी तत्वों का समन्वय", "type": "leaf"},
                    {"label": "विशेषता: स्वर के सटीक गायन के स्थान पर गायन के दौरान राग के विस्तार और लचीलेपन (improvisation) पर जोर", "type": "leaf"}
                ]},
                {"label": "गायन शैलियाँ", "type": "branch", "date": "शैलियाँ", "children": [
                    {"label": "ध्रुपद: सबसे प्राचीन और गंभीर शैली; संस्कृत मंत्रोच्चार; स्वामी हरिदास, तानसेन", "type": "leaf"},
                    {"label": "ख्याल: अधिक लचीली और अलंकृत शैली; उर्दू/ब्रजभाषा बंदिश; द्रुत और विलंबित लय", "type": "leaf"},
                    {"label": "ठुमरी: अर्ध-शास्त्रीय श्रृंगार रस प्रधान शैली; राधा-कृष्ण प्रेम विषय; वाजिद अली शाह", "type": "leaf"}
                ]}
            ]
        else:
            return [
                {"label": "Origin & Characteristics", "type": "branch", "date": "North", "children": [
                    {"label": "Perso-Arabic synthesis: Shaped by Amir Khusrau introducing new ragas and Sufi devotional singing", "type": "leaf"},
                    {"label": "Improvisation: Emphasizes vocal elaboration within ragas over rigid adherence to fixed compositions", "type": "leaf"}
                ]},
                {"label": "Major Vocal Styles", "type": "branch", "date": "Genres", "children": [
                    {"label": "Dhrupad: Oldest style; majestic and spiritual; emphasizes breath control; patronized by Akbar (Tansen)", "type": "leaf"},
                    {"label": "Khayal: Romantic and ornamental style; uses fast tempos (Drut) and decorative trills (Taans)", "type": "leaf"},
                    {"label": "Thumri: Semi-classical style centered on erotic-mystic themes of Radha-Krishna; popularized in Avadh", "type": "leaf"}
                ]}
            ]

    # 4. Carnatic Music
    elif fl == 'music-carnatic-music':
        if is_hindi:
            return [
                {"label": "मूल सिद्धांत और विशेषताएँ", "type": "branch", "date": "दक्षिण भारत", "children": [
                    {"label": "पूर्णतः स्वदेशी: बिना किसी बाहरी या फारसी प्रभाव के विशुद्ध रूप से विकसित प्रणाली", "type": "leaf"},
                    {"label": "संरचनात्मक स्थिरता: रचना (कृति) पर आधारित; गायन में आलाप की तुलना में तालबद्धता पर अधिक बल", "type": "leaf"},
                    {"label": "मेलकर्ता व्यवस्था: वेंकटमखिन द्वारा प्रतिपादित 72 जनक रागों (मेलकर्ता) की वैज्ञानिक वर्गीकरण प्रणाली", "type": "leaf"}
                ]},
                {"label": "संगीत की त्रिमूर्ति", "type": "branch", "date": "त्रिमूर्ति", "children": [
                    {"label": "त्यागराज: राम भक्ति पर आधारित सैकड़ों भक्ति गीतों (कीर्तन) के रचयिता", "type": "leaf"},
                    {"label": "मुथुस्वामी दीक्षितर: संस्कृत रचनाकार; रागों के शास्त्रीय सौंदर्य के लिए प्रसिद्ध", "type": "leaf"},
                    {"label": "श्यामा शास्त्री: जटिल तालबद्ध पैटर्न और देवी कामाक्षी की आराधना के संगीतकार", "type": "leaf"}
                ]}
            ]
        else:
            return [
                {"label": "Core Principles & Structure", "type": "branch", "date": "South", "children": [
                    {"label": "Indigenous style: Retained original Sanskrit-Dravidian roots without Perso-Arabic influence", "type": "leaf"},
                    {"label": "Composition focus: Centered on written lyrics (Kritis); features strict adherence to Tala beats", "type": "leaf"},
                    {"label": "Melakarta system: Scientific scheme of 72 parent ragas formulated by Venkatamakhin", "type": "leaf"}
                ]},
                {"label": "Trinity of Carnatic Music", "type": "branch", "date": "Trinity", "children": [
                    {"label": "Tyagaraja: Famed composer of devotional Telugu kritis, establishing the Pancharatna Kritis", "type": "leaf"},
                    {"label": "Muthuswami Dikshitar: Sanskrit scholar known for detailed depictions of ragas and temples", "type": "leaf"},
                    {"label": "Syama Sastri: Oldest of the trinity, noted for complex rhythmic structures (Tala) and Tamil compositions", "type": "leaf"}
                ]}
            ]

    # 5. Music Gharanas
    elif fl == 'music-different-gharanas-or-schools':
        if is_hindi:
            return [
                {"label": "घराना प्रथा का विकास", "type": "branch", "date": "परंपरा", "children": [
                    {"label": "गुरु-शिष्य परंपरा: मुगल दरबारों के पतन के बाद क्षेत्रीय रियासतों में विकसित गायन की विशिष्ट शैलियाँ", "type": "leaf"},
                    {"label": "ग्वालियर घराना: सबसे पुराना और बुनियादी घराना; सरल राग प्रस्तुति और बंदिश की स्पष्टता", "type": "leaf"}
                ]},
                {"label": "अन्य प्रमुख घराने", "type": "branch", "date": "स्कूल्स", "children": [
                    {"label": "किराना घराना: उस्ताद अब्दुल करीम खान; स्वरों की शुद्धता और करुण रस की प्रधानता पर बल", "type": "leaf"},
                    {"label": "आगरा घराना: नोम-तोम आलाप और लयकारी (लय के साथ खेल) के लिए प्रसिद्ध", "type": "leaf"},
                    {"label": "पटियाला घराना: बड़े गुलाम अली खान; तेज तान और ठुमरी गायन में महारत", "type": "leaf"}
                ]}
            ]
        else:
            return [
                {"label": "Concept of Gharanas", "type": "branch", "date": "Lineage", "children": [
                    {"label": "Guru-Shishya Parampara: Lineages of instruction developing regional styles after Mughal decline", "type": "leaf"},
                    {"label": "Gwalior Gharana: The oldest style; focuses on simple raga presentation, clear pronunciation of words", "type": "leaf"}
                ]},
                {"label": "Key Vocal Schools", "type": "branch", "date": "Gharanas", "children": [
                    {"label": "Kirana Gharana: Founded by Abdul Karim Khan; prioritizes microtonal swara tuning and emotional depth", "type": "leaf"},
                    {"label": "Agra Gharana: Stresses nom-tom alap, powerful masculine voice projections, and complex rhythm play", "type": "leaf"},
                    {"label": "Patiala Gharana: Promoted by Bade Ghulam Ali Khan; noted for blistering taans and classical thumri", "type": "leaf"}
                ]}
            ]

    # 6. Music Forms (Dhrupad, Khayal, Thumri, etc.)
    elif fl == 'music-forms-of-indian-music':
        if is_hindi:
            return [
                {"label": "शास्त्रीय गायन रूप", "type": "branch", "date": "वर्गीकरण", "children": [
                    {"label": "ध्रुपद: संस्कृत मंत्रोच्चार पर आधारित भक्ति गायन; वीणा और पखावज का प्रयोग; गंभीर रस", "type": "leaf"},
                    {"label": "ख्याल: शाब्दिक अर्थ 'विचार'; कल्पनाशीलता, जटिल तान और आलाप की बहुतायत", "type": "leaf"}
                ]},
                {"label": "अर्ध-शास्त्रीय रूप", "type": "branch", "date": "गीत", "children": [
                    {"label": "ठुमरी: श्रृंगार रस प्रधान गीत; ब्रजभाषा; हाव-भाव और गायकी पर बल; गिरिजा देवी", "type": "leaf"},
                    {"label": "टप्पा: पंजाब के ऊंट चालकों के लोकगीतों से विकसित; तेज और घुमावदार तानों की भरमार", "type": "leaf"},
                    {"label": "तराना: निरर्थक शब्दों (जैसे तोम, ता, ना, दानी) का प्रयोग, जो ताल की लय बढ़ाने के लिए गाए जाते हैं", "type": "leaf"}
                ]}
            ]
        else:
            return [
                {"label": "Classical Forms (Dhrupad & Khayal)", "type": "branch", "date": "Classical", "children": [
                    {"label": "Dhrupad: Devotional Sanskrit hymns; lacks ornamentation; accompanied by Pakhawaj drum", "type": "leaf"},
                    {"label": "Khayal: Means 'imagination'; features flexible improvisations, highly decorated vocal patterns (Taans)", "type": "leaf"}
                ]},
                {"label": "Light/Semi-Classical Forms", "type": "branch", "date": "Semi-Classical", "children": [
                    {"label": "Thumri: Expressive lyrical songs in Braj bhasha; focuses on romance and separated lovers", "type": "leaf"},
                    {"label": "Tappa: Derived from Punjabi camel riders' tunes; features fast, zigzag vocal ornaments", "type": "leaf"},
                    {"label": "Tarana: Syllable-based songs (Tana, Dere) without words, showcasing technical speed of singers", "type": "leaf"}
                ]}
            ]

    # 7. Folk Music
    elif fl == 'music-folk-music':
        if is_hindi:
            return [
                {"label": "उत्तर व पश्चिम भारत का लोक संगीत", "type": "branch", "date": "पश्चिम", "children": [
                    {"label": "मांड (राजस्थान): राजपूत वीरता और स्वागत गीत (जैसे केसरिया बालम); मांड गायकी शैली", "type": "leaf"},
                    {"label": "लमन (हिमाचल): प्रेम गीत जो वादियों में गूँजते हैं; लड़ीदार लय", "type": "leaf"}
                ]},
                {"label": "पूर्व व मध्य भारत का संगीत", "type": "branch", "date": "पूर्व", "children": [
                    {"label": "बाउल (बंगाल): रहस्यवादी संगीत परंपरा (एकतारा का प्रयोग); रवींद्रनाथ टैगोर इससे प्रभावित थे", "type": "leaf"},
                    {"label": "पोवाड़ा (महाराष्ट्र): शिवाजी महाराज के शौर्य गाथाओं का गान करने वाले वीर रस गीत", "type": "leaf"}
                ]}
            ]
        else:
            return [
                {"label": "Northern & Western Folk Music", "type": "branch", "date": "North/West", "children": [
                    {"label": "Maand (Rajasthan): Aristocratic ballad tradition celebrating historic events, e.g. Kesariya Balam", "type": "leaf"},
                    {"label": "Laman (Himachal): Love songs sung by hill communities, characterized by long sustained notes", "type": "leaf"}
                ]},
                {"label": "Eastern & Southern Folk Music", "type": "branch", "date": "East/South", "children": [
                    {"label": "Baul (Bengal): Mystic songs sung by wandering minstrels, using Ektara and promoting humanist philosophy", "type": "leaf"},
                    {"label": "Powada (Maharashtra): Narrative ballads highlighting the military triumphs of Chhatrapati Shivaji", "type": "leaf"}
                ]}
            ]

    # 8. Musical Instruments
    elif fl == 'music-musical-instruments':
        if is_hindi:
            return [
                {"label": "तत और सुषिर वाद्य (हवा व तार वाले)", "type": "branch", "date": "वाद्य यंत्र", "children": [
                    {"label": "तत वाद्य (तंतु वाद्य): तारों के कंपन से बजने वाले; जैसे सितार, सरोद, सारंगी, वीणा", "type": "leaf"},
                    {"label": "सुषिर वाद्य (वायु वाद्य): फूंक मारकर बजाए जाने वाले; जैसे बांसुरी, शहनाई, शंख", "type": "leaf"}
                ]},
                {"label": "अवनद्ध और घन वाद्य (आघात वाले)", "type": "branch", "date": "आघात", "children": [
                    {"label": "अवनद्ध वाद्य (चर्म वाद्य): चमड़े से ढके ड्रम; जैसे तबला, मृदंगम, पखावज, ढोलक", "type": "leaf"},
                    {"label": "घन वाद्य (ठोस वाद्य): धातु या लकड़ी से बने बिना तार के वाद्य; जैसे मंजीरा, घटम (मिट्टी का घड़ा), झांझ", "type": "leaf"}
                ]}
            ]
        else:
            return [
                {"label": "Tata & Sushira Vadya", "type": "branch", "date": "Instruments", "children": [
                    {"label": "Tata Vadya (Chordophones): Stringed instruments played with bows or plucks, e.g. Sitar, Sarod, Veena", "type": "leaf"},
                    {"label": "Sushira Vadya (Aerophones): Wind instruments sounded by column of air, e.g. Bansuri, Shehnai, Nadaswaram", "type": "leaf"}
                ]},
                {"label": "Avanaddha & Ghana Vadya", "type": "branch", "date": "Percussion", "children": [
                    {"label": "Avanaddha Vadya (Membranophones): Drums covered with animal skin membranes, e.g. Tabla, Mridangam, Pakhawaj", "type": "leaf"},
                    {"label": "Ghana Vadya (Idiophones): Solid percussion instruments made of metal or clay, e.g. Ghatam, Manjira", "type": "leaf"}
                ]}
            ]

    # 9. Music Institutions
    elif fl == 'music-institutions-related-to-music-in-india':
        if is_hindi:
            return [
                {"label": "राष्ट्रीय संगीत अकादमियाँ", "type": "branch", "date": "संस्थान", "children": [
                    {"label": "संगीत नाटक अकादमी (1953): संगीत, नृत्य और नाटक के संरक्षण की राष्ट्रीय अकादमी; राष्ट्रपति द्वारा पुरस्कार प्रदान किए जाते हैं", "type": "leaf"},
                    {"label": "भातखंडे संगीत संस्थान (लखनऊ): पंडित विष्णु नारायण भातखंडे द्वारा स्थापित; शास्त्रीय संगीत की राष्ट्रीय स्वरलिपि (notation) का विकास किया", "type": "leaf"},
                    {"label": "मद्रास संगीत अकादमी: दक्षिण भारत में कर्नाटक संगीत के प्रचार और संरक्षण का मुख्य केंद्र", "type": "leaf"}
                ]}
            ]
        else:
            return [
                {"label": "National Music Academies", "type": "branch", "date": "Academies", "children": [
                    {"label": "Sangeet Natak Akademi: Est. 1953; apex body preserving performing arts; administers National Awards", "type": "leaf"},
                    {"label": "Bhatkhande Music Institute: Created by Pandit V.N. Bhatkhande; pioneered standardization of notation systems", "type": "leaf"},
                    {"label": "Madras Music Academy: Key institute in South India organizing the annual December Music Festival", "type": "leaf"}
                ]}
            ]

    # 10. Classical Dances (Dances-Eight-Classical-Dance-Forms)
    elif fl == 'dances-eight-classical-dance-forms-in-india':
        if is_hindi:
            return [
                {"label": "दक्षिण व पूर्व भारतीय शास्त्रीय नृत्य", "type": "branch", "date": "शास्त्रीय नृत्य", "children": [
                    {"label": "भरतनाट्यम (TN): देवदासी परंपरा; 'अग्नि नृत्य'; एकल कलाकार (एकाहार्य); चिदंबरम मंदिर के तोरणों पर चित्र", "type": "leaf"},
                    {"label": "कथकली (केरल): विशाल मुखौटा और हरा/लाल रंग का मेकअप; अच्छाई-बुराई की लड़ाई; आँखों की हरकत (भ्रू संचालन)", "type": "leaf"},
                    {"label": "कुचिपुड़ी (AP): पीतल की थाली के किनारों पर पैर रखकर नृत्य (तरंगम); भागवत मेला नाटक परंपरा", "type": "leaf"},
                    {"label": "ओडिसी (ओडिशा): त्रिभंग मुद्रा (शरीर के तीन घुमाव); पानी का तत्व (जल तत्व); जगन्नाथ मंदिर से संबंध", "type": "leaf"}
                ]},
                {"label": "उत्तर व पूर्वोत्तर के शास्त्रीय नृत्य", "type": "branch", "date": "नृत्य रूप", "children": [
                    {"label": "कथक (UP): 'कथा' कहने की कला; चक्कर (स्पिन), तीव्र पदचाल (ततकार) और जुगलबंदी (तबले के साथ)", "type": "leaf"},
                    {"label": "सत्रिया (असम): वैष्णव संतों (शंकरदेव) द्वारा सत्रीय मठों में शुरू किया गया; कृष्ण कथाएँ", "type": "leaf"},
                    {"label": "मणिपुरी (मणिपुर): रासलीला; कोमल गतियाँ; घंटी के आकार की पोशाक (कुमिन); कोई पैरों की थाप नहीं", "type": "leaf"}
                ]}
            ]
        else:
            return [
                {"label": "Southern & Eastern Classical Dances", "type": "branch", "date": "Forms", "children": [
                    {"label": "Bharatanatyam (TN): Originally Sadir Attam by Devadasis; represents fire element; features Ekaharya (one dancer plays many roles)", "type": "leaf"},
                    {"label": "Kathakali (Kerala): Green face paint (heroic) and red/black (evil); story play based on epics; eye exercises", "type": "leaf"},
                    {"label": "Kuchipudi (Andhra): Features Tarangam (dancing on brass plate edges) and pot-balancing; Jalarigutta roots", "type": "leaf"},
                    {"label": "Odissi (Odisha): Characterized by Tribhanga posture (body bends at neck, waist, knee) and wet-cloth mimics", "type": "leaf"}
                ]},
                {"label": "Northern & North-Eastern Forms", "type": "branch", "date": "Dance Styles", "children": [
                    {"label": "Kathak (UP): Reciters of epics; highlights fast footwork (Tatkar), pirouettes, and jugalbandi with Tabla", "type": "leaf"},
                    {"label": "Sattriya (Assam): Introduced by Bhakti saint Sankaradeva inside Vaishnavite monasteries called Sattras", "type": "leaf"},
                    {"label": "Manipuri (Manipur): Centered on Raslila; soft swaying strides; dancers wear cylindrical skirts (Kumin)", "type": "leaf"}
                ]}
            ]

    # 11. Dances Concept of Dance in India (Natya Shastra Tandava/Lasya)
    elif fl == 'dances-concept-of-dance-in-india':
        if is_hindi:
            return [
                {"label": "तांडव और लास्य (मूल गतियाँ)", "type": "branch", "date": "नाट्यशास्त्र", "children": [
                    {"label": "तांडव: शिव का उग्र, ऊर्जावान और पुरुषोचित नृत्य; शक्ति और विनाश का प्रतीक", "type": "leaf"},
                    {"label": "लास्य: पार्वती का कोमल, सुंदर और स्त्रीत्व प्रधान नृत्य; प्रेम और श्रृंगार का प्रतीक", "type": "leaf"},
                    {"label": "शास्त्रीय अंग: नृत्त (शुद्ध लयबद्ध गतिविधि), नृत्य (अभिव्यंजक नृत्य), और नाट्य (नाटकीय अभिनय)", "type": "leaf"}
                ]}
            ]
        else:
            return [
                {"label": "Tandava vs Lasya", "type": "branch", "date": "Foundations", "children": [
                    {"label": "Tandava: Vigorous, energetic dance of Shiva representing cosmic destruction and strength", "type": "leaf"},
                    {"label": "Lasya: Graceful, delicate dance of Parvati representing love, beauty, and feminine charm", "type": "leaf"},
                    {"label": "Natya Triad: Nritta (pure technical dance), Nritya (interpretative mime), and Natya (dramatic plot)", "type": "leaf"}
                ]}
            ]

    # 12. Dances Concept of Ashta Nayika
    elif fl == 'dances-concept-of-ashta-nayika':
        if is_hindi:
            return [
                {"label": "अष्ट नायिका वर्गीकरण", "type": "branch", "date": "नायिका", "children": [
                    {"label": "अवस्थाएं: प्रेम की आठ अलग-अलग स्थितियों में नायिका का वर्गीकरण (जैसे वासवसज्जा - प्रिय का इंतजार करती हुई)", "type": "leaf"},
                    {"label": "विरहोत्कंठिता: नायक की अनुपस्थिति या देरी से तड़पती और व्याकुल नायिका", "type": "leaf"},
                    {"label": "अभिसारिका: सामाजिक बंधनों की परवाह किए बिना प्रिय से मिलने जाने वाली साहसी नायिका", "type": "leaf"}
                ]}
            ]
        else:
            return [
                {"label": "Eight Heroines (Ashta Nayika)", "type": "branch", "date": "Nayikas", "children": [
                    {"label": "Vasakasajja: The heroine who decorates her bedchamber, waiting expectantly for her lover's return", "type": "leaf"},
                    {"label": "Virahotkanthita: The distressed heroine suffering from separation due to her lover's delay", "type": "leaf"},
                    {"label": "Abhisarika: The bold heroine who sets aside social norms to go and meet her beloved in secret", "type": "leaf"}
                ]}
            ]

    # 13. Dances Rasa and Bhava
    elif fl == 'dances-rasa-and-bhava':
        if is_hindi:
            return [
                {"label": "रस और भाव (अभिव्यक्ति)", "type": "branch", "date": "नवरस", "children": [
                    {"label": "नवरस: नौ बुनियादी मानवीय भावनाएं (जैसे श्रृंगार-प्रेम, वीर-साहस, रौद्र-क्रोध, शांत-शांति)", "type": "leaf"},
                    {"label": "भाव: चेहरे की मांसपेशियों और आँखों द्वारा रस को व्यक्त करने की शारीरिक अवस्था; स्थायी और संचारी भाव", "type": "leaf"}
                ]}
            ]
        else:
            return [
                {"label": "Navarasa & Bhava Expressions", "type": "branch", "date": "Rasas", "children": [
                    {"label": "Navarasa: Nine primary emotional flavors (Shringara-love, Veera-heroism, Raudra-anger, Shanta-peace)", "type": "leaf"},
                    {"label": "Bhava: Emotional state portrayed through gestures (Mudras) and facial expressions (Abhinaya)", "type": "leaf"}
                ]}
            ]

    # 14. Dances Folk Dances
    elif fl == 'dances-folk-dances':
        if is_hindi:
            return [
                {"label": "प्रमुख भारतीय लोक नृत्य", "type": "branch", "date": "लोक नृत्य", "children": [
                    {"label": "कालबेलिया (राजस्थान): सपेरा जनजाति का नृत्य; नागिन जैसी गतियाँ; यूनेस्को अमूर्त विरासत", "type": "leaf"},
                    {"label": "छऊ नृत्य (बंगाल/झारखंड): अर्ध-शास्त्रीय मुखौटा नृत्य; युद्ध गतियाँ; सरायकेला, मयूरभंज और पुरुलिया शैलियाँ", "type": "leaf"},
                    {"label": "गरबा (गुजरात): मिट्टी के दीये वाले मटके (गर्भ दीप) के चारों ओर किया जाने वाला नवरात्र नृत्य", "type": "leaf"}
                ]}
            ]
        else:
            return [
                {"label": "Key Indian Folk Dances", "type": "branch", "date": "Folk", "children": [
                    {"label": "Kalbelia (Rajasthan): Snake charmers' dance featuring winding movements; inscribed in UNESCO heritage", "type": "leaf"},
                    {"label": "Chhau (East India): Semi-classical mask dance featuring martial steps; styles include Purulia and Mayurbhanj", "type": "leaf"},
                    {"label": "Garba (Gujarat): Navaratri dance performed around a perforated clay pot containing a lamp (Garbha Deep)", "type": "leaf"}
                ]}
            ]

    # 15. Dances Modern Dances
    elif fl == 'dances-modern-dances':
        if is_hindi:
            return [
                {"label": "आधुनिक नृत्य का विकास", "type": "branch", "date": "आधुनिकता", "children": [
                    {"label": "उदय शंकर: भारतीय आधुनिक नृत्य के जनक; भारतीय शास्त्रीय मुद्राओं को पश्चिमी बैले के साथ मिलाकर फ्यूजन शैली बनाई", "type": "leaf"},
                    {"label": "शांति बर्धन: उदय शंकर के सहयोगी; कठपुतली और पशु नृत्य शैलियों का उपयोग करके आधुनिक नृत्य नाटक विकसित किए", "type": "leaf"}
                ]}
            ]
        else:
            return [
                {"label": "Modern Dance Pioneers", "type": "branch", "date": "Modern", "children": [
                    {"label": "Uday Shankar: Father of Modern Indian Dance; created a new fusion style combining classical temple poses with Western ballet", "type": "leaf"},
                    {"label": "Shanti Bardhan: Introduced creative puppet-dances and animal movements in choreographing ballet dramas", "type": "leaf"}
                ]}
            ]

    # 16. Puppetry Shadow Puppets
    elif fl == 'puppetry-shadow-puppets':
        if is_hindi:
            return [
                {"label": "छाया कठपुतली (Shadow Puppets)", "type": "branch", "date": "छाया", "children": [
                    {"label": "थोलू बोमलता (AP): विशाल, रंगीन और पारदर्शी चमड़े की पुतलियाँ, जिन पर पौराणिक कथाएँ दिखाई जाती हैं", "type": "leaf"},
                    {"label": "रावणछाया (ओडिशा): हिरण की खाल से बनी बिना जोड़ (jointless) वाली पुतलियाँ; हिलते हुए पेड़ों की छाया पृष्ठभूमि", "type": "leaf"}
                ]}
            ]
        else:
            return [
                {"label": "Shadow Puppetry Traditions", "type": "branch", "date": "Shadow", "children": [
                    {"label": "Tholu Bommalata (Andhra): Large, translucent colored leather puppets cast on rear-lit screens", "type": "leaf"},
                    {"label": "Ravana Chhaya (Odisha): Made of single sheets of jointless deer skin, projecting solid shadows", "type": "leaf"}
                ]}
            ]

    # 17. Puppetry String Puppets
    elif fl == 'puppetry-string-puppets':
        if is_hindi:
            return [
                {"label": "धागा कठपुतली (String Puppets)", "type": "branch", "date": "धागा", "children": [
                    {"label": "कठपुतली (राजस्थान): लकड़ी की बनी पुतलियाँ, जो बिना पैरों के होती हैं; लंबी घाघरा-चोली व धागों से नियंत्रण", "type": "leaf"},
                    {"label": "कुंधई (ओडिशा): हल्के लकड़ी के जोड़दार पैर-हाथ; संगीत और ढोलक की संगत", "type": "leaf"}
                ]}
            ]
        else:
            return [
                {"label": "String Puppetry Traditions", "type": "branch", "date": "String", "children": [
                    {"label": "Kathputli (Rajasthan): Carved wooden puppets without legs, wearing flowing skirts, managed by strings", "type": "leaf"},
                    {"label": "Kundhei (Odisha): Jointed puppets made of light wood, showing detailed leg/hand movements", "type": "leaf"}
                ]}
            ]

    # 18. Sports Animal Sports
    elif fl == 'sports-animal-sports':
        if is_hindi:
            return [
                {"label": "पारंपरिक पशु खेल", "type": "branch", "date": "पशु खेल", "children": [
                    {"label": "जल्लीकट्टू (TN): मट्टू पोंगल पर किया जाने वाला सांडों को वश में करने का खेल", "type": "leaf"},
                    {"label": "कम्बाला (KA): कीचड़ भरे धान के खेतों में भैंसों की दौड़; तटीय कर्नाटक की परंपरा", "type": "leaf"}
                ]}
            ]
        else:
            return [
                {"label": "Traditional Animal Sports", "type": "branch", "date": "Animal Sports", "children": [
                    {"label": "Jallikattu (TN): Bull-taming event conducted during Mattu Pongal in rural Tamil districts", "type": "leaf"},
                    {"label": "Kambala (Karnataka): Buffalo race held in wet paddy fields of coastal Karnataka districts", "type": "leaf"}
                ]}
            ]

    # 19. Sports Forms of Traditional Martial Arts
    elif fl == 'sports-forms-of-traditional-martial-arts':
        if is_hindi:
            return [
                {"label": "भारतीय युद्ध कलाएँ (Martial Arts)", "type": "branch", "date": "युद्ध कला", "children": [
                    {"label": "कलरीपायट्टु (केरल): भारत की सबसे पुरानी युद्ध कला; उरुमी (लचीली तलवार) का प्रयोग; शारीरिक संतुलन", "type": "leaf"},
                    {"label": "गटका (पंजाब): सिख योद्धाओं (निहंग) द्वारा लाठियों और ढाल के साथ किया जाने वाला प्रदर्शन", "type": "leaf"},
                    {"label": "थांग-ता (मणिपुर): तलवार (थांग) और भाले (ता) का उपयोग करने वाला मणिपुरी युद्ध कौशल", "type": "leaf"},
                    {"label": "सिलांबम (TN): लंबी लाठी (स्टाफ) से लड़ने का तमिल कौशल; चोल राजाओं द्वारा संरक्षित", "type": "leaf"}
                ]}
            ]
        else:
            return [
                {"label": "Traditional Martial Arts", "type": "branch", "date": "Martial", "children": [
                    {"label": "Kalaripayattu (Kerala): One of the oldest martial arts; features flexible sword (Urumi) and defensive leaps", "type": "leaf"},
                    {"label": "Gatka (Punjab): Armed staff-fighting technique originated by Sikh warriors (Nihangs)", "type": "leaf"},
                    {"label": "Thang-Ta (Manipur): Combines sword (Thang) and spear (Ta) movements in ritualistic stances", "type": "leaf"},
                    {"label": "Silambam (Tamil Nadu): Staff-fencing art using bamboo sticks, dating back to Sangam literature", "type": "leaf"}
                ]}
            ]

    # 20. Sports Genesis of Martial Arts
    elif fl == 'sports-genesis-of-martial-arts':
        if is_hindi:
            return [
                {"label": "युद्ध कलाओं की उत्पत्ति", "type": "branch", "date": "उत्पत्ति", "children": [
                    {"label": "धनुर्वेद: प्राचीन वेदों का उपवेद (धनुर्वेद) जो युद्ध कौशल, तीरंदाजी और अस्त्रों के उपयोग से संबंधित है", "type": "leaf"},
                    {"label": "बौद्ध भिक्षु प्रभाव: बौद्ध भिक्षुओं द्वारा आत्मरक्षा के लिए विकसित कौशल, जो भारत से चीन (शालिन मंदिर) तक फैला", "type": "leaf"}
                ]}
            ]
        else:
            return [
                {"label": "Genesis of Martial Systems", "type": "branch", "date": "Genesis", "children": [
                    {"label": "Dhanurveda: Vedic upaveda describing military science, archery rules, and weapon training", "type": "leaf"},
                    {"label": "Buddhist Monk Dispersion: Self-defense moves practiced by travelling monks, spreading to Shaolin temple", "type": "leaf"}
                ]}
            ]

    # 21. Sports Various Type of Sports (Traditional Games)
    elif fl == 'sports-various-type-of-sports':
        if is_hindi:
            return [
                {"label": "पारंपरिक भारतीय खेल", "type": "branch", "date": "खेल प्रकार", "children": [
                    {"label": "मल्लखंब: लकड़ी के खंभे पर किया जाने वाला योगासन और जिमनास्टिक प्रदर्शन; मध्य प्रदेश का राज्य खेल", "type": "leaf"},
                    {"label": "खो-खो व कबड्डी: प्राचीन स्वदेशी खेल; त्वरित निर्णय और फुर्तीले शारीरिक संतुलन पर आधारित", "type": "leaf"}
                ]}
            ]
        else:
            return [
                {"label": "Traditional Indian Games", "type": "branch", "date": "Games", "children": [
                    {"label": "Mallakhamb: Gymnastic and yogic postures performed on a vertical wooden pole", "type": "leaf"},
                    {"label": "Kabaddi & Kho-Kho: Indigenous team sports relying on speed, tactical holds, and tag movements", "type": "leaf"}
                ]}
            ]

    # 22. Theatre History of Theatre in India (Origins & Cave Theatres)
    elif fl == 'theatre-history-of-theatre-in-india':
        if is_hindi:
            return [
                {"label": "रंगमंच का इतिहास", "type": "branch", "date": "प्राचीन रंगमंच", "children": [
                    {"label": "रामगढ़ गुफाएं (छत्तीसगढ़): भारत की सबसे पुरानी गुफा रंगमंचशाला (Sitabenga Cave Theatre), जहाँ संस्कृत नाटकों का मंचन होता था", "type": "leaf"},
                    {"label": "नाट्यशास्त्र उत्पत्ति: देवताओं के मनोरंजन के लिए ब्रह्मा द्वारा पंचम वेद के रूप में नाट्य की रचना की गई", "type": "leaf"}
                ]}
            ]
        else:
            return [
                {"label": "Early Theatre History", "type": "branch", "date": "History", "children": [
                    {"label": "Ramgarh Caves: Houses the ancient Sitabenga Cave Theatre in Chhattisgarh, featuring carved steps", "type": "leaf"},
                    {"label": "Panchama Veda: Legendary origin in Natya Shastra as the 5th Veda created for common enlightenment", "type": "leaf"}
                ]}
            ]

    # 23. Theatre Classical Sanskrit Theatre
    elif fl == 'theatre-classical-sanskrit-theatre':
        if is_hindi:
            return [
                {"label": "शास्त्रीय संस्कृत नाटक", "type": "branch", "date": "संस्कृत नाटक", "children": [
                    {"label": "विशेषताएँ: सुखांत अंत (happy endings); द्विभाषी नाटक (उच्च पात्र संस्कृत बोलते थे, महिलाएं व शूद्र प्राकृत)", "type": "leaf"},
                    {"label": "विदूषक: नाटक का हास्य पात्र (जोकर), जो अक्सर नायक का दोस्त और ब्राह्मण होता था", "type": "leaf"},
                    {"label": "महान लेखक: भास (चारुदत्त), शूद्रक (मृच्छकटिकम् - मिट्टी की गाड़ी), कालिदास (अभिज्ञानशाकुंतलम्)", "type": "leaf"}
                ]}
            ]
        else:
            return [
                {"label": "Classical Sanskrit Theatre Rules", "type": "branch", "date": "Sanskrit", "children": [
                    {"label": "Language rule: Bilingual scripts; elite male characters speak Sanskrit, while females and commoners speak Prakrit", "type": "leaf"},
                    {"label": "Vidushaka: Comic jester character; acts as the confidant of the hero, typically a clever but gluttonous Brahmin", "type": "leaf"},
                    {"label": "Dramatists: Bhasa (Swapnavasavadatta), Shudraka (Mrichchhakatika), and Kalidasa (Abhijnanasakuntalam)", "type": "leaf"}
                ]}
            ]

    # 24. Theatre Modern Theatre in India
    elif fl == 'theatre-modern-theatre-in-india':
        if is_hindi:
            return [
                {"label": "राष्ट्रीय नाट्य विद्यालय व रंगमंच", "type": "branch", "date": "आधुनिक नाटक", "children": [
                    {"label": "राष्ट्रीय नाट्य विद्यालय (NSD - 1959): दिल्ली; इब्राहिम अलकाजी ने इसे विश्व स्तर पर स्थापित किया", "type": "leaf"},
                    {"label": "हबीब तनवीर: नया थियेटर (Naya Theatre); छत्तीसगढ़ी लोक कलाकारों के साथ काम (जैसे चरणदास चोर)", "type": "leaf"},
                    {"label": "विजय तेंदुलकर: 'घासीराम कोतवाल' (शक्ति और राजनीति का द्वंद्व)", "type": "leaf"}
                ]}
            ]
        else:
            return [
                {"label": "NSD & Post-Independence Theatre", "type": "branch", "date": "NSD Era", "children": [
                    {"label": "National School of Drama: Under Ebrahim Alkazi, introduced realistic set design and proscenium stages", "type": "leaf"},
                    {"label": "Habib Tanvir: Founded Naya Theatre using tribal actors from Chhattisgarh in modern plays", "type": "leaf"},
                    {"label": "Vijay Tendulkar: Marathi playwright noted for Ghashiram Kotwal and Shakharam Binder", "type": "leaf"}
                ]}
            ]

    # 25. Theatre Regional Theatre (Folk Play Styles)
    elif fl == 'theatre-regional-theatre':
        if is_hindi:
            return [
                {"label": "क्षेत्रीय लोक रंगमंच", "type": "branch", "date": "लोक रंगमंच", "children": [
                    {"label": "भवाई (गुजरात): तेज गति वाला सामाजिक व्यंग्य; भुंगल वाद्य का प्रयोग; रंगमंच पर मिट्टी के घड़े संतुलित करना", "type": "leaf"},
                    {"label": "नौटंकी (UP): धर्मनिरपेक्ष और रोमांटिक नाटक; नगाड़े (धमसा) की थाप पर संगीत संवाद", "type": "leaf"},
                    {"label": "जात्रा (बंगाल): खुले मैदानों में मंचित किए जाने वाले संगीतमय नाटक; चैतन्य महाप्रभु के भक्ति आंदोलन से जुड़े", "type": "leaf"}
                ]}
            ]
        else:
            return [
                {"label": "Regional Folk Theatres", "type": "branch", "date": "Folk", "children": [
                    {"label": "Bhavai (Gujarat): Social satire using the long brass Bhungal horn, featuring balancing acts", "type": "leaf"},
                    {"label": "Nautanki (UP): Secular musical romantic tales staged with high-pitched singing and Nagada drums", "type": "leaf"},
                    {"label": "Jatra (Bengal): Melodramatic musical plays performed in open arenas during Bhakti festivals", "type": "leaf"}
                ]}
            ]

    # 26. Theatre Renaissance of Indian Theatre
    elif fl == 'theatre-renaissance-of-indian-theatre':
        if is_hindi:
            return [
                {"label": "इप्टा (IPTA) और राष्ट्रवादी रंगमंच", "type": "branch", "date": "पुनर्जागरण", "children": [
                    {"label": "इप्टा (IPTA - 1943): ब्रिटिश विरोधी राष्ट्रवादी आंदोलन; बिजन भट्टाचार्य का 'नबन्ना' नाटक; सामाजिक यथार्थवाद", "type": "leaf"},
                    {"label": "तीसरा रंगमंच (Third Theatre): बादल सरकार; नाटक को ऑडिटोरियम से निकालकर नुक्कड़ नाटक के रूप में सड़कों पर लाए", "type": "leaf"}
                ]}
            ]
        else:
            return [
                {"label": "Theatre Renaissance & IPTA", "type": "branch", "date": "Renaissance", "children": [
                    {"label": "IPTA (1943): Anti-fascist and anti-imperialist movement; produced 'Nabanna' during Bengal famine", "type": "leaf"},
                    {"label": "Third Theatre: Badal Sircar's rejection of proscenium stages, developing street plays and direct contact", "type": "leaf"}
                ]}
            ]

    # 27. Theatre Traditional Theatre (Ritual & Temple Theatre)
    elif fl == 'theatre-traditional-theatre':
        if is_hindi:
            return [
                {"label": "पारंपरिक व अनुष्ठानिक रंगमंच", "type": "branch", "date": "पारंपरिक", "children": [
                    {"label": "कूटियाट्टम (केरल): संस्कृत रंगमंच; यूनेस्को अमूर्त विरासत; चाक्यार और नंग्यार समुदायों द्वारा मंचन", "type": "leaf"},
                    {"label": "यक्षगान (कर्नाटक): रामायण/महाभारत के युद्ध दृश्यों का भव्य वेशभूषा और नृत्य के साथ मंचन", "type": "leaf"},
                    {"label": "भांड पाथेर (कश्मीर): व्यंग्य और नकल; किसानों के जीवन पर सामंतों के शोषण को हास्य रूप में दर्शाना", "type": "leaf"}
                ]}
            ]
        else:
            return [
                {"label": "Traditional & Ritual Theatre", "type": "branch", "date": "Traditional", "children": [
                    {"label": "Kutiyattam (Kerala): Only surviving Sanskrit temple theatre, declared UNESCO Oral Heritage", "type": "leaf"},
                    {"label": "Yakshagana (Karnataka): Heavy makeup, elaborate crowns, and stylized dialogue explaining Puranic battles", "type": "leaf"},
                    {"label": "Bhand Pather (Kashmir): Secular satire featuring folk music, humor, and social critique", "type": "leaf"}
                ]}
            ]

    # 28. Cinema in India
    elif fl == 'cinema-in-india':
        if is_hindi:
            return [
                {"label": "मूक और सवाक फिल्म युग", "type": "branch", "date": "इतिहास", "children": [
                    {"label": "राजा हरिश्चंद्र (1913): दादासाहेब फाल्के द्वारा निर्देशित भारत की पहली मूक फीचर फिल्म", "type": "leaf"},
                    {"label": "आलम आरा (1931): अर्देशिर ईरानी द्वारा निर्देशित पहली सवाक (बोलती) फिल्म; संगीत युग की शुरुआत", "type": "leaf"},
                    {"label": "स्वर्ण युग (1950s): सत्यजीत रे (पथेर पांचाली), ऋत्विक घटक, गुरु दत्त; वैश्विक स्तर पर पहचान", "type": "leaf"},
                    {"label": "समानांतर सिनेमा (Parallel Cinema): मणाल सेन, श्याम बेनेगल; सामाजिक यथार्थवाद और स्टार-सिस्टम का विरोध", "type": "leaf"}
                ]}
            ]
        else:
            return [
                {"label": "Silent & Talkie Era", "type": "branch", "date": "History", "children": [
                    {"label": "Raja Harishchandra (1913): Directed by Dadasaheb Phalke, India's first silent feature film", "type": "leaf"},
                    {"label": "Alam Ara (1931): Directed by Ardeshir Irani, the first talkie film introducing musical playback", "type": "leaf"},
                    {"label": "Golden Age (1950s): Satyajit Ray's Pather Panchali (Apu Trilogy) winning honors at Cannes", "type": "leaf"},
                    {"label": "Parallel Cinema: Mrinal Sen, Shyam Benegal; rejected mainstream formulas for harsh socio-political realism", "type": "leaf"}
                ]}
            ]

    # Fallback
    else:
        if is_hindi:
            return [
                {"label": "प्रदर्शन कला सामान्य", "type": "branch", "date": "कला", "children": [
                    {"label": "शास्त्रीय संगीत, लोक संगीत, नृत्य, थियेटर और मार्शल आर्ट का समग्र इतिहास", "type": "leaf"},
                    {"label": "नाट्यशास्त्र के नवरस सिद्धांत और गुरु-शिष्य परंपरा का भारतीय कला पर प्रभाव", "type": "leaf"}
                ]}
            ]
        else:
            return [
                {"label": "Performing Arts Overview", "type": "branch", "date": "Overview", "children": [
                    {"label": "Comprehensive overview of Indian musical forms, gharanas, classical dance rules, and theatre lineages", "type": "leaf"},
                    {"label": "Encompasses shadow puppetry, regional sports, and historical evolution of cinema", "type": "leaf"}
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
