#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import re
import json

BASE = r"upsc/ancient_history/History-of-Post-Mauryan-Period"

def get_clean_title(folder_name):
    title = folder_name.replace('-', ' ')
    skip = {'of', 'and', 'the', 'for', 'in', 'with', 'to', 'on', 'by', 'or', 'a', 'an', 'about'}
    return ' '.join(w if w.lower() in skip else w.capitalize() for w in title.split())

def get_branches(folder_name, is_hindi):
    fl = folder_name.lower()

    # 1. Shungas
    if 'shunga' in fl:
        if is_hindi:
            return [
                {"label": "शुंग वंश (185-73 ई.पू.): स्थापना", "type": "branch", "date": "185-73 BCE", "children": [
                    {"label": "पुष्यमित्र शुंग: मौर्य सेनापति; अंतिम मौर्य राजा बृहद्रथ की हत्या; नए राजवंश की स्थापना", "type": "leaf"},
                    {"label": "ब्राह्मण प्रतिक्रिया: बौद्ध धर्म के विरुद्ध; वैदिक धर्म का पुनरुद्धार; अश्वमेध यज्ञ किए", "type": "leaf"},
                    {"label": "ग्रीक आक्रमण का प्रतिरोध: इंडो-ग्रीक मेनांडर (मिलिंद) को रोका; पाटलिपुत्र की रक्षा", "type": "leaf"}
                ]},
                {"label": "शुंग काल: उपलब्धियाँ", "type": "branch", "date": "कला-संस्कृति", "children": [
                    {"label": "साँची स्तूप: तोरण द्वार (Gateways) शुंग काल में जोड़े; बौद्ध कला का विकास; अशोक का स्तूप विस्तारित", "type": "leaf"},
                    {"label": "भरहुत स्तूप: शुंग काल की प्रमुख बौद्ध कला; जातक कथाओं का चित्रण; यक्ष-यक्षिणी मूर्तियाँ", "type": "leaf"},
                    {"label": "अंतिम शासक: देवभूति (अंतिम); वासुदेव (कण्व) द्वारा हत्या; 73 ई.पू. में वंश समाप्त", "type": "leaf"}
                ]}
            ]
        else:
            return [
                {"label": "Shunga Dynasty (185-73 BCE): Foundation", "type": "branch", "date": "185-73 BCE", "children": [
                    {"label": "Pushyamitra Shunga: Mauryan army chief; killed last Maurya king Brihadratha; founded dynasty", "type": "leaf"},
                    {"label": "Brahmanical Reaction: Counter to Buddhism; Vedic revival; performed two Ashvamedha yajnas", "type": "leaf"},
                    {"label": "Resisted Indo-Greek Invasion: Blocked Menander (Milinda) from Pataliputra; defended Magadha", "type": "leaf"}
                ]},
                {"label": "Shunga Period: Achievements", "type": "branch", "date": "Arts & Culture", "children": [
                    {"label": "Sanchi Stupa: Toranas (gateways) added during Shunga period; richly carved Buddhist art", "type": "leaf"},
                    {"label": "Bharhut Stupa: Major Shunga Buddhist art; Jataka stories carved; Yaksha-Yakshini sculptures", "type": "leaf"},
                    {"label": "Decline: Devabhuti (last); killed by Vasudeva Kanva in 73 BCE; replaced by Kanva dynasty", "type": "leaf"}
                ]}
            ]

    # 2. Kanvas
    elif 'kanva' in fl:
        if is_hindi:
            return [
                {"label": "कण्व वंश (73-28 ई.पू.)", "type": "branch", "date": "73-28 BCE", "children": [
                    {"label": "वासुदेव कण्व: शुंग के मंत्री; देवभूति की हत्या करके सत्ता प्राप्त की; मगध पर शासन", "type": "leaf"},
                    {"label": "4 राजा: वासुदेव → भूमिमित्र → नारायण → सुशर्मन; कुल 45 वर्ष का शासन", "type": "leaf"},
                    {"label": "अंत: सातवाहन शासक सिमुक द्वारा 28 ई.पू. में पराजित; मगध की स्वतंत्रता का अंत", "type": "leaf"}
                ]},
                {"label": "कण्व काल: महत्व", "type": "branch", "date": "महत्व", "children": [
                    {"label": "संक्रमण काल: मौर्योत्तर विखंडन; क्षेत्रीय शक्तियों का उदय; केंद्रीय शक्ति का ह्रास", "type": "leaf"},
                    {"label": "ब्राह्मण शासन जारी: वैदिक परंपरा का समर्थन; यज्ञ-अनुष्ठान; शुंग काल की नीतियाँ", "type": "leaf"}
                ]}
            ]
        else:
            return [
                {"label": "Kanva Dynasty (73-28 BCE)", "type": "branch", "date": "73-28 BCE", "children": [
                    {"label": "Vasudeva Kanva: Shunga minister; killed Devabhuti; seized Magadha; founded Kanva dynasty", "type": "leaf"},
                    {"label": "4 Kings: Vasudeva → Bhumimitra → Narayana → Susharman; total 45 years of rule", "type": "leaf"},
                    {"label": "End: Defeated by Satavahana king Simuka in 28 BCE; end of Magadha's political significance", "type": "leaf"}
                ]},
                {"label": "Kanva Period: Significance", "type": "branch", "date": "Significance", "children": [
                    {"label": "Transitional Period: Post-Mauryan fragmentation; rise of regional powers; central authority declined", "type": "leaf"},
                    {"label": "Brahmanical Continuity: Vedic traditions supported; sacrificial rituals; continuation of Shunga policies", "type": "leaf"}
                ]}
            ]

    # 3. Chedis
    elif 'chedi' in fl:
        if is_hindi:
            return [
                {"label": "चेदि वंश (कलिंग): खारवेल", "type": "branch", "date": "1-2 शताब्दी ई.पू.", "children": [
                    {"label": "महामेघवाहन वंश: कलिंग (ओडिशा) का सबसे प्रसिद्ध राजवंश; खारवेल सबसे प्रतापी; मौर्योत्तर काल", "type": "leaf"},
                    {"label": "खारवेल की हाथीगुम्फा प्रशस्ति: भुवनेश्वर (उदयगिरि); 17 पंक्तियों में शासन का विवरण; प्राकृत भाषा में", "type": "leaf"},
                    {"label": "सैनिक अभियान: मगध से जैन प्रतिमाएँ वापस लाईं; दक्षिण भारत तक विजय; सातकर्णि को पराजित", "type": "leaf"}
                ]},
                {"label": "खारवेल के काल की उपलब्धियाँ", "type": "branch", "date": "खारवेल", "children": [
                    {"label": "जैन धर्म का संरक्षण: जैन मुनियों को आश्रय; उदयगिरि-खंडगिरि गुफाएँ; जैन कला का विकास", "type": "leaf"},
                    {"label": "कलिंग नहर: अशोक काल की नहर को पुनः खुदवाया; सिंचाई और व्यापार; प्रजाहित कार्य", "type": "leaf"},
                    {"label": "महत्व: मौर्योत्तर काल में कलिंग की स्वतंत्र शक्ति; दक्षिण-पूर्व एशिया से व्यापार", "type": "leaf"}
                ]}
            ]
        else:
            return [
                {"label": "Chedi Dynasty (Kalinga): Kharavela", "type": "branch", "date": "1st-2nd Century BCE", "children": [
                    {"label": "Mahameghavahana Dynasty: Most famous post-Mauryan dynasty of Kalinga (Odisha); Kharavela paramount", "type": "leaf"},
                    {"label": "Hathigumpha Inscription (Udayagiri): 17-line Prakrit record of Kharavela's conquests and achievements", "type": "leaf"},
                    {"label": "Military Campaigns: Retrieved Jain images from Magadha; defeated Satakari; reached south India", "type": "leaf"}
                ]},
                {"label": "Kharavela's Achievements", "type": "branch", "date": "Kharavela", "children": [
                    {"label": "Jain Patronage: Provided refuge to Jain monks; Udayagiri-Khandagiri caves; Jain art flourished", "type": "leaf"},
                    {"label": "Kalinga Canal: Re-dug the Mauryan canal; irrigation and trade; welfare work for subjects", "type": "leaf"},
                    {"label": "Significance: Independent Kalinga power in post-Mauryan era; SE Asia maritime trade", "type": "leaf"}
                ]}
            ]

    # 4. Indo-Greeks
    elif 'indo-greek' in fl or 'indo greek' in fl:
        if is_hindi:
            return [
                {"label": "इंडो-ग्रीक: उत्तर-पश्चिम भारत पर आक्रमण", "type": "branch", "date": "200-45 BCE", "children": [
                    {"label": "बैक्ट्रिया से आगमन: डेमेट्रियस (190 ई.पू.); भारत में ग्रीक शासन; पंजाब और सिंध तक विस्तार", "type": "leaf"},
                    {"label": "मेनांडर (मिलिंद) I (155-130 ई.पू.): सबसे महत्वपूर्ण; मिलिंदपन्हो — नागसेन से संवाद; बौद्ध धर्म अपनाया", "type": "leaf"},
                    {"label": "राजधानी: सागल (स्यालकोट); 'सोटर' (उद्धारकर्ता) उपाधि; न्यायपूर्ण शासन के लिए प्रसिद्ध", "type": "leaf"}
                ]},
                {"label": "इंडो-ग्रीक का भारतीय सभ्यता पर प्रभाव", "type": "branch", "date": "सांस्कृतिक प्रभाव", "children": [
                    {"label": "द्विभाषी सिक्के: ग्रीक और खरोष्ठी/ब्राह्मी लिपि; पहली बार राजाओं के चित्र सिक्कों पर; हेलेनिस्टिक कला", "type": "leaf"},
                    {"label": "गांधार कला: ग्रीक-बौद्ध शिल्प का मिश्रण; बुद्ध को यूनानी रूप में चित्रण; अपोलो जैसी शैली", "type": "leaf"},
                    {"label": "ज्योतिष: ग्रीक ज्योतिष का भारत में आगमन; राशि चक्र (Zodiac); खगोल-विज्ञान का आदान-प्रदान", "type": "leaf"}
                ]}
            ]
        else:
            return [
                {"label": "Indo-Greeks: NW India Invasions", "type": "branch", "date": "200-45 BCE", "children": [
                    {"label": "Entry from Bactria: Demetrius (190 BCE); Greek rule in India; extended to Punjab and Sindh", "type": "leaf"},
                    {"label": "Menander (Milinda) I (155-130 BCE): Most important; Milindapanha — dialogue with Nagasena; adopted Buddhism", "type": "leaf"},
                    {"label": "Capital Sagala (Sialkot): Title 'Soter' (Saviour); remembered for just and capable governance", "type": "leaf"}
                ]},
                {"label": "Indo-Greek Impact on Indian Civilization", "type": "branch", "date": "Cultural Impact", "children": [
                    {"label": "Bilingual Coins: Greek + Kharoshthi/Brahmi; first portrait coins of kings; Hellenistic artistic style", "type": "leaf"},
                    {"label": "Gandhara Art: Greco-Buddhist sculpture; Buddha depicted in Apollo-like form; drapery technique", "type": "leaf"},
                    {"label": "Astrology: Greek zodiac system entered India; Horashatra (from Horoscope); astronomical exchange", "type": "leaf"}
                ]}
            ]

    # 5. Parthians
    elif 'parthian' in fl:
        if is_hindi:
            return [
                {"label": "पार्थियन (पह्लव): भारत में शासन", "type": "branch", "date": "1 शताब्दी ई.", "children": [
                    {"label": "उत्पत्ति: ईरानी मूल के पह्लव; इंडो-ग्रीकों के बाद उत्तर-पश्चिम भारत में; गोंडोफर्निस सबसे प्रसिद्ध", "type": "leaf"},
                    {"label": "गोंडोफर्निस (20-45 CE): पार्थियन राजा; सेंट थॉमस की यात्रा से जुड़े; ईसाई धर्म का पहला भारतीय संपर्क", "type": "leaf"},
                    {"label": "राजधानी: तक्षशिला; उत्तर-पश्चिम में शासन; बाद में कुषाणों ने विस्थापित किया", "type": "leaf"}
                ]},
                {"label": "पार्थियन शासन का महत्व", "type": "branch", "date": "महत्व", "children": [
                    {"label": "व्यापार: रेशम मार्ग पर नियंत्रण; रोम और भारत के बीच मध्यस्थ; व्यापार से समृद्धि", "type": "leaf"},
                    {"label": "सांस्कृतिक प्रभाव: ईरानी वास्तुकला तत्व; सिक्कों पर ईरानी शैली; भारत-ईरान सांस्कृतिक संबंध", "type": "leaf"}
                ]}
            ]
        else:
            return [
                {"label": "Parthians (Pahlavas): Rule in India", "type": "branch", "date": "1st Century CE", "children": [
                    {"label": "Origin: Iranian-origin Pahlavas; succeeded Indo-Greeks in NW India; Gondophernes most famous", "type": "leaf"},
                    {"label": "Gondophernes (20-45 CE): Parthian king; associated with Saint Thomas's India mission; earliest Christian contact", "type": "leaf"},
                    {"label": "Capital Taxila: Ruled NW India; later displaced by Kushanas; transitional period", "type": "leaf"}
                ]},
                {"label": "Parthian Rule: Significance", "type": "branch", "date": "Significance", "children": [
                    {"label": "Trade: Controlled Silk Route; intermediary between Rome and India; trade-derived prosperity", "type": "leaf"},
                    {"label": "Cultural Impact: Iranian architectural elements; Iranian numismatic style; India-Iran cultural relations", "type": "leaf"}
                ]}
            ]

    # 6. Sakas
    elif 'saka' in fl:
        if is_hindi:
            return [
                {"label": "शक: भारत पर आक्रमण और शासन", "type": "branch", "date": "2 ई.पू. - 4 ई.", "children": [
                    {"label": "उत्पत्ति: मध्य एशिया के Scythian; इंडो-ग्रीकों के बाद; 5 शाखाएँ — उत्तरापथ, पश्चिमी, दक्षिणी आदि", "type": "leaf"},
                    {"label": "पश्चिमी क्षत्रप: उज्जैन केंद्र; रुद्रदामन I (130-150 CE) सबसे महत्वपूर्ण; जूनागढ़ अभिलेख; सुदर्शन झील की मरम्मत", "type": "leaf"},
                    {"label": "रुद्रदामन I: पहले शुद्ध संस्कृत अभिलेख के लेखक; सातवाहनों को पराजित किया; संस्कृत साहित्य का संरक्षण", "type": "leaf"}
                ]},
                {"label": "शक शासन का अंत और प्रभाव", "type": "branch", "date": "अंत", "children": [
                    {"label": "चंद्रगुप्त II 'विक्रमादित्य' द्वारा समाप्त: 388-409 CE; 'शकारि' उपाधि; पश्चिम भारत गुप्त साम्राज्य में", "type": "leaf"},
                    {"label": "शक संवत् (78 CE): राष्ट्रीय कैलेंडर का आधार; अभी भी भारत सरकार का आधिकारिक कैलेंडर", "type": "leaf"},
                    {"label": "सांस्कृतिक प्रभाव: मध्य एशियाई घुड़सवारी; लंबे कोट (कफ्तान) शैली; रत्न-जड़ित आभूषण", "type": "leaf"}
                ]}
            ]
        else:
            return [
                {"label": "Sakas: Invasion and Rule in India", "type": "branch", "date": "2 BCE - 4 CE", "children": [
                    {"label": "Origin: Central Asian Scythians; succeeded Indo-Greeks; 5 branches — Taxila, Mathura, Ujjain, Nasik, Gujarat", "type": "leaf"},
                    {"label": "Western Kshatrapas: Ujjain centre; Rudradaman I (130-150 CE) most important; Junagadh inscription", "type": "leaf"},
                    {"label": "Rudradaman I: First pure Sanskrit inscription (Junagadh); defeated Satavahanas; repaired Sudarsana Lake", "type": "leaf"}
                ]},
                {"label": "End of Saka Rule & Impact", "type": "branch", "date": "Legacy", "children": [
                    {"label": "Destroyed by Chandragupta II 'Vikramaditya' (388-409 CE): Title 'Shakari'; W. India absorbed into Guptas", "type": "leaf"},
                    {"label": "Shaka Samvat (78 CE): Basis of India's National Calendar; still official Government of India calendar", "type": "leaf"},
                    {"label": "Cultural Legacy: Central Asian equestrian culture; long-coat style; gem-studded jewellery traditions", "type": "leaf"}
                ]}
            ]

    # 7. Satavahanas
    elif 'satavahana' in fl:
        if is_hindi:
            return [
                {"label": "सातवाहन वंश: दक्कन का सबसे महत्वपूर्ण राजवंश", "type": "branch", "date": "230 BCE - 220 CE", "children": [
                    {"label": "स्थापना: सिमुक द्वारा; कण्व वंश को पराजित कर मगध पर अस्थायी कब्जा; मुख्य क्षेत्र: दक्कन और आंध्र", "type": "leaf"},
                    {"label": "गौतमीपुत्र शातकर्णि (106-130 CE): सबसे महान; शकों को पराजित; 'त्रिसमुद्रतोयपीत' उपाधि; नाशिक प्रशस्ति", "type": "leaf"},
                    {"label": "वाशिष्ठीपुत्र पुलुमावी: गौतमीपुत्र के उत्तराधिकारी; रुद्रदामन I से वैवाहिक संबंध; अमरावती के संरक्षक", "type": "leaf"}
                ]},
                {"label": "सातवाहन: अर्थव्यवस्था, कला और संस्कृति", "type": "branch", "date": "उपलब्धियाँ", "children": [
                    {"label": "विदेश व्यापार: रोमन साम्राज्य से; मसाले, कपास, हाथीदांत; पश्चिमी बंदरगाह — भड़ौच, सोपारा", "type": "leaf"},
                    {"label": "अमरावती और नागार्जुनकोंड स्तूप: उत्कृष्ट बौद्ध कला; संगमरमर की नक्काशी; UPSC महत्वपूर्ण", "type": "leaf"},
                    {"label": "भाषा-साहित्य: प्राकृत भाषा; गाथासप्तशती (हाल द्वारा); पहला ज्ञात प्राकृत काव्य संग्रह", "type": "leaf"}
                ]}
            ]
        else:
            return [
                {"label": "Satavahana Dynasty: Most Important Post-Mauryan Deccan Power", "type": "branch", "date": "230 BCE - 220 CE", "children": [
                    {"label": "Founded by Simuka: Defeated Kanva dynasty; main territory Deccan and Andhra; 'Dakshinapatha' rulers", "type": "leaf"},
                    {"label": "Gautamiputra Satakarni (106-130 CE): Greatest; defeated Sakas; title 'Trisamudratoyapita'; Nashik inscription", "type": "leaf"},
                    {"label": "Vasishthiputra Pulumavi: Successor; matrimonial alliance with Rudradaman I; Amaravati patronage", "type": "leaf"}
                ]},
                {"label": "Satavahanas: Economy, Art & Culture", "type": "branch", "date": "Achievements", "children": [
                    {"label": "Foreign Trade: Roman Empire; spices, cotton, ivory; western ports — Bharuch (Broach), Sopara", "type": "leaf"},
                    {"label": "Amaravati & Nagarjunakonda Stupas: Outstanding Buddhist art; marble carving; highly important for UPSC", "type": "leaf"},
                    {"label": "Language & Literature: Prakrit language; Gathasaptashati (by King Hala); earliest Prakrit anthology", "type": "leaf"}
                ]}
            ]

    # 8. Kushans
    elif 'kushan' in fl and 'kanishka' not in fl:
        if is_hindi:
            return [
                {"label": "कुषाण वंश: मध्य एशिया से भारत तक", "type": "branch", "date": "1-3 शताब्दी CE", "children": [
                    {"label": "उत्पत्ति: Yuezhi जनजाति (चीनी तुर्किस्तान); बैक्ट्रिया होते हुए भारत में; कुजुल कडफिसेस — संस्थापक", "type": "leaf"},
                    {"label": "कुजुल कडफिसेस: पहले कुषाण राजा; मध्य-एशिया से उत्तर-पश्चिम भारत तक; ग्रीक और भारतीय सिक्के जारी", "type": "leaf"},
                    {"label": "विमा कडफिसेस: शिव-भक्त; सोने के सिक्के जारी; भारत में स्वर्ण-मुद्रा का पुनर्प्रवर्तन", "type": "leaf"}
                ]},
                {"label": "कुषाण साम्राज्य: विस्तार और व्यापार", "type": "branch", "date": "साम्राज्य", "children": [
                    {"label": "साम्राज्य विस्तार: अफगानिस्तान, पाकिस्तान, उत्तर भारत, मध्य एशिया; 'रेशम मार्ग' पर नियंत्रण", "type": "leaf"},
                    {"label": "व्यापार: चीन-रोम-भारत त्रिकोण; मसाले, कपास, रत्न; कुषाण मुद्राएँ — व्यापक प्रसार", "type": "leaf"}
                ]}
            ]
        else:
            return [
                {"label": "Kushan Dynasty: From Central Asia to India", "type": "branch", "date": "1st-3rd Century CE", "children": [
                    {"label": "Origin: Yuezhi tribe (Chinese Turkestan); via Bactria into India; Kujula Kadphises — founder", "type": "leaf"},
                    {"label": "Kujula Kadphises: First Kushan king; NW India conquest; issued Greek and Indian-style coins", "type": "leaf"},
                    {"label": "Vima Kadphises: Shaivite; issued gold coins; re-introduced gold coinage in India on large scale", "type": "leaf"}
                ]},
                {"label": "Kushan Empire: Expansion & Trade", "type": "branch", "date": "Empire", "children": [
                    {"label": "Extent: Afghanistan, Pakistan, N. India, Central Asia; controlled the Silk Route between China and Rome", "type": "leaf"},
                    {"label": "Trade: China-Rome-India triangle; spices, cotton, gems; Kushan coins had wide circulation", "type": "leaf"}
                ]}
            ]

    # 9. Kushans Kanishka's Rule
    elif 'kanishka' in fl:
        if is_hindi:
            return [
                {"label": "कनिष्क (78-101 CE): कुषाण वंश का शिखर", "type": "branch", "date": "78-101 CE", "children": [
                    {"label": "महान बौद्ध संरक्षक: चौथी बौद्ध संगीति (कश्मीर); महायान बौद्ध धर्म का प्रसार; अश्वघोष दरबारी कवि", "type": "leaf"},
                    {"label": "शक संवत् (78 CE): कुछ विद्वान कनिष्क से जोड़ते हैं; भारत का राष्ट्रीय कैलेंडर", "type": "leaf"},
                    {"label": "साम्राज्य: पाटलिपुत्र से मध्य एशिया तक; कश्मीर और अफगानिस्तान; चीन से युद्ध; ग्रीष्मकालीन राजधानी कनिष्कपुर", "type": "leaf"}
                ]},
                {"label": "कनिष्क: कला, साहित्य और विरासत", "type": "branch", "date": "सांस्कृतिक योगदान", "children": [
                    {"label": "गांधार कला का चरमोत्कर्ष: यूनानी-रोमन-भारतीय शैली का मिश्रण; पेशावर स्तूप; बुद्ध की मूर्तियाँ", "type": "leaf"},
                    {"label": "दरबारी विद्वान: अश्वघोष (बुद्धचरित); नागार्जुन (माध्यमिक दर्शन); वसुमित्र; चरक (चरकसंहिता)", "type": "leaf"},
                    {"label": "सिक्के: बहु-धार्मिक; शिव, बुद्ध, ग्रीक, ईरानी देवता एक साथ; धार्मिक सहिष्णुता का प्रतीक", "type": "leaf"}
                ]}
            ]
        else:
            return [
                {"label": "Kanishka (78-101 CE): Zenith of Kushan Dynasty", "type": "branch", "date": "78-101 CE", "children": [
                    {"label": "Great Buddhist Patron: 4th Buddhist Council (Kashmir); spread of Mahayana Buddhism; Ashvaghosha court poet", "type": "leaf"},
                    {"label": "Shaka Era (78 CE): Some scholars attribute to Kanishka; India's National Calendar basis", "type": "leaf"},
                    {"label": "Empire: Pataliputra to Central Asia; Kashmir, Afghanistan; summer capital at Kanishkapura (Peshawar)", "type": "leaf"}
                ]},
                {"label": "Kanishka: Art, Literature & Legacy", "type": "branch", "date": "Cultural Contributions", "children": [
                    {"label": "Peak of Gandhara Art: Greek-Roman-Indian synthesis; Peshawar stupa; Buddha sculptures in Apollo style", "type": "leaf"},
                    {"label": "Court Scholars: Ashvaghosha (Buddhacharita); Nagarjuna (Madhyamika philosophy); Charaka (Charakasamhita)", "type": "leaf"},
                    {"label": "Coins: Multi-religious — Shiva, Buddha, Greek, Iranian deities together; symbol of religious tolerance", "type": "leaf"}
                ]}
            ]

    # Fallback
    else:
        if is_hindi:
            return [{"label": "मौर्योत्तर काल", "type": "branch", "date": "200 BCE - 300 CE", "children": [
                {"label": "मौर्य साम्राज्य के बाद भारत में क्षेत्रीय शक्तियों का उदय", "type": "leaf"}]}]
        else:
            return [{"label": "Post-Mauryan Period", "type": "branch", "date": "200 BCE - 300 CE", "children": [
                {"label": "Rise of regional powers in India after Mauryan Empire's decline", "type": "leaf"}]}]

def process_file(html_path, is_hindi):
    print(f"Processing: {html_path} (hindi={is_hindi})")
    with open(html_path, 'r', encoding='utf-8') as f:
        html = f.read()
    html = html.replace('\r\n', '\n')
    for old in ['    <link rel="stylesheet" href="/assets/css/mindmap.min.css?v=2">\n',
                '    <link rel="stylesheet" href="/assets/css/mindmap.min.css?v=1">\n',
                '    <link rel="stylesheet" href="/assets/css/mindmap.min.css">\n']:
        html = html.replace(old, '')
    html = re.sub(r'\s*<!-- Interactive Mindmap -->.*?<!-- Deep-Dive Study Guide \(Dynamically Rendered\) -->', '\n            <!-- Deep-Dive Study Guide (Dynamically Rendered) -->', html, flags=re.DOTALL)
    html = re.sub(r'\s*<!-- Interactive Mindmap -->.*?renderMindmap\(.*?\);\s*</script>', '', html, flags=re.DOTALL)

    folder_name = os.path.basename(os.path.dirname(html_path))
    if folder_name == 'hi':
        folder_name = os.path.basename(os.path.dirname(os.path.dirname(html_path)))

    clean_title = get_clean_title(folder_name)
    topic_name = clean_title
    cj = os.path.join(os.path.dirname(html_path), "content.json")
    if os.path.exists(cj):
        try:
            topic_name = json.load(open(cj, encoding='utf-8')).get('hero', {}).get('title', topic_name)
        except Exception:
            pass

    branches = get_branches(folder_name, is_hindi)
    mindmap_data = {"label": clean_title, "type": "root", "children": branches}

    css_link = '    <link rel="stylesheet" href="/assets/css/mindmap.min.css?v=2">\n'
    if css_link not in html:
        html = html.replace('</head>', css_link + '</head>')

    if is_hindi:
        instr = 'किसी <strong style="color:#a78bfa;">बैंगनी</strong> या <strong style="color:#2ecc71;">हरे</strong> <strong>+</strong> पर क्लिक करें।'
        title_text = f"{topic_name} &mdash; इंटरैक्टिव माइंडमैप"
    else:
        instr = 'Tap a <strong style="color:#a78bfa;">purple</strong> or <strong style="color:#2ecc71;">green</strong> <strong>+</strong> to expand.'
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
    if re.search(r'<!-- Deep-Dive Study Guide \(Dynamically Rendered\) -->\s*<div class="card-premium" id="deep-dive-section">', html):
        html = re.sub(r'(<!-- Deep-Dive Study Guide \(Dynamically Rendered\) -->\s*<div class="card-premium" id="deep-dive-section">)', mindmap_card + r'\1', html)
    else:
        marker = '<div class="tab-panel active" id="notes-panel" role="tabpanel" aria-labelledby="notes-panel">'
        if marker in html:
            html = html.replace(marker, marker + '\n' + mindmap_card, 1)

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

def main():
    total = 0
    for root, dirs, files in os.walk(BASE):
        parts = os.path.relpath(root, BASE).split(os.sep)
        is_hindi = 'hi' in parts
        for file in files:
            if file == "index.html":
                process_file(os.path.join(root, file), is_hindi)
                total += 1
    print(f"\nDone! Patched {total} files.")

if __name__ == '__main__':
    main()
