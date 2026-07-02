#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import re
import json

BASE = r"upsc/ancient_history/History-of-Gupta-Age-Golden-Age"

def get_clean_title(folder_name):
    title = folder_name.replace('-', ' ')
    skip = {'of', 'and', 'the', 'for', 'in', 'with', 'to', 'on', 'by', 'or', 'a', 'an', 'about'}
    return ' '.join(w if w.lower() in skip else w.capitalize() for w in title.split())

def get_custom_branches(folder_name, is_hindi):
    fl = folder_name.lower()

    # 1. Administration
    if 'administration' in fl:
        if is_hindi:
            return [
                {"label": "गुप्त प्रशासन: केंद्रीय ढाँचा", "type": "branch", "date": "4-6 शताब्दी ई.", "children": [
                    {"label": "राजपद: चक्रवर्ती और देवपुत्र की उपाधियाँ; दैवीय अधिकार का सिद्धांत; अश्वमेध यज्ञ", "type": "leaf"},
                    {"label": "मंत्रिपरिषद: कुमारामात्य (प्रमुख अधिकारी); महासंधिविग्रहिक (युद्ध एवं शांति मंत्री); महादंडनायक (सर्वोच्च न्यायाधीश)", "type": "leaf"},
                    {"label": "राजकोषीय व्यवस्था: भाग (कर), बलि, शुल्क, उद्रंग; राज्य की आय के स्रोत", "type": "leaf"}
                ]},
                {"label": "प्रांतीय और स्थानीय प्रशासन", "type": "branch", "date": "प्रांत", "children": [
                    {"label": "देश/राष्ट्र: प्रांत; गोप्ता (राज्यपाल); उपरिक (जिला अधिकारी); विषयपति (जिलाधिकारी)", "type": "leaf"},
                    {"label": "ग्राम: ग्रामिक (ग्राम प्रधान); पाँच सदस्यीय परिषद; कर वसूली और स्थानीय विवाद निपटाना", "type": "leaf"},
                    {"label": "नगर प्रशासन: पुस्तपाल (लेखाकार); शौल्किक (शुल्क संग्राहक); नगरश्रेष्ठी (नगर व्यापारी प्रमुख)", "type": "leaf"}
                ]}
            ]
        else:
            return [
                {"label": "Gupta Administration: Central Structure", "type": "branch", "date": "4th-6th Century CE", "children": [
                    {"label": "Kingship: Titles — Chakravartin, Devputra; divine right theory; Ashvamedha Yajna performed", "type": "leaf"},
                    {"label": "Council: Kumaramatya (chief officers); Mahasandhivigrahika (war & peace minister); Mahadandanayaka (chief justice)", "type": "leaf"},
                    {"label": "Revenue: Bhaga (land tax), Bali (tribute), Shulka (customs duties), Udranga (house tax)", "type": "leaf"}
                ]},
                {"label": "Provincial & Local Administration", "type": "branch", "date": "Provinces", "children": [
                    {"label": "Desha/Rashtra: Province governed by Gopa or Uparika; Vishayapati administered districts", "type": "leaf"},
                    {"label": "Village: Gramika (village headman); five-member council handled tax collection and disputes", "type": "leaf"},
                    {"label": "Urban: Pustapala (accountant); Shaulkika (customs officer); Nagarashreshthi (guild head)", "type": "leaf"}
                ]}
            ]

    # 2. Art and Architecture
    elif 'art' in fl and 'architecture' in fl:
        if is_hindi:
            return [
                {"label": "गुप्त कला और स्थापत्य: विशेषताएँ", "type": "branch", "date": "स्वर्ण युग", "children": [
                    {"label": "नागर मंदिर शैली: उत्तर भारतीय शिखर शैली का विकास; देवगढ़ का दशावतार मंदिर (UP); भूमरा का मंदिर", "type": "leaf"},
                    {"label": "अजंता गुफाएँ (फेज़ 2): गुप्त काल में 16-29 गुफाएँ; बोधिसत्व पद्मपाणि; विश्व धरोहर", "type": "leaf"},
                    {"label": "मथुरा और सारनाथ मूर्तिकला: बुद्ध की 'ध्यान मुद्रा'; पारदर्शी वस्त्र तकनीक; आदर्श सौंदर्य", "type": "leaf"}
                ]},
                {"label": "धातु और चित्रकला", "type": "branch", "date": "कला", "children": [
                    {"label": "मेहरौली लौह स्तंभ (4-5 शताब्दी): चंद्रगुप्त द्वितीय काल; 98% शुद्ध लोहा; जंग रहित; विश्व धातुकर्म चमत्कार", "type": "leaf"},
                    {"label": "सुल्तानगंज बुद्ध (बिहार): 7.5 फुट ऊँचा तांबे का बुद्ध; गुप्त धातु कला का सर्वोत्तम उदाहरण", "type": "leaf"},
                    {"label": "अजंता भित्तिचित्र: टेम्परा पद्धति; जातक कथाएँ; जीवंत रंग और प्रकृतिवाद", "type": "leaf"}
                ]}
            ]
        else:
            return [
                {"label": "Gupta Art & Architecture: Highlights", "type": "branch", "date": "Golden Age", "children": [
                    {"label": "Nagara Temple Style: Development of N. Indian shikhara tradition; Dashavatara Temple Deogarh (UP)", "type": "leaf"},
                    {"label": "Ajanta Caves (Phase 2): Caves 16-29 painted in Gupta period; Bodhisattva Padmapani masterpiece", "type": "leaf"},
                    {"label": "Mathura & Sarnath Sculpture: Buddha in dhyana mudra; transparent drapery; idealized beauty", "type": "leaf"}
                ]},
                {"label": "Metal Work & Painting", "type": "branch", "date": "Arts", "children": [
                    {"label": "Mehrauli Iron Pillar: Chandragupta II era; 98% pure iron; rust-free for 1600 years; metallurgical marvel", "type": "leaf"},
                    {"label": "Sultanganj Buddha (Bihar): 7.5 ft copper Buddha; finest Gupta metal casting example", "type": "leaf"},
                    {"label": "Ajanta Murals: Tempera technique; Jataka stories; vivid naturalism; UNESCO World Heritage Site", "type": "leaf"}
                ]}
            ]

    # 3. Economy
    elif 'economy' in fl:
        if is_hindi:
            return [
                {"label": "गुप्त कालीन अर्थव्यवस्था: कृषि और भूमि", "type": "branch", "date": "आर्थिक विकास", "children": [
                    {"label": "भूमि अनुदान: ब्राह्मणों और मंदिरों को भूमि दान (अग्रहार और देवगृह); कर मुक्त; भूमि का निजी स्वामित्व", "type": "leaf"},
                    {"label": "कृषि: उन्नत सिंचाई; बहुफसल; गेहूँ, चावल, गन्ना, कपास; गाँव स्वशासी इकाई", "type": "leaf"},
                    {"label": "कर व्यवस्था: भाग (1/4-1/6 उपज); बलि (अतिरिक्त कर); हिरण्य (नकद); विष्टि (बेगार)", "type": "leaf"}
                ]},
                {"label": "व्यापार और वाणिज्य", "type": "branch", "date": "व्यापार", "children": [
                    {"label": "आंतरिक व्यापार: श्रेणियाँ (Guilds) शक्तिशाली; नगर केंद्र; नदी मार्ग; उज्जैन, पाटलिपुत्र व्यापार केंद्र", "type": "leaf"},
                    {"label": "विदेशी व्यापार: रोमन साम्राज्य, दक्षिण-पूर्व एशिया; सोने के सिक्के (दिनार); मसाले, वस्त्र, रत्न निर्यात", "type": "leaf"},
                    {"label": "मुद्रा प्रणाली: सोने के दिनार; चाँदी के रूपक; ताँबे के कर्षापण; गुप्त मुद्राएँ सर्वोत्तम", "type": "leaf"}
                ]}
            ]
        else:
            return [
                {"label": "Gupta Economy: Agriculture & Land", "type": "branch", "date": "Economy", "children": [
                    {"label": "Land Grants: Agrahara (to Brahmins) and Devagriha (to temples); tax-free; private land ownership grew", "type": "leaf"},
                    {"label": "Agriculture: Advanced irrigation; multi-cropping; wheat, rice, sugarcane, cotton; villages self-sufficient", "type": "leaf"},
                    {"label": "Tax System: Bhaga (1/4-1/6 produce); Bali (additional tax); Hiranya (cash tax); Vishti (forced labour)", "type": "leaf"}
                ]},
                {"label": "Trade & Commerce", "type": "branch", "date": "Trade", "children": [
                    {"label": "Internal Trade: Powerful Shrenis (guilds); Ujjain, Pataliputra as major hubs; river trade routes", "type": "leaf"},
                    {"label": "Foreign Trade: With Roman Empire and SE Asia; gold Dinar coins; spices, textiles, gems exported", "type": "leaf"},
                    {"label": "Coinage: Gold Dinars (finest); Silver Rupaka; Copper Karshapana; Gupta coins most artistically superior", "type": "leaf"}
                ]}
            ]

    # 4. Literature
    elif 'literature' in fl:
        if is_hindi:
            return [
                {"label": "गुप्त काल: साहित्यिक उपलब्धियाँ", "type": "branch", "date": "संस्कृत साहित्य", "children": [
                    {"label": "कालिदास: मेघदूत, रघुवंश, कुमारसंभव (काव्य); अभिज्ञानशाकुंतलम्, मालविकाग्निमित्र, विक्रमोर्वशीय (नाटक)", "type": "leaf"},
                    {"label": "विशाखदत्त: मुद्राराक्षस (राजनीतिक नाटक); देवीचंद्रगुप्त (चंद्रगुप्त II पर)", "type": "leaf"},
                    {"label": "शूद्रक: मृच्छकटिकम् — नायिका वसंतसेना; व्यापारी पुत्र नायक; सामाजिक यथार्थवाद", "type": "leaf"},
                    {"label": "हरिषेण: प्रयाग प्रशस्ति — समुद्रगुप्त की उपलब्धियों का विवरण; इलाहाबाद स्तंभ पर उत्कीर्ण", "type": "leaf"}
                ]},
                {"label": "पुराण, व्याकरण और विज्ञान साहित्य", "type": "branch", "date": "पुराण और शास्त्र", "children": [
                    {"label": "18 महापुराणों का संकलन: विष्णु पुराण, वायु पुराण, मार्कंडेय पुराण; गुप्त काल में अंतिम रूप", "type": "leaf"},
                    {"label": "अमरकोष: अमरसिंह द्वारा; संस्कृत का पहला व्यवस्थित कोश; त्रिकांड में विभाजित", "type": "leaf"},
                    {"label": "आर्यभट्टीय: आर्यभट्ट की गणितीय-खगोलीय कृति; 499 ई.; दशमलव प्रणाली, π का मान 3.1416", "type": "leaf"}
                ]}
            ]
        else:
            return [
                {"label": "Gupta Period: Literary Achievements", "type": "branch", "date": "Sanskrit Literature", "children": [
                    {"label": "Kalidasa: Meghaduta, Raghuvamsa, Kumarasambhava (poetry); Abhijnanashakuntalam, Malavikagnimitra (plays)", "type": "leaf"},
                    {"label": "Vishakhadatta: Mudrarakshasa (political drama); Devichandraguptam (on Chandragupta II)", "type": "leaf"},
                    {"label": "Shudraka: Mricchakatikam — merchant's son hero; Vasantasena heroine; social realism", "type": "leaf"},
                    {"label": "Harishena: Prayaga Prashasti — records Samudragupta's conquests on Allahabad pillar", "type": "leaf"}
                ]},
                {"label": "Puranas, Grammar & Scientific Literature", "type": "branch", "date": "Scriptures", "children": [
                    {"label": "18 Mahapuranas compiled: Vishnu Purana, Vayu Purana, Markandeya Purana finalized in Gupta age", "type": "leaf"},
                    {"label": "Amarakosha: By Amarasimha; first systematic Sanskrit thesaurus; divided into three Kandas", "type": "leaf"},
                    {"label": "Aryabhatiya: By Aryabhata (499 CE); decimal system, value of π (3.1416), earth's rotation", "type": "leaf"}
                ]}
            ]

    # 5. Religion and Culture
    elif 'religion' in fl and 'culture' in fl:
        if is_hindi:
            return [
                {"label": "गुप्त काल: धर्म और सांस्कृतिक पुनरुत्थान", "type": "branch", "date": "धर्म", "children": [
                    {"label": "वैष्णव धर्म का उत्थान: गुप्त राजा स्वयं वैष्णव; विष्णु की आराधना; गरुड़ध्वज; भागवत धर्म का प्रसार", "type": "leaf"},
                    {"label": "शैव धर्म: कुमारगुप्त I — महेंद्रादित्य; शिव पूजा; पाशुपत संप्रदाय का उदय", "type": "leaf"},
                    {"label": "बौद्ध और जैन धर्म: नालंदा विश्वविद्यालय की स्थापना (5 शताब्दी); जैन मूर्तिकला; सह-अस्तित्व", "type": "leaf"}
                ]},
                {"label": "सांस्कृतिक विशेषताएँ", "type": "branch", "date": "संस्कृति", "children": [
                    {"label": "वर्ण व्यवस्था का कठोरीकरण: जाति व्यवस्था अधिक कठोर; अस्पृश्यता का उद्भव (चांडाल); स्त्रियों की स्थिति में गिरावट", "type": "leaf"},
                    {"label": "सती प्रथा का प्रारंभ: पहला स्पष्ट साक्ष्य गुप्त काल में; विधवाओं की स्थिति दयनीय", "type": "leaf"},
                    {"label": "संगीत और नृत्य: नाट्यशास्त्र का परिष्करण; भरतमुनि; शास्त्रीय नृत्य रूपों का विकास", "type": "leaf"}
                ]}
            ]
        else:
            return [
                {"label": "Gupta Period: Religion & Cultural Revival", "type": "branch", "date": "Religion", "children": [
                    {"label": "Vaishnavism Rise: Gupta kings were Vaishnavas; Garuda Dhvaja; spread of Bhagavata religion", "type": "leaf"},
                    {"label": "Shaivism: Kumaragupta I — Mahendraditya; Shiva worship; rise of Pasupata sect", "type": "leaf"},
                    {"label": "Buddhism & Jainism: Nalanda University founded (5th century); Jain sculpture flourished; coexistence", "type": "leaf"}
                ]},
                {"label": "Cultural Characteristics", "type": "branch", "date": "Culture", "children": [
                    {"label": "Caste Rigidity: Varna system more strict; untouchability emerged (Chandala); women's status declined", "type": "leaf"},
                    {"label": "Sati Practice: First clear evidence in Gupta period; widows' position became miserable", "type": "leaf"},
                    {"label": "Music & Dance: Natyashastra refined; classical dance forms developed; temples as performance spaces", "type": "leaf"}
                ]}
            ]

    # 6. Society
    elif 'society' in fl:
        if is_hindi:
            return [
                {"label": "गुप्त कालीन समाज: संरचना", "type": "branch", "date": "समाज", "children": [
                    {"label": "वर्ण व्यवस्था: ब्राह्मण — उच्चतम; भूमि अनुदान प्राप्त; अग्रहार व्यवस्था; राज्य के सहयोगी", "type": "leaf"},
                    {"label": "वैश्य और शूद्र: व्यापारी-वर्ग समृद्ध; शूद्रों की स्थिति में आंशिक सुधार; कृषि कार्य", "type": "leaf"},
                    {"label": "चांडाल: समाज से बहिष्कृत; नगर के बाहर निवास; फाह्यान ने इनकी दुर्दशा का उल्लेख किया", "type": "leaf"}
                ]},
                {"label": "महिलाएँ और विवाह संस्था", "type": "branch", "date": "महिलाएँ", "children": [
                    {"label": "स्त्रियों की स्थिति: प्रारंभिक गुप्त काल में अपेक्षाकृत स्वतंत्र; बाद में पर्दा प्रथा और बाल विवाह", "type": "leaf"},
                    {"label": "अष्टविवाह: आठ प्रकार के विवाह वैध; ब्राह्म विवाह श्रेष्ठ; गंधर्व और राक्षस विवाह भी प्रचलित", "type": "leaf"},
                    {"label": "गणिकाएँ: नर्तकी/वेश्या वर्ग; समाज में मान्यता; आम्रपाली जैसी शासकीय वेश्याएँ", "type": "leaf"}
                ]}
            ]
        else:
            return [
                {"label": "Gupta Society: Structure", "type": "branch", "date": "Society", "children": [
                    {"label": "Varna System: Brahmins at apex; received Agrahara land grants; state collaborators", "type": "leaf"},
                    {"label": "Vaishyas & Shudras: Merchant class prosperous; Shudras' condition marginally improved; agriculture", "type": "leaf"},
                    {"label": "Chandala (Untouchables): Excluded from society; lived outside cities; Fahien recorded their misery", "type": "leaf"}
                ]},
                {"label": "Women & Marriage Institution", "type": "branch", "date": "Women", "children": [
                    {"label": "Women's Status: Relatively free in early Gupta; later purdah system and child marriage emerged", "type": "leaf"},
                    {"label": "Eight Forms of Marriage: Brahma vivah (best); Gandharva and Rakshasa also recognized", "type": "leaf"},
                    {"label": "Ganika: Courtesans recognized socially; state-employed; continued from Mauryan tradition", "type": "leaf"}
                ]}
            ]

    # 7. Decline of Guptas
    elif 'decline' in fl:
        if is_hindi:
            return [
                {"label": "गुप्त साम्राज्य के पतन के कारण", "type": "branch", "date": "पतन (5-6 शताब्दी)", "children": [
                    {"label": "हूण आक्रमण: मिहिरकुल के नेतृत्व में श्वेत हूणों का आक्रमण; स्कंदगुप्त ने प्रारंभ में रोका; बाद में प्रांतों की हानि", "type": "leaf"},
                    {"label": "सामंतीकरण: भूमि अनुदान से सामंत वर्ग शक्तिशाली; केंद्रीय नियंत्रण कमजोर; प्रांतीय स्वायत्तता बढ़ी", "type": "leaf"},
                    {"label": "उत्तराधिकार संघर्ष: स्कंदगुप्त के बाद कमजोर उत्तराधिकारी; आंतरिक कलह; साम्राज्य टूटा", "type": "leaf"}
                ]},
                {"label": "आर्थिक और व्यापारिक पतन", "type": "branch", "date": "आर्थिक पतन", "children": [
                    {"label": "रोमन साम्राज्य का पतन: व्यापार में गिरावट; सोने की कमी; मुद्रा का अवमूल्यन", "type": "leaf"},
                    {"label": "विकेंद्रीकरण: स्थानीय सामंत आर्थिक रूप से स्वतंत्र; कर संग्रह में बाधा; व्यापारिक मार्गों पर अनियंत्रण", "type": "leaf"}
                ]}
            ]
        else:
            return [
                {"label": "Causes of Gupta Decline", "type": "branch", "date": "Decline 5th-6th CE", "children": [
                    {"label": "Huna Invasions: White Huns under Mihirakula; Skandagupta initially repelled; eventual loss of provinces", "type": "leaf"},
                    {"label": "Feudalization: Land grants created powerful feudal lords; weakened central control and revenue", "type": "leaf"},
                    {"label": "Succession Disputes: Weak successors after Skandagupta; internal strife fragmented the empire", "type": "leaf"}
                ]},
                {"label": "Economic & Trade Decline", "type": "branch", "date": "Economic Decline", "children": [
                    {"label": "Roman Trade Collapse: Fall of Rome disrupted trade; gold scarcity; currency debasement visible", "type": "leaf"},
                    {"label": "Decentralization: Local feudatories became economically independent; tax collection disrupted", "type": "leaf"}
                ]}
            ]

    # 8. Science and Technology
    elif 'science' in fl:
        if is_hindi:
            return [
                {"label": "गुप्त काल: विज्ञान और तकनीक", "type": "branch", "date": "वैज्ञानिक उपलब्धियाँ", "children": [
                    {"label": "आर्यभट्ट (476-550 CE): पृथ्वी गोल और अपनी धुरी पर घूमती है; π = 3.1416; शून्य/दशमलव की अवधारणा", "type": "leaf"},
                    {"label": "वराहमिहिर: पंचसिद्धांतिका; बृहत्संहिता (विश्वकोश); भूगोल, खगोल, ज्योतिष; पश्चिमी और भारतीय ज्ञान का समन्वय", "type": "leaf"},
                    {"label": "ब्रह्मगुप्त: ब्रह्मस्फुटसिद्धांत (628 CE); शून्य की गणितीय परिभाषा; नकारात्मक संख्याएँ", "type": "leaf"},
                    {"label": "आयुर्वेद: चरकसंहिता का पुनःसंकलन; धन्वन्तरि; शल्य चिकित्सा (Sushruta Samhita में); औषधि ज्ञान", "type": "leaf"}
                ]},
                {"label": "धातुकर्म और अभियांत्रिकी", "type": "branch", "date": "तकनीक", "children": [
                    {"label": "मेहरौली लौह स्तंभ: 7.21 मीटर; 6 टन; 98% शुद्ध लोहा; 1600+ वर्षों से जंग नहीं; phosphoric iron", "type": "leaf"},
                    {"label": "सुल्तानगंज बुद्ध: तांबे की ढलाई (lost-wax/cire perdue); विशाल आकार; उत्कृष्ट तकनीक", "type": "leaf"}
                ]}
            ]
        else:
            return [
                {"label": "Gupta Period: Science & Technology", "type": "branch", "date": "Scientific Achievements", "children": [
                    {"label": "Aryabhata (476-550 CE): Earth is spherical and rotates; π = 3.1416; decimal system, concept of zero", "type": "leaf"},
                    {"label": "Varahamihira: Panchasiddhantika; Brihatsamhita (encyclopaedia); astronomy, geography, botany", "type": "leaf"},
                    {"label": "Brahmagupta: Brahmasphutasiddhanta (628 CE); mathematical definition of zero; negative numbers", "type": "leaf"},
                    {"label": "Ayurveda: Charaka Samhita re-compiled; Dhanvantari; Sushruta Samhita for surgery; medicine flourished", "type": "leaf"}
                ]},
                {"label": "Metallurgy & Engineering", "type": "branch", "date": "Technology", "children": [
                    {"label": "Mehrauli Iron Pillar: 7.21m; 6 tonnes; 98% pure iron; rust-free 1600+ years; phosphoric iron technique", "type": "leaf"},
                    {"label": "Sultanganj Buddha: Large copper casting using lost-wax (cire perdue); superb technical mastery", "type": "leaf"}
                ]}
            ]

    # 9. Foreign Travellers
    elif 'foreign' in fl or 'travellers' in fl:
        if is_hindi:
            return [
                {"label": "गुप्त काल के प्रमुख विदेशी यात्री", "type": "branch", "date": "विदेशी यात्री", "children": [
                    {"label": "फाह्यान (399-414 CE): चीनी बौद्ध भिक्षु; चंद्रगुप्त II के काल में; बौद्ध ग्रंथों की तलाश; 'फोकुओजी' (बौद्ध देशों का वृत्तांत)", "type": "leaf"},
                    {"label": "फाह्यान के अवलोकन: पाटलिपुत्र समृद्ध नगर; लोग सुखी और सम्पन्न; जातियों की व्यवस्था; चांडालों की दुर्दशा; गायों की हत्या निषिद्ध", "type": "leaf"}
                ]},
                {"label": "अन्य यात्री और उनका विवरण", "type": "branch", "date": "अन्य यात्री", "children": [
                    {"label": "ह्वेनसांग (629-645 CE): हर्षवर्धन काल में; परंतु गुप्त साम्राज्य की उत्तर-कालीन स्थिति; नालंदा में अध्ययन", "type": "leaf"},
                    {"label": "फाह्यान की यात्रा महत्व: भारतीय जन-जीवन का प्रथम हस्त विदेशी विवरण; बौद्ध धर्म की स्थिति; पशु बलि का न होना", "type": "leaf"},
                    {"label": "मेगस्थनीज (मौर्य काल): इंडिका; गुप्त काल में मौर्य प्रशासन से तुलना; सामाजिक परिवर्तनों का आधार", "type": "leaf"}
                ]}
            ]
        else:
            return [
                {"label": "Key Foreign Travellers of Gupta Period", "type": "branch", "date": "Foreign Travellers", "children": [
                    {"label": "Fahien/Faxian (399-414 CE): Chinese Buddhist monk; visited during Chandragupta II; seeking Buddhist texts", "type": "leaf"},
                    {"label": "Fahien's Observations: Pataliputra prosperous; people happy and wealthy; no capital punishment; Chandalas outcaste", "type": "leaf"}
                ]},
                {"label": "Other Accounts & Their Significance", "type": "branch", "date": "Significance", "children": [
                    {"label": "Huien Tsang (629-645 CE): During Harsha's reign; studied at Nalanda; recorded post-Gupta India", "type": "leaf"},
                    {"label": "Fahien's Account Importance: First-hand foreign record of Indian social life; no animal slaughter; prosperity", "type": "leaf"},
                    {"label": "Comparison with Megasthenes: Mauryan vs Gupta governance; evolution of Indian social structure", "type": "leaf"}
                ]}
            ]

    # 10. Chandragupta I
    elif 'chandragupta-i' in fl:
        if is_hindi:
            return [
                {"label": "चंद्रगुप्त प्रथम (319-335 ई.)", "type": "branch", "date": "319-335 CE", "children": [
                    {"label": "गुप्त वंश का वास्तविक संस्थापक: 'महाराजाधिराज' की उपाधि धारण करने वाले पहले गुप्त शासक; राजनीतिक स्वतंत्रता की घोषणा", "type": "leaf"},
                    {"label": "लिच्छवि से विवाह: कुमारदेवी (लिच्छवि राजकुमारी) से विवाह; राजनीतिक गठबंधन; गुप्त-लिच्छवि संयुक्त सिक्के", "type": "leaf"},
                    {"label": "गुप्त संवत् का आरंभ: 319-320 ई. में गुप्त संवत् (कैलेंडर) की शुरुआत; 'नए युग' का प्रतीक", "type": "leaf"}
                ]},
                {"label": "साम्राज्य विस्तार", "type": "branch", "date": "साम्राज्य", "children": [
                    {"label": "क्षेत्र: मगध, प्रयाग, साकेत (अयोध्या) पर नियंत्रण; पूर्वी उत्तर प्रदेश और बिहार; 'आर्यावर्त' का एकीकरण", "type": "leaf"},
                    {"label": "उत्तराधिकार: समुद्रगुप्त को उत्तराधिकारी चुना; 'धरणिबंध' (पृथ्वी के स्वामी) की उपाधि दी", "type": "leaf"}
                ]}
            ]
        else:
            return [
                {"label": "Chandragupta I (319-335 CE)", "type": "branch", "date": "319-335 CE", "children": [
                    {"label": "True Founder of Gupta Empire: First to assume 'Maharajadhiraja' title; declared political independence", "type": "leaf"},
                    {"label": "Lichchhavi Alliance: Married Kumaradevi (Lichchhavi princess); political alliance; joint coins issued", "type": "leaf"},
                    {"label": "Gupta Era: Founded Gupta Samvat (calendar) in 319-320 CE; symbolized new political era", "type": "leaf"}
                ]},
                {"label": "Empire Expansion", "type": "branch", "date": "Empire", "children": [
                    {"label": "Territory: Control over Magadha, Prayaga, Saketa (Ayodhya); unified eastern UP and Bihar", "type": "leaf"},
                    {"label": "Succession: Chose Samudragupta as heir; granted title 'Dharanibandha' (bound to earth)", "type": "leaf"}
                ]}
            ]

    # 11. Chandragupta II (Vikramaditya)
    elif 'chandragupta-ii' in fl:
        if is_hindi:
            return [
                {"label": "चंद्रगुप्त द्वितीय 'विक्रमादित्य' (375-415 ई.)", "type": "branch", "date": "375-415 CE", "children": [
                    {"label": "शक विजय: पश्चिम भारत के शक क्षत्रपों को पराजित किया; गुजरात-मालवा पर अधिकार; 'शकारि' उपाधि", "type": "leaf"},
                    {"label": "नवरत्न: कालिदास, आर्यभट्ट, वराहमिहिर, धनवंतरि, अमरसिंह, शंकु, वेतालभट्ट, घटकर्पर, क्षपणक — दरबार के 9 विद्वान", "type": "leaf"},
                    {"label": "स्वर्ण सिक्के: सर्वोत्तम; विभिन्न प्रकार — अश्वारोही, सिंह-निहंता, वीणावादक, व्याघ्रनिहंता प्रकार", "type": "leaf"}
                ]},
                {"label": "साम्राज्य की चरम सीमा और विरासत", "type": "branch", "date": "स्वर्ण युग", "children": [
                    {"label": "साम्राज्य विस्तार: पूर्व में बंगाल से पश्चिम में गुजरात; उत्तर में हिमालय से दक्षिण में नर्मदा; सर्वोच्च विस्तार", "type": "leaf"},
                    {"label": "फाह्यान की यात्रा: इसी काल में; 'भारत की समृद्धि और शांति' का साक्ष्य; बौद्ध धर्म को संरक्षण", "type": "leaf"},
                    {"label": "उज्जैन: राजधानी बनाई; पश्चिमी व्यापार केंद्र; महाकालेश्वर मंदिर; विक्रम संवत् से जुड़ाव", "type": "leaf"}
                ]}
            ]
        else:
            return [
                {"label": "Chandragupta II 'Vikramaditya' (375-415 CE)", "type": "branch", "date": "375-415 CE", "children": [
                    {"label": "Shaka Conquest: Defeated Western Kshatrapa Shakas; annexed Gujarat and Malwa; earned title 'Shakari'", "type": "leaf"},
                    {"label": "Navaratnas: Kalidasa, Aryabhata, Varahamihira, Dhanvantari, Amarasimha — nine gems of his court", "type": "leaf"},
                    {"label": "Gold Coins: Most artistic; types — horseman, lion-slayer, lute-player, tiger-slayer; metallurgical excellence", "type": "leaf"}
                ]},
                {"label": "Peak Empire & Legacy", "type": "branch", "date": "Golden Age", "children": [
                    {"label": "Max Extent: Bengal to Gujarat (E-W); Himalayas to Narmada (N-S); greatest territorial extent", "type": "leaf"},
                    {"label": "Fahien's Visit: Witnessed prosperity and peace; confirms absence of capital punishment; rich cities", "type": "leaf"},
                    {"label": "Ujjain as Capital: Western trade hub; Mahakaleshwar Temple; associated with Vikram Samvat tradition", "type": "leaf"}
                ]}
            ]

    # 12. Kumaragupta I
    elif 'kumaragupta' in fl:
        if is_hindi:
            return [
                {"label": "कुमारगुप्त प्रथम (415-455 ई.)", "type": "branch", "date": "415-455 CE", "children": [
                    {"label": "उपाधियाँ: महेंद्रादित्य, शक्रादित्य; अश्वमेध यज्ञ किया; साम्राज्य को स्थिर बनाए रखा", "type": "leaf"},
                    {"label": "नालंदा विश्वविद्यालय: कुमारगुप्त प्रथम ने नालंदा की स्थापना की; बाद में हर्षवर्धन ने विस्तार किया; एशिया का प्रमुख ज्ञान केंद्र", "type": "leaf"},
                    {"label": "सिक्के: अश्वमेध प्रकार, मयूर प्रकार (कार्तिकेय से संबंध), गज-निहंता प्रकार; सर्वाधिक सिक्के इसी काल के", "type": "leaf"}
                ]},
                {"label": "चुनौतियाँ और पुश्यमित्र विद्रोह", "type": "branch", "date": "विद्रोह", "children": [
                    {"label": "पुश्यमित्र विद्रोह: नर्मदा क्षेत्र में विद्रोह; स्कंदगुप्त ने दबाया; गुप्त शक्ति की परीक्षा", "type": "leaf"},
                    {"label": "हूण आक्रमण की पृष्ठभूमि: कुमारगुप्त के अंतिम वर्षों में हूण दबाव आरंभ; स्कंदगुप्त को संघर्ष विरासत में मिला", "type": "leaf"}
                ]}
            ]
        else:
            return [
                {"label": "Kumaragupta I (415-455 CE)", "type": "branch", "date": "415-455 CE", "children": [
                    {"label": "Titles: Mahendraditya, Shakraditya; performed Ashvamedha yajna; maintained empire's stability", "type": "leaf"},
                    {"label": "Nalanda University: Founded by Kumaragupta I; later expanded by Harshavardhana; Asia's great learning centre", "type": "leaf"},
                    {"label": "Coins: Ashvamedha type, Peacock type (linked to Kartikeya), Elephant-slayer type; most coins issued", "type": "leaf"}
                ]},
                {"label": "Challenges & Pushyamitra Revolt", "type": "branch", "date": "Revolt", "children": [
                    {"label": "Pushyamitra Revolt: Revolt in Narmada region; suppressed by Skandagupta; tested Gupta strength", "type": "leaf"},
                    {"label": "Huna Pressure Begins: Hunas started pressing in Kumaragupta's final years; inherited by Skandagupta", "type": "leaf"}
                ]}
            ]

    # 13. Samudragupta
    elif 'samudragupta' in fl:
        if is_hindi:
            return [
                {"label": "समुद्रगुप्त: 'भारत का नेपोलियन' (335-375 ई.)", "type": "branch", "date": "335-375 CE", "children": [
                    {"label": "प्रयाग प्रशस्ति: हरिषेण द्वारा रचित; इलाहाबाद स्तंभ पर उत्कीर्ण; समुद्रगुप्त की सैनिक विजयों का विवरण", "type": "leaf"},
                    {"label": "आर्यावर्त विजय: 9 उत्तरी राजाओं को पराजित कर सीधे राज्य में मिलाया; विनाश और पुनः स्थापना", "type": "leaf"},
                    {"label": "दक्षिणापथ विजय: 12 दक्षिणी राजाओं को पराजित कर पुनः सिंहासन दिया; 'धर्मविजय' नीति", "type": "leaf"}
                ]},
                {"label": "उपलब्धियाँ और उपाधियाँ", "type": "branch", "date": "उपलब्धियाँ", "children": [
                    {"label": "विजय प्रकार: 5 प्रकार — प्रत्यंत राज्य (सीमावर्ती), आटविक राज्य (वन), द्वीपों के राजा; श्रीलंका तक संपर्क", "type": "leaf"},
                    {"label": "संगीत प्रेम: वीणा वादक के रूप में प्रसिद्ध; सिक्कों पर वीणा; 'कविराज' उपाधि; बहुआयामी प्रतिभा", "type": "leaf"},
                    {"label": "अश्वमेध यज्ञ: सार्वभौम सत्ता का प्रदर्शन; सोने के अश्वमेध प्रकार के सिक्के जारी किए", "type": "leaf"}
                ]}
            ]
        else:
            return [
                {"label": "Samudragupta: 'Napoleon of India' (335-375 CE)", "type": "branch", "date": "335-375 CE", "children": [
                    {"label": "Prayaga Prashasti: Composed by Harishena; engraved on Allahabad Pillar; details his military campaigns", "type": "leaf"},
                    {"label": "Aryavarta Conquests: 9 northern kings defeated and territories annexed; 'uprooting and replanting' policy", "type": "leaf"},
                    {"label": "Dakshinapatha: 12 southern kings defeated then restored to thrones; 'Dharma-vijaya' (righteous conquest)", "type": "leaf"}
                ]},
                {"label": "Achievements & Titles", "type": "branch", "date": "Achievements", "children": [
                    {"label": "5 Policy Types: Direct annexation, frontier states, forest chiefs, island rulers; contact with Sri Lanka", "type": "leaf"},
                    {"label": "Musician King: Played veena; veena depicted on coins; titled 'Kaviraja'; multi-talented ruler", "type": "leaf"},
                    {"label": "Ashvamedha Yajna: Proclaimed universal sovereignty; gold Ashvamedha-type coins issued", "type": "leaf"}
                ]}
            ]

    # 14. Skandagupta
    elif 'skandagupta' in fl:
        if is_hindi:
            return [
                {"label": "स्कंदगुप्त (455-467 ई.): हूण विजेता", "type": "branch", "date": "455-467 CE", "children": [
                    {"label": "हूण आक्रमण प्रतिरोध: 455-456 ई. में श्वेत हूणों (Hunas) को सिंधु नदी के तट पर निर्णायक पराजय दी", "type": "leaf"},
                    {"label": "सुदर्शन झील का पुनर्निर्माण: गुजरात में; मौर्य काल में चंद्रगुप्त मौर्य द्वारा निर्मित; स्कंदगुप्त ने बाढ़ के बाद पुनर्निर्मित किया", "type": "leaf"},
                    {"label": "जूनागढ़ शिलालेख: सुदर्शन झील पुनर्निर्माण का विवरण; प्रशासनिक क्षमता का प्रमाण", "type": "leaf"}
                ]},
                {"label": "साम्राज्य का संघर्ष और विरासत", "type": "branch", "date": "विरासत", "children": [
                    {"label": "वित्तीय संकट: हूण युद्धों से खजाना रिक्त; सोने के सिक्कों की गुणवत्ता में गिरावट; अर्थव्यवस्था कमजोर", "type": "leaf"},
                    {"label": "उत्तराधिकार विवाद: स्कंदगुप्त के बाद कमजोर उत्तराधिकारी; पुरगुप्त और नरसिंहगुप्त; साम्राज्य टूटना आरंभ", "type": "leaf"}
                ]}
            ]
        else:
            return [
                {"label": "Skandagupta (455-467 CE): Huna Conqueror", "type": "branch", "date": "455-467 CE", "children": [
                    {"label": "Huna Repulsion: Decisively defeated White Hunas (Pushyamitras) on banks of Indus in 455-456 CE", "type": "leaf"},
                    {"label": "Sudarsana Lake Repair: Gujarat; originally built by Chandragupta Maurya; Skandagupta restored after flood", "type": "leaf"},
                    {"label": "Junagadh Inscription: Details the lake restoration; testament to his administrative capability", "type": "leaf"}
                ]},
                {"label": "Imperial Struggle & Legacy", "type": "branch", "date": "Legacy", "children": [
                    {"label": "Financial Crisis: Huna wars drained treasury; gold coin quality declined; economic weakening began", "type": "leaf"},
                    {"label": "Succession Dispute: Weak successors (Purugupta, Narasimhagupta); empire began fragmenting after 467 CE", "type": "leaf"}
                ]}
            ]

    # 15. Srigupta
    elif 'srigupta' in fl:
        if is_hindi:
            return [
                {"label": "श्रीगुप्त: गुप्त वंश के संस्थापक (240-280 ई.)", "type": "branch", "date": "240-280 CE", "children": [
                    {"label": "वंश की शुरुआत: 'महाराज' की उपाधि; 'महाराजाधिराज' नहीं; छोटे सामंत शासक; मगध क्षेत्र में", "type": "leaf"},
                    {"label": "चीनी लेखक I-Tsing का संदर्भ: श्रीगुप्त ने चीनी बौद्ध भिक्षुओं के लिए मंदिर बनाया; 'मृगसिंहवन' में", "type": "leaf"},
                    {"label": "उत्तराधिकार: घटोत्कच (पुत्र); फिर चंद्रगुप्त प्रथम — जिन्होंने वास्तव में शाही शक्ति प्रतिष्ठित की", "type": "leaf"}
                ]},
                {"label": "ऐतिहासिक महत्व", "type": "branch", "date": "महत्व", "children": [
                    {"label": "वंश का नाम: गुप्त वंश का नाम इन्हीं के नाम पर; 'श्रीगुप्त' से 'गुप्त' साम्राज्य", "type": "leaf"},
                    {"label": "सीमित शक्ति: कुषाण और सातवाहनों के पतन के बाद शक्ति शून्य में उभरे; धीरे-धीरे विस्तार", "type": "leaf"}
                ]}
            ]
        else:
            return [
                {"label": "Srigupta: Dynasty Founder (240-280 CE)", "type": "branch", "date": "240-280 CE", "children": [
                    {"label": "Founder: Title 'Maharaja' (not Maharajadhiraja); small feudatory ruler in Magadha region", "type": "leaf"},
                    {"label": "I-Tsing's Reference: Srigupta built a temple for Chinese Buddhist monks at 'Mrigasimhavana'", "type": "leaf"},
                    {"label": "Succession: Ghatotkacha (son); then Chandragupta I who established real imperial power", "type": "leaf"}
                ]},
                {"label": "Historical Significance", "type": "branch", "date": "Significance", "children": [
                    {"label": "Dynasty Name: The 'Gupta' dynasty name derives from Sri-Gupta; foundational lineage", "type": "leaf"},
                    {"label": "Limited Power: Rose in power vacuum after Kushan and Satavahana decline; gradual expansion", "type": "leaf"}
                ]}
            ]

    # 16. Later Guptas
    elif 'later-guptas' in fl:
        if is_hindi:
            return [
                {"label": "उत्तर-गुप्त शासक: विखंडित साम्राज्य", "type": "branch", "date": "5-6 शताब्दी", "children": [
                    {"label": "पुरगुप्त: स्कंदगुप्त के बाद; कमजोर शासक; मगध क्षेत्र तक सीमित; हूण दबाव जारी", "type": "leaf"},
                    {"label": "नरसिंहगुप्त 'बालादित्य': हूण नेता मिहिरकुल को पराजित किया; बौद्ध धर्म का अनुयायी; नालंदा का संरक्षक", "type": "leaf"},
                    {"label": "कुमारगुप्त III और विष्णुगुप्त: अंतिम गुप्त शासक; 550 ई. तक; साम्राज्य पूरी तरह विखंडित", "type": "leaf"}
                ]},
                {"label": "क्षेत्रीय उत्तराधिकारी राज्य", "type": "branch", "date": "उत्तराधिकारी", "children": [
                    {"label": "मौखरी वंश: उत्तर प्रदेश; गुप्त सामंत से स्वतंत्र; हर्षवर्धन से संबंध; कन्नौज केंद्र", "type": "leaf"},
                    {"label": "वल्लभी वंश: गुजरात-सौराष्ट्र; मैत्रक वंश; गुप्त शासन के उत्तराधिकारी; व्यापार केंद्र", "type": "leaf"}
                ]}
            ]
        else:
            return [
                {"label": "Later Gupta Rulers: Fragmented Empire", "type": "branch", "date": "5th-6th Century", "children": [
                    {"label": "Purugupta: After Skandagupta; weak ruler; confined to Magadha; continued Huna pressure", "type": "leaf"},
                    {"label": "Narasimhagupta 'Baladitya': Defeated Huna chief Mihirakula; Buddhist follower; Nalanda patron", "type": "leaf"},
                    {"label": "Kumaragupta III & Vishnugupta: Last Gupta rulers; by 550 CE empire fully fragmented", "type": "leaf"}
                ]},
                {"label": "Regional Successor States", "type": "branch", "date": "Successors", "children": [
                    {"label": "Maukhari Dynasty: UP; former Gupta feudatories; linked to Harshavardhana; Kannauj as centre", "type": "leaf"},
                    {"label": "Vallabhi Dynasty: Gujarat-Saurashtra; Maitraka dynasty; successors of Gupta rule; trade hub", "type": "leaf"}
                ]}
            ]

    # 17. Other Important Dynasties
    elif 'other-important' in fl:
        if is_hindi:
            return [
                {"label": "गुप्त काल के समकालीन अन्य राजवंश", "type": "branch", "date": "समकालीन", "children": [
                    {"label": "वाकाटक वंश: दक्कन; चंद्रगुप्त II की पुत्री प्रभावतीगुप्त का विवाह; रुद्रसेन II; अजंता गुफाओं का संरक्षण", "type": "leaf"},
                    {"label": "शक क्षत्रप: पश्चिम भारत; रुद्रसिंह III (अंतिम); चंद्रगुप्त II द्वारा पराजित 388-409 ई.; उज्जैन पर अधिकार", "type": "leaf"},
                    {"label": "कदम्ब वंश: कर्नाटक; मयूरशर्मन ने स्थापना; दक्षिण भारत में ब्राह्मण शासकों का उदय", "type": "leaf"}
                ]},
                {"label": "उत्तर-पूर्वी और दक्षिणी राज्य", "type": "branch", "date": "क्षेत्रीय राज्य", "children": [
                    {"label": "पल्लव वंश: तमिलनाडु; कांची राजधानी; महाबलीपुरम का निर्माण; द्रविड़ स्थापत्य का आरंभ", "type": "leaf"},
                    {"label": "विष्णुकुंडि: आंध्र; सातवाहनों के उत्तराधिकारी; गुप्त काल के दक्षिण में; बौद्ध संरक्षक", "type": "leaf"}
                ]}
            ]
        else:
            return [
                {"label": "Contemporary Dynasties of Gupta Period", "type": "branch", "date": "Contemporary", "children": [
                    {"label": "Vakataka Dynasty: Deccan; Prabhavati Gupta (Chandragupta II's daughter) married Rudrasena II; Ajanta patronage", "type": "leaf"},
                    {"label": "Shaka Kshatrapas: Western India; Rudrasimha III (last); defeated by Chandragupta II (388-409 CE)", "type": "leaf"},
                    {"label": "Kadamba Dynasty: Karnataka; founded by Mayurasharman; first Brahmin rulers of S. India", "type": "leaf"}
                ]},
                {"label": "Northeastern & Southern States", "type": "branch", "date": "Regional States", "children": [
                    {"label": "Pallava Dynasty: Tamil Nadu; Kanchipuram capital; Mahabalipuram; early Dravidian architecture", "type": "leaf"},
                    {"label": "Vishnukundis: Andhra; Satavahana successors in south; Buddhist patrons during Gupta period", "type": "leaf"}
                ]}
            ]

    # 18. Sources of Information
    elif 'sources' in fl:
        if is_hindi:
            return [
                {"label": "गुप्त काल के स्रोत: साहित्यिक", "type": "branch", "date": "साहित्यिक स्रोत", "children": [
                    {"label": "अभिलेख (शिलालेख): प्रयाग प्रशस्ति (हरिषेण); मेहरौली लौह स्तंभ लेख; जूनागढ़ शिलालेख; मंदसौर लेख", "type": "leaf"},
                    {"label": "ताम्रपत्र: भूमि अनुदान के लिए; दामोदरपुर, पहारपुर; प्रशासनिक और आर्थिक जानकारी", "type": "leaf"},
                    {"label": "विदेशी विवरण: फाह्यान (399-414 CE); चीनी बौद्ध; धर्म, समाज, नगर-जीवन का वर्णन", "type": "leaf"}
                ]},
                {"label": "पुरातत्विक और मुद्राशास्त्रीय स्रोत", "type": "branch", "date": "पुरातात्विक", "children": [
                    {"label": "सोने के सिक्के: विभिन्न प्रकार (अश्वारोही, सिंहनिहंता, वीणावादक, अश्वमेध); शासकों की पहचान", "type": "leaf"},
                    {"label": "मंदिर और मूर्तियाँ: देवगढ़, भूमरा, नचना-कुठारा मंदिर; मथुरा-सारनाथ की मूर्तियाँ", "type": "leaf"},
                    {"label": "अजंता और एलोरा: गुप्त और वाकाटक संरक्षण; भित्तिचित्र और मूर्तिकला; धार्मिक-सांस्कृतिक जानकारी", "type": "leaf"}
                ]}
            ]
        else:
            return [
                {"label": "Sources for Gupta Period: Literary", "type": "branch", "date": "Literary Sources", "children": [
                    {"label": "Inscriptions: Prayaga Prashasti (Harishena); Mehrauli Iron Pillar; Junagadh; Mandasor inscriptions", "type": "leaf"},
                    {"label": "Copper Plates: Land grants; Damodarpur, Paharpur plates; administrative and economic information", "type": "leaf"},
                    {"label": "Foreign Accounts: Fahien (399-414 CE); Chinese Buddhist; religion, society and city life described", "type": "leaf"}
                ]},
                {"label": "Archaeological & Numismatic Sources", "type": "branch", "date": "Archaeological", "children": [
                    {"label": "Gold Coins: Various types (horseman, lion-slayer, lute player, Ashvamedha); identify each ruler", "type": "leaf"},
                    {"label": "Temples & Sculptures: Deogarh, Bhumara, Nachna-Kuthara temples; Mathura-Sarnath sculptures", "type": "leaf"},
                    {"label": "Ajanta & Ellora: Gupta and Vakataka patronage; murals and sculptures; religious-cultural data", "type": "leaf"}
                ]}
            ]

    # 19. Urban Centres
    elif 'urban' in fl:
        if is_hindi:
            return [
                {"label": "गुप्त काल के प्रमुख नगर", "type": "branch", "date": "नगर", "children": [
                    {"label": "पाटलिपुत्र (पटना): राजधानी; फाह्यान के अनुसार समृद्ध और विशाल; बौद्ध और हिंदू धर्म का केंद्र", "type": "leaf"},
                    {"label": "उज्जैन: चंद्रगुप्त II की द्वितीय राजधानी; पश्चिमी व्यापार केंद्र; महाकाल मंदिर; विद्या का केंद्र", "type": "leaf"},
                    {"label": "प्रयाग (इलाहाबाद): त्रिवेणी संगम; प्रयाग प्रशस्ति का स्थल; तीर्थराज; धार्मिक केंद्र", "type": "leaf"},
                    {"label": "वाराणसी: सारनाथ (बौद्ध); धार्मिक और शैक्षणिक; सारनाथ में गुप्त काल की सर्वोत्तम बुद्ध प्रतिमाएँ", "type": "leaf"}
                ]},
                {"label": "व्यापार नगर और बंदरगाह", "type": "branch", "date": "व्यापार", "children": [
                    {"label": "ताम्रलिप्ति (तमलुक): पूर्वी बंदरगाह; बंगाल की खाड़ी; दक्षिण-पूर्व एशिया से व्यापार; फाह्यान ने यहाँ से प्रस्थान किया", "type": "leaf"},
                    {"label": "भड़ौच (Bharuch): पश्चिमी बंदरगाह; रोमन व्यापार; नर्मदा नदी का मुहाना; प्राचीन Barygaza", "type": "leaf"}
                ]}
            ]
        else:
            return [
                {"label": "Major Urban Centres of Gupta Period", "type": "branch", "date": "Urban Centres", "children": [
                    {"label": "Pataliputra (Patna): Capital city; Fahien: 'prosperous and large'; Buddhist and Hindu religious centre", "type": "leaf"},
                    {"label": "Ujjain: Chandragupta II's second capital; western trade hub; Mahakal Temple; centre of learning", "type": "leaf"},
                    {"label": "Prayaga (Allahabad): Triveni Sangam; site of Prayaga Prashasti; premier pilgrimage centre", "type": "leaf"},
                    {"label": "Varanasi: Sarnath (Buddhist); best Gupta-era Buddha statues at Sarnath Museum", "type": "leaf"}
                ]},
                {"label": "Trade Cities & Ports", "type": "branch", "date": "Trade", "children": [
                    {"label": "Tamralipti (Tamluk): Eastern port on Bay of Bengal; SE Asia trade; Fahien departed from here", "type": "leaf"},
                    {"label": "Bharuch (Broach): Western port; Roman trade; Narmada estuary; ancient Barygaza of Greek records", "type": "leaf"}
                ]}
            ]

    # Fallback
    else:
        if is_hindi:
            return [{"label": "गुप्त काल", "type": "branch", "date": "स्वर्ण युग", "children": [
                {"label": "गुप्त साम्राज्य की प्रमुख विशेषताएँ और उपलब्धियाँ", "type": "leaf"}]}]
        else:
            return [{"label": "Gupta Age", "type": "branch", "date": "Golden Age", "children": [
                {"label": "Key features and achievements of the Gupta Empire", "type": "leaf"}]}]

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

    branches = get_custom_branches(folder_name, is_hindi)
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
