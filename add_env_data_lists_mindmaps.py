#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import re
import json

BASE = r"upsc/environment/Relevant-Environmental-Data-Lists"

def get_clean_title(folder_name):
    title = folder_name.replace('-', ' ')
    words = []
    skip = {'of','and','the','for','in','with','to','on','by','or','a','an','at'}
    for w in title.split():
        if w.lower() in skip:
            words.append(w.lower())
        else:
            words.append(w.capitalize())
    return ' '.join(words)

def get_custom_branches(folder_name, is_hindi):
    fl = folder_name.lower()

    # 1. Biosphere Reserves (general)
    if 'biosphere-reserves' in fl and 'unesco' not in fl:
        if is_hindi:
            return [
                {"label": "जैवमंडल आरक्षित क्षेत्र: भारत में कुल 18", "type": "branch", "date": "18 जैवमंडल", "children": [
                    {"label": "नीलगिरि (1986): भारत का पहला जैवमंडल आरक्षित क्षेत्र; केरल, कर्नाटक, तमिलनाडु; शोला वन और नीलगिरि तहर के लिए प्रसिद्ध", "type": "leaf"},
                    {"label": "नंदा देवी (1988): उत्तराखंड; UNESCO की सूची में; हिम तेंदुआ और हिमालयी वनस्पति का आवास", "type": "leaf"},
                    {"label": "सुंदरबन (1989): पश्चिम बंगाल; UNESCO की सूची में; रॉयल बंगाल टाइगर और मैंग्रोव का विश्व का सबसे बड़ा डेल्टा", "type": "leaf"},
                    {"label": "मन्नार की खाड़ी (1989): तमिलनाडु; UNESCO की सूची में; प्रवाल भित्ति, डुगोंग और समुद्री घास", "type": "leaf"},
                    {"label": "मानस (1989): असम; UNESCO की सूची में; एक सींग वाला गैंडा, बाघ, और हाथी", "type": "leaf"},
                    {"label": "ग्रेट निकोबार (1989): अंडमान और निकोबार; UNESCO की सूची में; लेदरबैक कछुआ और खारे पानी का मगरमच्छ", "type": "leaf"}
                ]},
                {"label": "अतिरिक्त प्रमुख जैवमंडल (12)", "type": "branch", "date": "शेष 12", "children": [
                    {"label": "नोकरेक (1988): मेघालय; गारो पहाड़ियाँ; रेड पांडा और हाथी का आवास; UNESCO सूची में", "type": "leaf"},
                    {"label": "सिमलीपाल (1994): ओडिशा; बाघ आरक्षित क्षेत्र भी; मेलानिस्टिक (काला) बाघ के लिए प्रसिद्ध", "type": "leaf"},
                    {"label": "दिहांग-दिबांग (1998): अरुणाचल प्रदेश; ऑर्किड की समृद्ध विविधता; मिश्मी पहाड़ियाँ", "type": "leaf"},
                    {"label": "कंचनजंगा (2000): सिक्किम; UNESCO सूची में; हिम तेंदुआ, हिम भालू, लाल पांडा", "type": "leaf"},
                    {"label": "पन्ना (2011): मध्यप्रदेश; विंध्य पर्वतमाला; बाघ और घड़ियाल का आवास", "type": "leaf"},
                    {"label": "शेषाचलम (2010): आंध्रप्रदेश; पूर्वी घाट; स्लॉथ बेयर और लंगूर", "type": "leaf"}
                ]}
            ]
        else:
            return [
                {"label": "India's 18 Biosphere Reserves", "type": "branch", "date": "18 Biospheres", "children": [
                    {"label": "Nilgiri (1986): India's FIRST biosphere reserve; Kerala, Karnataka, TN; Shola forests and Nilgiri Tahr", "type": "leaf"},
                    {"label": "Nanda Devi (1988): Uttarakhand; UNESCO-listed; Snow leopard and high-altitude Himalayan flora", "type": "leaf"},
                    {"label": "Sundarbans (1989): West Bengal; UNESCO-listed; World's largest mangrove delta; Royal Bengal Tiger", "type": "leaf"},
                    {"label": "Gulf of Mannar (1989): Tamil Nadu; UNESCO-listed; Coral reefs, Dugong and Seagrass beds", "type": "leaf"},
                    {"label": "Manas (1989): Assam; UNESCO-listed; One-horned rhinoceros, Bengal Tiger, Asian Elephant", "type": "leaf"},
                    {"label": "Great Nicobar (1989): A&N Islands; UNESCO-listed; Leatherback turtle and Saltwater crocodile", "type": "leaf"}
                ]},
                {"label": "12 Additional Biospheres", "type": "branch", "date": "Remaining 12", "children": [
                    {"label": "Nokrek (1988): Meghalaya; Garo Hills; Red Panda habitat; UNESCO-listed", "type": "leaf"},
                    {"label": "Simlipal (1994): Odisha; Also a Tiger Reserve; famous for melanistic (black) tigers", "type": "leaf"},
                    {"label": "Dibang-Dihang (1998): Arunachal Pradesh; Rich orchid diversity; Mishmi Hills", "type": "leaf"},
                    {"label": "Khangchendzonga (2000): Sikkim; UNESCO-listed; Snow leopard, Red Panda, Brown Bear", "type": "leaf"},
                    {"label": "Panna (2011): Madhya Pradesh; Vindhyan ranges; Tiger and Gharial habitat", "type": "leaf"},
                    {"label": "Seshachalam (2010): Andhra Pradesh; Eastern Ghats; Sloth Bear and Langur", "type": "leaf"}
                ]}
            ]

    # 2. Biosphere Reserves in UNESCO Map/List
    elif 'biosphere' in fl and 'unesco' in fl:
        if is_hindi:
            return [
                {"label": "UNESCO MAB सूची में 12 भारतीय जैवमंडल", "type": "branch", "date": "UNESCO MAB", "children": [
                    {"label": "नीलगिरि (2000): UNESCO MAB में सम्मिलित पहला भारतीय जैवमंडल; 5520 वर्ग किमी; तीन राज्यों में फैला", "type": "leaf"},
                    {"label": "मन्नार की खाड़ी (2001): 10,500 वर्ग किमी; 21 द्वीप; डुगोंग संरक्षण के लिए महत्वपूर्ण", "type": "leaf"},
                    {"label": "सुंदरबन (2001): 9630 वर्ग किमी; विश्व की सबसे बड़ी मैंग्रोव प्रणाली", "type": "leaf"},
                    {"label": "नंदा देवी (2004): 5,860 वर्ग किमी; UNESCO विश्व धरोहर स्थल भी", "type": "leaf"},
                    {"label": "नोकरेक (2009): 820 वर्ग किमी; साइट्रस के जंगली पूर्वज पाए जाते हैं", "type": "leaf"},
                    {"label": "ग्रेट निकोबार (2013): 885 वर्ग किमी; सबसे दक्षिणी छोर पर स्थित", "type": "leaf"}
                ]},
                {"label": "हाल में UNESCO में सम्मिलित जैवमंडल", "type": "branch", "date": "हालिया", "children": [
                    {"label": "पचमढ़ी (2009): मध्यप्रदेश; सतपुड़ा पर्वतमाला; 'सतपुड़ा की रानी'", "type": "leaf"},
                    {"label": "अचानकमार-अमरकंटक (2012): MP-CG सीमा; नर्मदा नदी का उद्गम", "type": "leaf"},
                    {"label": "अगस्त्यमलाई (2016): केरल-TN; UNESCO सूची में शामिल; जैव विविधता हॉटस्पॉट", "type": "leaf"},
                    {"label": "खंगचेंदज़ोंगा (2018): सिक्किम; 8,586 मीटर ऊँचाई पर स्थित चोटी वाला", "type": "leaf"},
                    {"label": "पन्ना (2020): UNESCO MAB में नवीनतम शामिल; उत्तरी विंध्य में स्थित", "type": "leaf"}
                ]}
            ]
        else:
            return [
                {"label": "India's 12 UNESCO MAB-listed Biospheres", "type": "branch", "date": "UNESCO MAB", "children": [
                    {"label": "Nilgiri (2000): India's FIRST to join UNESCO MAB Network; 5520 sq km spanning 3 states", "type": "leaf"},
                    {"label": "Gulf of Mannar (2001): 10,500 sq km; 21 islands; Key for Dugong conservation", "type": "leaf"},
                    {"label": "Sundarbans (2001): 9630 sq km; World's largest mangrove delta ecosystem", "type": "leaf"},
                    {"label": "Nanda Devi (2004): 5860 sq km; Also a UNESCO World Heritage Site", "type": "leaf"},
                    {"label": "Nokrek (2009): 820 sq km; Wild relatives of Citrus species found here", "type": "leaf"},
                    {"label": "Great Nicobar (2013): 885 sq km; India's southernmost biosphere reserve", "type": "leaf"}
                ]},
                {"label": "Recently Added UNESCO Biospheres", "type": "branch", "date": "Recent", "children": [
                    {"label": "Pachmarhi (2009): MP; Satpura range; 'Queen of Satpura'", "type": "leaf"},
                    {"label": "Achanakmar-Amarkantak (2012): MP-CG border; Source of Narmada river", "type": "leaf"},
                    {"label": "Agasthyamalai (2016): Kerala-TN border; Biodiversity hotspot with rare orchids", "type": "leaf"},
                    {"label": "Khangchendzonga (2018): Sikkim; Around India's highest peak at 8586m", "type": "leaf"},
                    {"label": "Panna (2020): Newest addition to UNESCO MAB; Located in northern Vindhyas", "type": "leaf"}
                ]}
            ]

    # 3. Elephant Reserves
    elif 'elephant' in fl:
        if is_hindi:
            return [
                {"label": "हाथी आरक्षित क्षेत्र: भारत में कुल 33", "type": "branch", "date": "33 आरक्षित", "children": [
                    {"label": "पहला हाथी आरक्षित (1992): 'प्रोजेक्ट एलीफेंट' 1992 में शुरू; सिंगलीला-सुंदरबन (पश्चिम बंगाल) पहला घोषित", "type": "leaf"},
                    {"label": "प्रमुख दक्षिण भारत: नीलगिरि (TN-KA-KE), अनामलाई (TN), वायनाड (KE), पेरियार (KE)", "type": "leaf"},
                    {"label": "उत्तर-पूर्व में: डेहिंग-पटकाई (असम), काजीरंगा-कार्बी आंगलोंग (असम), दिहांग-देबांग (अरुणाचल)", "type": "leaf"},
                    {"label": "मध्य भारत: मयूरभंज (ओडिशा), महानदी (ओडिशा-झारखंड), कमलांग (अरुणाचल)", "type": "leaf"}
                ]},
                {"label": "प्रोजेक्ट एलीफेंट और प्रबंधन", "type": "branch", "date": "प्रबंधन", "children": [
                    {"label": "हाथी गलियारे: भारत में 101 हाथी गलियारे; इनमें से 96 में मानव-हाथी संघर्ष की समस्या", "type": "leaf"},
                    {"label": "MIKE साइटों से जुड़ाव: हाथी आरक्षित और MIKE (Monitoring Illegal Killing of Elephants) साइटें आपस में जुड़ी हैं", "type": "leaf"},
                    {"label": "जनसंख्या: भारत में लगभग 30,000 एशियाई हाथी; विश्व की 60% जनसंख्या; IUCN: लुप्तप्राय", "type": "leaf"}
                ]}
            ]
        else:
            return [
                {"label": "India's 33 Elephant Reserves", "type": "branch", "date": "33 Reserves", "children": [
                    {"label": "Project Elephant (1992): Launched in 1992; Singhalia-Sundarbans (West Bengal) was the first notified reserve", "type": "leaf"},
                    {"label": "South India Key Reserves: Nilgiri (TN-KA-KE), Anamalai (TN), Wayanad (KE), Periyar (KE)", "type": "leaf"},
                    {"label": "Northeast India: Dehing-Patkai (Assam), Kaziranga-Karbi Anglong (Assam), Dibang-Dihang (Arunachal)", "type": "leaf"},
                    {"label": "Central India: Mayurbhanj (Odisha), Mahanadi (Odisha-Jharkhand), Kameng (Arunachal)", "type": "leaf"}
                ]},
                {"label": "Project Elephant & Management", "type": "branch", "date": "Management", "children": [
                    {"label": "Elephant Corridors: 101 corridors identified in India; 96 face human-elephant conflict pressures", "type": "leaf"},
                    {"label": "MIKE link: Elephant Reserves overlap with MIKE (Monitoring Illegal Killing of Elephants) sites", "type": "leaf"},
                    {"label": "Population: ~30,000 Asian Elephants in India = 60% of global population; IUCN: Endangered", "type": "leaf"}
                ]}
            ]

    # 4. Sacred Groves
    elif 'sacred' in fl:
        if is_hindi:
            return [
                {"label": "पवित्र उपवन: परिभाषा और महत्व", "type": "branch", "date": "परिभाषा", "children": [
                    {"label": "देवभूमि: स्थानीय समुदायों द्वारा देवी-देवताओं को समर्पित संरक्षित वन; वहाँ शिकार और पेड़ काटना वर्जित", "type": "leaf"},
                    {"label": "पर्यावरणीय महत्व: जैव विविधता के 'द्वीप'; दुर्लभ औषधीय पौधों का भंडार; जल स्रोतों की रक्षा", "type": "leaf"}
                ]},
                {"label": "राज्य-वार पवित्र उपवन (प्रमुख)", "type": "branch", "date": "राज्य-वार", "children": [
                    {"label": "केरल: 'काव' (Kavu); देवी भगवती को समर्पित; 1000+ काव पूरे केरल में; सर्पकाव प्रसिद्ध", "type": "leaf"},
                    {"label": "मेघालय: 'लॉ-खिंथांग' (Law Kyntang); खासी और जैंतिया जनजाति; मेघालय में सर्वाधिक पवित्र उपवन", "type": "leaf"},
                    {"label": "राजस्थान: 'ओरण' (Oran); बिश्नोई समुदाय; खेजड़ी वृक्ष की रक्षा के लिए 363 लोगों का बलिदान (अमृता देवी)", "type": "leaf"},
                    {"label": "महाराष्ट्र: 'देवराई' (Devrai); पश्चिमी घाट में; 1500+ देवराई; जलागम संरक्षण में महत्वपूर्ण", "type": "leaf"},
                    {"label": "हिमाचल/उत्तराखंड: 'देवबन' या 'देवतावन'; देवदार और बांज ओक के वन", "type": "leaf"},
                    {"label": "झारखंड/ओडिशा: 'जाहेर' (Jaher); संताल और मुंडा जनजाति; सरना स्थल", "type": "leaf"}
                ]}
            ]
        else:
            return [
                {"label": "Sacred Groves: Definition & Significance", "type": "branch", "date": "Concept", "children": [
                    {"label": "Community-protected forest patches dedicated to local deities; hunting and tree-felling strictly forbidden", "type": "leaf"},
                    {"label": "Ecological role: Biodiversity 'islands'; storehouse of rare medicinal plants; protect water sources", "type": "leaf"}
                ]},
                {"label": "State-wise Major Sacred Groves", "type": "branch", "date": "State-wise", "children": [
                    {"label": "Kerala: 'Kavu' — Dedicated to Goddess Bhagavati; 1000+ Kavus; Serpent Kavu (Sarpa Kavu) are iconic", "type": "leaf"},
                    {"label": "Meghalaya: 'Law Kyntang' — Khasi & Jaintia tribes; highest density of sacred groves in India", "type": "leaf"},
                    {"label": "Rajasthan: 'Oran' — Bishnoi community; 363 lives sacrificed protecting Khejri trees (Amrita Devi)", "type": "leaf"},
                    {"label": "Maharashtra: 'Devrai' — Western Ghats; 1500+ Devrais; critical for watershed conservation", "type": "leaf"},
                    {"label": "HP/Uttarakhand: 'Devban/Devatavan' — Dense Deodar and Banj Oak forests", "type": "leaf"},
                    {"label": "Jharkhand/Odisha: 'Jaher' — Santhal and Munda tribes; Sarna worship sites", "type": "leaf"}
                ]}
            ]

    # 5. Mangrove Sites
    elif 'mangrove' in fl:
        if is_hindi:
            return [
                {"label": "भारत में मैंग्रोव: स्थिति और विस्तार", "type": "branch", "date": "4975 वर्ग किमी", "children": [
                    {"label": "कुल क्षेत्र: भारत में 4975 वर्ग किमी मैंग्रोव (FSI रिपोर्ट 2021); विश्व का 3% मैंग्रोव भारत में", "type": "leaf"},
                    {"label": "सुंदरबन: 2114 वर्ग किमी; भारत का 42% मैंग्रोव; सबसे बड़ा; सुंदरी वृक्ष (Heritiera fomes) विशेषता", "type": "leaf"},
                    {"label": "गुजरात: 1177 वर्ग किमी; कच्छ की खाड़ी में; दूसरा सबसे बड़ा; मैंग्रोव क्षेत्र में वृद्धि", "type": "leaf"},
                    {"label": "अंडमान-निकोबार: 616 वर्ग किमी; सबसे घने मैंग्रोव; 38+ प्रजातियाँ", "type": "leaf"}
                ]},
                {"label": "अन्य महत्वपूर्ण मैंग्रोव स्थल", "type": "branch", "date": "राज्य-वार", "children": [
                    {"label": "ओडिशा: भितरकनिका (660 वर्ग किमी); तीसरा सबसे बड़ा; खारे पानी के मगरमच्छ का प्रमुख आवास", "type": "leaf"},
                    {"label": "महाराष्ट्र: मुंबई और रत्नागिरी के मैंग्रोव; 2015 में वन्य संरक्षित घोषित", "type": "leaf"},
                    {"label": "कर्नाटक: कुंदापुर (उडुपी जिला); पश्चिमी तट के मैंग्रोव", "type": "leaf"},
                    {"label": "PICHAVARAM: तमिलनाडु; एशिया का दूसरा सबसे बड़ा मैंग्रोव; कावेरी डेल्टा", "type": "leaf"}
                ]}
            ]
        else:
            return [
                {"label": "India's Mangrove Cover: Status", "type": "branch", "date": "4975 sq km", "children": [
                    {"label": "Total: 4975 sq km of mangroves (FSI 2021); India holds ~3% of world's total mangroves", "type": "leaf"},
                    {"label": "Sundarbans: 2114 sq km; 42% of India's mangroves; Sundari tree (Heritiera fomes) is iconic", "type": "leaf"},
                    {"label": "Gujarat: 1177 sq km; Gulf of Kutch; 2nd largest; growing mangrove cover", "type": "leaf"},
                    {"label": "Andaman & Nicobar: 616 sq km; Most dense; 38+ species including Rhizophora", "type": "leaf"}
                ]},
                {"label": "Other Key Mangrove Sites", "type": "branch", "date": "State-wise", "children": [
                    {"label": "Odisha: Bhitarkanika (660 sq km); 3rd largest; Prime habitat for Saltwater Crocodile", "type": "leaf"},
                    {"label": "Maharashtra: Mumbai and Ratnagiri mangroves; declared Protected Forest in 2015", "type": "leaf"},
                    {"label": "Karnataka: Kundapur (Udupi district); Western coast mangroves along estuaries", "type": "leaf"},
                    {"label": "Pichavaram (Tamil Nadu): 2nd largest mangrove in Asia; Cauvery delta", "type": "leaf"}
                ]}
            ]

    # 6. MIKE Sites
    elif 'mike' in fl:
        if is_hindi:
            return [
                {"label": "MIKE: संक्षिप्त परिचय", "type": "branch", "date": "MIKE Program", "children": [
                    {"label": "MIKE = Monitoring the Illegal Killing of Elephants; CITES (Convention on International Trade in Endangered Species) का कार्यक्रम", "type": "leaf"},
                    {"label": "उद्देश्य: हाथियों की अवैध हत्या पर नज़र रखना; 'PIKE' (Proportion of Illegally Killed Elephants) सूचकांक का उपयोग", "type": "leaf"}
                ]},
                {"label": "भारत में प्रमुख MIKE साइटें", "type": "branch", "date": "साइटें", "children": [
                    {"label": "काजीरंगा-कार्बी आंगलोंग: असम; MIKE केंद्र; एशियाई हाथियों की सर्वाधिक घनत्व", "type": "leaf"},
                    {"label": "नागरहोल-बांदीपुर: कर्नाटक-केरल; दक्षिण भारत की प्रमुख MIKE साइट", "type": "leaf"},
                    {"label": "पेरियार: केरल; MIKE निगरानी; इलायची पहाड़ियों में हाथी", "type": "leaf"},
                    {"label": "वाल्मीकि: बिहार; उत्तर भारत में MIKE साइट; नेपाल सीमा के निकट", "type": "leaf"},
                    {"label": "सिमलीपाल: ओडिशा; पूर्वी भारत MIKE केंद्र; मेलानिस्टिक बाघ भी यहाँ", "type": "leaf"},
                    {"label": "सत्यमंगलम: तमिलनाडु; नीलगिरि बायोस्फीयर का हिस्सा; हाथी-मानव संघर्ष जोन", "type": "leaf"}
                ]}
            ]
        else:
            return [
                {"label": "MIKE: Introduction & Purpose", "type": "branch", "date": "MIKE Program", "children": [
                    {"label": "MIKE = Monitoring the Illegal Killing of Elephants; a CITES-run global program", "type": "leaf"},
                    {"label": "Uses PIKE index (Proportion of Illegally Killed Elephants) to measure poaching pressure trends", "type": "leaf"}
                ]},
                {"label": "Major MIKE Sites in India", "type": "branch", "date": "Sites", "children": [
                    {"label": "Kaziranga-Karbi Anglong: Assam; Key MIKE site; Highest elephant density in Asia", "type": "leaf"},
                    {"label": "Nagarhole-Bandipur: Karnataka-Kerala; Prime South India MIKE site in Nilgiri cluster", "type": "leaf"},
                    {"label": "Periyar: Kerala; MIKE monitoring hub; Cardamom Hills elephant population", "type": "leaf"},
                    {"label": "Valmiki: Bihar; North India MIKE site; Near Nepal border (transboundary elephants)", "type": "leaf"},
                    {"label": "Simlipal: Odisha; East India MIKE centre; Also hosts melanistic tigers", "type": "leaf"},
                    {"label": "Sathyamangalam: Tamil Nadu; Part of Nilgiri Biosphere; High human-elephant conflict zone", "type": "leaf"}
                ]}
            ]

    # 7. National Parks
    elif 'national-parks' in fl:
        if is_hindi:
            return [
                {"label": "राष्ट्रीय उद्यान: आधारभूत तथ्य", "type": "branch", "date": "106 राष्ट्रीय उद्यान", "children": [
                    {"label": "भारत का पहला: जिम कॉर्बेट राष्ट्रीय उद्यान (1936); उत्तराखंड; बाघ और हाथी; रामगंगा नदी", "type": "leaf"},
                    {"label": "सबसे बड़ा: हेमिस (लद्दाख); 4400 वर्ग किमी; हिम तेंदुए के लिए विश्व प्रसिद्ध", "type": "leaf"},
                    {"label": "सबसे छोटा: साउथ बटन द्वीप राष्ट्रीय उद्यान (अंडमान); 0.03 वर्ग किमी", "type": "leaf"},
                    {"label": "वन्यजीव (संरक्षण) अधिनियम 1972: राष्ट्रीय उद्यानों को कानूनी दर्जा; अंदर कोई भी मानवीय गतिविधि वर्जित", "type": "leaf"}
                ]},
                {"label": "राज्य-वार प्रमुख राष्ट्रीय उद्यान", "type": "branch", "date": "राज्य-वार", "children": [
                    {"label": "मध्यप्रदेश (7): कान्हा, बांधवगढ़, पेंच, पन्ना, सतपुड़ा, माधव, संजय; 'टाइगर स्टेट'", "type": "leaf"},
                    {"label": "अंडमान-निकोबार: 9 राष्ट्रीय उद्यान; सबसे अधिक; महात्मा गांधी समुद्री राष्ट्रीय उद्यान प्रसिद्ध", "type": "leaf"},
                    {"label": "उत्तराखंड: कॉर्बेट, राजाजी, नंदा देवी, फूलों की घाटी, गंगोत्री", "type": "leaf"},
                    {"label": "केरल: साइलेंट वैली (वर्षावन); एर्नाकुलम मथिकेट्टन; पेरियार", "type": "leaf"}
                ]}
            ]
        else:
            return [
                {"label": "National Parks: Key Facts", "type": "branch", "date": "106 NPs", "children": [
                    {"label": "First NP: Jim Corbett (1936); Uttarakhand; Tiger, Elephant; Ramganga river through the park", "type": "leaf"},
                    {"label": "Largest: Hemis (Ladakh); 4400 sq km; World-famous for Snow Leopard sightings", "type": "leaf"},
                    {"label": "Smallest: South Button Island NP (Andaman); just 0.03 sq km", "type": "leaf"},
                    {"label": "Wildlife (Protection) Act 1972: Gives legal status; no human activity allowed inside NP boundary", "type": "leaf"}
                ]},
                {"label": "State-wise Major National Parks", "type": "branch", "date": "State-wise", "children": [
                    {"label": "Madhya Pradesh (7): Kanha, Bandhavgarh, Pench, Panna, Satpura, Madhav, Sanjay; 'Tiger State'", "type": "leaf"},
                    {"label": "Andaman & Nicobar (9): Most NPs by state; Mahatma Gandhi Marine NP is iconic", "type": "leaf"},
                    {"label": "Uttarakhand: Corbett, Rajaji, Nanda Devi, Valley of Flowers, Gangotri", "type": "leaf"},
                    {"label": "Kerala: Silent Valley (Rainforest); Mathikettan; Periyar (Cardamom Hills)", "type": "leaf"}
                ]}
            ]

    # 8. Natural World Heritage Sites
    elif 'natural-world-heritage' in fl:
        if is_hindi:
            return [
                {"label": "प्राकृतिक विश्व धरोहर स्थल: भारत में 7", "type": "branch", "date": "7 स्थल", "children": [
                    {"label": "काजीरंगा राष्ट्रीय उद्यान (1985): असम; एक सींग वाले गैंडे की सबसे बड़ी आबादी; बाघ, हाथी भी", "type": "leaf"},
                    {"label": "केवलादेव राष्ट्रीय उद्यान (1985): राजस्थान; भरतपुर पक्षी अभयारण्य; साइबेरियन सारस (विलुप्तप्राय)", "type": "leaf"},
                    {"label": "मानस वन्यजीव अभयारण्य (1985): असम; बाघ, गैंडा, हाथी, गोल्डन लंगूर", "type": "leaf"},
                    {"label": "सुंदरबन राष्ट्रीय उद्यान (1987): पश्चिम बंगाल; विश्व का सबसे बड़ा मैंग्रोव; बाघ", "type": "leaf"},
                    {"label": "नंदा देवी और फूलों की घाटी (1988, विस्तार 2005): उत्तराखंड; अल्पाइन फूल", "type": "leaf"},
                    {"label": "पश्चिमी घाट (2012): TN, KE, KA, GJ, MH; जैव विविधता हॉटस्पॉट; 39 स्थलों का समूह", "type": "leaf"},
                    {"label": "ग्रेट हिमालयन राष्ट्रीय उद्यान (2014): हिमाचल प्रदेश; हिम तेंदुआ और हिमालयी भूरा भालू", "type": "leaf"}
                ]},
                {"label": "UNESCO नामांकन मानदंड", "type": "branch", "date": "मानदंड", "children": [
                    {"label": "मानदंड ix: पारिस्थितिक प्रक्रियाओं का उत्कृष्ट उदाहरण (जैसे मैंग्रोव, अल्पाइन पारिस्थितिकी)", "type": "leaf"},
                    {"label": "मानदंड x: सर्वाधिक जैव विविधता और लुप्तप्राय प्रजातियों का आवास", "type": "leaf"}
                ]}
            ]
        else:
            return [
                {"label": "India's 7 Natural World Heritage Sites", "type": "branch", "date": "7 Sites", "children": [
                    {"label": "Kaziranga NP (1985): Assam; Largest population of one-horned rhinoceros; Tiger, Elephant", "type": "leaf"},
                    {"label": "Keoladeo Ghana NP (1985): Rajasthan; Bharatpur Bird Sanctuary; Siberian Crane (critical)", "type": "leaf"},
                    {"label": "Manas Wildlife Sanctuary (1985): Assam; Tiger, Rhino, Elephant, Golden Langur", "type": "leaf"},
                    {"label": "Sundarbans NP (1987): West Bengal; World's largest mangrove ecosystem; Bengal Tiger", "type": "leaf"},
                    {"label": "Nanda Devi & Valley of Flowers (1988, ext. 2005): Uttarakhand; Alpine meadows", "type": "leaf"},
                    {"label": "Western Ghats (2012): TN, KE, KA, GJ, MH; Biodiversity hotspot; 39 property cluster", "type": "leaf"},
                    {"label": "Great Himalayan NP (2014): Himachal Pradesh; Snow Leopard and Himalayan Brown Bear", "type": "leaf"}
                ]},
                {"label": "UNESCO Nomination Criteria", "type": "branch", "date": "Criteria", "children": [
                    {"label": "Criterion ix: Outstanding examples of ongoing ecological processes (mangroves, alpine)", "type": "leaf"},
                    {"label": "Criterion x: Most significant habitats for in-situ conservation of threatened species", "type": "leaf"}
                ]}
            ]

    # 9. Ramsar Wetland Sites
    elif 'ramsar' in fl:
        if is_hindi:
            return [
                {"label": "रामसर आर्द्रभूमि: भारत में 75+", "type": "branch", "date": "75+ स्थल", "children": [
                    {"label": "रामसर कन्वेंशन (1971): ईरान के रामसर शहर में हस्ताक्षरित; 1975 में लागू; आर्द्रभूमि संरक्षण का अंतर्राष्ट्रीय ढांचा", "type": "leaf"},
                    {"label": "भारत का पहला रामसर स्थल: चिल्का झील (ओडिशा) और केवलादेव (राजस्थान) — 1981 में एक साथ पहले घोषित", "type": "leaf"},
                    {"label": "सर्वाधिक रामसर: तमिलनाडु (14); उत्तरप्रदेश (10); फिर पंजाब और गुजरात", "type": "leaf"},
                    {"label": "भारत का सबसे बड़ा रामसर: सुंदरबन (West Bengal); 4230 वर्ग किमी", "type": "leaf"}
                ]},
                {"label": "प्रमुख रामसर स्थलों की सूची", "type": "branch", "date": "महत्वपूर्ण स्थल", "children": [
                    {"label": "चिल्का (ओडिशा): एशिया की सबसे बड़ी खारे पानी की झील; इरावदी डॉल्फिन; प्रवासी पक्षियों का आश्रय", "type": "leaf"},
                    {"label": "लोकटक (मणिपुर): भारत का एकमात्र तैरता हुआ राष्ट्रीय उद्यान; फुमदी (तैरती भूमि)", "type": "leaf"},
                    {"label": "वुलर (J&K): भारत की सबसे बड़ी मीठे पानी की झील; झेलम नदी का विस्तार; प्रवासी बत्तख", "type": "leaf"},
                    {"label": "भोज (MP): ऊपरी और निचला तालाब भोपाल; पुष्पीय पौधों की समृद्ध विविधता", "type": "leaf"},
                    {"label": "नलसरोवर (गुजरात): गुजरात का सबसे बड़ा वेटलैंड; फ्लेमिंगो और पेलिकन", "type": "leaf"},
                    {"label": "कांजली (पंजाब): काली बेईं नदी; पंजाब का महत्वपूर्ण रामसर स्थल", "type": "leaf"}
                ]}
            ]
        else:
            return [
                {"label": "India's 75+ Ramsar Wetlands", "type": "branch", "date": "75+ Sites", "children": [
                    {"label": "Ramsar Convention (1971): Signed in Ramsar, Iran; enforced 1975; international wetland treaty", "type": "leaf"},
                    {"label": "India's First (1981): Chilika Lake (Odisha) AND Keoladeo (Rajasthan) — designated together", "type": "leaf"},
                    {"label": "Most Ramsar Sites: Tamil Nadu (14); Uttar Pradesh (10); then Punjab and Gujarat", "type": "leaf"},
                    {"label": "Largest Ramsar in India: Sundarbans (WB); 4230 sq km", "type": "leaf"}
                ]},
                {"label": "Key Ramsar Sites", "type": "branch", "date": "Important Sites", "children": [
                    {"label": "Chilika (Odisha): Asia's largest brackish water lake; Irrawaddy dolphin; migratory birds", "type": "leaf"},
                    {"label": "Loktak (Manipur): India's only floating national park; Phumdis (floating biomass islands)", "type": "leaf"},
                    {"label": "Wular (J&K): India's largest freshwater lake; extension of Jhelum river; migratory ducks", "type": "leaf"},
                    {"label": "Bhoj (MP): Upper and Lower Bhopal Lake; rich aquatic plant biodiversity", "type": "leaf"},
                    {"label": "Nalsarovar (Gujarat): Gujarat's largest wetland; Flamingos and Pelicans in winter", "type": "leaf"},
                    {"label": "Kanjali (Punjab): Kali Bein stream; important Punjab Ramsar site", "type": "leaf"}
                ]}
            ]

    # 10. Tiger Reserves
    elif 'tiger' in fl:
        if is_hindi:
            return [
                {"label": "प्रोजेक्ट टाइगर और बाघ आरक्षित: तथ्य", "type": "branch", "date": "54 बाघ आरक्षित", "children": [
                    {"label": "प्रोजेक्ट टाइगर (1973): इंदिरा गांधी सरकार ने शुरू किया; पहले 9 बाघ आरक्षित घोषित; NTCA (राष्ट्रीय बाघ संरक्षण प्राधिकरण) 2006 में गठित", "type": "leaf"},
                    {"label": "पहला बाघ आरक्षित: जिम कॉर्बेट (उत्तराखंड) — 1973 में प्रोजेक्ट टाइगर के पहले रिजर्व में से एक", "type": "leaf"},
                    {"label": "सबसे बड़ा: नागार्जुनसागर-श्रीशैलम (तेलंगाना-AP); 3296 वर्ग किमी", "type": "leaf"},
                    {"label": "सबसे छोटा: बोर (महाराष्ट्र); 138.12 वर्ग किमी", "type": "leaf"}
                ]},
                {"label": "राज्य-वार प्रमुख बाघ आरक्षित", "type": "branch", "date": "राज्य-वार", "children": [
                    {"label": "मध्यप्रदेश (7): बांधवगढ़, कान्हा, पेंच, पन्ना, सतपुड़ा, संजय-डुबरी, वीरांगना दुर्गावती; सर्वाधिक रिजर्व", "type": "leaf"},
                    {"label": "कर्नाटक (5): बांदीपुर, नागरहोल, भद्रा, काली, बीआर हिल्स", "type": "leaf"},
                    {"label": "उत्तराखंड (3): कॉर्बेट, राजाजी, (कालागढ़ क्षेत्र)", "type": "leaf"},
                    {"label": "महाराष्ट्र (6): ताडोबा-अंधारी (सर्वाधिक बाघ घनत्व), पेंच, मेलघाट, नवेगाँव, बोर, सह्याद्री", "type": "leaf"},
                    {"label": "सर्वाधिक बाघ: मध्यप्रदेश (785) > कर्नाटक (563) > उत्तराखंड (560); NTCA सर्वेक्षण 2022", "type": "leaf"}
                ]}
            ]
        else:
            return [
                {"label": "Project Tiger & Tiger Reserves: Facts", "type": "branch", "date": "54 Reserves", "children": [
                    {"label": "Project Tiger (1973): Launched by Indira Gandhi; first 9 reserves designated; NTCA formed in 2006", "type": "leaf"},
                    {"label": "First Tiger Reserve: Jim Corbett (Uttarakhand) — among the original 9 in 1973", "type": "leaf"},
                    {"label": "Largest: Nagarjunasagar-Srisailam (Telangana-AP); 3296 sq km across two states", "type": "leaf"},
                    {"label": "Smallest: Bor (Maharashtra); 138 sq km", "type": "leaf"}
                ]},
                {"label": "State-wise Major Tiger Reserves", "type": "branch", "date": "State-wise", "children": [
                    {"label": "Madhya Pradesh (7): Bandhavgarh, Kanha, Pench, Panna, Satpura, Sanjay-Dubri, Veerangana; Most reserves", "type": "leaf"},
                    {"label": "Karnataka (5): Bandipur, Nagarhole, Bhadra, Kali, BR Hills; 2nd largest tiger population", "type": "leaf"},
                    {"label": "Uttarakhand (3): Corbett, Rajaji; river-based corridors for tigers", "type": "leaf"},
                    {"label": "Maharashtra (6): Tadoba-Andhari (highest tiger density), Pench, Melghat, Bor, Sahyadri", "type": "leaf"},
                    {"label": "Tiger Census 2022: MP (785) > Karnataka (563) > Uttarakhand (560); India total = 3167 tigers", "type": "leaf"}
                ]}
            ]

    # Fallback
    else:
        if is_hindi:
            return [
                {"label": "पर्यावरण डेटा सूची", "type": "branch", "date": "संरक्षण", "children": [
                    {"label": "भारत में पर्यावरण संरक्षण से संबंधित महत्वपूर्ण डेटा और सूचियाँ", "type": "leaf"}
                ]}
            ]
        else:
            return [
                {"label": "Environmental Data Lists", "type": "branch", "date": "Conservation", "children": [
                    {"label": "Key data lists related to environmental conservation in India for UPSC preparation", "type": "leaf"}
                ]}
            ]

def process_file(html_path, is_hindi):
    print(f"Processing: {html_path} (is_hindi={is_hindi})")
    with open(html_path, 'r', encoding='utf-8') as f:
        html = f.read()

    html = html.replace('\r\n', '\n')
    html = html.replace('    <link rel="stylesheet" href="/assets/css/mindmap.min.css?v=2">\n', '')
    html = html.replace('    <link rel="stylesheet" href="/assets/css/mindmap.min.css?v=1">\n', '')
    html = html.replace('    <link rel="stylesheet" href="/assets/css/mindmap.min.css">\n', '')

    mindmap_div_pattern = r'\s*<!-- Interactive Mindmap -->.*?<!-- Deep-Dive Study Guide \(Dynamically Rendered\) -->'
    html = re.sub(mindmap_div_pattern, '\n            <!-- Deep-Dive Study Guide (Dynamically Rendered) -->', html, flags=re.DOTALL)
    script_pattern = r'\s*<!-- Interactive Mindmap -->.*?renderMindmap\(.*?\);\s*</script>'
    html = re.sub(script_pattern, '', html, flags=re.DOTALL)

    folder_path = os.path.dirname(html_path)
    folder_name = os.path.basename(folder_path)
    if folder_name == 'hi':
        parent_folder = os.path.dirname(folder_path)
        folder_name = os.path.basename(parent_folder)

    content_json_path = os.path.join(os.path.dirname(html_path), "content.json")
    clean_title = get_clean_title(folder_name)
    topic_name = clean_title
    if os.path.exists(content_json_path):
        try:
            with open(content_json_path, 'r', encoding='utf-8') as f:
                c_data = json.load(f)
                topic_name = c_data.get('hero', {}).get('title', topic_name)
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

def main():
    total = 0
    for root, dirs, files in os.walk(BASE):
        rel_path = os.path.relpath(root, BASE)
        parts = rel_path.split(os.sep)
        is_hindi = 'hi' in parts
        for file in files:
            if file == "index.html":
                process_file(os.path.join(root, file), is_hindi)
                total += 1
    print(f"\nDone! Patched {total} files.")

if __name__ == '__main__':
    main()
