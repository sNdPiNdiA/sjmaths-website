#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import re
import json

BASE = r"upsc/art_and_culture/Religion-Language-and-Literature"

def get_clean_title(folder_name):
    title = folder_name.replace('-', ' ')
    words = []
    acronyms = {'upsc', 'ad', 'bc', 'ii', 'iii', 'eic'}
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

    # 1. Bhakti Movement (General Concepts)
    if fl == 'bhakti-movement':
        if is_hindi:
            return [
                {"label": "उत्पत्ति और मुख्य विशेषताएं", "type": "branch", "date": "अवधारणा", "children": [
                    {"label": "भक्ति मार्ग: ईश्वर के प्रति बिना शर्त आत्मसमर्पण द्वारा मोक्ष; जातिगत भेदभाव और कर्मकांडीय जटिलता का विरोध", "type": "leaf"},
                    {"label": "क्षेत्रीय भाषाएँ: उपदेश स्थानीय जनभाषा (जैसे ब्रजभाषा, मराठी, बंगाली) में दिए गए, जिससे क्षेत्रीय साहित्य का विकास हुआ", "type": "leaf"}
                ]},
                {"label": "सगुण बनाम निर्गुण", "type": "branch", "date": "वर्गीकरण", "children": [
                    {"label": "सगुण भक्ति: रूप और अवतारों वाले ईश्वर की पूजा (राम/कृष्ण); जैसे तुलसीदास (रामचरितमानस), मीराबाई, सूरदास", "type": "leaf"},
                    {"label": "निर्गुण भक्ति: निराकार, अमूर्त ईश्वर की पूजा; जैसे कबीर (दोहे, बीजक), गुरु नानक (सिख धर्म के संस्थापक)", "type": "leaf"}
                ]}
            ]
        else:
            return [
                {"label": "Origins & Core Philosophy", "type": "branch", "date": "Philosophy", "children": [
                    {"label": "Devotional Path: Salvation (Moksha) through absolute devotion to a personal god, rejecting rigid caste rules", "type": "leaf"},
                    {"label": "Vernacular growth: Sermons delivered in local languages (Marathi, Bengali, Hindi), leading to literary growth", "type": "leaf"}
                ]},
                {"label": "Saguna vs Nirguna Schools", "type": "branch", "date": "Schools", "children": [
                    {"label": "Saguna: Worship of God with form, attributes, and incarnations (Rama/Krishna); Surdas, Tulsidas, Mirabai", "type": "leaf"},
                    {"label": "Nirguna: Worship of a formless, abstract Supreme Being without physical representations; Kabir, Guru Nanak", "type": "leaf"}
                ]}
            ]

    # 2. Bhakti Movement Religions (Philosophies & Sects)
    elif fl == 'bhakti-movement-religions':
        if is_hindi:
            return [
                {"label": "दार्शनिक मत (वेदांत)", "type": "branch", "date": "दार्शनिक मत", "children": [
                    {"label": "अद्वैत वेदांत (शंकराचार्य): अद्वैतवाद (ज्ञान मार्ग); ब्रह्म ही एकमात्र सत्य है, जगत मिथ्या है", "type": "leaf"},
                    {"label": "विशिष्टाद्वैत (रामानुजाचार्य): सगुण ब्रह्म की आराधना; भक्ति मार्ग द्वारा मोक्ष", "type": "leaf"},
                    {"label": "द्वैतवाद (माधवाचार्य): आत्मा और परमात्मा को पृथक माना गया; शुद्ध द्वैत", "type": "leaf"},
                    {"label": "शुद्धाद्वैत (वल्लभाचार्य): पुष्टिमार्ग के संस्थापक; कृष्ण भक्ति का प्रचार", "type": "leaf"}
                ]},
                {"label": "शैव और वैष्णव संप्रदाय", "type": "branch", "date": "संप्रदाय", "children": [
                    {"label": "आलवार (वैष्णव): 12 संत जिन्होंने विष्णु की भक्ति में तमिल भजनों 'नालायिर दिव्य प्रबंधम' की रचना की", "type": "leaf"},
                    {"label": "नयनार (शैव): 63 संत जिन्होंने शिव की आराधना में 'तेवरम' संकलन की रचना की", "type": "leaf"}
                ]}
            ]
        else:
            return [
                {"label": "Philosophical Schools (Vedanta)", "type": "branch", "date": "Philosophy", "children": [
                    {"label": "Advaita (Shankaracharya): Absolute Monism; Brahman is the sole reality; world is illusion (Maya)", "type": "leaf"},
                    {"label": "Vishishtadvaita (Ramanuja): Qualified Monism; advocates devotion to Saguna Brahman as the path to release", "type": "leaf"},
                    {"label": "Dvaita (Madhvacharya): Dualism; asserts distinct, eternal realities of the soul and the Creator", "type": "leaf"},
                    {"label": "Shuddhadvaita (Vallabhacharya): Pure Monism; established the Pushtimarg sect centered on child Krishna", "type": "leaf"}
                ]},
                {"label": "Shaiva & Vaishnava Sects", "type": "branch", "date": "Sects", "children": [
                    {"label": "Alvars: 12 Vaishnavite saints of South India; composed the compilation 'Nalayira Divya Prabandham'", "type": "leaf"},
                    {"label": "Nayanars: 63 Shaivite saints of South India; composed the canonical hymns compiled in 'Tevaram'", "type": "leaf"}
                ]}
            ]

    # 3. Saints of Bhakti Movement (Individual Saints)
    elif fl == 'saints-of-bhakti-movement':
        if is_hindi:
            return [
                {"label": "उत्तर व पूर्वी भारत के संत", "type": "branch", "date": "संत", "children": [
                    {"label": "कबीर: जुलाहा; हिंदू-मुस्लिम पाखंडों का खंडन किया; 'बीजक' में उनकी शिक्षाएं संकलित हैं", "type": "leaf"},
                    {"label": "गुरु नानक: सिख धर्म की स्थापना; लंगर (सामूहिक रसोई) प्रथा शुरू कर सामाजिक समानता की नींव रखी", "type": "leaf"},
                    {"label": "चैतन्य महाप्रभु (बंगाल): संकीर्तन (सामूहिक कीर्तन) प्रथा शुरू की; गौड़ीय वैष्णववाद का प्रचार किया", "type": "leaf"}
                ]},
                {"label": "महाराष्ट्र धर्म के संत", "type": "branch", "date": "महाराष्ट्र", "children": [
                    {"label": "ज्ञानेश्वर: मराठी भाषा में 'ज्ञानेश्वरी' (गीता पर टीका) लिखी; वारकरी संप्रदाय की नींव रखी", "type": "leaf"},
                    {"label": "नामदेव: दर्जी समुदाय से; उनके कई अभंग सिखों के पवित्र ग्रंथ गुरु ग्रंथ साहिब में शामिल हैं", "type": "leaf"},
                    {"label": "तुकाराम: छत्रपति शिवाजी महाराज के समकालीन; विठोबा के भक्त; लोकगीत शैली में अभंगों की रचना की", "type": "leaf"}
                ]}
            ]
        else:
            return [
                {"label": "Northern & Eastern Reformers", "type": "branch", "date": "Saints", "children": [
                    {"label": "Kabir: Weaver saint who criticized orthodox rituals; teachings preserved in the 'Bijak'", "type": "leaf"},
                    {"label": "Guru Nanak: Founded Sikhism; introduced the communal kitchen (Langar) to abolish caste hierarchies", "type": "leaf"},
                    {"label": "Chaitanya Mahaprabhu: Popularized ecstatic congregational singing (Kirtan) and Gaudiya Vaishnavism in Bengal", "type": "leaf"}
                ]},
                {"label": "Maharashtra Dharma & Varkaris", "type": "branch", "date": "Varkari", "children": [
                    {"label": "Jnaneshwar: Wrote the Marathi commentary 'Jnaneshwari'; established the Varkari pilgrimage system", "type": "leaf"},
                    {"label": "Namdev: Tailor saint whose devotional verses (Abhangs) are also incorporated in Guru Granth Sahib", "type": "leaf"},
                    {"label": "Tukaram: Devoted to Lord Vithoba of Pandharpur; composed highly popular social-reform abhangas", "type": "leaf"}
                ]}
            ]

    # 4. Languages Classical Language
    elif 'classical-language' in fl:
        if is_hindi:
            return [
                {"label": "शास्त्रीय भाषा का दर्जा और मापदंड", "type": "branch", "date": "मापदंड", "children": [
                    {"label": "प्राचीनता: प्रारंभिक ग्रंथों का दर्ज इतिहास 1500-2000 वर्ष पुराना होना चाहिए", "type": "leaf"},
                    {"label": "मौलिकता: साहित्यिक परंपरा स्वदेशी और स्वतंत्र होनी चाहिए; किसी अन्य भाषा समुदाय से उधार न ली गई हो", "type": "leaf"}
                ]},
                {"label": "मान्यता प्राप्त भाषाएं (2024 तक)", "type": "branch", "date": "भाषाएँ", "children": [
                    {"label": "प्रारंभिक छह: तमिल (प्रथम, 2004), संस्कृत (2005), कन्नड़ (2008), तेलुगु (2008), मलयालम (2013), ओडिया (2014)", "type": "leaf"},
                    {"label": "नवीनतम जुड़ाव (2024): मराठी, पालि, प्राकृत और असमिया को हाल ही में शास्त्रीय भाषा का दर्जा दिया गया", "type": "leaf"},
                    {"label": "लाभ: अंतरराष्ट्रीय पुरस्कारों की स्थापना, विश्वविद्यालयों में भाषा पीठ (Chairs) और शोध हेतु वित्तीय अनुदान", "type": "leaf"}
                ]}
            ]
        else:
            return [
                {"label": "Criteria for Classical Status", "type": "branch", "date": "Criteria", "children": [
                    {"label": "Antiquity: High antiquity of early texts/recorded history spanning 1500 to 2000 years", "type": "leaf"},
                    {"label": "Originality: Literary tradition must be original and not borrowed from another speech community", "type": "leaf"}
                ]},
                {"label": "Recognized Languages & Benefits", "type": "branch", "date": "Languages", "children": [
                    {"label": "First Six: Tamil (2004), Sanskrit (2005), Kannada (2008), Telugu (2008), Malayalam (2013), Odia (2014)", "type": "leaf"},
                    {"label": "New Inclusions (2024): Marathi, Pali, Prakrit, and Assamese recently declared classical languages", "type": "leaf"},
                    {"label": "Benefits: Funding for research centers of excellence and creation of academic chairs in central universities", "type": "leaf"}
                ]}
            ]

    # 5. Literature Influence Contribution of Foreign Languages
    elif 'foreign-languages' in fl:
        if is_hindi:
            return [
                {"label": "फारसी और अरबी का योगदान", "type": "branch", "date": "मध्यकाल", "children": [
                    {"label": "राजभाषा: दिल्ली सल्तनत और मुगल काल के दौरान फारसी प्रशासनिक और दरबारी भाषा बनी", "type": "leaf"},
                    {"label": "ऐतिहासिक ग्रंथ: तारीख (जैसे जियाउद्दीन बरनी की तारीख-ए-फिरोजशाही, अबुल फजल की आईन-ए-अकबरी)", "type": "leaf"},
                    {"label": "अनुवाद कार्य: दारा शिकोह द्वारा उपनिषदों का फारसी अनुवाद (सिर्र-ए-अकबर)", "type": "leaf"}
                ]},
                {"label": "यूरोपीय और अंग्रेजी का योगदान", "type": "branch", "date": "आधुनिक काल", "children": [
                    {"label": "मुद्रण तकनीक: पुर्तगालियों द्वारा गोवा में प्रिंटिंग प्रेस की शुरुआत (1556 ई.); ईसाई धर्मग्रंथों का अनुवाद", "type": "leaf"},
                    {"label": "अंग्रेजी अनुवाद: विलियम जोन्स द्वारा संस्कृत ग्रंथों (अभिज्ञानशाकुंतलम्) का अनुवाद; गद्य (Prose) और उपन्यासों का उदय", "type": "leaf"}
                ]}
            ]
        else:
            return [
                {"label": "Persian & Arabic Literary Synthesis", "type": "branch", "date": "Medieval", "children": [
                    {"label": "Court Language: Persian served as the official court and administrative language under Delhi Sultanate and Mughals", "type": "leaf"},
                    {"label": "Historical Chronicles: Standardized writing of Tarikhs, e.g. Barani's Tarikh-i-Firoz Shahi and Abul Fazl's Akbarnama", "type": "leaf"},
                    {"label": "Translations: Upanishads translated into Persian as 'Sirr-i-Akbar' by Mughal prince Dara Shikoh", "type": "leaf"}
                ]},
                {"label": "Western & English Contributions", "type": "branch", "date": "Colonial", "children": [
                    {"label": "Printing Press: Introduced by Portuguese Jesuits in Goa (1556), establishing movable-type printing", "type": "leaf"},
                    {"label": "Indology: Translation of Sanskrit texts by Sir William Jones (Asiatic Society) introducing Indian epics to the West", "type": "leaf"}
                ]}
            ]

    # 6. Sanskrit Literature
    elif fl == 'literature-sanskrit-literature':
        if is_hindi:
            return [
                {"label": "वैदिक और व्याकरण साहित्य", "type": "branch", "date": "वैदिक", "children": [
                    {"label": "संहिताएं: चार वेद, ब्राह्मण ग्रंथ, आरण्यक और उपनिषद (दार्शनिक सार/वेदांत)", "type": "leaf"},
                    {"label": "पाणिनि की अष्टाध्यायी: संस्कृत व्याकरण का सबसे वैज्ञानिक और व्यवस्थित ग्रंथ (5वीं सदी ई.पू.)", "type": "leaf"}
                ]},
                {"label": "शास्त्रीय नाटक और काव्य", "type": "branch", "date": "शास्त्रीय", "children": [
                    {"label": "कालिदास: अभिज्ञानशाकुंतलम् (विश्व प्रसिद्ध नाटक), मेघदूत, रघुवंश और कुमारसंभव", "type": "leaf"},
                    {"label": "शूद्रक व विशाखदत्त: 'मृच्छकटिकम्' (मिट्टी का खिलौना गाड़ी) और 'मुद्राराक्षस' (ऐतिहासिक राजनीतिक नाटक)", "type": "leaf"},
                    {"label": "बाणभट्ट: राजा हर्षवर्धन के दरबारी कवि; 'हर्षचरित' (जीवनी) और 'कादंबरी' (गद्य) के लेखक", "type": "leaf"}
                ]}
            ]
        else:
            return [
                {"label": "Vedic & Grammatical Foundations", "type": "branch", "date": "Vedic", "children": [
                    {"label": "Shruti Canon: Consists of the four Vedas, Brahmanas, Aranyakas, and Upanishads (philosophical core)", "type": "leaf"},
                    {"label": "Panini's Ashtadhyayi: Definitive 8-chapter treatise on Sanskrit grammar, regularizing phonetics", "type": "leaf"}
                ]},
                {"label": "Classical Drama & Prose", "type": "branch", "date": "Classical", "children": [
                    {"label": "Kalidasa: Wrote landmark plays like Abhijnanasakuntalam, and lyric poetry like Meghaduta", "type": "leaf"},
                    {"label": "Shudraka & Visakhadatta: Mrichchhakatika (realist urban drama) and Mudrarakshasa (historical political thriller)", "type": "leaf"},
                    {"label": "Banabhatta: Famed prose biographer who composed Harshacharita and the complex romance Kadambari", "type": "leaf"}
                ]}
            ]

    # 7. Other Important Literatures (Sangam, Pali, Prakrit)
    elif fl == 'literature-other-important-literatures':
        if is_hindi:
            return [
                {"label": "तमिल संगम साहित्य", "type": "branch", "date": "संगम", "children": [
                    {"label": "परिषद्: मदुरै के पांड्य राजाओं के संरक्षण में आयोजित तीन साहित्यिक परिषदों (संगमों) में संकलित", "type": "leaf"},
                    {"label": "वर्गीकरण: अहम (प्रेम/आंतरिक भावनाएं) और पुरम (युद्ध, वीरता और राजा की प्रशंसा) में विभाजित", "type": "leaf"},
                    {"label": "महाकाव्य: शिलप्पादिकारम (इलांगो आदिगल द्वारा रचित नूपुर की कहानी) और मणिमेकलै", "type": "leaf"}
                ]},
                {"label": "बौद्ध और जैन साहित्य (पालि व प्राकृत)", "type": "branch", "date": "पालि-प्राकृत", "children": [
                    {"label": "पालि बौद्ध ग्रंथ: त्रिपिटक (विनय - नियम, सुत्त - उपदेश, अभिधम्म - दर्शन); जातक कथाएँ", "type": "leaf"},
                    {"label": "प्राकृत जैन ग्रंथ: अर्धमागधी भाषा में रचित जैन अंग और उपांग सिद्धांत", "type": "leaf"}
                ]}
            ]
        else:
            return [
                {"label": "Sangam Tamil Literature", "type": "branch", "date": "Sangam", "children": [
                    {"label": "Conclaves: Composed in three poetic assemblies under Pandya patronage at Madurai", "type": "leaf"},
                    {"label": "Aham & Puram: Classification into Aham (subjective love/feelings) and Puram (objective war/heroism)", "type": "leaf"},
                    {"label": "Tamil Epics: Silappadikaram (The Tale of the Anklet by Ilango Adigal) and Manimekalai", "type": "leaf"}
                ]},
                {"label": "Heterodox Canons (Pali & Prakrit)", "type": "branch", "date": "Pali/Prakrit", "children": [
                    {"label": "Buddhist Pali: Tripitakas (Vinaya, Sutta, Abhidhamma) and Jataka stories of Buddha's past lives", "type": "leaf"},
                    {"label": "Jain Prakrit: Canonical scriptures composed in Ardhamagadhi, structured into Angas and Upangas", "type": "leaf"}
                ]}
            ]

    # 8. Christianity
    elif fl == 'religions-christianity':
        if is_hindi:
            return [
                {"label": "भारत में ईसाई धर्म का आगमन", "type": "branch", "date": "इतिहास", "children": [
                    {"label": "संत थॉमस (52 ई.): केरल के मालाबार तट पर आगमन; सीरियाई ईसाई (नसरानी) समुदाय की स्थापना की", "type": "leaf"},
                    {"label": "जेसुइट मिशन (1542): पुर्तगालियों के साथ सेंट फ्रांसिस जेवियर का आगमन; कोंकण और गोवा में धर्म प्रचार", "type": "leaf"}
                ]},
                {"label": "कला, वास्तुकला और प्रभाव", "type": "branch", "date": "प्रभाव", "children": [
                    {"label": "चर्च वास्तुकला: गोवा में बारोक (Baroque) और मैनुअलिन स्थापत्य शैलियों का प्रवेश (जैसे बेसिलिका ऑफ बॉम जीसस)", "type": "leaf"},
                    {"label": "शिक्षा और प्रेस: मुद्रण तकनीक का प्रसार, बाइबिल का क्षेत्रीय भारतीय भाषाओं में अनुवाद", "type": "leaf"}
                ]}
            ]
        else:
            return [
                {"label": "Arrival & Denominations", "type": "branch", "date": "History", "children": [
                    {"label": "St. Thomas (52 AD): Landed on Malabar Coast, establishing early Syriac Christian (Nasrani) traditions", "type": "leaf"},
                    {"label": "Jesuit Missions (1542): Franciscans and Jesuits (St. Francis Xavier) arrived under Portuguese patronage", "type": "leaf"}
                ]},
                {"label": "Cultural & Architectural Legacy", "type": "branch", "date": "Legacy", "children": [
                    {"label": "Church building: Introduced Baroque and Manueline designs in Goa, e.g. Se Cathedral", "type": "leaf"},
                    {"label": "Social Impact: Pioneered western educational institutions, printing presses, and translations of local idioms", "type": "leaf"}
                ]}
            ]

    # 9. Hinduism
    elif fl == 'religions-hinduism':
        if is_hindi:
            return [
                {"label": "वैदिक से पौराणिक संक्रमण", "type": "branch", "date": "संक्रमण", "children": [
                    {"label": "वैदिक कर्मकांड: यज्ञ, आहुति और प्राकृतिक देवताओं (इंद्र, वरुण, अग्नि) की पूजा", "type": "leaf"},
                    {"label": "पौराणिक भक्ति: त्रिमूर्ति (ब्रह्मा, विष्णु, शिव) के प्रति भक्ति; 18 महापुराणों की रचना; मूर्ति पूजा", "type": "leaf"}
                ]},
                {"label": "षड्दर्शन (छह दार्शनिक मत)", "type": "branch", "date": "दर्शन", "children": [
                    {"label": "सांख्य व योग: सांख्य (कपिल - प्रकृति व पुरुष); योग (पतंजलि - अष्टांग योग)", "type": "leaf"},
                    {"label": "न्याय व वैशेषिक: न्याय (गौतम - तर्कशास्त्र); वैशेषिक (कणाद - परमाणु सिद्धांत)", "type": "leaf"},
                    {"label": "मीमांसा व वेदांत: पूर्व मीमांसा (जैमिनी - यज्ञ); उत्तर मीमांसा/वेदांत (बादरायण - ब्रह्मज्ञान)", "type": "leaf"}
                ]}
            ]
        else:
            return [
                {"label": "Vedic to Puranic Shift", "type": "branch", "date": "Transition", "children": [
                    {"label": "Vedic Ritualism: Focused on fire sacrifices (Yajnas) and chants invoking natural deities like Indra/Agni", "type": "leaf"},
                    {"label": "Puranic Sectarianism: Emergence of temple worship, bhakti to the Trinity, and compilation of the Puranas", "type": "leaf"}
                ]},
                {"label": "Six Orthodox Philosophies (Shad-Darshana)", "type": "branch", "date": "Philosophy", "children": [
                    {"label": "Rational systems: Samkhya (dualism of Purusha/Prakriti by Kapila) and Yoga (meditation by Patanjali)", "type": "leaf"},
                    {"label": "Logical systems: Nyaya (logic by Gautama) and Vaisheshika (atomism theory of matter by Kanada)", "type": "leaf"},
                    {"label": "Textual systems: Mimamsa (ritual action by Jaimini) and Vedanta (absolute reality of Brahman by Badarayana)", "type": "leaf"}
                ]}
            ]

    # 10. Islam
    elif fl == 'religions-islam':
        if is_hindi:
            return [
                {"label": "इस्लाम के पांच बुनियादी स्तंभ", "type": "branch", "date": "स्तंभ", "children": [
                    {"label": "ईमान (शहादा): अल्लाह की एकता में विश्वास; नमाज (दैनिक प्रार्थना); जकात (दान); रोजा (उपवास); हज (तीर्थयात्रा)", "type": "leaf"}
                ]},
                {"label": "सूफीवाद (रहस्यवादी परंपरा)", "type": "branch", "date": "सूफी", "children": [
                    {"label": "अवधारणा: संगीत (शमा), प्रेम और ध्यान के माध्यम से अल्लाह के साथ सीधा आध्यात्मिक संबंध; खानकाह (मठ)", "type": "leaf"},
                    {"label": "चिश्ती सिलसिला: ख्वाजा मोइनुद्दीन चिश्ती (अजमेर); राजकीय पदों का त्याग, संगीत सम्मेलनों का आयोजन", "type": "leaf"},
                    {"label": "सुहरावर्दी सिलसिला: बहाउद्दीन जकारिया; राजकीय पदों को स्वीकार किया; अमीरों के बीच काम किया", "type": "leaf"}
                ]}
            ]
        else:
            return [
                {"label": "Five Pillars of Islam", "type": "branch", "date": "Pillars", "children": [
                    {"label": "Tenets: Shahada (creed), Salat (prayer), Zakat (alms), Sawm (fasting), and Hajj (pilgrimage)", "type": "leaf"}
                ]},
                {"label": "Sufism & Major Orders (Silsilas)", "type": "branch", "date": "Sufism", "children": [
                    {"label": "Mystic Devotion: Stressed spiritual purification, universal love, music assemblies (Sama), and Khanqah centers", "type": "leaf"},
                    {"label": "Chishti Silsila: Moinuddin Chishti (Ajmer) and Nizamuddin Auliya; avoided state court associations", "type": "leaf"},
                    {"label": "Suhrawardi Silsila: Standardized by Bahauddin Zakariya; accepted state administrative offices", "type": "leaf"}
                ]}
            ]

    # 11. Jainism
    elif fl == 'religions-jainism':
        if is_hindi:
            return [
                {"label": "मूल दार्शनिक सिद्धांत", "type": "branch", "date": "दर्शन", "children": [
                    {"label": "अहिंसा: सबसे महत्वपूर्ण व्रत (मन, वचन और कर्म से हिंसा का त्याग); अनेकांतवाद (सत्य के अनेक पहलू)", "type": "leaf"},
                    {"label": "स्यादवाद: ज्ञान की सापेक्षता का सिद्धांत; पंच महाव्रत (सत्य, अहिंसा, अस्तेय, अपरिग्रह, ब्रह्मचर्य)", "type": "leaf"},
                    {"label": "तीर्थंकर: 24 तीर्थंकर; पहले ऋषभदेव, 23वें पार्श्वनाथ, और 24वें वर्धमान महावीर", "type": "leaf"}
                ]},
                {"label": "संप्रदाय और बौद्धिक संगीतियां", "type": "branch", "date": "इतिहास", "children": [
                    {"label": "विभाजन: दिगंबर (भद्रबाहु के नेतृत्व में नग्न संप्रदाय) और श्वेतांबर (स्थूलभद्र के नेतृत्व में सफेद वस्त्र धारी)", "type": "leaf"},
                    {"label": "संगीतियां: प्रथम परिषद पाटलिपुत्र में (12 अंगों का संकलन); द्वितीय परिषद वल्लभी (गुजरात) में", "type": "leaf"}
                ]}
            ]
        else:
            return [
                {"label": "Core Tenets & Tirthankaras", "type": "branch", "date": "Tenets", "children": [
                    {"label": "Ahimsa: Non-injury to all living beings, the highest ethic; Anekantavada (multiplicity of truth views)", "type": "leaf"},
                    {"label": "Vows: Five vows of Satya, Ahimsa, Asteya (non-stealing), Aparigraha (non-possession), Brahmacharya", "type": "leaf"},
                    {"label": "Tirthankaras: 24 teachers; Rishabhadeva (first), Parsvanatha (23rd), Vardhamana Mahavira (24th)", "type": "leaf"}
                ]},
                {"label": "Schism & Councils", "type": "branch", "date": "History", "children": [
                    {"label": "Digambara vs Svetambara: Digambaras (led by Bhadrabahu, sky-clad) and Svetambaras (led by Sthulabhadra, white-clad)", "type": "leaf"},
                    {"label": "Councils: 1st Council at Pataliputra; 2nd Council at Valabhi (Gujarat) which codified Svetambara Anga texts", "type": "leaf"}
                ]}
            ]

    # 12. Judaism
    elif fl == 'religions-judaism':
        if is_hindi:
            return [
                {"label": "भारत में यहूदी बस्तियाँ", "type": "branch", "date": "यहूदी", "children": [
                    {"label": "कोच्चि यहूदी: मालाबार तट; 70 ई. में जेरूसलम के दूसरे मंदिर के विनाश के बाद आगमन का इतिहास", "type": "leaf"},
                    {"label": "बेने इजरायल: महाराष्ट्र का कोंकण तट; स्थानीय मराठा समाज में पूरी तरह घुले-मिले", "type": "leaf"},
                    {"label": "बगदादी यहूदी: 18वीं-19वीं शताब्दी में इराक और सीरिया से व्यापार हेतु मुंबई और कोलकाता आए", "type": "leaf"}
                ]},
                {"label": "धार्मिक वास्तुकला", "type": "branch", "date": "आराधनालय", "children": [
                    {"label": "सिनैगॉग (Synagogue): कोच्चि का परदेसी सिनैगॉग (1568 ई.); चीनी हाथ से पेंट की हुई सिरेमिक टाइलें", "type": "leaf"},
                    {"label": "सद्भाव: यहूदी समुदाय को भारत में कभी भी धार्मिक उत्पीड़न का सामना नहीं करना पड़ा", "type": "leaf"}
                ]}
            ]
        else:
            return [
                {"label": "Three Jewish Settlements", "type": "branch", "date": "Settlements", "children": [
                    {"label": "Cochin Jews: Settled on Malabar Coast; claims arrival after destruction of Second Temple in Jerusalem in 70 AD", "type": "leaf"},
                    {"label": "Bene Israel: Settled in Konkan (Maharashtra), adopting Marathi names while preserving Jewish rituals", "type": "leaf"},
                    {"label": "Baghdadi Jews: Arrived in 18th-19th c. as traders in Mumbai and Kolkata, led by Sassoon family", "type": "leaf"}
                ]},
                {"label": "Integration & Synagogues", "type": "branch", "date": "Integration", "children": [
                    {"label": "Harmonious existence: Notable history of zero persecution of Jews in India", "type": "leaf"},
                    {"label": "Synagogue Architecture: Paradesi Synagogue (Kochi) built in 1568, featuring hand-painted Chinese willow-pattern tiles", "type": "leaf"}
                ]}
            ]

    # 13. Pre-Vedic Religion
    elif fl == 'religions-pre-vedic-religion':
        if is_hindi:
            return [
                {"label": "हड़प्पा कालीन धार्मिक मान्यताएं", "type": "branch", "date": "हड़प्पा", "children": [
                    {"label": "मातृदेवी की पूजा: उर्वरता सूचक मिट्टी की मूर्तियाँ; पौधों को गर्भ से निकलते हुए दिखाया गया है", "type": "leaf"},
                    {"label": "पशुपति महादेव: जानवरों (हाथी, बाघ, गैंडा, भैंसा) से घिरे योगासन में बैठे तीन मुख वाले देवता", "type": "leaf"},
                    {"label": "प्रकृति पूजा: पीपल के वृक्ष, कूबड़ वाले बैल की पूजा और स्नानागार के जल-शुद्धि अनुष्ठान", "type": "leaf"}
                ]},
                {"label": "ताम्रपाषाण और जनजातीय मान्यताएं", "type": "branch", "date": "ताम्रपाषाण", "children": [
                    {"label": "अग्नि वेदियाँ: कालीबंगन और लोथल में प्राप्त अग्नि वेदियाँ जो अनुष्ठानिक आहुति को दर्शाती हैं", "type": "leaf"},
                    {"label": "जीववाद: प्रकृति के विभिन्न तत्वों और रक्षक शक्तियों में अटूट विश्वास", "type": "leaf"}
                ]}
            ]
        else:
            return [
                {"label": "Harappan Religious Cults", "type": "branch", "date": "Harappan", "children": [
                    {"label": "Mother Goddess: Terracotta figurines showing female deities, associated with earth fertility", "type": "leaf"},
                    {"label": "Pashupati Seal: Seated horned figure in yogic posture surrounded by wild animals", "type": "leaf"},
                    {"label": "Animism & Bathing: Worship of pipal trees, bulls, and purification rites (Great Bath)", "type": "leaf"}
                ]},
                {"label": "Chalcolithic & Tribal Beliefs", "type": "branch", "date": "Chalcolithic", "children": [
                    {"label": "Fire Altars: Excavated brick hearth pits at Kalibangan and Lothal indicating domestic fire rituals", "type": "leaf"},
                    {"label": "Nature worship: Reverence for river deities, local spirits, and protective tribal totems", "type": "leaf"}
                ]}
            ]

    # 14. Zoroastrianism
    elif fl == 'religions-zoroastrianism':
        if is_hindi:
            return [
                {"label": "पारसी प्रवास और मूल दर्शन", "type": "branch", "date": "दर्शन", "children": [
                    {"label": "प्रवास: धार्मिक उत्पीड़न से बचने के लिए 8वीं शताब्दी में फारस से गुजरात (संजान) आए पारसी", "type": "leaf"},
                    {"label": "त्रिसूत्र: हुमता (अच्छे विचार), हुख्ता (अच्छे शब्द), ह्वरश्ता (अच्छे कर्म); पवित्र ग्रंथ जेंद अवेस्ता", "type": "leaf"}
                ]},
                {"label": "धार्मिक प्रथाएं और योगदान", "type": "branch", "date": "अगियारी", "children": [
                    {"label": "अग्नि पूजा: फायर टेम्पल (अगियारी) में पवित्र अग्नि का निरंतर प्रज्वलन; जल और पृथ्वी की पवित्रता का सम्मान", "type": "leaf"},
                    {"label": "दखमा (Tower of Silence): शवों को प्रकृति के हवाले (आकाश दफन) करने की प्रथा ताकि तत्वों को प्रदूषित न किया जाए", "type": "leaf"},
                    {"label": "आधुनिक प्रभाव: टाटा, गोदरेज, वाडिया और होमी जहांगीर भाभा जैसे दिग्गजों द्वारा भारतीय राष्ट्र निर्माण में योगदान", "type": "leaf"}
                ]}
            ]
        else:
            return [
                {"label": "Migration & Core Tenets", "type": "branch", "date": "Parsis", "children": [
                    {"label": "Persian migration: Zoroastrians fled Islamic persecution, landing in Sanjan (Gujarat) in 8th c.", "type": "leaf"},
                    {"label": "Threefold path: Humata (good thoughts), Hukhta (good words), Hvarshta (good deeds); Holy text: Zend Avesta", "type": "leaf"}
                ]},
                {"label": "Ritual Practice & Modern Impact", "type": "branch", "date": "Agiyari", "children": [
                    {"label": "Fire Worship: Maintaining the sacred fire inside Fire Temples (Agiyaris); reverence for clean water", "type": "leaf"},
                    {"label": "Dakhma (Tower of Silence): Exposure of deceased to birds (sky burials) to avoid defiling soil/fire", "type": "leaf"},
                    {"label": "Nation Builders: Outsized role in Indian science and industry (Tata, Godrej, Homi Bhabha)", "type": "leaf"}
                ]}
            ]

    # 15. Philosophy in India (Orthodox & Heterodox Systems)
    elif fl == 'philosophy-in-india':
        if is_hindi:
            return [
                {"label": "षड्दर्शन (छह आस्तिक दार्शनिक मत)", "type": "branch", "date": "आस्तिक", "children": [
                    {"label": "सांख्य व योग: सांख्य (कपिल - प्रकृति-पुरुष द्वैत); योग (पतंजलि - समाधि मार्ग)", "type": "leaf"},
                    {"label": "न्याय व वैशेषिक: न्याय (गौतम - तर्कशास्त्र); वैशेषिक (कणाद - परमाणुवाद)", "type": "leaf"},
                    {"label": "मीमांसा व वेदांत: पूर्व मीमांसा (जैमिनी - कर्मकांड); उत्तर मीमांसा (बादरायण - ज्ञान योग)", "type": "leaf"}
                ]},
                {"label": "नास्तिक दर्शन (अवैदिक)", "type": "branch", "date": "नास्तिक", "children": [
                    {"label": "चार्वाक (लोकायत): पूर्ण भौतिकवादी दर्शन; 'यावज्जीवेत् सुखं जीवेत् ऋणं कृत्वा घृतं पिवेत्'", "type": "leaf"},
                    {"label": "आजीवक संप्रदाय: मक्खलि गोशाल; नियतिवाद (नियति ही सब कुछ तय करती है, मानव कर्म निरर्थक है)", "type": "leaf"}
                ]}
            ]
        else:
            return [
                {"label": "Six Orthodox Systems (Shad-Darshana)", "type": "branch", "date": "Astika", "children": [
                    {"label": "Samkhya & Yoga: Dualism of spirit/matter by Kapila, and spiritual path by Patanjali", "type": "leaf"},
                    {"label": "Nyaya & Vaisheshika: Logic and epistemology by Gautama, and atomic realism of matter by Kanada", "type": "leaf"},
                    {"label": "Mimamsa & Vedanta: Vedic hermeneutics by Jaimini, and Upanishadic non-dualism by Badarayana", "type": "leaf"}
                ]},
                {"label": "Heterodox Systems (Nastika)", "type": "branch", "date": "Nastika", "children": [
                    {"label": "Charvaka (Lokayata): Materialist school advocating sensory pleasure as the ultimate good", "type": "leaf"},
                    {"label": "Ajivika Sect: Founded by Makkhali Gosala, propagating strict determinism (Niyati) of life events", "type": "leaf"}
                ]}
            ]

    # 16. Religions Buddhism
    elif fl == 'religions-buddhism':
        if is_hindi:
            return [
                {"label": "चार आर्य सत्य और अष्टांगिक मार्ग", "type": "branch", "date": "मूल सिद्धांत", "children": [
                    {"label": "चार आर्य सत्य: दुःख है, दुःख का कारण (तृष्णा) है, दुःख निरोध है, और दुःख निरोध का मार्ग है", "type": "leaf"},
                    {"label": "अष्टांगिक मार्ग: सम्यक दृष्टि, संकल्प, वाक, कर्मांत, आजीव, व्यायाम, स्मृति, समाधि (मोक्ष मार्ग)", "type": "leaf"}
                ]},
                {"label": "बौद्ध संगीतियां और संप्रदाय", "type": "branch", "date": "इतिहास", "children": [
                    {"label": "संगीतियां: राजगृह (प्रथम), वैशाली (द्वितीय), पाटलिपुत्र (तृतीय - अशोक), कश्मीर (चतुर्थ - कनिष्क)", "type": "leaf"},
                    {"label": "संप्रदाय: हीनयान (थेरवाद - प्रतीकात्मक बुद्ध), महायान (बुद्ध की मूर्ति पूजा), वज्रयान (तांत्रिक प्रभाव)", "type": "leaf"}
                ]}
            ]
        else:
            return [
                {"label": "Noble Truths & Eightfold Path", "type": "branch", "date": "Core Teachings", "children": [
                    {"label": "Four Noble Truths: Life is suffering (Dukkha), cause is desire, cessation is possible, path is Eightfold", "type": "leaf"},
                    {"label": "Eightfold Path: Right view, resolve, speech, action, livelihood, effort, mindfulness, concentration", "type": "leaf"}
                ]},
                {"label": "Councils & Major Sects", "type": "branch", "date": "History", "children": [
                    {"label": "Four Councils: Rajgriha (1st), Vaishali (2nd), Pataliputra (3rd under Ashoka), Kashmir (4th under Kanishka)", "type": "leaf"},
                    {"label": "Schools: Hinayana (orthodox Theravada), Mahayana (worships Bodhisattvas), and Vajrayana (tantric rituals)", "type": "leaf"}
                ]}
            ]

    # 17. Religions Sikhism
    elif fl == 'religions-sikhism':
        if is_hindi:
            return [
                {"label": "दस गुरु और गुरु ग्रंथ साहिब", "type": "branch", "date": "इतिहास", "children": [
                    {"label": "गुरु नानक (प्रथम): सिख धर्म के संस्थापक; करतारपुर में लंगर और संगत की स्थापना की", "type": "leaf"},
                    {"label": "गुरु अर्जुन देव: आदि ग्रंथ का संकलन कराया; अमृतसर में स्वर्ण मंदिर की आधारशिला रखवाई; मुगलों द्वारा शहादत", "type": "leaf"},
                    {"label": "गुरु गोविंद सिंह: 1699 में आनंदपुर साहिब में खालसा पंथ की स्थापना की; पांच ककार अनिवार्य किए", "type": "leaf"}
                ]},
                {"label": "सिख धर्म की मूल शिक्षाएं", "type": "branch", "date": "सिद्धांत", "children": [
                    {"label": "मूल मंत्र: नाम जपो (ईश्वर का स्मरण), कीरत करो (ईमानदारी की कमाई), वंड छको (साझेदारी)", "type": "leaf"},
                    {"label": "सामाजिक सुधार: जाति व्यवस्था, लैंगिक भेदभाव और मूर्ति पूजा का पूर्ण निषेध", "type": "leaf"}
                ]}
            ]
        else:
            return [
                {"label": "Ten Gurus & Scripture", "type": "branch", "date": "Gurus", "children": [
                    {"label": "Guru Nanak (1st): Founded the faith, establishing the institutions of Langar (kitchen) and Sangat", "type": "leaf"},
                    {"label": "Guru Arjan Dev (5th): Compiled the Adi Granth; built Harmandir Sahib; martyred under Jahangir", "type": "leaf"},
                    {"label": "Guru Gobind Singh (10th): Founded the Khalsa in 1699, institutionalizing the Five K's and Guru Granth Sahib as eternal Guru", "type": "leaf"}
                ]},
                {"label": "Core Ethics & Social Reforms", "type": "branch", "date": "Teachings", "children": [
                    {"label": "Triple Pillars: Naam Japna (meditating on Name), Kirat Karni (honest labor), Vand Chhakna (charity)", "type": "leaf"},
                    {"label": "Equality: Rejected all caste classifications and ascetic withdrawals, prioritizing active householder life", "type": "leaf"}
                ]}
            ]

    # Fallback
    else:
        if is_hindi:
            return [
                {"label": "धर्म, भाषा व साहित्य", "type": "branch", "date": "धर्म व साहित्य", "children": [
                    {"label": "प्राचीन धर्मों (हिंदू, जैन, बौद्ध) का उद्भव और ऐतिहासिक प्रसार", "type": "leaf"},
                    {"label": "संस्कृत, तमिल संगम, और विभिन्न मध्ययुगीन व आधुनिक भाषाओं का साहित्यिक विकास", "type": "leaf"}
                ]}
            ]
        else:
            return [
                {"label": "Religion & Literature Overview", "type": "branch", "date": "Overview", "children": [
                    {"label": "Chronological evolution of major religions (Hinduism, Buddhism, Jainism, Sufi Islam, Judaism, Parsis)", "type": "leaf"},
                    {"label": "Traces classical and vernacular literary outputs from Sanskrit grammar to Tamil Sangam epics", "type": "leaf"}
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
