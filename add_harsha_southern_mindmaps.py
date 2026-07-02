#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import re
import json

BASE = r"upsc/ancient_history/Harshvardhan-and-Southern-Dynasties"

def get_clean_title(folder_name):
    title = folder_name.replace('-', ' ')
    skip = {'of', 'and', 'the', 'for', 'in', 'with', 'to', 'on', 'by', 'or', 'a', 'an', 'about'}
    return ' '.join(w if w.lower() in skip else w.capitalize() for w in title.split())

def get_branches(rel_path, is_hindi):
    """rel_path is relative to BASE, e.g. 'Administration' or 'Pallavas.../Administration'"""
    rp = rel_path.replace('\\', '/').lower()
    is_pallava = 'pallava' in rp or 'chalukya' in rp

    # ── HARSHA SUBTOPICS ────────────────────────────────────────────────────

    if 'military' in rp:
        if is_hindi:
            return [
                {"label": "हर्षवर्धन की सैन्य विजयें", "type": "branch", "date": "606-647 CE", "children": [
                    {"label": "उत्तरी भारत का एकीकरण: थानेश्वर + कन्नौज; भाई राज्यवर्धन की मृत्यु का बदला; शशांक (गौड़) से संघर्ष", "type": "leaf"},
                    {"label": "पंजाब, उत्तर प्रदेश, बिहार, बंगाल, उड़ीसा पर अधिकार; विंध्याचल तक साम्राज्य; 'उत्तरापथ का स्वामी'", "type": "leaf"},
                    {"label": "दक्कन में असफलता: चालुक्य राजा पुलकेशिन II ने नर्मदा के तट पर हर्ष को रोका (618-619 CE); दक्षिण विजय नाकाम", "type": "leaf"},
                    {"label": "पाँच हाथी और पचास हजार पैदल सेना; घोड़े और हाथियों की सेना; व्यूह-रचना में दक्षता", "type": "leaf"}
                ]},
                {"label": "कूटनीतिक संबंध", "type": "branch", "date": "कूटनीति", "children": [
                    {"label": "चीन से दूत विनिमय: ह्वेनसांग की यात्रा (629-645 CE); चीनी सम्राट तांग के साथ संबंध", "type": "leaf"},
                    {"label": "कन्नौज सम्मेलन (643 CE): ह्वेनसांग की उपस्थिति; हर्ष की कूटनीतिक शक्ति का प्रदर्शन", "type": "leaf"}
                ]}
            ]
        else:
            return [
                {"label": "Harshvardhan's Military Conquests", "type": "branch", "date": "606-647 CE", "children": [
                    {"label": "North India Unification: Merged Thaneshwar + Kannauj; avenged brother Rajyavardhana's murder by Shashanka (Gauda)", "type": "leaf"},
                    {"label": "Controlled Punjab, UP, Bihar, Bengal, Odisha; empire up to Vindhyas; called 'Lord of Uttarapatha'", "type": "leaf"},
                    {"label": "Southern Failure: Chalukya king Pulakesi II blocked Harsha at Narmada (618-619 CE); could not cross into Deccan", "type": "leaf"},
                    {"label": "Army: 5 lakh infantry, 50,000 cavalry, 60,000 war elephants; expert battle formations", "type": "leaf"}
                ]},
                {"label": "Diplomatic Relations", "type": "branch", "date": "Diplomacy", "children": [
                    {"label": "China Exchange: Huien Tsang visited (629-645 CE); envoys sent to Tang Emperor; cultural diplomacy", "type": "leaf"},
                    {"label": "Kannauj Assembly (643 CE): Grand religious assembly witnessed by Huien Tsang; Buddhist diplomacy", "type": "leaf"}
                ]}
            ]

    elif not is_pallava and 'administration' in rp:
        if is_hindi:
            return [
                {"label": "हर्ष का प्रशासन: केंद्रीय ढाँचा", "type": "branch", "date": "शासन व्यवस्था", "children": [
                    {"label": "राजपद: हर्ष स्वयं सर्वोच्च; लेकिन सामंती प्रवृत्ति; सामंत राजाओं को स्वायत्तता", "type": "leaf"},
                    {"label": "मंत्री: अवंतिनी (महाप्रतीहार); सिंहनाद (महाबलाधिकृत); प्रमुख मंत्री परिषद", "type": "leaf"},
                    {"label": "ह्वेनसांग का विवरण: राजा भ्रमण पर; प्रजा सुखी; दंड-विधान सौम्य; कारागार लगभग नहीं", "type": "leaf"}
                ]},
                {"label": "राजस्व और स्थानीय प्रशासन", "type": "branch", "date": "राजस्व", "children": [
                    {"label": "भूमि कर: उपज का 1/6 भाग; बलि और भाग; गुप्त काल की परंपरा जारी", "type": "leaf"},
                    {"label": "विषय (जिला): विषयपति द्वारा; नगर प्रशासन: नगरपति; ग्राम: ग्रामभोजक", "type": "leaf"},
                    {"label": "प्रत्येक 5 वर्ष में प्रयाग महामोक्षपरिषद: अपार दान; बाद में स्वयं वस्त्रहीन", "type": "leaf"}
                ]}
            ]
        else:
            return [
                {"label": "Harsha's Administration: Central Structure", "type": "branch", "date": "Governance", "children": [
                    {"label": "Kingship: Harsha supreme but feudal tendencies; vassal kings given autonomy within empire", "type": "leaf"},
                    {"label": "Ministers: Avantini (Mahapratihara); Simhanada (Mahabaladhikrita); key council of ministers", "type": "leaf"},
                    {"label": "Huien Tsang's Account: King toured constantly; people prosperous; punishment mild; few prisons", "type": "leaf"}
                ]},
                {"label": "Revenue & Local Administration", "type": "branch", "date": "Revenue", "children": [
                    {"label": "Land Tax: 1/6 of produce (Bali and Bhaga); continuation of Gupta tradition", "type": "leaf"},
                    {"label": "Vishaya (District): Vishayapati; Nagarapati (urban); Gramabhojaka (village headman)", "type": "leaf"},
                    {"label": "Prayaga Mahamokshaparishad every 5 years: Massive charity; Harsha gave away even his own clothes", "type": "leaf"}
                ]}
            ]

    elif not is_pallava and 'economy' in rp:
        if is_hindi:
            return [
                {"label": "हर्ष कालीन अर्थव्यवस्था", "type": "branch", "date": "अर्थव्यवस्था", "children": [
                    {"label": "कृषि प्रधान: धान, गेहूँ, गन्ना; भूमि अनुदान जारी; ब्राह्मणों और बौद्ध मठों को भूमि दान", "type": "leaf"},
                    {"label": "व्यापार: गंगा-जमुना मार्ग; कन्नौज प्रमुख व्यापार केंद्र; विदेशी व्यापार में कमी (गुप्त काल की तुलना में)", "type": "leaf"},
                    {"label": "श्रेणियाँ (Guilds) कमजोर पड़ीं: सामंतवाद बढ़ा; स्थानीय आत्मनिर्भरता; मुद्रा अर्थव्यवस्था सीमित हुई", "type": "leaf"}
                ]},
                {"label": "हर्ष की दानशीलता", "type": "branch", "date": "दान", "children": [
                    {"label": "प्रयाग सम्मेलन: प्रत्येक 5 वर्ष; विशाल दान; ह्वेनसांग के अनुसार राज्य की सभी संपदा वितरित", "type": "leaf"},
                    {"label": "राज्य व्यय: 1/4 राज्य रक्षा; 1/4 मंत्री-अधिकारी वेतन; 1/4 विद्वानों को; 1/4 दान — ह्वेनसांग का विभाजन", "type": "leaf"}
                ]}
            ]
        else:
            return [
                {"label": "Harsha's Economy", "type": "branch", "date": "Economy", "children": [
                    {"label": "Agriculture Dominant: Rice, wheat, sugarcane; land grants to Brahmins and Buddhist monasteries continued", "type": "leaf"},
                    {"label": "Trade: Ganga-Yamuna routes; Kannauj as main hub; foreign trade declined compared to Gupta era", "type": "leaf"},
                    {"label": "Guilds Weakened: Feudalism rose; local self-sufficiency; monetized economy contracted", "type": "leaf"}
                ]},
                {"label": "Harsha's Philanthropy", "type": "branch", "date": "Charity", "children": [
                    {"label": "Prayaga Assembly (every 5 yrs): Massive charity distribution; Huien Tsang: Harsha gave away all royal wealth", "type": "leaf"},
                    {"label": "State Expenditure Split: 1/4 defense; 1/4 officials; 1/4 scholars; 1/4 charity — per Huien Tsang", "type": "leaf"}
                ]}
            ]

    elif not is_pallava and 'society' in rp:
        if is_hindi:
            return [
                {"label": "हर्ष कालीन समाज", "type": "branch", "date": "समाज", "children": [
                    {"label": "वर्ण व्यवस्था: अधिक कठोर; जाति-प्रथा जटिल; ब्राह्मण वर्चस्व बढ़ा; भूमि अनुदान से शक्तिशाली", "type": "leaf"},
                    {"label": "महिलाएँ: कुछ उच्च वर्ग की महिलाएँ शिक्षित; सती और बाल-विवाह प्रचलित; पर्दा-प्रथा नहीं", "type": "leaf"},
                    {"label": "ह्वेनसांग: लोग शांतिप्रिय; शाकाहारी प्रचलित; गाय की हत्या निषिद्ध; व्यापारी ईमानदार", "type": "leaf"}
                ]},
                {"label": "संस्कृति और शिक्षा", "type": "branch", "date": "संस्कृति", "children": [
                    {"label": "नालंदा विश्वविद्यालय: हर्ष का संरक्षण; 10,000 छात्र; 1,500 अध्यापक; ह्वेनसांग ने अध्ययन किया; बहुविषयक", "type": "leaf"},
                    {"label": "हर्ष की साहित्यिक कृतियाँ: नागानंद, रत्नावली, प्रियदर्शिका (संस्कृत नाटक); 'कविराज' उपाधि", "type": "leaf"},
                    {"label": "बाणभट्ट: हर्षचरित और कादंबरी; हर्ष का दरबारी कवि; संस्कृत गद्य का स्वर्ण युग", "type": "leaf"}
                ]}
            ]
        else:
            return [
                {"label": "Harsha's Society", "type": "branch", "date": "Society", "children": [
                    {"label": "Varna System: More rigid; caste complexity grew; Brahmins powerful through land grants", "type": "leaf"},
                    {"label": "Women: Upper-class women educated; Sati and child marriage prevalent; no purdah yet", "type": "leaf"},
                    {"label": "Huien Tsang: People peaceful; vegetarianism common; cow slaughter prohibited; honest traders", "type": "leaf"}
                ]},
                {"label": "Culture & Education", "type": "branch", "date": "Culture", "children": [
                    {"label": "Nalanda University: Harsha's patronage; 10,000 students; 1,500 teachers; Huien Tsang studied here", "type": "leaf"},
                    {"label": "Harsha's Literary Works: Nagananda, Ratnavali, Priyadarshika (Sanskrit plays); titled 'Kaviraja'", "type": "leaf"},
                    {"label": "Banabhatta: Harshacharita and Kadambari; court poet; golden age of Sanskrit prose literature", "type": "leaf"}
                ]}
            ]

    elif not is_pallava and 'religion' in rp and 'buddhism' not in rp:
        if is_hindi:
            return [
                {"label": "हर्ष की धार्मिक नीति", "type": "branch", "date": "धर्म", "children": [
                    {"label": "शैव से बौद्ध परिवर्तन: प्रारंभ में शिव-भक्त; फिर ह्वेनसांग के प्रभाव में बौद्ध धर्म स्वीकार; महायान शाखा", "type": "leaf"},
                    {"label": "धार्मिक सहिष्णुता: ब्राह्मण, बौद्ध, जैन सभी को संरक्षण; कन्नौज सम्मेलन में बौद्ध विद्वान; सर्वधर्म समभाव", "type": "leaf"},
                    {"label": "गो-हत्या पर प्रतिबंध: पूरे साम्राज्य में; अहिंसा का प्रसार; बौद्ध प्रभाव स्पष्ट", "type": "leaf"}
                ]},
                {"label": "धार्मिक सम्मेलन", "type": "branch", "date": "सम्मेलन", "children": [
                    {"label": "कन्नौज सम्मेलन (643 CE): महायान बौद्ध धर्म का समर्थन; 18 राजा; 3000 भिक्षु; ह्वेनसांग ने विजय की घोषणा की", "type": "leaf"},
                    {"label": "प्रयाग सम्मेलन: प्रत्येक 5 वर्ष; पंचवर्षीय दान; चार धर्मों को एक साथ संरक्षण दिया", "type": "leaf"}
                ]}
            ]
        else:
            return [
                {"label": "Harsha's Religious Policy", "type": "branch", "date": "Religion", "children": [
                    {"label": "Shaiva to Buddhist: Initially Shaivite; converted to Mahayana Buddhism under Huien Tsang's influence", "type": "leaf"},
                    {"label": "Religious Tolerance: Patronage to Brahmins, Buddhists, Jains; Kannauj assembly hosted all scholars", "type": "leaf"},
                    {"label": "Cow Slaughter Banned: Throughout empire; spread of Ahimsa; clear Buddhist influence on policy", "type": "leaf"}
                ]},
                {"label": "Religious Assemblies", "type": "branch", "date": "Assemblies", "children": [
                    {"label": "Kannauj Assembly (643 CE): 18 kings; 3000 monks; Huien Tsang proclaimed Mahayana victory; grandest assembly", "type": "leaf"},
                    {"label": "Prayag Assembly (every 5 yrs): Charity to all four religions; symbol of Harsha's syncretic approach", "type": "leaf"}
                ]}
            ]

    elif 'buddhism' in rp:
        if is_hindi:
            return [
                {"label": "हर्ष और बौद्ध धर्म", "type": "branch", "date": "बौद्ध संरक्षण", "children": [
                    {"label": "महायान बौद्ध धर्म: हर्ष ने अपनाया; बोधिसत्व की अवधारणा; बुद्ध की मूर्तियाँ; स्तूप निर्माण", "type": "leaf"},
                    {"label": "नालंदा को दान: 100+ गाँव दान; महाविहार का विस्तार; ह्वेनसांग को विशेष सुविधाएँ", "type": "leaf"},
                    {"label": "ह्वेनसांग की यात्रा: 629-645 CE; 17 वर्ष भारत में; Si-Yu-Ki (पश्चिमी देशों का वृत्तांत); बौद्ध ग्रंथों की खोज", "type": "leaf"}
                ]},
                {"label": "ह्वेनसांग के अवलोकन और हर्ष का योगदान", "type": "branch", "date": "ह्वेनसांग", "children": [
                    {"label": "ह्वेनसांग: हर्ष न्यायी, उदार, कुशल शासक; गाँव समृद्ध; रात्रि में चोरी नहीं होती; मृत्युदंड नहीं", "type": "leaf"},
                    {"label": "कन्नौज बौद्ध सभा: हर्ष की अध्यक्षता; ह्वेनसांग मुख्य वक्ता; हिनायान बौद्धों ने विरोध; 'महायान सूर्य' उपाधि", "type": "leaf"},
                    {"label": "बौद्ध धर्म का प्रसार: हर्ष के काल में उत्तर भारत में; लेकिन इसके बाद गिरावट आरंभ; इस्लाम का आगमन", "type": "leaf"}
                ]}
            ]
        else:
            return [
                {"label": "Harsha and Buddhism", "type": "branch", "date": "Buddhist Patronage", "children": [
                    {"label": "Mahayana Buddhism: Harsha's adopted faith; Bodhisattva concept; Buddha images; stupa construction", "type": "leaf"},
                    {"label": "Nalanda Donations: 100+ villages donated; expanded Mahavihara; special hospitality to Huien Tsang", "type": "leaf"},
                    {"label": "Huien Tsang's Visit: 629-645 CE; 17 years in India; Si-Yu-Ki record; Buddhist text collection", "type": "leaf"}
                ]},
                {"label": "Huien Tsang's Observations & Harsha's Legacy", "type": "branch", "date": "Huien Tsang", "children": [
                    {"label": "Huien Tsang: Harsha just, generous, able ruler; villages prosperous; no theft at night; no capital punishment", "type": "leaf"},
                    {"label": "Kannauj Buddhist Assembly: Harsha presided; Huien Tsang main speaker; Hinayana opponents; 'Sun of Mahayana'", "type": "leaf"},
                    {"label": "Buddhism's Spread: Last great Buddhist royal patronage in North India; decline began after Harsha's death", "type": "leaf"}
                ]}
            ]

    elif not is_pallava and 'art' in rp:
        if is_hindi:
            return [
                {"label": "हर्ष कालीन कला और स्थापत्य", "type": "branch", "date": "कला", "children": [
                    {"label": "सीमित स्थायी स्मारक: हर्ष का काल संक्रमण का; गुप्त शैली जारी; पत्थर की बजाय लकड़ी और ईंट का अधिक उपयोग", "type": "leaf"},
                    {"label": "बौद्ध विहार और स्तूप: नालंदा का विस्तार; हर्ष द्वारा नए स्तूप; ह्वेनसांग के अनुसार हजारों मठ", "type": "leaf"},
                    {"label": "कन्नौज: राजधानी; गंगा तट पर; भव्य महल और मंदिर; ह्वेनसांग ने भव्यता का वर्णन किया", "type": "leaf"}
                ]},
                {"label": "साहित्यिक कला", "type": "branch", "date": "साहित्य", "children": [
                    {"label": "हर्षचरित (बाणभट्ट): संस्कृत गद्य की सर्वोत्तम कृति; हर्ष की जीवनी; उच्चारण शैली अलंकृत", "type": "leaf"},
                    {"label": "हर्ष के नाटक: नागानंद (बौद्ध कथा), रत्नावली, प्रियदर्शिका (श्रृंगार नाटिका); संस्कृत नाट्य परंपरा जारी", "type": "leaf"}
                ]}
            ]
        else:
            return [
                {"label": "Harsha's Art & Architecture", "type": "branch", "date": "Art", "children": [
                    {"label": "Limited Monuments: Transitional period; Gupta style continued; wood and brick over stone preferred", "type": "leaf"},
                    {"label": "Buddhist Viharas & Stupas: Nalanda expansion; new stupas by Harsha; Huien Tsang: thousands of monasteries", "type": "leaf"},
                    {"label": "Kannauj Capital: On Ganga banks; grand palaces and temples; Huien Tsang described its splendour", "type": "leaf"}
                ]},
                {"label": "Literary Arts", "type": "branch", "date": "Literature", "children": [
                    {"label": "Harshacharita (Banabhatta): Finest Sanskrit prose; Harsha's biography; ornate style (Mahakavya)", "type": "leaf"},
                    {"label": "Harsha's Plays: Nagananda (Buddhist tale); Ratnavali, Priyadarshika (romantic plays); Sanskrit drama continued", "type": "leaf"}
                ]}
            ]

    # ── PALLAVA & CHALUKYA SUBTOPICS ─────────────────────────────────────

    elif is_pallava and 'administration' in rp:
        if is_hindi:
            return [
                {"label": "पल्लव प्रशासन (कांची)", "type": "branch", "date": "पल्लव", "children": [
                    {"label": "राजतंत्र: पल्लव राजा — महेंद्रवर्मन I, नरसिंहवर्मन I; 'महामल्ल' उपाधि; देवीय अधिकार का सिद्धांत", "type": "leaf"},
                    {"label": "कांची राजधानी: प्रशासनिक और सांस्कृतिक केंद्र; मंत्रिपरिषद; स्थानीय नाडु (क्षेत्र) व्यवस्था", "type": "leaf"},
                    {"label": "सभा और उर: ब्राह्मण गाँव में सभा; व्यापारी गाँव में उर; स्वशासन; कर वसूली; स्थानीय न्याय", "type": "leaf"}
                ]},
                {"label": "चालुक्य प्रशासन (बादामी)", "type": "branch", "date": "चालुक्य", "children": [
                    {"label": "पुलकेशिन II: बादामी चालुक्य; सबसे शक्तिशाली; हर्ष को नर्मदा पर रोका; ऐहोल अभिलेख में विजयों का वर्णन", "type": "leaf"},
                    {"label": "सामंत व्यवस्था: महामंडलेश्वर (बड़े सामंत); मंडलेश्वर (छोटे); केंद्रीय सत्ता के अधीन; युद्ध में सेना देते थे", "type": "leaf"}
                ]}
            ]
        else:
            return [
                {"label": "Pallava Administration (Kanchi)", "type": "branch", "date": "Pallavas", "children": [
                    {"label": "Monarchy: Pallava kings — Mahendravarman I, Narasimhavarman I 'Mamalla'; divine right theory", "type": "leaf"},
                    {"label": "Kanchi Capital: Administrative and cultural centre; council of ministers; Nadu (regional) system", "type": "leaf"},
                    {"label": "Sabha & Ur: Brahmin village assemblies (Sabha); merchant village assemblies (Ur); self-governance", "type": "leaf"}
                ]},
                {"label": "Chalukya Administration (Badami)", "type": "branch", "date": "Chalukyas", "children": [
                    {"label": "Pulakesi II: Most powerful Badami Chalukya; blocked Harsha at Narmada; Aihole inscription details victories", "type": "leaf"},
                    {"label": "Feudal System: Mahamandalesvaras (great feudatories); Mandalesvaras (lesser); provided troops to king", "type": "leaf"}
                ]}
            ]

    elif is_pallava and 'economy' in rp:
        if is_hindi:
            return [
                {"label": "पल्लव अर्थव्यवस्था", "type": "branch", "date": "पल्लव", "children": [
                    {"label": "कृषि: नहर-सिंचाई; तमिलनाडु में धान की खेती; मंदिरों को भूमि दान (देवदान); मठों को अमृतांगल", "type": "leaf"},
                    {"label": "विदेशी व्यापार: ममल्लापुरम बंदरगाह; दक्षिण-पूर्व एशिया (इंडोनेशिया, मलाया); सोना, मसाले, कपास", "type": "leaf"},
                    {"label": "श्रेणियाँ: व्यापारी संघ; नगरम (व्यापारी संघ) शक्तिशाली; बंदरगाह व्यापार से राजस्व", "type": "leaf"}
                ]},
                {"label": "चालुक्य अर्थव्यवस्था", "type": "branch", "date": "चालुक्य", "children": [
                    {"label": "कृषि: कर्नाटक में मोटे अनाज (ज्वार, बाजरा); मुलकी (कर) व्यवस्था; भूमि सर्वेक्षण", "type": "leaf"},
                    {"label": "व्यापार: कर्नाटक से उत्तर और दक्षिण; अरब व्यापारियों से संपर्क; घोड़े और मसाले का व्यापार", "type": "leaf"}
                ]}
            ]
        else:
            return [
                {"label": "Pallava Economy", "type": "branch", "date": "Pallavas", "children": [
                    {"label": "Agriculture: Canal irrigation; rice cultivation in Tamil Nadu; Devadana (temple land grants); Amritangal (mathas)", "type": "leaf"},
                    {"label": "Foreign Trade: Mamallapuram port; SE Asia (Indonesia, Malaya, Java); gold, spices, textiles exported", "type": "leaf"},
                    {"label": "Guilds: Nagaram (merchant guilds) powerful; port trade generated significant revenue", "type": "leaf"}
                ]},
                {"label": "Chalukya Economy", "type": "branch", "date": "Chalukyas", "children": [
                    {"label": "Agriculture: Karnataka — coarse grains (sorghum, millet); Mulki (tax) system; land surveys", "type": "leaf"},
                    {"label": "Trade: Karnataka linked N-S trade; contact with Arab merchants; horse and spice trade important", "type": "leaf"}
                ]}
            ]

    elif is_pallava and 'society' in rp:
        if is_hindi:
            return [
                {"label": "पल्लव समाज और संस्कृति", "type": "branch", "date": "समाज", "children": [
                    {"label": "ब्राह्मण प्रभुत्व: पल्लव राजा ब्राह्मण थे (विवादित); ब्राह्मणों को अग्रहार भूमि; वर्ण व्यवस्था कठोर", "type": "leaf"},
                    {"label": "भक्ति आंदोलन: नयनमार (शैव) और अलवार (वैष्णव); तमिल भक्ति साहित्य; देवारम और नलायर दिव्य प्रबंधम", "type": "leaf"},
                    {"label": "तमिल साहित्य: संगम साहित्य की परंपरा; पल्लव दरबार में संस्कृत और तमिल दोनों; थेवारम भजन", "type": "leaf"}
                ]},
                {"label": "चालुक्य समाज और संस्कृति", "type": "branch", "date": "चालुक्य समाज", "children": [
                    {"label": "विविधता: ब्राह्मण, क्षत्रिय, व्यापारी; कन्नड़ भाषा का उदय; कन्नड़ साहित्य का प्रारंभ", "type": "leaf"},
                    {"label": "मेगुटी मंदिर अभिलेख (634 CE): रविकीर्ति द्वारा; सबसे पुरानी कन्नड़ कविता का संदर्भ; पुलकेशिन II की प्रशस्ति", "type": "leaf"}
                ]}
            ]
        else:
            return [
                {"label": "Pallava Society & Culture", "type": "branch", "date": "Society", "children": [
                    {"label": "Brahmin Dominance: Pallavas gave Agrahara land; Varna system strict; Brahmins as administrators", "type": "leaf"},
                    {"label": "Bhakti Movement: Nayanmars (Shaiva) and Alvars (Vaishnava) saints; Tamil devotional literature flourished", "type": "leaf"},
                    {"label": "Tamil Literature: Sangam tradition continued; Devaram and Nalayira Divya Prabandham composed", "type": "leaf"}
                ]},
                {"label": "Chalukya Society & Culture", "type": "branch", "date": "Chalukya Society", "children": [
                    {"label": "Diversity: Brahmins, Kshatriyas, traders; rise of Kannada language and Kannada literature", "type": "leaf"},
                    {"label": "Meguti Temple Inscription (634 CE): By Ravikirti; early Kannada poetry reference; Pulakesi II prashasti", "type": "leaf"}
                ]}
            ]

    elif is_pallava and 'religion' in rp:
        if is_hindi:
            return [
                {"label": "पल्लव धर्म", "type": "branch", "date": "पल्लव", "children": [
                    {"label": "शैव धर्म: अधिकांश पल्लव राजा शैव; कांची का कैलाशनाथ मंदिर; ममल्लापुरम में शिव मंदिर", "type": "leaf"},
                    {"label": "भक्ति आंदोलन का जन्म: नयनमार संत (63 शैव संत); अप्पर, सम्बंदर, सुंदरर; देवारम 12 खंड; मंदिर-केंद्रित भक्ति", "type": "leaf"},
                    {"label": "बौद्ध और जैन: कांची में दोनों; महेंद्रवर्मन I पहले जैन फिर शैव; बौद्ध विहार; धार्मिक सहिष्णुता", "type": "leaf"}
                ]},
                {"label": "चालुक्य धर्म", "type": "branch", "date": "चालुक्य", "children": [
                    {"label": "हिंदू धर्म: चालुक्य वैष्णव और शैव दोनों; पट्टडकल के मंदिर; विरूपाक्ष मंदिर (शिव); UNESCO WHS", "type": "leaf"},
                    {"label": "जैन धर्म: पश्चिमी चालुक्यों के अंतर्गत; अयोध्या में जैन मंदिर; व्यापारी वर्ग में जैन धर्म लोकप्रिय", "type": "leaf"}
                ]}
            ]
        else:
            return [
                {"label": "Pallava Religion", "type": "branch", "date": "Pallavas", "children": [
                    {"label": "Shaivism: Most Pallava rulers Shaivite; Kailasanatha Temple Kanchi; Mamallapuram Shiva shrines", "type": "leaf"},
                    {"label": "Bhakti Movement Birth: 63 Nayanmars (Shaiva saints); Appar, Sambandar, Sundarar; Devaram hymns composed", "type": "leaf"},
                    {"label": "Buddhism & Jainism: Both in Kanchi; Mahendravarman I was Jain then converted to Shaivism", "type": "leaf"}
                ]},
                {"label": "Chalukya Religion", "type": "branch", "date": "Chalukyas", "children": [
                    {"label": "Hinduism: Chalukyas patronized Vaishnava and Shaiva temples; Pattadakal complex; Virupaksha Temple (UNESCO)", "type": "leaf"},
                    {"label": "Jainism: Popular under Western Chalukyas; merchant class patronized Jain temples; coexistence", "type": "leaf"}
                ]}
            ]

    elif is_pallava and 'art' in rp:
        if is_hindi:
            return [
                {"label": "पल्लव कला और स्थापत्य: द्रविड़ शैली का उदय", "type": "branch", "date": "पल्लव कला", "children": [
                    {"label": "ममल्लापुरम (महाबलीपुरम): यूनेस्को विश्व धरोहर; रथ मंदिर (पंच पांडव रथ); अर्जुन की तपस्या (विश्व की सबसे बड़ी बेस रिलीफ)", "type": "leaf"},
                    {"label": "मंडप शैली: पहाड़ी को काटकर बनाए गए गुफा मंदिर; महेंद्रवर्मन I द्वारा शुरू; वर्गाकार स्तंभ", "type": "leaf"},
                    {"label": "कांची का कैलाशनाथ मंदिर: 8 शताब्दी; राजसिंह द्वारा; संरचनात्मक मंदिर; द्रविड़ शिखर (विमान) का प्रारंभिक रूप", "type": "leaf"},
                    {"label": "तटीय मंदिर (Shore Temple): ममल्लापुरम; पत्थर का पहला संरचनात्मक मंदिर; समुद्र के किनारे; UNESCO WHS", "type": "leaf"}
                ]},
                {"label": "चालुक्य कला और स्थापत्य", "type": "branch", "date": "चालुक्य कला", "children": [
                    {"label": "ऐहोल: मंदिर स्थापत्य का प्रयोगशाला; 125+ मंदिर; गुडिगुड्डा, दुर्गा, लाड खान मंदिर; विभिन्न शैलियों का प्रयोग", "type": "leaf"},
                    {"label": "बादामी गुफा मंदिर: 4 गुफाएँ (3 हिंदू, 1 जैन); वाराह, नटराज, महिषमर्दिनी उत्कृष्ट मूर्तियाँ", "type": "leaf"},
                    {"label": "पट्टडकल: UNESCO WHS; विरूपाक्ष मंदिर, संगमेश्वर मंदिर; नागर और द्रविड़ का मिश्रण; राष्ट्रकूट और चालुक्य शैली", "type": "leaf"}
                ]}
            ]
        else:
            return [
                {"label": "Pallava Art & Architecture: Birth of Dravidian Style", "type": "branch", "date": "Pallava Art", "children": [
                    {"label": "Mamallapuram (UNESCO WHS): Pancha Pandava Rathas (monolithic); Arjuna's Penance (world's largest bas-relief)", "type": "leaf"},
                    {"label": "Mandapa Style: Rock-cut cave temples initiated by Mahendravarman I; square pillars; Varaha cave", "type": "leaf"},
                    {"label": "Kailasanatha Temple Kanchi: 8th century; by Rajasimha; early structural temple; Dravidian vimana", "type": "leaf"},
                    {"label": "Shore Temple Mamallapuram: First free-standing stone structural temple; by sea; UNESCO WHS; Rajasimha era", "type": "leaf"}
                ]},
                {"label": "Chalukya Art & Architecture", "type": "branch", "date": "Chalukya Art", "children": [
                    {"label": "Aihole: 'Cradle of Indian temples'; 125+ temples; Gudiguddaa, Durga, Lad Khan temples; experimental styles", "type": "leaf"},
                    {"label": "Badami Cave Temples: 4 caves (3 Hindu, 1 Jain); Varaha, Nataraja, Mahishamardini superb sculptures", "type": "leaf"},
                    {"label": "Pattadakal (UNESCO WHS): Virupaksha Temple, Sangameshvara; blend of Nagara and Dravida styles", "type": "leaf"}
                ]}
            ]

    # Fallback
    else:
        if is_hindi:
            return [{"label": "हर्षवर्धन और दक्षिणी राजवंश", "type": "branch", "date": "7वीं शताब्दी", "children": [
                {"label": "UPSC के लिए हर्ष और पल्लव-चालुक्य काल की प्रमुख विशेषताएँ", "type": "leaf"}]}]
        else:
            return [{"label": "Harsha & Southern Dynasties", "type": "branch", "date": "7th Century", "children": [
                {"label": "Key features of Harsha, Pallava and Chalukya periods for UPSC", "type": "leaf"}]}]

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

    abs_base = os.path.abspath(BASE)
    abs_dir  = os.path.abspath(os.path.dirname(html_path))
    rel_path = os.path.relpath(abs_dir, abs_base)

    folder_name = os.path.basename(abs_dir)
    if folder_name == 'hi':
        folder_name = os.path.basename(os.path.dirname(abs_dir))

    clean_title = get_clean_title(folder_name)
    topic_name  = clean_title
    cj = os.path.join(abs_dir, "content.json")
    if os.path.exists(cj):
        try:
            topic_name = json.load(open(cj, encoding='utf-8')).get('hero', {}).get('title', topic_name)
        except Exception:
            pass

    branches = get_branches(rel_path, is_hindi)
    mindmap_data = {"label": clean_title, "type": "root", "children": branches}

    css_link = '    <link rel="stylesheet" href="/assets/css/mindmap.min.css?v=2">\n'
    if css_link not in html:
        html = html.replace('</head>', css_link + '</head>')

    if is_hindi:
        instr      = 'किसी <strong style="color:#a78bfa;">बैंगनी</strong> या <strong style="color:#2ecc71;">हरे</strong> <strong>+</strong> पर क्लिक करें।'
        title_text = f"{topic_name} &mdash; इंटरैक्टिव माइंडमैप"
    else:
        instr      = 'Tap a <strong style="color:#a78bfa;">purple</strong> or <strong style="color:#2ecc71;">green</strong> <strong>+</strong> to expand.'
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

    tree_json     = json.dumps(mindmap_data)
    lang_str      = "'hi'" if is_hindi else "'en'"
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
        parts    = os.path.relpath(root, BASE).split(os.sep)
        is_hindi = 'hi' in parts
        for file in files:
            if file == "index.html":
                process_file(os.path.join(root, file), is_hindi)
                total += 1
    print(f"\nDone! Patched {total} files.")

if __name__ == '__main__':
    main()
